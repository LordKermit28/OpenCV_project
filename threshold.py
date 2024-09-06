import cv2
import numpy as np

def find_green_square_contour_threshold(image):
    # Преобразование изображения в цветовое пространство HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Определение более широкого диапазона цветов для зелёного квадрата
    lower_green = np.array([35, 20, 20])  # Нижний предел для тёмных и тусклых оттенков зелёного
    upper_green = np.array([100, 255, 255])  # Верхний предел для ярких оттенков зелёного

    # Создание маски для зелёного квадрата
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Применение морфологических операций для улучшения маски
    kernel = np.ones((5, 5), np.uint8)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    # Поиск контуров внутри маски
    contours, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Поиск контура с наибольшей площадью, чтобы отсеять лишнее
    max_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area and 5000 < area < 150000:  # Ограничение на площадь
            # Проверка фигуры контура на квадратность
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if 0.8 <= aspect_ratio <= 1.2:  # Проверка на квадратность
                max_area = area
                max_contour = contour

    # Рисование контура на изображении
    if max_contour is not None:
        print("Контур найден, рисуем его на изображении.")
        cv2.drawContours(image, [max_contour], -1, (0, 0, 255), 2)
    else:
        print("Контур не найден.")

    return image






