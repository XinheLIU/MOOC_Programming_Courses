function type=integerize(A)
maxi=max(max(A))
if maxi<=2^8-1
    type='uint8'
elseif maxi<=2^16-1
    type='uint16'
elseif maxi<=2^32-1
    type='uint32'
elseif maxi<=2^64-1
     type='uint64'
else 
     type='NONE'  
end
    