# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
from fractions import Fraction
from math import gcd
s2 = []

print('\n'.join([str(Fraction(i,j)) for i in range(1,11) for j in range(1,12) if i < j and not s2.count(Fraction(i,j)) and gcd(i,j) == 1]))