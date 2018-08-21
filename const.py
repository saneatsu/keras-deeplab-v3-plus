hand_signs = ('R0_L0', 'R0_L1', 'R1_L0', 'R1_L1') # 0:gu 1:pa 2: chi　

# Video: Original videos
video_train_dir = './video_train/{}/'
video_valid_dir = './video_valid/{}/'

# Frame: Just divide video to frame
frame_train_dir = './frame_train/{}/'
frame_valid_dir = './frame_valid/{}/'

# Musk: Resize and musk for semantic segmentation  
musk_width  = 512
musk_height = 512
musk_train_dir = '/home/ubuntu/Code/keras-deeplab-v3-plus/musk/{}'

# Image: Frame(or Musk) + Background image
image_train_dir = './image_train/{}/'
image_valid_dir = './image_valid/{}/'

# Train, Valid: Image + Augmentation
train_width  = 257
train_height = 257
train_dir = './train/{}/'
valid_dir = './valid/{}/'