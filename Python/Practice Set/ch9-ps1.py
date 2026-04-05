# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
i = open("twinkle.txt")
content = i.read()
if("twinkle" in content):
    print("The word Twinkle is present in the content")

else:
    print("The word Twinkle is not in the content")