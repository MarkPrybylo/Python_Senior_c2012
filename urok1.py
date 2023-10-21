# a = int(input("Input num: "))
# b = 0
# i = 0
# while b <= 100:
#     print(b)
#     b += a
#     i += 1
# print(f"I added {a} {i} times")
a = ["pineapple", "pear", "cake", "apple", "lemon", "chocolate", "peach", "candy"]
for i in a:
    if i == "chocolate" or i == "candy" or i == "cake":
        a.remove(i)
print(a)