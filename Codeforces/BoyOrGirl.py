def distinct_char(s):
    unique_char = set(s)
    return len(unique_char)


username = input("")

length = distinct_char(username)
if length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
