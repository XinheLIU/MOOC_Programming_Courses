function m=June2015 
m=cell(30,3)
for dd=1:30
m{dd,1}='June'
m{dd,2}=dd
remin=rem(dd,7)
switch remin
    case 4
        day= 'Thu'
    case 5
        day='Fri'  
    case 6
        day= 'Sat'
    case 0
        day= 'Sun'
    case 1
        day='Mon'
    case 2
        day='Tue',
    case 3
        day= 'Wed'   
end
m{dd,3}=day
end
