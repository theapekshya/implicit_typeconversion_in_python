#implict type conversion

a=5
b=2 
c=a/b
print(c)
print(type(c))   #determine datatype i.e. here float ,because python gives data without loss it gives 2.5 not 2

x=10
y=5.5
add=x+y
print(add)
print(type(add))  #gives float value 


a='hey\n'          
b='how are you'
c= a+b             #concatination string
print(c)
print
(type(c))          #str datatype



a=10
b='5'              # number string
r= a+b
print(r)            # error, int and str cannot be concatinated in implicit