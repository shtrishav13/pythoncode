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

print('apple'<'apple')