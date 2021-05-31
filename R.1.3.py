def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [1, 2, 3, 4, 6, 6, 7, 8, 20]

print(minmax(alpha))
