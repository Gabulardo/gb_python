list_in = input("введите несколько слов через пробел: ")
my_list = []
num = 1
for el in range(list_in.count(' ') + 1):
    my_list = list_in.split()
    if len(str(my_list)) <= 10:
        print(f" {num} {my_list [el]}")
        num += 1
    else:
        print(f" {num} {my_list [el] [0:10]}")
        num += 1
