import random

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья!"
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
         (player_choice == 'ножницы' and computer_choice == 'бумага') or \
         (player_choice == 'бумага' and computer_choice == 'камень'):
        return "Ты победил!"
    else:
        return "Компьютер победил!"

def rock_paper_scissors():
    print("Давай сыграем в игру 'Камень, ножницы, бумага'!")
    while True:
        player_choice = input("Выбери камень, ножницы или бумагу (для выхода введи 'выход'): ").lower()
        
        if player_choice in ['камень', 'ножницы', 'бумага']:
            computer_choice = get_computer_choice()
            print(f"Компьютер выбрал: {computer_choice}")
            result = determine_winner(player_choice, computer_choice)
            print(result)
        elif player_choice == 'выход':
            print("Спасибо за игру!")
            break
        else:
            print("Неверный выбор. Попробуй еще раз!")

if __name__ == "__main__":
    rock_paper_scissors()
