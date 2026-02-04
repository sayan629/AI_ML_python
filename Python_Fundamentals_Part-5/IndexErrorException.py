
numbers = [10, 20, 30, 40]


try:
    # Attempt to access an invalid index
    print(numbers[6])


except IndexError:
    print("Index out of range. Please use a valid index.")
