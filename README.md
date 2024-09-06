Shape Detection and Recognition using OpenCV
This project focuses on detecting and recognizing hand-drawn shapes (triangle, square, rectangle, circle, ellipse, star, pentagon) from a noisy image using OpenCV.
It involves:
- Preprocessing the image (grayscale conversion, noise reduction).
- Detecting contours to approximate shapes.
- Classifying shapes based on their geometry.
  
How to Run
Install dependencies:
pip install -r requirements.txt
Run the script:
python shape_detection.py

The program will display the original image and the image with detected shapes, labeling each shape with its name.
![output](https://github.com/user-attachments/assets/a2a4ff4b-23eb-4671-bfcc-786037983f23)
