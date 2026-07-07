name = raw_input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

fh= open(name)

cou=dict()

for line in fh:
  line=line.rstrip()
  if line=='': continue
  words=line.split()
  if words[0]!='From':continue
  word=words[1]          
  cou[word]=cou.get(word,0)+1
            
maxval=None
maxkee=None
for kee, val in cou.items():
    if maxval== None or maxval<val :
        maxval=val
        maxkee=kee
        
print maxkee,maxval