def count_words(text):
    #Function to count the number of words in the given text
    
    # Split the text by spaces to get individual words
    words = text.split()
    
    # Return the length of the list of words
    return len(words)
def main():
    
    print("Welcome to the Word Counter program!")
    
    
    # take sentence or paragraph as input from user
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    
    # Checking for empty input
    if not user_input:
        print("Error: You entered an empty string. Please provide some text.")
        return
    
    # Count the number of words in the input
    count = count_words(user_input)
    
    # Display the word count to the user
    print(f"The number of words in the given text is: {count}")
if __name__ == "__main__":
    main()
