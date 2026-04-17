import random

def calculator():
    while True:
        print("\n=== Меню калькулятора ===")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("0. Выход в главное меню")
        number_choice = input("Ваш выбор: ")

        if number_choice == '0':
            break

        if number_choice not in ('1', '2', '3', '4'):
            print("Неверный выбор, попробуйте снова.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числа!")
            continue

        if number_choice == '1':
            c = a + b
            print(f"Результат сложения: {c}")
        elif number_choice == '2':
            c = a - b
            print(f"Результат вычитания: {c}")
        elif number_choice == '3':
            c = a * b
            print(f"Результат умножения: {c}")
        elif number_choice == '4':
            if b == 0:
                print("Ошибка: деление на ноль!")
            else:
                c = a / b
                print(f"Результат деления: {c}")

def random_number():
    try:
        low = int(input("Нижняя граница: "))
        high = int(input("Верхняя граница: "))
        if low > high:
            low, high = high, low
        print(f"Случайное число: {random.randint(low, high)}")
    except ValueError:
        print("Ошибка: введите целые числа!")
def temperature_converter():
    print("1. Цельсий → Фаренгейт")
    print("2. Фаренгейт → Цельсий")
    choice = input("Выберите направление: ")
    try:
        temp = float(input("Введите температуру: "))
        if choice == '1':
            print(f"{temp}°C = {temp * 9/5 + 32}°F")
        elif choice == '2':
            print(f"{temp}°F = {(temp - 32) * 5/9}°C")
        else:
            print("Неверный выбор")
    except ValueError:
        print("Ошибка: введите число!")