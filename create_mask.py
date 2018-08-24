import os
import glob
import cv2
import numpy as np

import model
import const

from keras.applications.mobilenetv2 import preprocess_input


if __name__ == '__main__':
    # Load images from 'frame_train' dir
    img_dic = {}
        for hand_sign in const.HAND_SIGNS:
        imgs_fpath = glob.glob(os.path.join(const.FRAME_TRAIN_DIR.format(hand_sign), "*.jpg"))
        img_dic.update({ hand_sign: imgs_fpath })
        print(len(imgs_fpath))
            
    # Create model
    model_dlv3 = model.Deeplabv3()

    # Mask image
    for hand_sign, imgs_fpath in img_dic.items():
        const.check_folder_existence(const.MASK_DIR.format(hand_sign))
        for img_fpath in imgs_fpath:
            img = preprocess_input(cv2.imread(img_fpath).astype("float"))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (const.MASK_WIDTH, const.MASK_HEIGHT))

            predicted = model_dlv3.predict(img[np.newaxis, ...])

            # Get only person and background
            back_score = predicted[0,:,:,0]
            person_score = predicted[0,:,:,15]

            # Mask only background and person
            mask = (person_score > back_score).astype("uint8")*255
            img_name = img_fpath.split('/')[-1]
            save_folder = const.MASK_SAVE_DIR.format(hand_sign, img_name)
            print(save_folder)
            cv2.imwrite(save_folder, mask)