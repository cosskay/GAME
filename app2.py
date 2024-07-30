import random

def guess_number():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("Привет! Давай сыграем в игру. Я загадал число от 1 до 20.")
    
    while True:
        guess = int(input("Попробуй угадать: "))

        attempts += 1

        if guess < number_to_guess:
            print("Твое число слишком маленькое. Попробуй еще раз!")
        elif guess > number_to_guess:
            print("Твое число слишком большое. Попробуй еще раз!")
        else:
            print(f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток!")
            break

if __name__ == "__main__":
    guess_number()
