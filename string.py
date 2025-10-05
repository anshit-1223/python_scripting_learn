#String in Python
name = "Anshit Verma"
print(name)

#Slicing

str = "hello"
print(str[1:3])


#Slice from the start
print(str[:5])

#Slice to the End
print(str[1:])

#Negative Indexing
print(str[-4:0])

#Uppercase and lowercase
print(str.upper())
print(str.lower())

#Remove Whitespaces

str = " Hello, World!! "
print(str)
str=str.strip()
print(str)

#Replace
print(str.replace("H","J"))

#Split String [splits in list]
print(str.split(","))
