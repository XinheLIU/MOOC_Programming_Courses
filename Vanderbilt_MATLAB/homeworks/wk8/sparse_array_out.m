function B=sparse_array_out(A,filename)
rows=size(A,1)
columns=size(A,2)
zeros=nnz(A)

fid = fopen(filename,'w+')
if fid<0
    fprintf('error opening files/n')
    B=false
    return;
else 
    B=true
end
fwrite(fid,rows,'uint32')
fwrite(fid,columns,'uint32')
fwrite(fid,zeros,'uint32')
for i=1:size(A,1)
    for j=1:size(A,2)  
        if ~(A(i,j)==0)
        fwrite(fid,i,'uint32')
        fwrite(fid,j,'uint32')
        fwrite(fid,A(i,j),'double')
        end
    end
end
fclose(fid)


