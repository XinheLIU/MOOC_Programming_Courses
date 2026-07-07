fname = raw_input("Enter file name: ")
fh= open(fname)
lst=list()

for line in fh:
    line=line.rstrip()
        words=line.split()
            lst=lst+words

lst.sort()
list(set(lst))

new_list=list()
for word in lst:
    if word not in new_list:
        new_list.append(word)

print new_list
