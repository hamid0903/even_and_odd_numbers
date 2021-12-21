#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int=4268

n1=var_int%10
var_int//=10

n2=var_int%10
var_int//=10

n3=var_int%10
n4=var_int//10
var_int=(n1+1)%2+(n2+1)%2+(n3+1)%2+(n4+1)%2

print(var_int)

