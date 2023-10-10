def f(x):
    return x ** 3 - 4 * x ** 2 + 2


def df(x):
    return 3 * x ** 2 - 6 * x


def newton_method(x0, epsilon=1e-4, max_iterations=1000):
    for i in range(max_iterations):
        x1 = x0 - f(x0) / df(x0)

        print(f'Итерация {i + 1}: x = {x1}, f(x) = {f(x1)}')

        if abs(x1 - x0) < epsilon:
            print(f"Успешно достигнута точность {epsilon} за {i + 1} итераций.")
            return x1

        x0 = x1

    raise ValueError(f"Не удалось достичь точности {epsilon} за {max_iterations} итераций.")


x0 = float(input("Введите начальное значение x0: "))

result = newton_method(x0)

print(f"Приближенный корень: {result}")
