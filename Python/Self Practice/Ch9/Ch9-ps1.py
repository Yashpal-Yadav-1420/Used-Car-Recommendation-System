# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

'''f = open("This.txt", "r")
text = f.read()
print("Twinkle" in text)
f.close''' 

# with loop 
f = open("This.txt", "r")
text = f.read()

if("Twinkle" in text):
    print("Twinkle is present")

else:
    print("Twinkle is not present")
f.close 
