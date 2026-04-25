# Простой, но надёжный калькулятор на Python
# Вторая работа в портфолио — Script Master

def calculator():
    print("=== Простой Калькулятор ===\n")
    
    while True:
        try:
            a = input("Введите первое число (или 'exit' для выхода): ").strip()
            if a.lower() == 'exit':
                print("Программа завершена. До свидания!")
                break
            a = float(a)
            
            b = input("Введите второе число: ").strip()
            if b.lower() == 'exit':
                print("Программа завершена.")
                break
            b = float(b)
            
            action = input("Выберите действие (+, -, *, /): ").strip()
            
            if action == "+":
                result = a + b
            elif action == "-":
                result = a - b
            elif action == "*":
                result = a * b
            elif action == "/":
                if b == 0:
                    print("Ошибка: Деление на ноль невозможно!")
                    continue
                result = a / b
            else:
                print("Ошибка: Неизвестное действие! Используйте только +, -, *, /")
                continue
            
            # Красивый вывод
            print(f"\nРезультат: {a} {action} {b} = {result}\n")
            
        except ValueError:
            print("Ошибка: Пожалуйста, вводите только числа!\n")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}\n")

# Запуск калькулятора
if __name__ == "__main__":
    calculator()
