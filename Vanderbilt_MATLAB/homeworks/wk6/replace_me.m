function w = replace_me(v,a,b,c)

if nargin==2
        c=0
        b=0
end

if nargin==3
        c=b
end        
    w=[]
for i=1:length(v)
    if v(i)==a
    w=[w b c]
    else
    w=[w v(i)]
    end
end