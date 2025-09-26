print("Введите первое число:")
first = int(input())
while first != int(first):
    print("Введите цифру или число:")
    first = input()
print("Введите второе число")
second = int(input())
while second != int(second):
    print("Введите цифру или число:")
    secnond = input()
print("Введите операцию для чисел: (+, -, /, *)")
operation = input()
result = f"{first}{operation}{second}"
print(f"Результат операции {first} {operation} {second} = {eval(result)}")