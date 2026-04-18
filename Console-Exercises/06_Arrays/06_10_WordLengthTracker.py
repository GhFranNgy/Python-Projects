value_Words = {}
occurence_Words = {}

while True:
    sentence = input("Enter\n")
    if sentence.strip() == "": 
        print("Invalid input")
        continue
    break

list_Words = [word.strip(".,!?") for word in sentence.split()]

for word in list_Words:

    key = len(word)

    # counter of same length
    if key in value_Words:
        value_Words[key].append(word)
    else:
        value_Words[key] = [word]

    # counter of same word
    if word in occurence_Words:
        occurence_Words[word] += 1
    else:
        occurence_Words[word] = 1

most_common_word = None
highest_count = 0

for word, count in occurence_Words.items():
    if count > highest_count:
        highest_count = count
        most_common_word = word

print("\nMost common word:", most_common_word, "\n")
print(value_Words, "\n")
print(occurence_Words)