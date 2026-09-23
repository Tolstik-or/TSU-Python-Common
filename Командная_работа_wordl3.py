newgame = "Y" # Подготовка для новой игры

def charac_checker(word):
    russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in word:
        if char not in russian: 
            return False
        else:
            return True
        # return word != all(char in russian for char in word)

while newgame == "Y":
    # Начинаем игру и подготавливаем нужные технические значения
    print("HELLO, WORLDLE")
    word = "скоро"
    guess = None
    turns = 5
    while guess != word:
        guess = input("Введите слово: ")

        if guess == '':
            print('Вам нужно что-то ввести.')

        elif len(guess) != 5:
            print('Мы принимаем только слова из 5 букв.')

        elif (charac_checker(guess) == False):
            print('В вашем слове есть что-то, кроме русских букв.')
        
        elif guess == word: # Механика выигрыша
            print("Вы победили!")
            print(guess)
            break
        
        else:
            turns -= 1 # Механика прохождения ходов
            if turns == 0: # Механика проигрыша
                print("Вы проиграли!")
                print(word)
                break
            
            hint = list() # Механика подсказки, какие буквы игрок угадал
            for i in range(len(word)):
                if guess[i] == word[i]:
                    hint.append(guess[i])
                else:
                    hint.append("?")
            print(hint)
            
            print("У вас осталось", turns, "шага")
            
    newgame = input("Хотите попробовать снова? Y/N ") # Запускаем новую игру
