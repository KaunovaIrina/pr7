def convert(n):
    if n < 5:
        return str(n)
    else:
        return convert(n // 5) + str(n % 5)

number = input("Введите целое простое десятичное число: ")

if number.isdigit():
    number = int(number)
    print(f"Пятеричное представление: {convert(number)}")
else:
    print("Ошибка: введите корректное целое число.")