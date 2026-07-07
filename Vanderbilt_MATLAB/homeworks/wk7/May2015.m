function m=May2015
m=[]
for dd=1:31
n.month='May'
n.date=dd
remin=rem(dd,7)
switch remin
    case 0
        n.day= 'Thu'
    case 1
        n.day='Fri'  
    case 2
        n.day= 'Sat'
    case 3
        n.day= 'Sun'
    case 4
        n.day='Mon'
    case 5
        n.day='Tue',
    case 6
        n.day= 'Wed'   
end
m=[m n]
end


