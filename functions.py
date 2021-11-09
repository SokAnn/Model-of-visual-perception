import numpy as np
import cv2


# реакция клетки на световое пятно малого размера
def check_point_stimulus(cell):
    responses = []
    response_map = np.zeros((256, 256), dtype=np.int16)
    for i in range(0, 13):
        for j in range(0, 13):
            image = np.zeros((256, 256), dtype=np.int16)
            cv2.circle(image, center=(128 + i - 6, 128 + j - 6), radius=1, color=(255, 255, 255), thickness=-1)
            v = cell.get_response(image)
            responses.append(v + 128)
            cv2.circle(response_map, center=(i * 16 + 32, j * 16 + 32), radius=2, color=int(v), thickness=-1)
    return response_map


# реакция клетки на стимул в форме светлого пятна на темном фоне
def check_circle_stimulus(cell):
    responses = []
    for i in range(0, 30):
        image = np.zeros((256, 256), dtype=np.int16)
        cv2.circle(image, (128, 128), radius=i, color=(255, 255, 255), thickness=(i * 2 + 1))
        v = cell.get_response(image)
        responses.append(v)
    return responses


# реакция клетки на стимул в виде линии, проходящей через центр рецептивного поля
def rotate_line(cell):
    responses = []
    angles = []
    for i in range(0, 360, 10):
        angle_grad = i
        angle = i / 180 * np.pi
        image = np.zeros((256, 256), dtype=np.int16)
        cv2.line(image, (128 + int(100 * np.cos(angle)), 128 + int(100 * np.sin(angle))),
                 (128 - int(100 * np.cos(angle)), 128 - int(100 * np.sin(angle))), color=(255, 255, 255),
                 thickness=3, lineType=8)
        v = cell.get_response(image)
        responses.append(v)
        angles.append(angle_grad)
    return responses, angles


# реакция клетки на стимул в виде вертикальной линии, сдвигающейся вдоль оси абсцисс
def vertical_line_shift(cell):
    responses = []
    shifts = []
    for i in range(-50, 50):
        shifts.append(i)
        image = np.zeros((256, 256), dtype=np.int16)
        cv2.line(image, (i + 128, 0), (i + 128, 256), color=255, thickness=3, lineType=8)
        v = cell.get_response(image)
        responses.append(v)
    return responses, shifts


# реакция клетки на стимул в виде горизонтальной линии, сдвигающейся вдоль оси ординат
def horizontal_line_shift(cell):
    responses = []
    shifts = []
    for j in range(-50, 50):
        shifts.append(j)
        image = np.zeros((256, 256), dtype=np.int16)
        cv2.line(image, (0, j + 128), (256, j + 128), color=255, thickness=3, lineType=8)
        v = cell.get_response(image)
        responses.append(v)
    return responses, shifts
