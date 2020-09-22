from PIL import ImageOps, ImageEnhance, Image
import numpy as np
import random
import math
import cv2

"""
Transforamtions that we can apply on an image and the range of magnitude:

Rotate, {0, 90, -90, 180}
Flip
Mirror
Equalize
Solarize, [0, 255]
Contrast, [0.1, 1.9]
Color, [0.1, 1.9]
Brightness, [0.1, 1.9]
Sharpness, [0.1, 1.9]
"""

def rotate(img, alpha):
    '''
    {'method': 'rotate', 'angle': alpha}
    '''
    return img.rotate(alpha)

def flip(img, v):
    '''
    {'method': 'flip', 'value': v}
    '''
    return ImageOps.flip(img)

def mirror(img, v):
    '''
    {'method': 'mirror', 'value': v}
    '''
    return ImageOps.mirror(img)

def equalize(img, v):
    '''
    {'method': 'equalize'}
    '''

    return ImageOps.equalize(img)

def solarize(img, v):
    '''
    {'method': 'solarize', 'value': v}
    '''

    return ImageOps.solarize(img, v)

def contrast(img, v):
    '''
    {'method': 'contrast', 'value': v}
    '''

    return ImageEnhance.Contrast(img).enhance(v)

def color(img, v):
    '''
    {'method': 'color', 'value': v}
    '''

    return ImageEnhance.Color(img).enhance(v)

def brightness(img, v):
    '''
    {'method': 'brightness', 'value': v}
    '''

    return ImageEnhance.Brightness(img).enhance(v)

def sharpness(img, v):
    '''
    {'method': 'sharpness', 'value': v}
    '''

    return ImageEnhance.Sharpness(img).enhance(v)

def name_to_fct(method):

    op = {'rotate': rotate, 'flip': flip, 'mirror': mirror, 'equalize': equalize, 'solarize': solarize,
           'contrast': contrast, 'color': color, 'brightness': brightness, 'sharpness': sharpness}

    return op[method]


class RandAugmentation:

    def __init__(self):

        self.list = [(rotate, 0, 360), (flip, 0, 1), (mirror, 0, 1), (equalize, 0, 1), (solarize, 0, 255),
                     (contrast, 0.5, 1.9), (color, 0.1, 1.9), (brightness, 0.5, 1.9), (sharpness, 0.1, 1.9)]

    def __call__(self, img):

        ops = random.choice(self.list)

        op, minv, maxv = ops
        
        if op.__name__ == 'rotate':
            alpha = random.choice([90, -90, 180])
            augment = {"method": op.__name__, "value": alpha}
            img_ = op(img, alpha)

        elif op.__name__ in ['flip', 'mirror', 'equalize']:
            img_ = op(img, 0)
            augment = {"method": op.__name__, "value": 0}

        else:
            val = random.uniform(minv, maxv)
            augment = {"method": op.__name__, "value": val}
            img_ = op(img, val)

        return img_, augment