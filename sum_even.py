#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int=8234

n1=var_int%10
var_int//=10

n2=var_int%10
var_int//=10

n3=var_int%10
n4=var_int//10
var_int=(1-n1%2)*n1+(1-n2%2)*n2+(1-n3%2)*n3+(1-n4%2)*n4

print(var_int)