function vec=neighbor(v)

col=size(v,2)

if isvector(v)==false || col<=1
    vec=[]
    return;
end
for c=1:(col-1)
    vec(c)=abs(v(c+1)-v(c))
end


