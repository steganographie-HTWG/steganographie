from ocr import recognizeCharacters, createLetterImages
from cv2 import cv2

def test_recognize_characters():
    characters, boxes = recognizeCharacters('ocr/example/demo_01.png')
    
    assert 'HelloWorld' == characters
    firstBox = boxes[0][1]
    assert 79 < firstBox['x'] < 81
    assert 71 < firstBox['y'] < 73
    assert 39 < firstBox['w'] < 41
    assert 55 < firstBox['h'] < 57

def test_create_letter_images():
    characters, boxes = recognizeCharacters('ocr/example/demo_01.png')
    createLetterImages(characters, boxes, 'ocr/example/demo_01.png', 200, save_files=True)