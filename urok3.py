nominal1 = int(input("Введіть перший номінал: "))
nominal2 = int(input("Введіть другий номінал: "))
sum = int(input("Введіть суму, яка вийде із цих монет: "))
a = 0
b = 10
c = 0
a = nominal1 * b
def check_first_n():
    global a
    global b
    while a > sum:
        b -= 1
        a = nominal1 * b
        print(f"{a} = {nominal1} * {b}")
    print(f"Першим номіналом вийшло {a} монет ({nominal1} * {b}).")
check_first_n()
sum2 = a + nominal2
if sum2 > sum:
    a = nominal1 * b
    print(f"{a} = {nominal1} * {b}")
    while a < sum:
        a += nominal2
        if a > sum:
            print(f"\n{a} ({a - nominal2} + {nominal2}) > {sum}\n")
            check_first_n()
            c = 0
        else:
            print(f"{a} = {a - nominal2} + {nominal2}")
            c += 1
        if a == sum:
            break
    print(f"Алгоритм завершений. Вам потрібно {b} монет по {nominal1} та {c} монет по {nominal2}:\n{sum} = {nominal1 * b} + {nominal2 * c}")
else:
    sum2 = a + nominal2
    print(f"{sum2} = {a} + {nominal2}")
    c += 1
    while sum2 < sum:
        c += 1
        sum2 += nominal2
        print(f"{sum2} = {sum2} + {nominal2}")
    print(f"Алгоритм завершений. Вам потрібно {b} монет по {nominal1} та {c} монет по {nominal2}:\n{sum} = {nominal1 * b} + {nominal2 * c}.")
    if sum2 != sum:
        print(f"Правда вам залишеться ще {sum2 - sum} монет")