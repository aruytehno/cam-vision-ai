# src/filters.py

import cv2
from config import BLUR_KSIZE, CONTRAST_ALPHA

def apply_blur(frame):
    return cv2.GaussianBlur(frame, BLUR_KSIZE, 0)

def apply_contrast(frame):
    return cv2.convertScaleAbs(frame, alpha=CONTRAST_ALPHA, beta=0)
