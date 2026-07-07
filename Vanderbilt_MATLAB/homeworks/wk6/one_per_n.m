function n=one_per_n(x)
sum=0
i=1
while sum<x
    sum=sum+1/i
    i=i+1
    if i>=10002
       n=-1
       return;
    end
end
n=i-1