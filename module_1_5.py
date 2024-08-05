immutable_var = (1, '2', [3, 4])
print(immutable_var)
immutable_var[2].append(5)
'''Кортежи являются неизменяемым типом данных. 
Но они могут содержать в себе изменяемые элементы, как в данном примере. 
Список внутри кортежа изменить можно.'''
print( immutable_var)
print(type( immutable_var))

mutable_list = [1, 2, '3', 'start']
print(mutable_list)
mutable_list[2] = 3
print(mutable_list)
print(type(mutable_list))