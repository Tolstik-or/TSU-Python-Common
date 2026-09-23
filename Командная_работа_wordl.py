newgame = "Y" # Подготовка для новой игры
while newgame == "Y":
    # Начинаем игру и подготавливаем нужные технические значения
    print("WORLDL")
    word = "lorry"
    guess = None
    turns = 5
    while guess != word:
        guess = input("your guess:")    
        
        if guess == word: # Механика выигрыша
            print("You've won!!!")
            print(guess)
            break
        
        else:
            turns -= 1 # Механика прохождения ходов
            if turns == 0: # Механика проигрыша
                print("You've lost!!!")
                print(word)
                break
            
            hint = list() # Механика подсказки, какие буквы игрок угадал
            for i in range(len(word)):
                if guess[i] == word[i]:
                    hint.append(guess[i])
                else:
                    hint.append("?")
            print(hint)
            
            print("You have", turns, "turns left")
            
    newgame = input("Would you like to play again? Y/N ") # Запускаем новую игру
