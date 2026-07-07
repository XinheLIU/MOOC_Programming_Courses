function sum=halfsum(A)
[row col]=size(A)
sum=0
r=1
for c=1:col
    while r<=c && r<=row
        sum=sum+A(r,c)
        r=r+1
    end
    r=1
end

