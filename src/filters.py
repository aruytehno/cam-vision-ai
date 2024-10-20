import cv2

def apply_blur(frame, ksize=(5, 5)):
    return cv2.GaussianBlur(frame, ksize, 0)

def apply_contrast(frame, alpha=1.5):
    return cv2.convertScaleAbs(frame, alpha=alpha, beta=0)
