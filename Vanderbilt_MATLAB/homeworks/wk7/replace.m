function rep=replace(c,c1,c2)
rep=cell(size(c))
for i=1:size(c,1)
    for j=1:size(c,2)
        ctt=char(c(i,j))
        loc=findstr(ctt,c1)
        if size(loc,1)>0
        for k=1:length(loc)
            ctt(loc(k):loc(k)+length(c2)-1)=c2
        end
        end
        rep{i,j}=ctt
    end
end
   
