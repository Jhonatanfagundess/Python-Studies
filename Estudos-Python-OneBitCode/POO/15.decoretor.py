from decoretor import my_decorator,uppercase_decorator,split_strinf

#Exemplo 1
@my_decorator
def my_function():
    print("Dentro da função")

my_function()    


#Exemplo 2
@uppercase_decorator
def text():
    return 'Hello world'

print(text())

#Exemplo 3
@split_strinf
@uppercase_decorator
def example():
    return 'Aprendendo Python'

print(example())
    
    