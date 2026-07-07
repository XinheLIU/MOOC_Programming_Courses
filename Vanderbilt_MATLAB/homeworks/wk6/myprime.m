function judge=myprime(n)
if n==2
    judge=true
    return;
end

s=fix(n^0.5)+1
for i=2:s
    if rem(n,i)==0
        judge=false
        return;
    end
end
judge=true
