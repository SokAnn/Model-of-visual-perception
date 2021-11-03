import simple as s
import numpy as np

# сложная вертикальная клетка
class VerticalComplexCell():
    # инициализация сложной вертикальной клетки
    def __init__(self, position, size=15):
        self.simple_vert_cells = []
        self.size = size
        for i in range(-(size // 2), size // 2 + 1):
            self.simple_vert_cells.append(s.VerticalSimpleCell((i + position[0], position[1])))
            #print(position[0], '\t', i + position[1], '\t complex')

    # получение отклика
    def get_response(self, image):
        responses = []
        for cell in self.simple_vert_cells:
            responses.append(cell.get_response(image))
        print('simple responses (complex cell) ', responses)
        return np.max(responses)

# сложная горизонтальная клетка
class HorizontalComplexCell():
    # инициализация сложной горизонтальной клетки
    def __init__(self, position, size=15):
        self.simple_hor_cells = []
        self.size = size
        for i in range(-(size // 2), size // 2 + 1):
            self.simple_hor_cells.append(s.HorizontalSimpleCell((position[0], i + position[1])))

    # получение отклика
    def get_response(self, image):
        responses = []
        for cell in self.simple_hor_cells:
            responses.append(cell.get_response(image))
        return np.max(responses)

# сложная диагональная клетка
class DiagonalComplexCell():
    # инициализация сложной диагональной клетки
    def __init__(self, position, size=15):
        self.simple_diag_cells = []
        self.size = size
        for i in range(-(size // 2), size // 2 + 1):
            self.simple_diag_cells.append(s.DiagonalSimpleCell((i + position[0], i + position[1])))

    # получение отклика
    def get_response(self, image):
        responses = []
        for cell in self.simple_diag_cells:
            responses.append(cell.get_response(image))
        return np.max(responses)
