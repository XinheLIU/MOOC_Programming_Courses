function check=queen_check(board)
A=double(board)
check=true
for i=1:size(A,1)       %check rows
    if sum(A(i,:))>1
        check=false
        return;
    end
end

for j=1:size(A,2)           %check colums
    if sum(A(:,j))>1
        check=false
        return;
    end
end
for k=-7:7                  %check diagonals
 if sum(diag(A,k))>1
     check=false
     return;
 end
end

A=flipud(A)

for h=-7:7                  %check diagonals2
 if sum(diag(A,h))>1
     check=false
     return;
 end
end


