def ReverseString(input_str):
    return input_str[::-1]

def main():
    input_str = "Hello, World!"
    print("Original string: ", input_str)
    reversed_str = ReverseString(input_str)
    print("Reversed string: ", reversed_str)

if __name__ == "__main__":
    main()
