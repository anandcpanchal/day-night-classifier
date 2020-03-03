import os

import cv2
import numpy as np

from matplotlib import pyplot as plt

import argparse

parser = argparse.ArgumentParser( description='Classify input image in day or night' )
parser.add_argument( '-i', '--input_image', required = True)
parser.add_argument( '-t', '--threshold', default = 100)
parser.add_argument( '-d', '--debug', default = False)
args = vars( parser.parse_args() )


def f_get_image( image_path_ia ):
    try:
        image_oa = cv2.imread( image_path_ia )
        return image_oa
    except:
        print(" Error while reading input image path, please recheck")
        exit()

def f_show_image( image_path_ia , classification_ia):
    image_ = f_get_image( image_path_ia )
    plt.imshow( image_ )
    plt.title( classification_ia )
    plt.show( block = False )
    timeout_ = 3
    plt.pause( timeout_ )
    plt.close()

def f_get_hsv_average( image_path_ia ):
    root_image_ = f_get_image( image_path_ia )
    hsv_image_ = cv2.cvtColor( root_image_, cv2.COLOR_BGR2HSV )
    h_, w_, d_ = hsv_image_.shape
    sum_brightness_ = np.sum( hsv_image_[:,:,2] )
    area_ = h_ * w_ * 1.0
    avg_oa = sum_brightness_ / area_
    if args['debug']:
        print(" hsv_average : ", avg_oa)
    return avg_oa


def f_classify_day( path_ia, threshold_ia ):

    avg_ = f_get_hsv_average( path_ia )

    if avg_ < float(threshold_ia):
        title_oa = "Night image"
    else:
        title_oa = "Day image"

    if args['debug']:
        f_show_image( path_ia, title_oa )

    print( title_oa )

    return title_oa

f_classify_day( args['input_image'], args['threshold'] )
