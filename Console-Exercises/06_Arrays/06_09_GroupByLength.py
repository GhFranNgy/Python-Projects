while True:
    input_words = str(input("Enter Words, seperate them with a \",\"\n"))

    if input_words == "": print("Your List is empty") 
    else: break

current_Word = ""
list_Words = []

# convert string into list
for char in input_words:
    if char == ",":
        current_Word = current_Word.strip()
        list_Words.append(current_Word)
        current_Word = ""
    else:
        current_Word += char
    
# for last word
current_Word = current_Word.strip()
list_Words.append(current_Word)

# other version:
# list_words = [word.strip() for word in input_words.split(",")]

groups = {}

for word in list_Words:

    length = len(word)

    if length not in groups:
        groups[length] = []

    groups[length].append(word)

print(groups)