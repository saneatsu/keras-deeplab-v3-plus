import os
import shutil


HAND_SIGNS = ('R0_L0', 'R0_L1', 'R1_L0', 'R1_L1') # 0:gu 1:pa 2: chi　

# Video: Original videos
VIDEO_TRAIN_DIR = './video_train/{}/'
VIDEO_VALID_DIR = './video_valid/{}/'

# Frame: Just divide video to frame
# out=1920x1920
FRAME_TRAIN_DIR = './frame_train/{}/'
FRAME_VALID_DIR = './frame_valid/{}/'

# Mask: Resize and mask for semantic segmentation
# create_mask.py(out=512x512)
MASK_WIDTH  = 512
MASK_HEIGHT = 512
MASK_DIR = './mask/{}/'
MASK_SAVE_DIR = './mask/{}/{}'

# Image: Frame(or Mask) + Background image(
# create_image.py(out=257x257)
IMAGE_TRAIN_DIR = './image_train/{}/'
IMAGE_VALID_DIR = './image_valid/{}/'

# Train, Valid: Image + Augmentation
TRAIN_WIDTH  = 257
TRAIN_HEIGHT = 257
TRAIN_DIR = './train/{}/'
VALID_DIR = './valid/{}/'

# Background image dir
BGS_NUM = 5
BG_DIR = './bg/'


def check_folder_existence(dir):
    """
    Delete the directory tree if it exists.
    Make the directory if it doesn't exist.
    Parameters
    ----------
    dir : str
        directory's absolute path
    """
    if os.path.exists(dir):
        shutil.rmtree(dir)

    if not os.path.exists(dir):
        os.makedirs(dir)