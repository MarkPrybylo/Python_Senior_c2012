import random
menu = ""
maxnum = 0
maxtries = 0
history = []
while menu.lower() != "стоп":
    menu = input("Ласкаво просимо у гру 'Вгадай число'! Ваш вибір:\n    грати - грати у гру,\n"
                 "    стат - статистика (лише за цю гру)\n    стоп - припинити грати\nВиберіть варіант: ")
    if menu.lower() == "грати":
        difficulty = int(input("Виберіть складність за допомогою цифр.\n   0 - проста (5 спроб, від 1 до 10)\n"
                               "   1 - середня (3 спроби, від 1 до 25)\n   2 - складна (3 спроби, від 1 до 50)\n"
                               "Ваш вибір: "))
        if difficulty == 0:
            maxtries = 5
            maxnum = 10
        elif difficulty == 1:
            maxtries = 3
            maxnum = 25
        elif difficulty == 2:
            maxtries = 3
            maxnum = 50
        else:
            print("Невідома складність!")
        tries = 0
        num = random.randint(1, maxnum)
        while tries < maxtries:
            guess = int(input("\nВгадай число: "))
            if guess > num:
                print(f"Число менше {num}")
                tries += 1
            elif guess < num:
                print("Число більше")
                tries += 1
            else:
                print("Ви вгадали!")
                tries += 1
                break
        print(f"Гра завершена! Правильною цифрою була {num}, у вас це зайняло {tries} спроб.")
        game_list = [num, tries]
        history.append(game_list)
    elif menu.lower() == "стат":
        print("\nВаша статистика:")
        for i in history:
            print(f"Гра {history.index(i)}: число {i[0]}, спроб {i[1]}")