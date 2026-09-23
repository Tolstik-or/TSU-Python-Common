newgame = "Y" # Подготовка для новой игры

def charac_checker(word):
    russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in word:
        if char not in russian: 
            return False
        else:
            return True
        # return word != all(char in russian for char in word)

def hmm(writ,wha): 
    #функция возвращает какие буквы 
    #из введённого слова (writ) 
    #есть в загаданном слове (wha)

    #красные буквы - нету в слове
    #белые буквы - есть в слове, но не на своём месте
    #зелёные буквы - на своём месте

    res = "[ "
    for i in range(0,len(writ)-1): #смотрим, какие буквы находятся на своём месте
        if writ[i] == wha[i]: res = res + "\033[92m" + writ[i] + "\033[0m | "#print(writ[i],"находится на своём месте")
        elif writ[i] in wha: res = res + writ[i] + " | " #print(writ[i],"есть в загаданном слове")
        else: res = res + "\033[91m" + writ[i] + "\033[0m | " #print(writ[i],"нету в загаданном слове")

    if writ[len(writ)-1] == wha[len(writ)-1]: res = res + "\033[92m" + writ[len(writ)-1] + "\033[0m ]"
    elif writ[len(writ)-1] in wha: res = res + writ[len(writ)-1] + " ]"
    else: res = res + "\033[91m" + writ[len(writ)-1] + "\033[0m ]"

    print(res)

#hmm("abc","acd")

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
            
            hmm(guess,word)# Показываем угаданные буквы и подсвечиваем их нужным цветом.
            
            print("У вас осталось", turns, "шага")
            
    newgame = input("Хотите попробовать снова? Y/N ") # Запускаем новую игру
