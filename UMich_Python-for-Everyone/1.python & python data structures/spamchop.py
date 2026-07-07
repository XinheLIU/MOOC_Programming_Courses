x = 'From marquard@uct.ac.za:  0.8475'
# print x
pos = x.find(':‘）
# print pos
# print x[pos:]
num=float(x[pos+1:])
print num		#, type(num)