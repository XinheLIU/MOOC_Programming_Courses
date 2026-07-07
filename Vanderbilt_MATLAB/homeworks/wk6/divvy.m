function B = divvy(A,k)
A(~(A/k==fix(A/k)))=A(~(A/k==fix(A/k)))*k
B=A
