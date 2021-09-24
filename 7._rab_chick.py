from sympy import symbols, Eq,solve
rab,chick = symbols('rabbits,chicken')
value1=Eq(( rab + chick ),35)
value2=Eq(( 4*rab + 2*chick ),94)
print(solve((value1,value2),(rab,chick)))