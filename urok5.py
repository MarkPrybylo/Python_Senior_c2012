import random
words = ["яблуко", "миша", "слон", "апельсин", "кокос", "кіт", "буйвол", "кавун", "жаба", "телевізор", "вугілля", "ведмідь"]
words_color = ["різний", "сірий", "сірий", "помаранчевий", "коричневий", "різний", "коричневий", "зелений", "зелений", "чорний", "чорний", "різний"]
words_lives = [False, True, True, False, False, True, True, False, True, False, False, True]
words_size = ["малий", "малий", "великий", "середній", "середній", "середній", "великий", "великий", "малий", "великий", "малий", "великий"]
i = random.randint(0, len(words) - 1)
word = words[i]
guessed_letters = 0
tries = 0
guessed_text = []
while guessed_letters < len(word):
    if len(guessed_text) > 0:
        print(f"Слово: {guessed_text}{'_' * (len(word) - guessed_letters)}, колір: {words_color[i]}, живе: {words_lives[i]}, розмір: {words_size[i]}")
    else:
        print(f"Слово: {'_' * (len(word))}, колір: {words_color[i]}, живе: {words_lives[i]}, розмір: {words_size[i]}")
    guess = input("Введіть вашу букву: ")
    tries += 1
    if guess in word and guess != "":
        print(f"Правильно! Було спроб: {tries}")
        guessed_text.append(guess)
        guessed_letters += len(guess)
    else:
        print(f"Неправильно! Попробуй ще раз. Було спроб: {tries}")
print(f"Ти відгадав слово! Цим словом було '{word}', і відгадування у вас зайняло {tries} спроб")
