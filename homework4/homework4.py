def convert_to_quinary(n):
    """Преобразует десятичное число в пятеричное."""
    if n < 5:
        return str(n)
    else:
        return convert_to_quinary(n // 5) + str(n % 5)

def solve_equation(a, b, c):
    """Решает уравнение x = a + b * 4 - c."""
    return a + b * 4 - c

# Получение ввода от пользователя с проверкой
try:
    a = int(input("Введите целое число a: "))
    b = int(input("Введите целое число b: "))
    c = int(input("Введите целое число c: "))
except ValueError:
    print("Ошибка: Введите целые числа.")
    exit()  # Завершение программы

# Решение уравнения и преобразование в пятеричную систему
x = solve_equation(a, b, c)
quinary_result = convert_to_quinary(x)

print(f"Результат в десятичной системе: {x}")
print(f"Результат в пятеричной системе: {quinary_result}")
