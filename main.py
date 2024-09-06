import cv2
import matplotlib.pyplot as plt
from canny import find_green_square_contour_canny
from threshold import find_green_square_contour_threshold

def main():
    image_path = "image"

    # Здесь мы загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Изображение не может быть загружено. Нужно проверить путь.")

    # Обработка изображений двумя методами
    image_canny = find_green_square_contour_canny(image.copy()) #Canny
    image_threshold = find_green_square_contour_threshold(image.copy()) #threshold

    # Выводим итог с помощью Matplotlib
    plt.figure(figsize=(15, 7))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image_canny, cv2.COLOR_BGR2RGB))
    plt.title("Canny Method")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image_threshold, cv2.COLOR_BGR2RGB))
    plt.title("Threshold Method")
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()