words = ["Donkey", "bad", "ganda"]

with open("This.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("This.txt", "w") as f:
    f.write(content)