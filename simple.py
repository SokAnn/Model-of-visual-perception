import ganglionic as g

# вертикальная простая клетка
class VerticalSimpleCell():
    # инициализация простой вертикальной клетки
    def __init__(self, position, size=3):
        self.ganglionic_cells = []
        self.size = size
        d = 3
        for i in range(-(size // 2), size // 2 + 1):
            for j in range(-(size // 2), size // 2 + 1):
                isoff = True
                if i == 0:
                    isoff = False
                self.ganglionic_cells.append(g.GanglionicCell((position[0] + i * d, position[1] + j * d), isoff=isoff))
                #print('\t\t\t', position[0] + i * d, '\t', position[1] + j * d, '\t simple')

    # получение отклика
    def get_response(self, image):
        response = 0
        for cell in self.ganglionic_cells:
            response += cell.get_response(image)
        #print('ganglionic responses (simple cell) ', response)
        return response

# горизонтальная простая клетка
class HorizontalSimpleCell():
    # инициализация простой горизонтальной клетки
    def __init__(self, position, size=7):
        self.ganglionic_cells = []
        self.size = size
        d = 3
        for i in range(-(size // 2), size // 2 + 1):
            for j in range(-(size // 2), size // 2 + 1):
                isoff = True
                if j == 0:
                    isoff = False
                self.ganglionic_cells.append(g.GanglionicCell((position[0] + i * d, position[1] + j * d), isoff=isoff))

    # получение отклика
    def get_response(self, image):
        response = 0
        for cell in self.ganglionic_cells:
            response += cell.get_response(image)
        return response

# диагональная простая клетка
class DiagonalSimpleCell():
    # инициализация простой диагональной клетки
    def __init__(self, position, size=7):
        self.ganglionic_cells = []
        self.size = size
        d = 3
        for i in range(-(size // 2), size // 2 + 1):
            for j in range(-(size // 2), size // 2 + 1):
                isoff = True
                if i == j:
                    isoff = False
                self.ganglionic_cells.append(g.GanglionicCell((position[0] + i * d, position[1] + j * d), isoff=isoff))

    # получение отклика
    def get_response(self, image):
        response = 0
        for cell in self.ganglionic_cells:
            response += cell.get_response(image)
        return response
