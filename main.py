from src.camera import Camera
from src.face_detection import detect_and_track_faces
from src.filters import apply_blur, apply_contrast
import cv2

def main():
    cam = Camera()
    current_filter = None

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        # Распознаем и отслеживаем лица
        frame_with_faces = detect_and_track_faces(frame)

        # Применение фильтра на основе нажатой клавиши
        if current_filter == 'blur':
            frame_with_faces = apply_blur(frame_with_faces)
        elif current_filter == 'contrast':
            frame_with_faces = apply_contrast(frame_with_faces)

        cv2.imshow('CamVisionAI', frame_with_faces)

        # Управление фильтрами
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            current_filter = 'blur'
        elif key == ord('c'):
            current_filter = 'contrast'
        elif key == ord('n'):
            current_filter = None  # Убрать все фильтры

    cam.release()

if __name__ == "__main__":
    main()
