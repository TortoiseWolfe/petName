def greet(name):
    return f"Hi, {name}!"

def get_name():
    return input("Please enter your name: ")

name = get_name()
print(greet(name))