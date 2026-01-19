beforeTxt = input("Text: \n")
afterTxt = ""

# reverse text 
for i in range(len(beforeTxt.lower()) -1, -1, -1):
    afterTxt += beforeTxt[i]

# Result Message
print(afterTxt)

if(afterTxt == beforeTxt):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

input("Press anything to close")