function [app,k]=approximate_pi(delta)
sum=0
k=0
while abs(12^0.5*sum-pi)>=delta
    sum=sum+(-3)^(-k)/(2*k+1)
    k=k+1
end
app=12^0.5*sum
k=k-1
