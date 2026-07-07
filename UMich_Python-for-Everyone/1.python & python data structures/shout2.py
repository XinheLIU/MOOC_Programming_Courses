# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
sum=0
count=0
num=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    else:
        num=float(line[20:])
        sum=sum+num;
        count=count+1		
avg=sum/count   
print 'Average spam confidence:',avg
