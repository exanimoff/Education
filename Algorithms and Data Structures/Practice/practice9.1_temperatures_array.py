def warming_rate(daily_temp_rate):
    n = len(daily_temp_rate)
    result = [0] * n
    stack = []

    for i in range(n):
        print(f"День {i + 1}: Температура {daily_temp_rate[i]}")

        while stack and daily_temp_rate[i] > daily_temp_rate[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index

            print(f"  Popped индекс {prev_index}, Новый result: {result}")

        stack.append(i)
        print(f"  Appended индекс {i} в стек, стек: {stack}")

    return result

daily_temp_rate = [18, 16, 16, 20, 21, 4, 7, 0, 27]
print(f'Изначальный массив: {daily_temp_rate}')
print('Результат          :', warming_rate(daily_temp_rate))
print(f'Изначальный массив: {daily_temp_rate}')
