#!/usr/bin/env python3

from cv2 import cv2
import numpy as np
import time
from cv2 import VideoWriter, VideoWriter_fourcc


def int2BGR(C):
    B = C % 256
    G = ((C-B)/256) % 256
    R = ((C-B)/256**2) - G/256
    return(B,G,R)

width = 1200
height = 15
frameRate = 30
seconds = 10
resolution = 10
loops = 1
lightness = 150
saturation = 180
speed = 20  #in pixels

blocks = width//resolution
frames = frameRate*seconds

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter("./line_20_loop.avi", fourcc, float(frameRate), (width, height))

frame = np.zeros((height, width, 3), dtype=np.uint8)

# startHue = 0
# for i in range(frames):
#     startHue += 180*loops*(i/frames) # Hue ranges from 0 to 180 in OpenCV
#     startHue %= 180
#     for block in range(blocks):
#         currentHue = 
#         frame[:, block*resolution: (block+1)*resolution, :] = (startHue*(block/blocks),lightness, saturation)
#         frame = cv2.cvtColor(frame, cv2.COLOR_HLS2BGR)
#     video.write(frame)

# video.release()

frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
for block in range(blocks):
    frame[:, block*resolution: (block+1)*resolution, :] = (180*(block/blocks),lightness, saturation)
frame = cv2.cvtColor(frame, cv2.COLOR_HLS2BGR)
cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

lastColumn = frame[:, -1:, :]
for i in range(frames):
    if np.array_equal(frame[:, -1:, :], lastColumn) and (i not in range(blocks+1)):
        print(i)
        break
    lastBlock = np.array(frame[:, -speed:, : ])
    firstBlock = np.array(frame[:, :-speed, :])
    frame[:, speed: , :] = firstBlock
    frame[:, :speed, :] = lastBlock
    video.write(frame)

video.release()


