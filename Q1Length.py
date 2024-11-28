# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

for _ in iter(int, 1): 
    word = input("Enter a word (or 'quit' to exit): ")
    if word == "quit":
        break
    print(f"Length: {len(word)}")
