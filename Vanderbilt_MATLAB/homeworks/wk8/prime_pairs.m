function p=prime_pairs(n)
p=-1
pri=primes(100000)
for i=1:length(pri)
    q=pri(i)
    if isprime(q+n)
        p=q
        return;
    end
end


