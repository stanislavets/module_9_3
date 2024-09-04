first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин строк
def difference_lengths():
    for f, s in zip(first, second):
        if len(f) != len(s):
            yield abs(len(f) - len(s))

# Генераторная сборка для сравнения длин строк в одинаковых позициях
def same_position_lengths():
    for i in range(len(first)):
        yield len(first[i]) == len(second[i])

# Вывод результатов
first_result = list(difference_lengths())
second_result = list(same_position_lengths())

print(first_result)
print(second_result)
