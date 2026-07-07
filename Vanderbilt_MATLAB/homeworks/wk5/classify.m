function ans=classify(x)
sz=size(x)
if sz(1,1)==0 || sz(1,2)==0
   ans=-1
elseif sz==[1 1]
    ans=0
elseif sz(1,1)>1 && sz(1,2)>1
    ans=2
else ans=1
end

   