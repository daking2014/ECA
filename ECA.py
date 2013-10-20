from optparse import OptionParser

#options
parser = OptionParser()
parser.add_option('-w', '--width',
					dest='width', default=71,
					help='The width of the diagram. Must be an even number.')
parser.add_option('-r', '--rulenumber',
					dest='rulenumber', default=90,
					help='The Wolfram rule number.')
parser.add_option('-g', '--generations',
					dest='gens', default=100,
					help='The number of generations to run for.')
(options, args) = parser.parse_args()

#setting options variables
width = int(options.width)
rulenumber = int(options.rulenumber)
gens = int(options.gens)

"""width = 101
rulenumber = 90
gens = 100"""

#the initial row
if width%2 == 0:
	print "Width must be an odd number!!"
first_row = ((width - 1) / 2)*'0' + '1' + ((width - 1) / 2)*'0'
print first_row

def take_rule(int):
	binary = []
	for i in xrange(7,-1,-1):
		binary.append((int & 2**i) >> i)
	rule = { '111': binary[0], '110': binary[1], '101': binary[2], '100': binary[3], '011': binary[4], '010': binary[5], '001': binary[6], '000': binary[7] }
	#print rule
	return rule
	
def apply_rule(previous, rule):
	for g in range(gens):
		if g == 0:
			previous = first_row
		else:
			previous = new
		#print previous
		new = ''
		for c in range(width):
			if previous[c-1]:
				seq1 = previous[c-1]
			else:
				seq1 = 0
			seq2 = previous[c]
			if c == width-1:
				seq3 = 0
			else:
				seq3 = previous[c+1]
			
			seq = str(seq1) + str(seq2) + str(seq3)
			#print seq
			
			new += str(rule[seq])
		print new

rule = take_rule(rulenumber)			
apply_rule(first_row, rule)
