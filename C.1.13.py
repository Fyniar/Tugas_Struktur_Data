my_list = [1, 2, 3, 4, 5, 7, 9, 10, 12, 14, 21]


def reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp


print(my_list)

print(reverse(my_list))
