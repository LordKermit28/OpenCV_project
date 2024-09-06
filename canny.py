import cv2
import numpy as np

def find_green_square_contour_canny(image):

    # Преобразование изображения в цветовое пространство HSV, чтобы оптимизировать обработку
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Определение диапазонов цветов для зеленого квадрата для оптимизации определения контуров
    lower_green = np.array([40, 40, 40])  # Нижний предел для зеленого цвета
    upper_green = np.array([80, 255, 255])  # Верхний предел для зеленого цвета

    # Создание маски для зеленого квадрата с использованием заданных диапозонов цветов
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Применение морфологических операций для улучшения маски
    kernel = np.ones((5, 5), np.uint8)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)

    # Поиск контуров внутри маски
    contours, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Поиск контура с наибольшей площадью, чтобы отсеять мусор
    max_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area and area < 150000:
            max_area = area
            max_contour = contour

    # Проверка на квадратность и замыкание контура чтобы ещё отсеять  лишние контуры
    if max_contour is not None:
        rect = cv2.minAreaRect(max_contour)
        box = cv2.boxPoints(rect)
        box = np.int32(box)
        cv2.drawContours(image, [box], -1, (0, 0, 255), 2)

    return image
























