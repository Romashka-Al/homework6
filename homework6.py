my_dict_hours_of_Dota2 = {'3loy_Chel': 5173, 'Yaggi': 9801, "Loli": 14001, "Ромашка": 0.1}
print(my_dict_hours_of_Dota2)
print(my_dict_hours_of_Dota2.get('Loli'), my_dict_hours_of_Dota2.get('zxc'))
my_dict_hours_of_Dota2.update({"Mayor_Degtyarov": 55.5, "Drakosha": 0})
print(my_dict_hours_of_Dota2.pop('3loy_Chel'))
print(my_dict_hours_of_Dota2)

my_set = {1, 1, 'zxc', 1, False, False, 'zxc'}
print(my_set)
my_set.update({13, 73})
my_set.remove(1)
print(my_set)