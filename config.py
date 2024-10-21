import cv2

# Путь к каскадам для распознавания лиц
FACE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

# Параметры фильтров
BLUR_KSIZE = (5, 5)
CONTRAST_ALPHA = 1.5
