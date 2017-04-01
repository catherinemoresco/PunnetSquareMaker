# PunnetSquareMaker
# Copyright (C) 2014 Catherine Moresco

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# The author can be reached by email at catherine.moresco@gmail.com.

import os
import re



def headtex():
	f= open('table.tex', 'w')
	f.write('\\begin{table}[]\n\\centering\n\\caption{My caption}\n\\label{my-label}\n')
	f.close()
	
def foottex():
	f= open('table.tex', 'a')
	f.write('\n\\end{tabular}\n\\end{table}')
	f.close()
		
	
def get_all_combinations(parent): # Finds all possible combinations of alleles a parent can pass on to their offspring, assuming independen assortment.
	if len(parent) == 1:
		return [parent[0][0], parent[0][1]]
	else:
		genlist = []
		for x in get_all_combinations(parent[1:]):
			genlist.append(parent[0][0] + x)
			genlist.append(parent[0][1] + x)
		return genlist

def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row

def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table

def print_table(table, c1, c2): # formats and prints Punnett square
	f= open('table.tex', 'a') # open the file
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print '',
	f.write('& ')
	for a in c2:
		print ' '*(len(c1[0])+3) + a + '',
		f.write('& ' + a + ' ')
	print '\n' + ' '*(len(c1[0])+1) + '-'*(divlength)
	f.write('\\\ \n& ')
	
	for i, row in enumerate(table):
		print c1[table.index(row)],
		f.write(c1[table.index(row)] + ' ')
		print '|',
		f.write('& ')
		for cell in row:
			print cell + ' | ',
			f.write(cell + ' & ')
		print '\n' + ' '*(len(c1[0])+1) + '-'*(divlength)
		if i != len(table)-1:
			f.write('\\\ \n& ')
	
def print_genotype_frequencies(table): # calculates frequencies for each genotype present in table
	f= open('table.tex', 'a') # open the file
	f.write('\n')
	calculated = []
	genotypes = [a for b in table for a in b]
	for x in genotypes:
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			print "The frequency of the " + x + " genotype is " + str(float(count)/float((len(genotypes)))*100) + "%."
			f.write("The frequency of the " + x + " genotype is " + str(float(count)/float((len(genotypes)))*100) + "\\%.\n")
		calculated.append(sorted(x))


print 'Hello, and welcome to the Punnett square maker! To get started, enter the genotype of the first parent. There should be two alleles for each gene, and each should be represented by one letter. The genes should be separated by spaces. For example, a valid genotype would be "Xx Yy zz", while "XxYyZz" would not.'
while True:
	p1 = raw_input("Please enter the genotype of the first parent: ").split(' ')
	p2 = raw_input("Please enter the gentype of the second parent: ").split(' ')
	headtex()
	c1 = get_all_combinations(p1)
	c2 = get_all_combinations(p2)
	a = make_table(c1, c2)
	print_table(a, c1, c2)
	foottex()
	print_genotype_frequencies(a)
	action = raw_input("Enter (Q) to quit, or (A) to make another!\n")
	if action == "Q":
		quit()
