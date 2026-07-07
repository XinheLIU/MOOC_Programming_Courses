function who=older(y1, m1, d1, y2, m2, d2)
if y1>y2
    who=-1
elseif y1==y2
    if m1>m2
        who=-1
    elseif m1==m2
        if d1>d2
            who=-1
        elseif d1==d2
            who=0
        else who=1
        end
    else who=1
    end
else who=1
end