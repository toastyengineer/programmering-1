def string_var(ove):
    print(ove)
    print(ove[-3:])
    print(ove[3:10])
    print(ove[0:2])


string_var("Det var en gång en man som hette Ove")
print()


def list_var(num_seq_list):
    print(num_seq_list)
    print(num_seq_list[0] - num_seq_list[3])
    print(num_seq_list[1] + num_seq_list[2] + num_seq_list[4])
    num_seq_list[0] = (num_seq_list[0]*num_seq_list[1])
    print(num_seq_list)


list_var([9, 162, 2, 99, 12])
print()


def tuple_var(num_seq_tuple):
    print(num_seq_tuple)
    print((num_seq_tuple[0] + num_seq_tuple[1]) / 2)
    num_seq_tuple = (num_seq_tuple[1], num_seq_tuple[0])
    print(num_seq_tuple)


tuple_var((1.05, 5.23))