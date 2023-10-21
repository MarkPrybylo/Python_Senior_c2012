# a = int(input("Input num: "))
# b = 0
# i = 0
# while b <= 100:
#     print(b)
#     b += a
#     i += 1
# print(f"I added {a} {i} times")
a = ["pineapple", "pear", "apple", "peach", "chocolate", "peach", "candy"]
for i in a:
    if i == "chocolate" or i == "candy":
        a.remove(i)
print(a)