from functools import reduce

import numpy as np
import skimage.io
from PIL import Image
import matplotlib.pyplot as plt
from skimage.filters import threshold_minimum, threshold_yen
import os
from collections import Counter
import pytube
import cv2
import pafy
import youtube_dl

#https://www.youtube.com/watch?v=uP4sKkvUWeM


def get_video_from_youtube(url, res):
    yt = pytube.YouTube(url)
    video_streams = yt.streams.filter(file_extension='mp4').all()
    target_stream = None

    for stream in video_streams:
        if res in stream.resolution:
            target_stream = stream
            break

    return target_stream


def preprocessing_examples():
    imageSize = (100,100)
    exPath = 'imgArEx.txt'
    if os.path.exists(exPath):
        return exPath
    imagesArrayExamples = open(exPath, 'a')
    rectangles = [
        (10,  7,  40,  38),
        (15, 13,  90,  90),
        (15, 15, 100, 100),
        (10, 10,  62,  62)
    ]

    for i in range(1,5):
        imgPath = 'Images\\Brimstone\\'+str(i)+'.jpg'
        img = Image.open(imgPath)
        cropRect = rectangles[i-1]
        img = img.crop(cropRect)
        img = img.resize(imageSize)
        img = skimage.color.rgb2gray(img)
        thresh = threshold_minimum(img)
        binary = img > thresh
        res = np.array(binary)
        line = res.tolist()
        lineToWrite = str(line)+"\n"
        imagesArrayExamples.write(lineToWrite)
        plt.subplot(2,2,i)
        plt.imshow(binary, cmap='gray')
    plt.show()
    imagesArrayExamples.close()
    return imagesArrayExamples


def preprocessing_input(img):
    img = Image.fromarray(img)
    imageSize = (100, 100)
    rectangles = [
        (10, 7, 40, 38),
        (15, 13, 90, 90),
        (15, 15, 100, 100),
        (10, 10, 62, 62),
        (1096, 183, 1127, 214)
    ]

    cropRect = rectangles[4]
    img = img.crop(cropRect)
    img = img.resize(imageSize)
    img = skimage.color.rgb2gray(img)
    thresh = threshold_yen(img)
    binary = img > thresh
    res = np.array(binary)
    line = res.tolist()
    #plt.imshow(binary, cmap='gray')
    #plt.show()
    return line


def compare(inputLine, exFile):
    examples = open(exFile, 'r').read().split('\n')
    matches = []
    for i, line in enumerate(examples):
        linePixels = line.split(', ')
        inputPixels = str(inputLine).split(', ')

        for j, px in enumerate(linePixels):
            if px==inputPixels[j]:
                matches.append(i)

    count = Counter(matches)

    if len(count)==0:
        return False
    if count[0] > 6500:
        print(count)
        return True
    return False


def process_video(video):
    cap = cv2.VideoCapture(video.url)
    found_item = False
    frame_count = 0
    frame_skip_count = 0
    frame_skip_interval = 20
    frame = None
    line = None
    while cap.isOpened() and not found_item:
        ret, frame = cap.read()
        #print(f'{frame_skip_count} - {frame_count}')
        frame_count += 1
        if frame_skip_count < frame_skip_interval:
            frame_skip_count += 1
            continue
        frame_skip_count = 0
        if not ret:
            break

        line = preprocessing_input(frame)
        comp = compare(line, exPath)
        if comp==True:
            break
    plt.imshow(frame)
    plt.show()

    print("end" + str(frame_count))


videoUrl = 'https://www.youtube.com/watch?v=468nBgqbr20' #ryfek
exPath = preprocessing_examples()
#img = Image.open('TEST.jpg')
#line = preprocessing_input(img)
#compare(line, exPath)
video = get_video_from_youtube(videoUrl, '720p')
process_video(video)

