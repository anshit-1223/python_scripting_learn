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
