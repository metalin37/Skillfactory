"""Игра угадай число"""

import numpy as np

def random_predict(number: int=np.random.randint(1, 101)) -> int:
    
    min = 1
    max = 100

    predict_number = int(np.random.randint(min, max + 1))  #программа начинает отгадывать число
    count = 0  #подсчет количества попыток на отгадывание числа

    while predict_number != number:
        count += 1
    
        if predict_number > number:
            max = predict_number
            predict_number = (min + max) // 2
        
        elif predict_number < number:
            min = predict_number
            predict_number = (min + max) // 2
            
        else:
            break 
        if count > 20: break#конец игры и выход из цикла
    #print(f"Робот угадал число! Это число = {number}, за {count} попыток.")
    return count

#print(random_predict(2))
def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(np.random.randint(1, 10)) # не фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список рандомных чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки.")
    return score

score_game(random_predict)