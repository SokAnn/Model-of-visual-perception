import matplotlib.pyplot as plt
import ganglionic as g
import simple as s
import complex as c
import functions as f


# тестирование модели
def testing(type_cell, name):
    plt.figure(name + 'responses to stimuli')
    ax1 = plt.subplot(2, 3, 1)
    ax1.set_title('point stimulus')
    ax1 = plt.imshow(f.check_point_stimulus(type_cell))

    ax2 = plt.subplot(2, 3, 2)
    ax2.set_title('circle stimulus')
    plt.plot(f.check_circle_stimulus(type_cell), 'blue')
    plt.xlabel('radius')
    plt.ylabel('response')

    ax3 = plt.subplot(2, 3, 3)
    ax3.set_title('rotate line stimulus')
    [resp, ang] = f.rotate_line(type_cell)
    ax3 = plt.plot(ang, resp, 'green')
    plt.xlabel('angle')
    plt.ylabel('response')

    ax4 = plt.subplot(2, 3, 4)
    ax4.set_title('shifted vertical line stimulus')
    [resp, shft] = f.vertical_line_shift(type_cell)
    ax4 = plt.plot(shft, resp, 'black')
    plt.xlabel('shift')
    plt.ylabel('response')

    ax5 = plt.subplot(2, 3, 5)
    ax5.set_title('shifted horizontal line stimulus')
    [resp, shft] = f.horizontal_line_shift(type_cell)
    ax5 = plt.plot(shft, resp, 'red')
    plt.xlabel('shift')
    plt.ylabel('response')


if __name__ == "__main__":
    cell_1 = g.GanglionicCell(position=(128, 128), central_radius=3, peripherial_radius=11)
    testing(cell_1, 'ganglionic on-cell (3, 11) ')

    cell_2 = g.GanglionicCell(position=(128, 128), central_radius=5, peripherial_radius=11)
    testing(cell_2, 'ganglionic on-cell (5, 11) ')

    cell_3 = s.VerticalSimpleCell(position=(128, 128))
    testing(cell_3, 'simple vertical cell ')

    cell_4 = s.HorizontalSimpleCell(position=(128, 128))
    testing(cell_4, 'simple horizontal cell ')

    cell_5 = c.VerticalComplexCell(position=(128, 128))
    testing(cell_5, 'complex vertical cell ')

    cell_6 = c.HorizontalComplexCell(position=(128, 128))
    testing(cell_6, 'complex horizontal cell ')

    cell_7 = s.DiagonalSimpleCell(position=(128, 128))
    testing(cell_7, 'simple diagonal cell ')

    cell_8 = c.DiagonalComplexCell(position=(128, 128))
    testing(cell_8, 'complex diagonal cell ')

    plt.show()
