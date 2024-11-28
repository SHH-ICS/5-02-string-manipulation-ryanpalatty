# Create a program that will accept a word and output the word one letter at a time in reverse.
word = input("Enter a word (or type 'quit' to exit): ")

while word.lower() != "quit":
    print("The word in reverse, one letter at a time:")
    for letter in reversed(word):
        print(letter)
    word = input("Enter another word (or type 'quit' to exit): ")

print("Goodbye!")