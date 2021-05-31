def sum_of_squares_odd2(n):
    return sum([a * a for a in range(0, n) if a % 2 != 0])


print(sum_of_squares_odd2(10))
