import numpy
from simplex import SimplexMethod

def is_pure(matrix):
    max_min = None
    min_max = None
    x = -1
    y = -1

    for i in range(len(matrix)):
        cur_max = min(matrix[i])
        if max_min is None or cur_max > max_min:
            max_min = cur_max
            y = i

    for i in range(len(matrix[0])):
        cur_min = max(matrix[:, i])
        if min_max is None or cur_min < min_max:
            min_max = cur_min
            x = i

    if min_max == max_min:
        return True, y, x, max_min
    else:
        return False, -1, -1, -1

def try_solve(matrix):
    pure = is_pure(matrix)
    if pure[0]:
        print("Чистая стратегия применима, седловая точка:", pure[1], pure[2])
        print("Цена игры = ", pure[3])
        print("Матожидание = ", pure[3])
    else:
        print("Чистая стратегия не применима")
        print("Матрица для решения Задачи Линейного Программирования:")
        print(matrix)

def task_1():
    matrix = numpy.array([
        [90.0, 76.5, 91.5, 91.5],
        [103.5, 90.0, 91.5, 103.5],
        [88.5, 88.5, 90.0, 103.5],
        [88.5, 76.5, 76.5, 90.0]
    ])
    print("Task 1:")
    print(is_pure(matrix))
    print('-' * 50)
    print()

def task_2():
    simplex = SimplexMethod.read_file(f'./input/task2.txt')
    print("Task 2:")
    print(simplex.solve())
    print(simplex.get_solution())
    print('-' * 50)
    print()

def task_3():
    simplex = SimplexMethod.read_file(f'./input/task3.txt')
    print("Task 3:")
    print(simplex.solve())
    print(simplex.get_solution())
    print("-" * 50)
    print()


def task_4():
    matrix = numpy.array([
        [4, 2],
        [2, 3]
    ])
    print("Task 4:")
    try_solve(matrix)
    simplex = SimplexMethod.read_file(f'./input/task4.txt')
    solve = simplex.solve()
    solution = simplex.get_solution()
    print("Target: ", solve)
    print("Solution: ", solution)
    print("Оптимальное решение в смешанной стратегии: ", [solution[i] / solve for i in range(len(solution[:-2]))])
    print("Цена игры", 1 / solve)
    print("-" * 50)
    print()


def task_5():
    matrix = numpy.array([
        [8, 4, 6],
        [4, 8, 5]
    ])
    print("Task 5:")
    try_solve(matrix)
    simplex = SimplexMethod.read_file(f'./input/task5.txt')
    solve = simplex.solve()
    solution = simplex.get_solution()
    print("Target: ", solve)
    print("Solution: ", solution)
    print("Оптимальное решение в смешанной стратегии: ", [solution[i] / solve for i in range(len(solution))])
    print("Цена игры", 1 / solve)
    print("-" * 50)
    print()

def task_6():
    matrix = numpy.array([
        [7, 2, 5, 1],
        [2, 2, 3, 4],
        [5, 3, 4, 4],
        [3, 2, 1, 6]
    ])
    print("Task 6:")
    try_solve(matrix)
    print('-' * 50)
    print()


def task_7():
    x = numpy.array([6 / 13, 3 / 13, 4 / 13])
    y = numpy.array([6 / 13, 4 / 13, 3 / 13])
    matrix = numpy.array([
        [1, -1, -1],
        [-1, -1, 3],
        [-1, 2, -1]
    ])
    print("Task 7:")
    print("Матожидание проигрыша первого игрока: ", -(x @ matrix @ y.T))
    print('-' * 50)
    print()


def task_8():
    matrix = numpy.array([
        [7, 1],
        [2, 11]
    ])
    print("Task 8:")
    try_solve(matrix)
    simplex = SimplexMethod.read_file(f'./input/task8.txt')
    solve = simplex.solve()
    solution = simplex.get_solution()
    print("Target: ", solve)
    print("Solution: ", solution)
    print("Оптимальное решение в смешанной стратегии: ", [solution[i] / solve for i in range(len(solution[:-2]))])
    print("Цена игры: ", 1 / solve)
    print("-" * 50)
    print()

def task_9():
    matrix = numpy.array([
        [2, 5, 1],
        [3, 4, 4],
        [2, 1, 6]
    ])
    print("Task 9:")
    try_solve(matrix)
    print('-' * 50)
    print()

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
