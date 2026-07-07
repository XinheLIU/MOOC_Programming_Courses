name = raw_input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

fh= open(name)

cou=dict()

for line in fh:
  line=line.rstrip()
  if line=='': continue
  words=line.split()
  if words[0]!='From':continue
  word=words[5]  
  lin=word.split(":")
  wrd=lin[0]
  cou[wrd]=cou.get(wrd,0)+1
            
flipped=list()

for kee, val in cou.items():
    newup=(kee,val)
    flipped.append(newup)
    
flipped.sort()

for kee, val in flipped[:]:
    print kee, val