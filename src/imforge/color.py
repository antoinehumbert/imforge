import cv2
import numpy as np


def _filter_color_cv2(image, min_color, max_color=None, fillcolor=None, keep=True):
    """
    Filter colors in the range [min_color, max_color] on given image.

    :param numpy.ndarray image: the (opencv) image to filter, in BGR mode.
    :param tuple[int,int,int] min_color: the minimum color (in HSV color space) to filter on
    :param Optional[tuple[int,int,int]] max_color: the maximum color (in HSV color space) to filter on. If not set, use
      the same as min_color, thus filtering on a single color.
    :param fillcolor: the color to use for filling erased areas (in same color space as image)
    :param bool keep: specify whether or not the filtered colors are to be kept (the default) or removed from image
    """
    if max_color is None:
        max_color = min_color
    if fillcolor is None:
        fillcolor = 0
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, min_color, max_color)
    background = np.full_like(image, fillcolor)
    if keep:
        background = cv2.bitwise_and(background, background, mask=cv2.bitwise_not(mask))
    else:
        # Inverse mask for keeping everything but filtered colors
        background = cv2.bitwise_and(background, background, mask=mask)
        mask = cv2.bitwise_not(mask)
    image[:] = cv2.add(cv2.bitwise_and(image, image, mask=mask), background)


def remove_color_cv2(image, min_color, max_color=None, fillcolor=None):
    """
    Remove colors in the range [min_color, max_color] on given image, replacing with fillcolor.

    :param numpy.ndarray image: the (opencv) image to filter, in BGR mode.
    :param tuple[int,int,int] min_color: the minimum color (in HSV color space) to filter on
    :param Optional[tuple[int,int,int]] max_color: the maximum color (in HSV color space) to filter on. If not set, use
      the same as min_color, thus filtering on a single color.
    :param fillcolor: the color to use for filling erased areas (in same color space as image)
    """
    _filter_color_cv2(image, min_color, max_color, fillcolor=fillcolor, keep=False)


def keep_color_cv2(image, min_color, max_color=None, fillcolor=None):
    """
    Keep colors in the range [min_color, max_color] on given image, replacing removed pixels with fillcolor.

    :param numpy.ndarray image: the (opencv) image to filter, in BGR mode.
    :param tuple[int,int,int] min_color: the minimum color (in HSV color space) to filter on
    :param Optional[tuple[int,int,int]] max_color: the maximum color (in HSV color space) to filter on. If not set, use
      the same as min_color, thus filtering on a single color.
    :param fillcolor: the color to use for filling erased areas (in same color space as image)
    """
    _filter_color_cv2(image, min_color, max_color, fillcolor=fillcolor, keep=True)
