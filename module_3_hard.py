'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №3.hard
Дополнительное практическое задание по модулю:"Подробнее о функциях"
'''


'''
Реализована функция по принципу т.н. "Машины Тьюринга" по работе с лентой символов
(вариант решения, по всей видимости, альтернативный - для разнообразия :) ...
'''
def turing_machine(data_structure):
    string = str(data_structure).lower() # Преобразование структуры данных в "ленту символов" и заодно все буквы - прописные
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] # Задание полного набора цифр (для определения цифр на "ленте"
    full_digit = '' # Для формирования единого числа из цифр на "ленте"
    count_sign = 0 # Счетчик искомых символов и чисел
    
    # Блок формирования начальных значений для "для начального статуса - q0 логического устройства машины"
    apostrophe_trigger = False # Триггер для встречающихся на "ленте" символов ' :True-строка символов началась,False-закончилась
    digit_flag = False # Флаг "на ленте идут цифры" - для формирования полного числа
    
    # Запуск "машины в работу" - "лента начинает движение под считывающей головкой машины"
    for sign in string: # q0 - qz, где: q - это "sign", qz - это "in string"
        # Реализация блока логики "машины"
        if sign == "'":
            apostrophe_trigger = not apostrophe_trigger # Если строка начинается или заканчивается - срабатывает логический триггер
            continue
        elif apostrophe_trigger:
            count_sign += 1 # Если с "ленты считался" символ строки - подсчитываем его 
            continue
        elif sign in digits:
            digit_flag = True # Начинаются цифры (а может она всего лишь одна)
            full_digit += sign # Формируем из цифр полное число           
        else:
            if digit_flag: #Если ряд цифр подряд "на ленте" закончился
                count_sign += int(full_digit) # Суммируем значение счетчика с полным числом
                digit_flag = False # Сбрасываем флаг цифр
                full_digit = '' # Сбрасываем числовой накопитель
    return count_sign


# Задание структуры данных
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Обращение к функции
print(turing_machine(data_structure))
