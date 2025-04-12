my_dict ={
    tuple: (1, 5, 7, None, 'text', False),
    list: [3, 6, 7, None, 'text', False],
    dict: {1: 3, 2: None, 3: 'Texy', 4: False, 5: 1.567},
    set: {4, 65, None, 'Text', False, 10}
}

print(my_dict[tuple][-1])  # печать последнего элемента

my_dict[list].append('sergei')  # добавление в конец списка еще одиного элемента
my_dict[list].pop(1)  # удалtybt второго  элемента списка

# print(my_dict[list])

my_dict[dict][('i am a tuple',)] = 123456  # добавление элемента
my_dict[dict].pop(2)  # удаление элемента (2)

# print(my_dict[dict])

my_dict[set].add('test')  # добавление нового элемента в множество
my_dict[set].discard(65)  # удаление элемента из множества
#  my_dict[set].remove(65)  # удаление элемента из множества
#  my_dict[set].pop()  # удаление неважно какого элемента из множества
#  print(my_dict[set])

print(my_dict)
