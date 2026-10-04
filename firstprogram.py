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
print(a is b)# false because they are different objects
print(a == b)# true because they have same values
print(a is c)# true because they are same objects
print(id(a))
print(id(b))   
print(id(c))

print(5 + 3*10 -4) 
print(2**3**2)


# 1. ARITHMETIC OPERATORS
# ---------------------------------------------------------
# 1. Addition (+)
print(5 + 3)  # Output: 8

# 2. Subtraction (-)
print(10 - 4)  # Output: 6

# 3. Multiplication (*):
print(4 * 2)  # Output: 8

# 4. Division (/): (always returns a float)
print(7 / 2)  # Output: 3.5

# 5. Floor Division (//): Divides and rounds DOWN to nearest integer
print(7 // 2)  # Output: 3

# 6. Modulus (%): Returns the remainder left over after division
print(7 % 3)  # Output: 1

# 7. Exponentiation (**): Raises left number to the power of right
print(2 ** 3)  # Output: 8



# 2. COMPARISON OPERATORS

# 1. Equal to (==): 
print(5 == 5)  # Output: True

# 2. Not equal to (!=): 
print(5 != 3)  # Output: True

# 3. Greater than (>): 
print(10 > 2)  # Output: True

# 4. Less than (<):
print(3 < 8)  # Output: True

# 5. Greater than or equal to (>=): 
print(5 >= 5)  # Output: True

# 6. Less than or equal to (<=):
print(4 <= 2)  # Output: False

# 3. ASSIGNMENT OPERATORS

x = 10
# 1. Assign (=): Stores a value
print(x)

x += 5
# 2. Add and assign (+=): Adds 5 to x
print(x)  # Output: 15

x -= 2
# 3. Subtract and assign (-=): Subtracts 2 from x
print(x)  # Output: 13

x *= 2
# 4. Multiply and assign (*=): Multiplies x by 2
print(x)  # Output: 26

x /= 2
# 5. Divide and assign (/=): Divides x by 2
print(x)  # Output: 13.0


# 4. LOGICAL OPERATORS

# 1. and: Returns True only if BOTH conditions are true
print((5 > 2) and (10 > 3))  # Output: True

# 2. or: Returns True if AT LEAST ONE condition is true
print((5 > 10) or (10 > 3))  # Output: True

# 3. not: Reverses the result (True becomes False)
print(not (5 > 2))  # Output: False



# 5. MEMBERSHIP OPERATORS

# 1. in: Returns True if item is present
print("pneumono" in "pneumonoultamicroscopicsilicovolcanoconiosis")  # Output: True

# 2. not in: Returns True if item is missing
print("cholera" not in "pneumonoultamicroscopicsilicovolcanoconiosis")  # Output: True



# 6. IDENTITY OPERATORS

x = None
# 1. is: Returns True if variables are the exact same object
print(x is None)  # Output: True

# 2. is not: Returns True if they are separate objects in memory
print([1, 2] is not [1, 2])  # Output: True



# 7. BITWISE OPERATORS

# 1. Bitwise AND (&): Sets bit to 1 if both bits are 1
print(5 & 3)  # Output: 1

# 2. Bitwise OR (|): Sets bit to 1 if either bit is 1
print(5 | 3)  # Output: 7

# 3. Bitwise XOR (^): Sets bit to 1 only if bits are different
print(5 ^ 3)  # Output: 6

# 4. Bitwise NOT (~): Inverts all bits
print(~5)  # Output: -6

# 5. Left Shift (<<): Shifts bits left (multiplies by 2)
print(5 << 1)  # Output: 10

# 6. Right Shift (>>): Shifts bits right (divides by 2)
print(5 >> 1)  # Output: 2