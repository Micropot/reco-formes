from PIL import Image
import os

def copy_paste(background_image):
    #mask_list = os.listdir(mask_list)

    '''mask = Image.open('/Users/arthurlamard/Documents/ISEN5/reco_formes/results/isen_Building_0.png')
    mask_copy = mask.copy()
    background = Image.open(background_image)
    background.paste(mask_copy, (0, 0), mask_copy)
    background.save(os.path.join('/Users/arthurlamard/Documents/ISEN5/reco_formes/results', mask.filename))
    print(f'save at path : {os.path.join("/Users/arthurlamard/Documents/ISEN5/reco_formes/results", mask.filename)}')
    '''
    # open the image
    Image1 = Image.open('/Users/arthurlamard/Documents/ISEN5/reco_formes/results/isen_Building_0.png')
    Image2 = Image.open(background_image)
    back_im = Image2.copy()
    back_im.paste(Image1, (0, 0))
    back_im.save('/Users/arthurlamard/Documents/ISEN5/reco_formes/results/final_2.png')