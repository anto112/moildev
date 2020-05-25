from libs.Moildev import Moildev
import numpy as np
import cv2

moildev = Moildev("raspicam", 1.4, 1.4, 1320.0, 1017.0, 1.048,
                  2592, 1944, 0, 0, 0, 0, -47.96, 222.86, 4.05)

image_input = cv2.imread("./Image/image.jpg")
h, w = image_input.shape[:2]
sensor_width = 2592
image_width = w
m_ratio = image_width / sensor_width
mapX = np.zeros((h, w), dtype=np.float32)
mapY = np.zeros((h, w), dtype=np.float32)
alphaOffset = 0
betaOffset = 0
zoom = 4

moildev.AnyPointM(mapX, mapY, w, h, alphaOffset, betaOffset, zoom, m_ratio)
result = cv2.remap(image_input, mapX, mapY, cv2.INTER_CUBIC)
result = cv2.resize(result, (800, 600), interpolation=cv2.INTER_AREA)
cv2.imshow("Result", result)
cv2.waitKey(10000)