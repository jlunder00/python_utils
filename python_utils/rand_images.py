import random
import numpy as np
from PIL import Image
from pathlib import Path





def random_rgb(width,height):
    im = Image.new("RGB", (height,width))
    im = np.array(im)

    for r in range(0, height):
        for c in range(0,width):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            im[r][c] = [red,green,blue]
    img = Image.fromarray(im, 'RGB')
    return img

def save_image(img, path=Path('./image'), format='jpg'):
    img.save(str(path), format)


if __name__ == '__main__':
    for i in range(100, 2000, 200):
        save_image(img=random_rgb(i, i), path=Path('/Data/test_images/image_'+str(i)+'_'+str(i)), format='jpg')

