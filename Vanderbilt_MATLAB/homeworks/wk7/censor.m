function rep=censor(c,c1)
rep=cell(0,0)
for i=1:size(c,1)
    for j=1:size(c,2)
        ctt=char(c(i,j))
        loc=findstr(ctt,c1)
        if size(loc,1)==0
        rep=[rep ctt]
        end
    end
end

if size(c,2)>size(c,1)
    rep=rep'
end
