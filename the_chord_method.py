def f(x):
    return x ** 3 - 4 * x ** 2 + 2


def chord_method(a, b, epsilon=1e-4, max_iterations=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("Метод хорд требует, чтобы f(a) и f(b) имели разные знаки в начальной точке.")

    for i in range(max_iterations):
        c = a - f(a) * (b - a) / (f(b) - f(a))

        print(f'Итерация {i + 1}: x = {c}, f(x) = {f(c)}')

        if abs(f(c)) < epsilon:
            print(f"Успешно достигнута точность {epsilon} за {i + 1} итераций.")
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    raise ValueError(f"Не удалось достичь точности {epsilon} за {max_iterations} итераций.")


a = float(input("Введите начало интервала: "))
b = float(input("Введите конец интервала: "))

result = chord_method(a, b)

print(f"Приближенный корень: {result}")
