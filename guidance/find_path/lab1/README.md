# Robotics-lab1

This code was developed by David Gomes, Tiago Pinto and Tomás Líbano Monteiro,
regarding the first laboratory of the Robotics course at Instituto Superior Técnico, 2022

## 1. Contents of folder

- main.py
- debug_plot.py
- image.py
- search.py
- robot.py
- test_draw_1.png
- test_draw_2.png

## 2. How to run the code

### 2.1 Preprocess images and draw

Change the following parameters in main.py:

- IMAGES_AVAILABLE: set a list with the available images names

- IM_NUM: list of indexes of images in IMAGES_AVAILABLE that should be processed (multiple images can be processed at once)

- ROBOT_IM_NUM: index of image in IMAGES_AVAILABLE that should be drawn (must have been preprocessed before or in the same run). Set ROBOT_IMG_NAME to none if you only want to preprocess images and no robot drawing.

- SERIAL_PORT_NAME: name of the serial port used to comunicate with the robot

Output

- The output will be a .txt for each processed image, that can later be read by the robot.py script to draw the respective image, and a gif with the points being drawn in the skeleton image

### 2.2 Draw an already preprocessed image

Change the following parameters in robot.py:

- TXT_NAME: .txt file that holds the points of the image to be drawn

- SERIAL_PORT_NAME: name of the serial port used to comunicate with the robot
