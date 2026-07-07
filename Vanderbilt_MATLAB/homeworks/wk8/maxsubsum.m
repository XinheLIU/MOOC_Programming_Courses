function [row,col,numrows,numcols,summa] = maxsubsum(A)
[m n]=size(A)
summa=sum(sum(A))
row=1
col=1
numrows=m
numcols=n
for i=1:m
    for j=1:n
        for k=0:(m-i)
            for h=0:(n-j)
                summa_temp=sum(sum(A(i:i+k,j:j+h)))
                if summa_temp>summa
                    summa=summa_temp
                    row=i
                    col=j
                    numrows=(k+1)
                    numcols=(h+1)
                end
            end
        end
    end
end