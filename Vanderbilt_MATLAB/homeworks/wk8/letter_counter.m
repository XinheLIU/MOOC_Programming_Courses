function num = letter_counter(filename)
fid=fopen(filename,'rt')
if fid<0
    fprintf('error opening file/n')
    num=-1
    return;
end
 
A=fread(fid,inf,'char')
B=char(A)
C=isletter(B)
num=sum(C)

fclose(fid)