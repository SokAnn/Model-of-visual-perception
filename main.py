import cv2
import numpy as np
import matplotlib.pyplot as plt
import ganglionic as g
import simple as s
import complex as c
import functions as f

# тестирование модели
def testing(type_cell, name):
    # plt.figure(name + 'point stimulus')
    # plt.title('point stimulus')
    # plt.imshow(f.check_point_stimulus(type_cell))

    # plt.figure(name + 'circle stimulus')
    # plt.title('circle stimulus')
    # plt.plot(f.check_circle_stimulus(type_cell), 'blue')
    # plt.xlabel('radius')
    # plt.ylabel('response')
    #
    # plt.figure(name + 'rotate line stimulus')
    # plt.title('rotate line stimulus')
    # [resp, ang] = f.rotate_line(type_cell)
    # plt.plot(ang, resp, 'green')
    # plt.xlabel('angle')
    # plt.ylabel('response')

    plt.figure(name + 'shifted vertical line stimulus')
    plt.title('shifted vertical line stimulus')
    [resp, shft] = f.vertical_line_shift(type_cell)
    plt.plot(shft, resp, 'black')
    plt.xlabel('shift')
    plt.ylabel('response')

    # plt.figure(name + 'shifted horizontal line stimulus')
    # plt.title('shifted horizontal line stimulus')
    # [resp, shft] = f.horizontal_line_shift(type_cell)
    # plt.plot(shft, resp, 'red')
    # plt.xlabel('shift')
    # plt.ylabel('response')

def main():
    print('Hi, world!')# check

    # check - radius
    # cell_1 = g.GanglionicCell(position=(128, 128), central_radius=3, peripherial_radius=11)
    # testing(cell_1, 'ganglionic on-cell (3, 11)')

    # cell_1 = g.GanglionicCell(position=(128, 128), central_radius=5, peripherial_radius=11)
    # testing(cell_1, 'ganglionic on-cell ')

    # cell_2 = g.GanglionicCell(position=(128, 128), central_radius=5, peripherial_radius=11, isoff=True)
    # testing(cell_2, 'ganglionic off-cell ')

    # cell_3 = s.VerticalSimpleCell(position=(128, 128))
    # testing(cell_3, 'simple vertical cell')

    # cell_4 = s.HorizontalSimpleCell(position=(128, 128))
    # testing(cell_4, 'simple horizontal cell')

    cell_5 = c.VerticalComplexCell(position=(128, 128))
    testing(cell_5, 'complex vertical cell ')

    # cell_6 = c.HorizontalComplexCell(position=(128, 128))
    # testing(cell_6, 'complex horizontal cell ')

    # cell_7 = s.DiagonalSimpleCell(position=(128, 128))
    # testing(cell_7, 'simple diagonal cell ')

    # cell_8 = c.DiagonalComplexCell(position=(128, 128))
    # testing(cell_8, 'complex diagonal cell ')

main()

