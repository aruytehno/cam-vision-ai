from src.camera import Camera
from src.face_detection import detect_faces
import cv2

def main():
    cam = Camera()

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        frame_with_faces = detect_faces(frame)
        cv2.imshow('CamVisionAI', frame_with_faces)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()

if __name__ == "__main__":
    main()
