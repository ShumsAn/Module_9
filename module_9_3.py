first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second,
# если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.

first_zip = zip((len(x) for x in first), (len(y) for y in second))
first_result = (x[0]-x[1] for x in first_zip if x[0]-x[1] != 0)

# В second_result запишите  генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

second_result = ((len(first[x])) == (len(second[x])) for x in range(len(first)))

print(list(first_result))
print(list(second_result))





