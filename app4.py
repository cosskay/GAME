import random

def read_countries(filename):
    countries = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 2:
                        country, capital = parts[0], parts[1]
                        countries[country] = capital
                    else:
                        print(f"Ошибка в строке: {line}. Ожидалось два значения (страна, столица).")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {filename}: {e}")
    
    return countries if countries else None

def get_random_country(countries):
    country = random.choice(list(countries.items()))
    return country

def guess_country_game(countries):
    if not countries:
        print("Нет доступных данных о странах. Игра не может быть запущена.")
        return
    
    print("Давай сыграем в игру 'Угадай страну'!")
    print("Я буду называть столицу, а ты должен угадать, какая это страна.")
    print("Для выхода из игры введи 'выход'.")

    while True:
        country, capital = get_random_country(countries)
        print(f"Столица: {capital}")
        guess = input("Твой ответ: ").strip().title()

        if guess == 'Выход':
            print("Спасибо за игру!")
            break
        elif guess in countries and countries[guess] == capital:
            print("Правильно! Это", country)
        else:
            print("Неверно. Правильный ответ:", country)

if __name__ == "__main__":
    filename = 'countries.txt'
    countries = read_countries(filename)
    if countries:
        guess_country_game(countries)
