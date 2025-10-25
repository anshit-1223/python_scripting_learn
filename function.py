#function in python
def my_function():
    print("Function Executed")
my_function()

#function with arguments
def my_name(name):
    print(name)
my_name("Anshit")


#arbitrary arguments - when you dont no the number of arguments will be passed into your function
def arbitrary_function(*fruits):
    print(fruits[1])

arbitrary_function("mango","apple","grapes")

#keyword arguments 
def keyword_function(java,python,linux):
    print(linux)

keyword_function(java="James",python="Guido",linux="Linus")


#return values in function
def sum_two(num1,num2):
    return num1+num2

print("Sum :",sum_two(2,3))

#variable scope
def my_func():
    x=300
    print(x)

my_func()


#function inside function
def func():
    x=20
    def inner_func():
        print(x)
    inner_func()
func()


# Global Scope
var1="Global Scope"
def global_scope():
    print(var1)

global_scope()
print(var1)

#Naming variables same inside and outside function, python will treat different.
var2="Global Variable"
def global_scope():
    var2="Local Variable"
    print(var2)

global_scope()

print(var2)

# **kwargs is used to accept any number of arguments in python
def stu_data(**student):
    print("Type",type(student))
    print("Name : ",student["name"])
    print("Age : ",student["age"])
    print("All data : ",student)

stu_data(name="Anshit",age=24,city="Berlin")

#Combine *args and **kwargs
# 1. regular parameters
# 2. *args
# 3. **kwargs
def combine(title,*args,**kwargs):
    print("Title : ",title)
    print("Positional Arguments :", args)
    print("Keyword Arguments :",kwargs)

combine("User Info","Anshit Verma",24,city="Lucknow")

#* and ** operators can also be used to unpack list when calling function
# Unpacking lists with *
def sum(a,b,c):
    return a+b+c

numbers=[1,2,3]
result=sum(*numbers)
print(result)

# Unpacking dictionaries with **
def full_name(fname,lname):
    print("Hello, ",fname,lname)

person={"fname":"Anshit","lname":"Verma"}
full_name(**person)

# nonlocal keyword is used to work with variables inside functions.
# the nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
    y="Jane"
    def myfunc2():
        nonlocal y
        y="hello"
    myfunc2()
    return y

print(myfunc1( ))

#Decorator in python
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "decorator function in python"
print(myfunction())