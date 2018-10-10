def string_var(ove):
    print(ove)
    print(ove[-3:])
    print(ove[3:11])
    print(ove[0:2])


print("-"*50,"\nString task: ")
string_var("This is a string that is over 20 characters long.")
print("-"*50,"\n")


def list_var(num_seq_list):
    print(num_seq_list)
    print(num_seq_list[0] - num_seq_list[1])
    print(num_seq_list[1] + num_seq_list[2] + num_seq_list[4])
    num_seq_list[0] = (num_seq_list[0]*num_seq_list[1])
    print(num_seq_list)


print("List task: ")
list_var([9, 162, 2, 99, 12])
print("-"*50,"\n")


def tuple_var(num_seq_tuple):
    print(num_seq_tuple)
    print((num_seq_tuple[0] + num_seq_tuple[1]) / 2)
    num_seq_tuple = (num_seq_tuple[1], num_seq_tuple[0])
    print(num_seq_tuple)


print("Tuple task: ")
tuple_var((1.05, 5.23))
print("-"*50,"\n")
