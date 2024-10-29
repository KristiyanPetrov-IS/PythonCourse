# Task 1
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('Rectangle', ['start', 'end', 'area'])

def calculate_area(a, b):
    width = abs(a.x - b.x)
    height = abs(a.y - b.y)

    return width * height



def get_areas(starting_points, ending_points, n):
    figures = list(map(lambda start, end: Rectangle(start, end, calculate_area(start, end)), starting_points, ending_points))
    return sorted(list(filter(lambda figure: figure.area > n, figures)), key=lambda figure: figure.area, reverse=True) 



# Task 1 - checks
starting_points = [
    Point(2, 3), 
    Point(0, 0), 
    Point(3, 4), 
    Point(5, 6),
    Point(3, 3),
]
ending_points = [
    Point(3, 4), 
    Point(-5, -9), 
    Point(7, 7), 
    Point(5, 6),
    Point(0, 0),
]

expected_result = [
    Rectangle(Point(x=0, y=0), Point(x=-5, y=-9), 45), 
    Rectangle(Point(x=3, y=4), Point(x=7, y=7), 12),
]

assert get_areas(starting_points, ending_points, 9) == expected_result

starting_points_2 = [
    Point(3, 4),
    Point(2, 3),
    Point(5, 6),
    Point(3, 3),
    Point(0, 0),
]
ending_points_2 = [
    Point(7, 7),
    Point(3, 4),
    Point(5, 6),
    Point(0, 0),
    Point(-5, -9),
]

expected_result_2 = [
    Rectangle(Point(x=0, y=0), Point(x=-5, y=-9), 45),
    Rectangle(Point(x=3, y=4), Point(x=7, y=7), 12),
]

assert get_areas(starting_points_2, ending_points_2, 9) == expected_result_2



# Task 2
COL = 0
ROW = 1
moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
def possible_moves(collumn, row):
    position = (ord(collumn.lower()) - ord('a'), row - 1)
    for move in moves:
        new_position_row = position[ROW] + move[ROW]
        new_position_col = position[COL] + move[COL]
        if 0 <= new_position_row < 8 and 0 <= new_position_col < 8:
            yield (chr(new_position_col + ord('a')), new_position_row + 1)



# Task 2 - checks
# 2 possible moves
assert set(possible_moves('a', 1)) == {('c', 2), ('b', 3)}
assert set(possible_moves('h', 1)) == {('f', 2), ('g', 3)}
assert set(possible_moves('h', 8)) == {('f', 7), ('g', 6)}
assert set(possible_moves('a', 8)) == {('c', 7), ('b', 6)}

# 3 possible moves
assert set(possible_moves('a', 2)) == {('c', 3), ('b', 4), ('c', 1)}
assert set(possible_moves('a', 7)) == {('c', 6), ('b', 5), ('c', 8)}
assert set(possible_moves('h', 2)) == {('g', 4), ('f', 1), ('f', 3)}
assert set(possible_moves('h', 7)) == {('f', 6), ('g', 5), ('f', 8)}

# 4 possible moves
assert set(possible_moves('a', 3)) == {('c', 4), ('b', 5), ('b', 1), ('c', 2)}
assert set(possible_moves('h', 6)) == {('g', 8), ('f', 5), ('g', 4), ('f', 7)}
assert set(possible_moves('g', 2)) == {('e', 1), ('f', 4), ('h', 4), ('e', 3)}

# 6 possible moves
assert set(possible_moves('b', 3)) == {('c', 5), ('d', 2), ('c', 1), ('d', 4), ('a', 5), ('a', 1)}
assert set(possible_moves('g', 6)) == {('f', 4), ('h', 4), ('e', 5), ('e', 7), ('h', 8), ('f', 8)}

# 8 possible moves
assert set(possible_moves('d', 4)) == {('b', 3), ('b', 5), ('c', 2), ('c', 6), ('e', 2), ('e', 6), ('f', 3), ('f', 5)}
assert set(possible_moves('f', 6)) == {('h', 7), ('g', 8), ('e', 8), ('g', 4), ('d', 5), ('e', 4), ('h', 5), ('d', 7)}

# Generator tests
for move in possible_moves('a', 1):
    assert move in {('c', 2), ('b', 3)}

generator = possible_moves('a', 1)
assert next(generator) in {('c', 2), ('b', 3)}
assert next(generator) in {('c', 2), ('b', 3)}

try:
    next(generator)
    assert False
except StopIteration:
    pass



# Task 3
def take(iterable, n):
    if n >= 0:
        for i in range(len(iterable)): 
            if i < n:
                yield iterable[i]
    else:
        for i in range(len(iterable) + n, len(iterable)):
            yield iterable[i]



# Task 3 - checks
sample = [1, 2, 3, 4, 5, 6]

expected_1 = [1, 2, 3]
actual_1 = list(take(sample, 3))

expected_2 = []
actual_2 = list(take(sample, 0))

expected_3 = [1, 2, 3, 4, 5, 6]
actual_3 = list(take(sample, 10))

expected_4 = [1, 2, 3, 4]
actual_4 = list(take(sample, 4))

expected_5 = [5, 6]
actual_5 = list(take(sample, -2))

expected_5 = [3, 4, 5, 6]
actual_5 = list(take(sample, -4))

assert expected_1 == actual_1
assert expected_2 == actual_2
assert expected_3 == actual_3
assert expected_4 == actual_4
assert expected_5 == actual_5


# Task 4
def pretty_print(matrix):
    print('-' * (len(matrix[0]) * 2 - 1))
    for row in matrix:
        print(' '.join(str(item) for item in row))
    print('-' * (len(matrix[0]) * 2 - 1))


def get_column(matrix, column):
    return list(map(lambda row: row[column], matrix))

def rotate_clockwise(matrix):
    return list(map(lambda col: get_column(matrix, col)[::-1], range(len(matrix[0]))))
    
def rotate_counterclockwise(matrix):
    return list(map(lambda col: get_column(matrix, len(matrix[0]) - 1 - col), range(len(matrix[0]))))

def flip_horizontal(matrix):
    return list(map(lambda row: row[::-1], matrix))
    
def flip_vertical(matrix):
    return matrix[::-1]



# Task 4 - checks
matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

expected_clockwise_1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
expected_counterclockwise_1 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
expected_flip_horizontal_1 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
expected_flip_vertical_1 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

assert rotate_clockwise(matrix_1) == expected_clockwise_1
assert rotate_counterclockwise(matrix_1) == expected_counterclockwise_1
assert flip_horizontal(matrix_1) == expected_flip_horizontal_1
assert flip_vertical(matrix_1) == expected_flip_vertical_1


matrix_2 = [[1, 2], [3, 4], [5, 6], [7, 8]]

expected_clockwise_2 = [[7, 5, 3, 1], [8, 6, 4, 2]]
expected_counterclockwise_2 = [[2, 4, 6, 8], [1, 3, 5, 7]]
expected_flip_horizontal_2 = [[2, 1], [4, 3], [6, 5], [8, 7]]
expected_flip_vertical_2 = [[7, 8], [5, 6], [3, 4], [1, 2]]

assert rotate_clockwise(matrix_2) == expected_clockwise_2
assert rotate_counterclockwise(matrix_2) == expected_counterclockwise_2
assert flip_horizontal(matrix_2) == expected_flip_horizontal_2
assert flip_vertical(matrix_2) == expected_flip_vertical_2


matrix_3 = [[1, 2, 3], [4, 5, 6]]

expected_clockwise_3 = [[4, 1], [5, 2], [6, 3]]
expected_counterclockwise_3 = [[3, 6], [2, 5], [1, 4]]
expected_flip_horizontal_3 = [[3, 2, 1], [6, 5, 4]]
expected_flip_vertical_3 = [[4, 5, 6], [1, 2, 3]]

assert rotate_clockwise(matrix_3) == expected_clockwise_3
assert rotate_counterclockwise(matrix_3) == expected_counterclockwise_3
assert flip_horizontal(matrix_3) == expected_flip_horizontal_3
assert flip_vertical(matrix_3) == expected_flip_vertical_3



# Task 5
def sdrawkcab(function):
    def reverse_string(data):
        if (isinstance(data, str)):
            return data[::-1]
        return data

    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        
        if isinstance(result, list):
            return list(map(lambda elem: reverse_string(elem), result))
        return reverse_string(result)  
    return inner


@sdrawkcab
def my_string_function(name):
    return f"Hello, {name}"

@sdrawkcab
def my_non_string_function():
    return 42

@sdrawkcab
def list_of_strings():
    return ["ab", "yaj", "yaj"]

@sdrawkcab
def list_of_ints():
    return [15, 16]

@sdrawkcab
def mixed_list():
    return [15, 16, "si", "a", "doog", "ecalp", "ot", "evah", "a", "reeb", "."]



# Task 5 - checks
expected_my_string_function_1 = "obuyL ,olleH"
expected_my_non_string_function = 42
expected_my_string_function_2 = "backwards ,olleH"
expected_list_of_strings = ["ba", "jay", "jay"]
expected_list_of_ints = [15, 16]
expected_mixed_list = [15, 16, "is", "a", "good", "place", "to", "have", "a", "beer", "."]

assert my_string_function("Lyubo") == expected_my_string_function_1
assert my_non_string_function() == expected_my_non_string_function
assert my_string_function("sdrawkcab") == expected_my_string_function_2
assert list_of_strings() == expected_list_of_strings
assert list_of_ints() == expected_list_of_ints
assert mixed_list() == expected_mixed_list