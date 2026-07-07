fname = raw_input("Enter file name: ")
if len(fname)==0 :
	fname='words.txt'

fhand = open(fname)
for line in fhand :
	line=line.rstrip().upper()
	print line