function A=sparse_array_in(filename)
fid=fopen(filename,'r')
if fid<0
    fprintf('error opening file/n')
    A=[]
    return;
end
rows=fread(fid,1,'uint32')
columns=fread(fid,1,'uint32')
zero=fread(fid,1,'uint32')
non_zero=rows*columns-zero
A=zeros(rows,columns)
for m=1:non_zero
    i=fread(fid,1,'uint32')         

    j=fread(fid,1,'uint32')

    k=fread(fid,1,'double')

    A(i,j)=k
end

A=double(A)                 %some questions are left still for this question
                            %for some values it does not seem to be correct
fclose(fid)

