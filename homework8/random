import random

def guess_number():
    # Генеруємо випадкове число від 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Вгадайте число від 1 до 100. У вас є 5 спроб.")

    # Починаємо цикл для 5 спроб
    while attempts < 5:
        guess = int(input("Ваше припущення: "))

        # Якщо припущення користувача правильне
        if guess == secret_number:
            print("Вітаємо! Ви вгадали правильне число.")
            return
        
        # Якщо припущення занадто високе
        elif guess > secret_number:
            print("Занадто високо.")
        
        # Якщо припущення занадто низьке
        else:
            print("Занадто низько.")
        
        attempts += 1
        print("У вас залишилося спроб:", 5 - attempts)

    # Якщо використані всі 5 спроб і число так і не вгадане
    print("Вибачте, у вас закінчилися спроби. Правильним числом було", secret_number)

# Викликаємо функцію для початку гри
guess_number()
