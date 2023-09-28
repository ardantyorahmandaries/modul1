random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_tuple = ()
string_list = []
int_dict = {}


for item in random_list:
    if isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)
    elif isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[(ratusan, puluhan, satuan)] = item

print("Data float dalam bentuk tuple:", float_tuple)
print("Data string dalam list:", string_list)
print("Data int dalam dictionary:", int_dict)