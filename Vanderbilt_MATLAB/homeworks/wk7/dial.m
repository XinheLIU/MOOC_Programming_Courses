function dia=dial(txt)
for i=1:length(txt)
    num=double(txt(i))
    if num==40 || num==41 || num==45
        num2=' '
    elseif num>=65 && num<=80
        num2=fix((num-2)/3)-19
    elseif num>=82 && num<=89
        num2=fix((num-3)/3)-19
    elseif (num<=57 && num>=48)||num==42||num==32||num==35
        num2=txt(i)
    else
        dia=[]
        return;
    end    
    dia(i)=num2str(num2)
    
end
