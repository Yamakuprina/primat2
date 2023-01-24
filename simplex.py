from __future__ import annotations
import numpy as np
import math
import itertools


class SimplexMethod:
    """Simplex класс реализует Симплекс-метод.
    	Решает задачу оптимизации линейного программирования"""
    a: np.array
    b: np.array
    c: np.array
    is_max: bool
    print_steps: bool
    table: np.array

    def __init__(
            self,
            a: np.array,
            b: np.array,
            c: np.array,
            is_max: bool,
            print_steps: bool = False
    ):
        self.a = a
        self.b = b
        self.c = c
        self.ans = 0
        self.is_max = is_max
        self.print_steps = print_steps
        self.make_new_shape()
        self.based_columns()
        self.b_less_zero_check()

    def b_less_zero_check(self):
        """Исправляет ситуацию, когда b < 0, если таковая существует"""
        if any(x < 0 for x in self.b):
            row_index = np.argmin(self.b)
            column_index = np.argmin(self.a[row_index])
            self.make_simplex_table(row_index, column_index)

    def based_columns(self):
        """Отвечает за создание столбцов, проходя циклами по ширине и длине"""

        columns = np.array(self.table).T
        rows_index = list(range(len(columns[0]) - 1))
        columns_index = list(range(len(columns) - 1))
        count = 0
        for i, col in enumerate(columns[:-1]):
            if self.based(col):
                count = count + 1
                rows_index.remove(np.argmax(col))
                columns_index.remove(np.argmax(columns_index))
        for i in range(len(columns[0]) - 1 - count):
            el_iter = itertools.product(rows_index, columns_index)
            index = next(el_iter)
            while self.table[index[0]][index[1]] == 0:
                index = next(el_iter)
            self.make_simplex_table(index[0], index[1])
            rows_index.remove(index[0])
            columns_index.remove(index[1])

    def make_new_shape(self):
        """Создает таблицы отсартированные по строкам"""

        xb = np.column_stack((self.a, self.b.T))
        z = np.column_stack(([self.c], [[self.ans]]))
        self.table = np.vstack((xb, z))

    @classmethod
    def read_file(cls, path: str) -> cls:
        """Преобразует данные из тестовых файлов в Simplex класс"""
        with open(path, "r") as f:
            is_max = False
            if f.readline().strip() == 'max':
                is_max = True
            f.readline()
            c = [float(num) for num in f.readline().strip().split(',')]
            f.readline()
            a_matrix = []
            for line in f:
                if not line.strip():
                    break
                a_matrix.append([float(num) for num in line.strip().split(',')])
            b_matrix = [float(num) for num in f.readline().strip().split(',')]
            return cls(np.array(a_matrix), np.array(b_matrix), np.array(c), is_max, print_steps=True)

    def is_optimized(self) -> bool:
        """Проверка на валидность столбца"""
        return any(x > 0 for x in self.c) if self.is_max else any(x < 0 for x in self.c)

    @staticmethod
    def based(column: np.array) -> bool:
        return sum(column) == 1 and column.tolist().count(0) == len(column) - 1

    def get_index_solving_column(self) -> int:
        """Возвращает метод с решением проблемной колонки"""
        return np.argmax(self.c) if self.is_max else np.argmin(self.c)

    def get_index_solving_row(self, column_index: int) -> int:
        """Анализирует все колонки и возвращает одну с минимальным ограничением"""
        restrictions = []
        for row_index in range(self.a.shape[0]):
            el = self.a[row_index][column_index]
            restrictions.append(math.inf if el <= 0 else self.b[row_index] / el)
        row_index = restrictions.index(min(restrictions))
        if restrictions[row_index] == math.inf:
            raise Exception('It is impossible to give the answer. Diapason of valid values is infinite')
        return row_index

    def make_simplex_table(self, solving_row_index: int, solving_column_index: int):
        """Отвечает за соблюдение условий перед следующим шагом, если есть проблемы решает их, если нет - делает следующий шаг"""
        self.b[solving_row_index] /= self.a[solving_row_index][solving_column_index]
        self.a[solving_row_index] /= self.a[solving_row_index][solving_column_index]
        for row_index in range(self.a.shape[0]):
            if row_index == solving_row_index:
                continue
            self.b[row_index] -= self.b[solving_row_index] * self.a[row_index][solving_column_index]
            self.a[row_index] -= self.a[solving_row_index] * self.a[row_index][solving_column_index]
        self.ans -= self.b[solving_row_index] * self.c[solving_column_index]
        self.c -= self.a[solving_row_index] * self.c[solving_column_index]
        self.make_new_shape()

    def solve(self) -> float:
        """ Основной метод, который отдает компилирует готовое решение"""
        if self.print_steps:
            print(self.table)
        while self.is_optimized():
            solving_column_index = self.get_index_solving_column()
            solving_row_index = self.get_index_solving_row(solving_column_index)
            self.make_simplex_table(solving_row_index, solving_column_index)
            if self.print_steps:
                print(self.table)
        return -self.ans

    def get_solution(self):
        """ Основной метод, который отдает готовое решение"""
        columns = self.table.T
        solutions = []
        for column in columns[:-1]:
            solution = 0
            if self.based(column):
                one_index = column.tolist().index(1)
                solution = columns[-1][one_index]
            solutions.append(solution)
        return solutions


if __name__ == '__main__':
    for task_num in range(1, 7):
        simplex = SimplexMethod.read_file(f'./input_files/task {task_num}.txt')
        print(simplex.solve())
        print(simplex.get_solution())