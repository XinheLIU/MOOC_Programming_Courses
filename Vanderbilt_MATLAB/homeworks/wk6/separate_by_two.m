function [even,odd]=separate_by_two(A)
odd=A(~(A/2==fix(A/2)))'
even=A(A/2==fix(A/2))'
