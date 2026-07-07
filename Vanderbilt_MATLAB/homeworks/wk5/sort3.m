function ans=sort3(a,b,c)
if b>c
x=b
b=c
c=x
end

if a>b
x=a
a=b
b=x
end

if b>c
x=b
b=c
c=x
end

ans=[a b c]

