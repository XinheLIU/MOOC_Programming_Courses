import re
fhand = open('regex_sum_238942.txt')
inp=fhand.read()
x = re.findall( '[0-9]+',inp)

for index, item in enumerate(x):
    x[index] = int(item)

sum = sum(x)

print sum