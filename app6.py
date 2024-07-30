import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import random

# Функция для получения URL изображения флага страны с помощью API Flagpedia.net
def get_flag_url(country_code):
    url = f"https://flagpedia.net/data/flags/h80/{country_code}.png"
    return url

# Функция для парсинга страницы Flagpedia.net и получения списка стран и их кодов
def get_countries():
    try:
        url = "https://flagpedia.net/index"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем успешность запроса
        soup = BeautifulSoup(response.content, 'html.parser')
        countries = {}

        # Находим таблицу с флагами и странами
        table = soup.find('table', class_='table-bordered')
        rows = table.find_all('tr')

        for row in rows[1:]:  # Пропускаем первую строку с заголовками
            columns = row.find_all('td')
            country_name = columns[0].text.strip()
            country_code = columns[2].text.strip().upper()
            countries[country_name] = get_flag_url(country_code)

        return countries
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return None

# Функция для отображения флага страны
def display_flag(country, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        img = Image.open(BytesIO(response.content))
        img.show()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")

# Основная функция игры
def guess_flag_game():
    print("Давай поиграем в игру 'Угадай флаг страны'!")
    
    # Получаем словарь со странами и URL их флагов
    flags = get_countries()
    
    if not flags:
        print("Не удалось получить данные о странах и флагах. Попробуйте позже.")
        return
    
    while True:
        # Выбираем случайную страну из словаря
        random_country = random.choice(list(flags.keys()))
        correct_answer = random_country
        
        print("Угадай флаг какой страны я загадал:")
        display_flag(random_country, flags[random_country])
        guess = input("Название страны: ").strip().capitalize()
        
        if guess == correct_answer:
            print(f"Поздравляю, правильный ответ - {correct_answer}!")
            break
        else:
            print(f"Неверно! Попробуй еще раз.")

# Запуск игры
guess_flag_game()
