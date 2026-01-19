beforeTxt = input("Text: \n")
afterTxt = ""

for i in range(len(beforeTxt.lower()) -1, -1, -1):
    afterTxt += beforeTxt[i]

print(afterTxt)

if(afterTxt == beforeTxt):
    print("Its a palindrome")
else:
    print("Its not a palindrome")