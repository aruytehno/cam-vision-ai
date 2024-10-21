# src/camera.py

import cv2
import logging

logging.basicConfig(level=logging.INFO)

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            logging.error("Не удалось открыть веб-камеру")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            logging.error("Не удалось получить кадр с камеры")
            return None
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
        logging.info("Веб-камера успешно завершила работу")
