function avg=moving_average(x)
persistent buffer
if size(buffer)<25
    buffer=[buffer x]
else
    buffer=[buffer(2:25) x]
end

avg=mean(buffer)
