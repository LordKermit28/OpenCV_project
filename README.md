# OpenCV_project
Contour Detection: Canny vs Threshold Methods
This repository contains a Python project focused on comparing two popular methods for detecting object contours in images:

Canny Edge Detection: A gradient-based method for finding edges in an image, suitable for detecting contours based on changes in intensity.
Thresholding Method: A method that segments objects in an image based on pixel intensity values, particularly useful when object color is well-defined.
Project Overview
The project demonstrates the strengths and weaknesses of both contour detection techniques using various image scenarios, including:

Black square on a white background: A controlled environment with high contrast.
Green square on a noisy, multicolored background: A more challenging environment with noise and multiple colors.
Black square with shadows and highlights: A scenario involving complex lighting conditions, such as shadows and reflections.
Features
Canny Edge Detection: Detects contours based on intensity gradients and changes in brightness. Works best when the image has distinct edges, but can pick up noise in complex environments.
Threshold-Based Detection: Segments objects based on predefined color or intensity ranges. More robust to noise but requires precise configuration of threshold values for effective contour detection.
Repository Structure
canny.py - Contains the implementation of contour detection using the Canny method.
threshold.py - Contains the implementation of contour detection using the thresholding method.
main.py - The entry point of the application. Compares both methods using different image scenarios and displays the results.
images/ - Sample images used for testing the algorithms (black square, green square, noisy backgrounds).
Getting Started
Clone the repository:

bash
Копировать код
git clone https://github.com/LordKermit28/название-репозитория.git
Install the required dependencies:

bash
Копировать код
pip install -r requirements.txt
Run the main.py file to compare the contour detection methods:

bash
Копировать код
python main.py
Usage
This project can be used to:

Compare the performance of different contour detection methods.
Understand the scenarios where each method performs better.
Apply these techniques in real-world image processing tasks, such as object detection or image segmentation.
Results
The repository includes several experiments demonstrating how Canny and thresholding methods behave in different scenarios. In some cases, the Canny method detects more contours due to noise, while the threshold method is more stable but can miss important details if not properly configured.

Contributions
Contributions are welcome! If you find an issue or want to enhance the comparison, feel free to submit a pull request.

License
This project is licensed under the MIT License.
