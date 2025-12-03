# [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print(even)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [num for num in numbers if num % 2 == 0]
print(even)

table = []
for i in range(1, 4):
    for j in range(1, 4):
        table.append(i * j)
print(table)

# [expression for item in iterable]
table = [i * j for i in range(1, 4) for j in range(1, 4)]
print(table)

numbers = [-5, 3, 2, -2, 0]
result = ["positive" if num > 0 else "negative" if num < 0 else "zero" for num in numbers]
print(result)

numbers = [1, 2, 3, 4, 5, 5]
squares = {num ** 2 for num in numbers}
print(squares)

users = [("admin", "root"), ("bobbo", "editor"), ("marcus", "hacker")]
roles = {name: role for name, role in users}
print(roles)

numbers = [1, 2, 3, 4, 5]
squares = (num ** 2 for num in numbers)
print(next(squares))
print(next(squares))
print(next(squares))


