#While loop in python
i=1
while i < 4:
    print(i)
    i=i+1

#break statement 
print("Break Statement")
i=1
while i < 4:
    print(i)
    if i == 2:
        break
    i=i+1

#else statement
print("Else Statement")
i=1
while i < 4:
    print(i)
    i=i+1
else:
    print("i is no longer less than 4")