my_dict = {'Nastya': 'Vladivostok', 'Sveta': 'Krasnoyarsk', 'Masha': 'Novosibirsk'}
print(my_dict)
print(my_dict['Sveta'])
print(my_dict.get('Anton'))
my_dict.update({'Kristins': 'Tomsk', 'Lida': 'Tayga'})
print(my_dict)
del1 = my_dict.pop('Masha')
print(del1)
print(my_dict)

my_set = {1, 2, 3, 3.14, 'one', 1, 2, 'one'}
print(my_set)
my_set.add(5)
my_set.add('all')
print(my_set)
my_set.discard('one')
print(my_set)