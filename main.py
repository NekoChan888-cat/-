def calculator():
    print("Калькулятор")
    print("Введите 'exit' для выхода.")
    
    while True:
        num1 = input("Первое число: ")
        if num1.lower() == 'exit':
            break
            
        operation = input("Введите операцию (+, -, *, /): ")
        if operation.lower() == 'exit':
            break
            
        num2 = input("Второе число: ")
        if num2.lower() == 'exit':
            break
        
        try:
            num1 = float(num1)
            num2 = float(num2)

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
        except ValueError:
            print("Ошибка: введите правильные числа.")

calculator()
