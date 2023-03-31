def greet(name):
    return f"Hello, {name}!"

def main():
    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting)

if __name__ == "__main__":
    main()
