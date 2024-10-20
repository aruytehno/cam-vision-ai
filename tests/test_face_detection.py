import unittest
import cv2
from src.face_detection import detect_faces

class TestFaceDetection(unittest.TestCase):
    def test_detect_faces(self):
        # Загрузим изображение для теста (замените путь на актуальный)
        test_image = cv2.imread('data/samples/test_face.jpg')
        result = detect_faces(test_image)
        self.assertIsNotNone(result, "Result should not be None")
        # Проверьте, что хотя бы одно лицо обнаружено
        self.assertGreater(len(result), 0, "Should detect at least one face")

if __name__ == '__main__':
    unittest.main()
