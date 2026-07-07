function w=large_elements(X)
w=[]
[row col]=size(X)
for r=1:row
    for c=1:col
        if X(r,c)>r+c
        w=[w;r,c]
        end
    end
end
