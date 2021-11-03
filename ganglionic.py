import cv2

# ганглиозная клетка
class GanglionicCell():
    # инициализация клетки
    def __init__(self, position, central_radius=5, peripherial_radius=11, isoff=False):
        self.pos = position
        self.s1 = central_radius
        self.s2 = peripherial_radius
        self.size = (central_radius, peripherial_radius)
        self.isoff = isoff
        #print('\t\t\t\t\t\t', self.pos, '\t ganglionic')

    # получение значения отклика на стимул
    def get_response(self, image):
        gauss_d1 = cv2.GaussianBlur(image, (self.s1, self.s1), sigmaX=0)
        gauss_d2 = cv2.GaussianBlur(image, (self.s2, self.s2), sigmaX=0)
        if self.isoff:
            laplace_response = gauss_d2 - gauss_d1
        else:
            laplace_response = gauss_d1 - gauss_d2
        v = laplace_response[self.pos[1], self.pos[0]]
        return v
