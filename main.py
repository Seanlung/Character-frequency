print("This program finds the most repeated character in a piece of text\n")
text = input("Enter your text here:\n")
character_frequency = {}

for char in text:
    if char in character_frequency:
        character_frequency[char] += 1
    else:
        character_frequency[char] = 1

sorted_char_frequency = sorted(character_frequency.items(),
                               key=lambda kv:kv[1],
                               reverse=True)
print(sorted_char_frequency[0])






