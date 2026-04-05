'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''

a = input("Enter your paragraph:")
if("Make a lot of money" in a or "buy now" in a or "Subscribe this" in a or "click this" in a ):
    print("This is a Spam")
elif("Make a lot of money" in a and "buy now" in a and "Subscribe this" in a and "click this" in a):
    print("This is a Spam")