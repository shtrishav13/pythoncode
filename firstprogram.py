# this is for single line comment ctrl slash
""" This is a multi-line comment shift alt a """
#this is the name of the person
name= "Rishav"
age= 17
address = "Bhaktapur"
# concate method
print("My name is" + name + " and I am " + str(age) + " years old. I live in " + address)
# f-string method
print(f"My name is {name} and I am {age} years old. I live in {address}.")
# format old method
print("My name is {} and I am {} years old. I live in {}.".format(name, age, address))
# format new method
print("My name is %s and I am %d years old. I live in %s." % (name, age, address))
#type of variable
print(type(name))
print(type(age))
print(type(address))



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3= input("Enter third number: ")
num4= input("Enter fourth number: ")
sum = num1 + num2
sum2= num3 + num4
print(f"The sum of {num1} and {num2} is {sum}.")
print(f"The sum of {num3} and {num4} is {sum2}.")
print(type(sum))
print(type(sum2))


print(6 and 7)

#true and false values

#if and is used then it returns first false if both are true then it returns last value
# if or is used then it returns first true if both are false then it returns last value

print('apple'<'aPPLE')
#ordinal
print(ord('A'))
print(ord('😅'))
print(ord('Z'))

#character
print(chr(67))
print(chr(128517))

print('"Hello i am Rishav"')
print("helllo \"hel\nlo\"")
print("hello \rworld")


print(5&3)
print(5|3)
print(5^3)
print(5&4)
print(5|4)
print(5^4)

print(5<<2)

#membership and identity operators

a= [1,2,3]
b= [1,2,3]
c= a
print(a is b)# false
print(a == b)# true
print(a is c)# true
print(id(a))
print(id(b))   
print(id(c))
