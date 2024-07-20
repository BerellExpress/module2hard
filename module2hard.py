def generate_password(n):
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i, n + 1)]
    filtered_pairs = [pair for pair in pairs if n % (pair[0] + pair[1]) == 0]
    return ''.join(map(str, filtered_pairs))

number = int(input("Введите число от 3 до 20: "))
password = generate_password(number)
print(f"Пароль для числа {number}: {password}")
