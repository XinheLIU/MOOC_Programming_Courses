function wave=square_wave(n)
wave=[]
sum=0
t=0

for i=1:1001
    for k=1:n
        sum=sum+(sin((2*k-1)*t))/(2*k-1)
    end
    t=t+(4*pi)/1000
    wave=[wave sum]
    sum=0   
end

    
