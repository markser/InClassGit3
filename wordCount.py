# to run the program
# python3 wordCount.py 
# then input string that we want to retrieve the number of words in the given string

def wordCount(userInputString):
    return (len(userInputString.split()))

def retrieve_input():
    userInputString = (input('Input a string to determine amount of words: '))
    if len(userInputString) < 0:
        print("Please input a string with characters")
    else:
        return userInputString
    print("Please enter a character ")

def main():
    userInputString = retrieve_input()
    print(wordCount(userInputString))
    return wordCount(userInputString)


if __name__ == "__main__":
    main()
