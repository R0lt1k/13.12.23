def plus_two(number):
    try:
        result = int(number) + 2
        print(f"Результат: {result}")
    except ValueError:
        print("Введено некорректное значение.")
        
input_number = input("Введите число: ")
plus_two(input_number)
