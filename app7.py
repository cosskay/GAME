from PIL import Image
import requests
from io import BytesIO
import random

# Словарь с парами "название страны" : "URL флага страны"
flags = {
    'Австралия': 'https://flagpedia.net/data/flags/h80/au.png',
    'Бразилия': 'https://flagpedia.net/data/flags/h80/br.png',
    'Канада': 'https://flagpedia.net/data/flags/h80/ca.png',
    'Германия': 'https://flagpedia.net/data/flags/h80/de.png',
    'Франция': 'https://flagpedia.net/data/flags/h80/fr.png',
    'Италия': 'https://flagpedia.net/data/flags/h80/it.png',
    'Япония': 'https://flagpedia.net/data/flags/h80/jp.png',
    'Россия': 'https://flagpedia.net/data/flags/h80/ru.png',
    'Испания': 'https://flagpedia.net/data/flags/h80/es.png',
    'Великобритания': 'https://flagpedia.net/data/flags/h80/gb.png'
}

def display_flag(country):
    url = flags[country]
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def guess_flag_game():
    print("Давай поиграем в игру 'Угадай флаг страны'!")
    countries = list(flags.keys())
    random_country = random.choice(countries)
    correct_answer = random_country
    
    while True:
        print("Угадай флаг какой страны я загадал:")
        display_flag(random_country)
        guess = input("Название страны: ").strip().capitalize()
        
        if guess == correct_answer:
            print(f"Поздравляю, правильный ответ - {correct_answer}!")
            break
        else:
            print(f"Неверно! Попробуй еще раз.")

guess_flag_game()
