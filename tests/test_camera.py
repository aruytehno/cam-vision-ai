import unittest
from src.camera import Camera

class TestCamera(unittest.TestCase):
    def test_camera_initialization(self):
        cam = Camera()
        self.assertIsNotNone(cam.cap.isOpened(), "Camera should be initialized")

    def test_get_frame(self):
        cam = Camera()
        frame = cam.get_frame()
        self.assertIsNotNone(frame, "Should return a valid frame")
        cam.release()

if __name__ == '__main__':
    unittest.main()
