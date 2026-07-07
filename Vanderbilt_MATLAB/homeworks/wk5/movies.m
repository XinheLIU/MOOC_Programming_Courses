function see=movies(hr1, min1, durmin1, hr2, min2, durmin2)

first=hr1*60+min1+durmin1
second=hr2*60+min2
lap=second-first

if lap<0
    see=false;
elseif lap>30
    see=false;
else
    see=true;
end
