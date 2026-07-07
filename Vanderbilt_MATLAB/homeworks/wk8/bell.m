function B=bell(n)

if n<=0 || ~(n==fix(n))
    B=[]
    return;
end

B=zeros(n)
B(1,1)=1
for i=2:n
    for j=1:i
        if j==1
            B(i,j)=B(i-1,i-1)
        else
            B(i,j)=B(i-1,j-1)+B(i,j-1)
        end
    end
end

for k=2:n
    B(:,k) = circshift(B(:,k),-k+1)
end
    
