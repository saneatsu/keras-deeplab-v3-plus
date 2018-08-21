import os
import shutil


hand_signs = ('R0_L0', 'R0_L1', 'R1_L0', 'R1_L1') # 0:gu 1:pa 2: chi　

# Video: Original videos
video_train_dir = './video_train/{}/'
video_valid_dir = './video_valid/{}/'

# Frame: Just divide video to frame
frame_train_dir = './frame_train/{}/'
frame_valid_dir = './frame_valid/{}/'

# Mask: Resize and mask for semantic segmentation  
mask_width  = 512
mask_height = 512
mask_dir = './mask/{}/'
mask_save_dir = './mask/{}/{}'

# Image: Frame(or Mask) + Background image
image_train_dir = './image_train/{}/'
image_valid_dir = './image_valid/{}/'

# Train, Valid: Image + Augmentation
train_width  = 257
train_height = 257
train_dir = './train/{}/'
valid_dir = './valid/{}/'


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