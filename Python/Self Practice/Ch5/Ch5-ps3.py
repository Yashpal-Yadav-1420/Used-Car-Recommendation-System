# Can we have a set with 18 (int) and '18' (str) as a value in it? - Yes
a = {18, "18"}
print(a)

s = set()
s.add(18)
s.add("18")

print(s)