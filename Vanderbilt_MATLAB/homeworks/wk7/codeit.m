function coded=codeit(txt)
num=double(txt)
for i=1:length(txt)
	if num(i)>=97 && num(i)<=122
        num(i)=219-num(i)
    end
    if num(i)>=65 && num(i)<=90
    num(i)=155-num(i)
    end
end
coded=char(num)
