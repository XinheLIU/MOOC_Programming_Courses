largest = None
smallest = None
while True:
 inp=raw_input('Enter a number:')
 
 #handle the edge cases
 
 if inp== 'done' : break
 if len(inp) < 1 : break		#check for empty line
 
 #do the work
 
 try:
  num=float(inp)
 except:
  print "invalid input"
  continue
 
 if smallest is None:
   smallest = num
 elif num<smallest:
   smallest=num
   
 if largest is None:
   largest = num
 elif num>largest:
   largest=num
 
print 'Maximum is', int(largest)
print 'Minimum is', int(smallest)
 