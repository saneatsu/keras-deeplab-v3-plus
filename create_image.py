import os
import shutil
import glob
import cv2
import numpy as np
import time
import random
from datetime import datetime

import const


def overlay_image(frame, mask, bg):
    """
    Overlay image to background image.
    Parameters
    ----------
    frame : numpy.ndarray
        target image
    mask : numpy.ndarray
        masked image
    bg : numpy.ndarray
        background image
    Returns
    -------
    overlaied_image : numpy.ndarray
        overlaied image
    """
    # Create a ROI for putting frame to top-left corner on bg    
    rows, cols = frame.shape[:2]
    bg = cv2.resize(bg, (512, 512))
    roi = bg[0:rows, 0:cols]
    
    _, mask = cv2.threshold(mask, thresh=127,  maxval=255, type=cv2.THRESH_BINARY)
    
    mask_inv = cv2.bitwise_not(mask) # inverse of mask
    
    blackout_bg = roi*(mask == 0)
    without_white = frame*(mask == 255)

    overlaied_image = cv2.add(blackout_bg, without_white)
    
    return overlaied_image


def load_bg(num):
    """
    Load background images.
    Parameters
    ----------
    num : int
        the number of how many images you want
    Returns
    -------
    bg_img : list
        background image's list
    """
    all_bg_img = glob.glob(os.path.join(const.BG_DIR, "*.jpg"))
    bg_img = random.sample(all_bg_img, num)

    return bg_img


if __name__ == '__main__':
    # Load images from 'mask' and 'frame_train' dir
    mask_dic = {}
    frame_dic = {}
    print('Load image and create dir')
    for hand_sign in const.HAND_SIGNS:
        print(hand_sign)
        const.check_folder_existence(const.IMAGE_TRAIN_DIR.format(hand_sign))

        mask_fpath = glob.glob(os.path.join(const.MASK_DIR.format(hand_sign), "*.jpg"))
        frame_fpath = glob.glob(os.path.join(const.FRAME_TRAIN_DIR.format(hand_sign), "*.jpg"))
        mask_dic.update({ hand_sign: mask_fpath })
        frame_dic.update({ hand_sign: frame_fpath })

    # Sort by keys
    sorted(mask_dic.items(), key=lambda x: x[1])
    sorted(frame_dic.items(), key=lambda x: x[1])

    # Check the order of keys
    print('Check the order of keys')
    for key in mask_dic.keys():
        print(key)

    # Loop for each hand
    for (hand_sign, mask_path_list), frame_path_list in zip(mask_dic.items(), frame_dic.values()):
        print('==========================')
        print(hand_sign)
        # Loop for each filepath list
        for mask_path, frame_path in zip(mask_path_list, frame_path_list):
            mask = cv2.imread(mask_path)   # (512, 512, 3)
            frame = cv2.imread(frame_path) # (1920, 1920, 3)
            frame = cv2.resize(frame, (512, 512))

            # Get file name
            mask_name = mask_path.split('/')[-1]
            frame_name = frame_path.split('/')[-1]

            if mask_name != frame_name:
                print('ERROR: Not equal filename')
            else:
                img_bgs = load_bg(const.bgs_num)

                # Overlay 'img_bgs' and 'frame'
                for img_bg in img_bgs:
                    bg = cv2.imread(img_bg)
                    image = overlay_image(frame, mask, bg)
                    image = cv2.resize(image, (257, 257))

                    # Rename file name
                    bg_name = img_bg.split('/')[2].split('.')[0]
                    f_name = frame_name.split('_')
                    f_name = f_name[0]+'_'+ \
                             f_name[1]+'_'+ \
                             f_name[2]+'_'+ \
                             bg_name+'_'+ \
                             f_name[3]
                    save_fpath = const.image_train_dir.format(hand_sign)+f_name

                    cv2.imwrite(save_fpath, image)
