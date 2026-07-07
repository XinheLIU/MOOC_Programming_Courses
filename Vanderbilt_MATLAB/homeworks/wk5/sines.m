function [s1, s2, sums] = sines(pts,amp,f1,f2)
switch nargin
    case 0
        pts=1000
        amp=1
        f1=100
        f2=105
    case 1
        amp=1
        f1=100
        f2=105       
    case 2
        f1=100
        f2=105 
    case 3
        f2=f1*1.05
end

incr1=2*f1*pi/(pts-1)
vec1=[0:incr1:2*f1*pi]
s1=amp*sin(vec1)

incr2=2*f2*pi/(pts-1)
vec2=[0:incr2:2*f2*pi]
s2=amp*sin(vec2)

sums=s1+s2


