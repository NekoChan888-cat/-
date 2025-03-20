print("Введите два числа и операцию: ")

num1 = float(input("Первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Второе число: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Неизвестная операция!"

print("Результат:", result)
