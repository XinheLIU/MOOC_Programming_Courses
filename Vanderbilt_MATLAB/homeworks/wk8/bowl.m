function score=bowl(pins)
if size(pins,2)>22 || size(pins,2)<11 ||sum(any(pins>10))>=1 || sum(any(pins<0))>=1
    score=-1
    return;
end
score=0
i=1
counter=1
while i<=length(pins) && counter<=9   %for the first 9 plays
    if pins(i)==10
        score=score+10+pins(i+1)+pins(i+2)
        i=i+1
        counter=counter+1
    elseif pins(i)<10
        if pins(i)+pins(i+1)==10
           score=score+10+pins(i+2)
        elseif pins(i)+pins(i+1)<10
           score=score+pins(i)+pins(i+1)
        else
            score=-1
            return;    
        end
        i=i+2
        counter=counter+1
    else
         score=-1
         return;    
    end
end
    n=length(pins)
    score=score+sum(pins(i:n))
    x=size(pins(i:n),2)
    if  x<2 || x>3
        score=-1
    else
    
        if pins(i)+pins(i+1)<10 && x>2
            score=-1
        end
    
        if pins(i)+pins(i+1)>=10 && x<=2
            score=-1
        end
        
    end
    
    if score>300
        score=0
    end
    
