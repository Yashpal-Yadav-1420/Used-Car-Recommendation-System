"""def analyze_text(text, top_n=10):

    text = text.lower()
    for char in ":;.!""''()-?" :
        text = text.replace(char, " ")

    words = text.split()


    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1


    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

    return {"word_frequencies": word_freq, "top_words": top_words}


text = "Hello, world! Hello Friends. Today there is a test. A python test, BDA test, FSP test."
result = analyze_text(text)
print(result)"""



"""str = "PYnative"
for i in range(len(str)):
    if i % 2 == 0:  # Checks if the index is even
        print(str[i])"""


"""str = "PYnative"
for i in range(0,7,2):
    print(str[i])"""

"""def fib(n):
   if n <= 1:
    return n
   return fib(n - 1) + fib(n - 2)
x = fib(10)
print(x)"""

"""def greedy_sum(weights, W):
    weights.sort(reverse=True)
    total = 0
    for w in weights:
        if w <= W:
            total += w
            W -= w
    return total
x = [5, 10, 20]
y = 30
z = greedy_sum(x,y)
print(z)"""

"""items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
items.sort(key=lambda x: x[0]/x[1], reverse=True)

value = 0
for val, wt in items:
    if wt <= capacity:
        capacity -= wt
        value += val
    else:
        value += val * (capacity / wt)
        break
print(value)"""

"""items = [(10, 60), (20, 100), (30, 120)]
items.sort(key=lambda x: x[1]/x[0], reverse=True)
print(items)"""

def greedy(arr):
    arr.sort()
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != result[-1]:
            result.append(arr[i])
    return result

