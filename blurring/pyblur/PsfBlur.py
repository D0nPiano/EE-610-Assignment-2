import numpy as np
import pickle
from PIL import Image
from scipy.ndimage.filters import convolve
import os.path

pickledPsfFilename = os.path.join(os.path.dirname( __file__),"psf.pkl")

with open(pickledPsfFilename, 'rb') as pklfile:
    psfDictionary = pickle.load(pklfile, encoding='latin1')
    cur_filter = []
    for i in range(len(psfDictionary)):
        cur_row = []
        for m in range(len(psfDictionary[i])):
            cur_cul = []
            for n in range(len(psfDictionary[i][m])):
                old_val = psfDictionary[i][m][n]
                cur_cul.append([old_val])
            cur_row.append(cur_cul)
        cur_filter.append(cur_row)
    psfDictionary = cur_filter


def PsfBlur(cur_img, psfid):
    imgarray = np.array(cur_img, dtype="float32")
    kernel = psfDictionary[psfid]
    convolved = convolve(imgarray, kernel)
    convolved = convolved.astype("uint8")
    img = Image.fromarray(convolved)
    return img
    
def PsfBlur_random(img):
    psfid = np.random.randint(0, len(psfDictionary))
    return (PsfBlur(img, psfid), PsfBlur_getKernel(psfid))
    
def PsfBlur_getKernel(psfid):
    return psfDictionary[psfid]