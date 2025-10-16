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