def print_params(a=1, b='Anton', c=True):
    print(a, b, c)


values_list = [25, 'Anna', False]
values_dict = {'a': 123, 'b': 'Sergey', 'c': True}
values_list_2 = ['Ron', 45]

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(56, *values_list_2)

