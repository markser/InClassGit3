# to run the program
# python3 palindrome.py 
# then input string that we want to test as palindrome

def palindrome(userInputString):
    return (userInputString == userInputString[::-1])

def retrieve_input():
    userInputString = (input('Input a string to test if palindrome: '))
    if (isinstance(userInputString, str)):
        if len(userInputString) < 0:
            print("Please input a string with characters")
        else:
            return userInputString
    print("Please enter a character ")

def main():
    userInputString = retrieve_input()
    if (userInputString is not None):
        print(palindrome(userInputString))


if __name__ == "__main__":
    main()
