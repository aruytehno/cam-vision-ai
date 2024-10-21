import cv2
import dlib

# Загрузка каскада для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Создаем корреляционный трекер для отслеживания лиц
trackers = []
detector = dlib.get_frontal_face_detector()


def detect_and_track_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Добавление нового трекера для каждого лица
    for (x, y, w, h) in faces:
        tracker = dlib.correlation_tracker()
        rect = dlib.rectangle(x, y, x + w, y + h)
        tracker.start_track(frame, rect)
        trackers.append(tracker)

    # Отслеживание лиц
    for tracker in trackers:
        tracker.update(frame)
        pos = tracker.get_position()
        x = int(pos.left())
        y = int(pos.top())
        w = int(pos.right() - x)
        h = int(pos.bottom() - y)

        # Рисуем рамку вокруг отслеживаемого лица
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame
