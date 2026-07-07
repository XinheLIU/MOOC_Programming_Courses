function gen=generationXYZ(born)
if born<1966
    gen='O'
elseif born>=1966 && born<=1980
    gen='X'
elseif born>=1981 && born<=1999
    gen='Y'
elseif born>=2000 && born<=2012
    gen='Z'
else
    gen='K'
end    