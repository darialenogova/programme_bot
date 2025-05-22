import time
import random
from random import choice
from string import printable
from gtts import gTTS
from num2words import num2words
import datetime


def coffee():
    while True: 
        print("Добро пожаловать! Это кофемашина.")
        time.sleep(3)
        price_of_coffee = 0

        coffee = input("Какое кофе вы хотите (капучино или латте)? ")

        if coffee == "капучино":
            price_of_coffee = 59.45        
        elif coffee == "латте":
            price_of_coffee = 70.7
        else:
            print("Такого нет")
            break

        print("Стоимость кофе:", price_of_coffee)
        money = float(input("Внесённые деньги: "))

        if money >= price_of_coffee:
            print("Оплата прошла успешно. Возьмите сдачу:", money - price_of_coffee)
            time.sleep(5)
            print("Кофе готов")
        elif money < price_of_coffee:
            print("Оплата не прошла. Недостаточно средств.")     
        break

def password():
    password_length = 6
    password = ''.join(choice(printable) for symbol in range(password_length))
    password = password.replace(' ', choice(printable))
    password = password.replace('\t', choice(printable))
    password = password.replace('\n', choice(printable))
    password = password.replace('\x0b', choice(printable))
    password = password.replace('\x0c', choice(printable))
    print('Ваш новый пароль:', password)

def history_aloud():
        message = input("Введите текст, который хотите озвучить:  ")
        language = 'ru'
        audio = gTTS(text=message, lang=language)
        file_name = "history.mp3"
        audio.save(file_name)

def guess_number():
    chance = 0
    number = random.randint(1, 10)
    while chance <= 5:
        print('Я загадал число между 1 и 10. Попробуй отгадать!')
        number_answer = int(input('Введи число: '))
        if number_answer < 1 or number_answer > 10:
            print('Вы ввели число выходящее из заданного диапазона.')
        elif number > number_answer:
            print('Моё число больше, чем введенное тобой.')
        elif number < number_answer:
            print('Моё число меньше, чем введенное тобой.')
        elif number == number_answer:
            print('Угадал, молодец!')
            print(f'Ты справился за {chance + 1} попытки')
            break
        chance += 1

def study_help():
    print("Привет! Я помогу тебе перевести число в английский язык!")
    number = int(input('Какое число необходимо перевести: '))
    print(num2words(number))

def age_determination():
    print("Здравствуй, пользователь!")
    name = input("Представься: ")
    day_birth = int(input("В какой день ты родился? "))
    month_birth = int(input("В какой месяц ты родился? "))
    year_birth = int(input("В каком году ты родился? "))
    date_birth = datetime.date(year_birth, month_birth, day_birth)
    today = datetime.datetime.now().date()
    birth_day = today - date_birth
    user_birth_day = birth_day.days
    age_user = user_birth_day // 365
    print(f"{name}, тебе сейчас {age_user} лет" )

def random_history():
    time_intervals = ['На прошлой неделе', 'Вчера', 'На следующей неделе', 'В ближайшее время','20 января', 'Совсем скоро']
    main_characters = ['кролик', 'слон','мышка', 'верблюд', 'кошка']
    main_characters_names = ['Ксюша', 'Максим', 'Юля', 'Никита', 'Станислава']
    events_country = ['в России', 'в Индии', 'в Германии', 'во Франции', 'в Америке']
    events_place = ['кино', 'университет', 'музей', 'школу', 'дом']
    story_end = ['обрел(а) много друзей', 'съел(а) вкуснятину', 'узнал(а) секрет', 'посмотрел(а) мультик', 'прочитал(а) книгу']
    history = f'{random.choice(time_intervals)} {random.choice(main_characters)} по имени {random.choice(main_characters_names)} живущий {random.choice(events_country)} посетил(а) {random.choice(events_place)} и {random.choice(story_end)}'
    print(history)

def play_bot(name_project):
    if name_project == "1":
        coffee()

    elif name_project == "2":
        password()

    elif name_project == "3":
        history_aloud()

    elif name_project == "4":
        guess_number()

    elif name_project == "5":
        study_help()

    elif name_project == "6":
        age_determination()

    elif name_project == "7":
        random_history()

    else:
        print("Такого проекта нет")

def main():
    print("Привет! Это бот для запуска разных программ. Вот программы, которые можно выбрать:")
    print(""" 1. Кофейный автомат \n 2. Генератор паролей \n 3. История вслух \n 4. Угадай число \n 5. Помощь в обучении \n 6. Определение возраста \n 7. Случайная история""")

    while True:
        name_project = input("Напиши номер программы, которую хочешь запустить: ")
        play_bot(name_project)
        play_again = input("\nХотите запустить другую программу? (да/нет): ")
        if play_again != 'да':
            print("До свидания")
            break


if __name__ == '__main__':
    main()