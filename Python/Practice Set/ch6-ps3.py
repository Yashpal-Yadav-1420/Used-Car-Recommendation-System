Text = input("Enter your Text: ")

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

if((p1 in Text) or (p2 in Text) or (p3 in Text) or (p4 in Text)):
    print("It si a spam mail or text")

else:
    print("just read it")