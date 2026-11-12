# Write a function to count vowels in a string

def count_char(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    print("Total vowels", count)

text_in = input("Enter text here: ")

count_char(text_in)