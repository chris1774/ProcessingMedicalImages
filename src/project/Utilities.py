import cv2
import numpy as np


def loadImage(image_path):
    image = cv2.imread(image_path, 0)
    return image


def loadMatrix(filename):
    matrix = np.load(filename, allow_pickle=True)
    return matrix


def saveImage(filename, image):
    cv2.imwrite(filename, image)
    return True


def saveMatrix(filename, matrix):
    np.save(filename, matrix)
    return True


def normalizeImage(image):
    return image / np.max(image) * 255


# Remember: the DFT its a decomposition of signals
#  To be able to save it as an image you must convert it.
def writableDFT(dft_image):
    converted = np.log(np.abs(dft_image))
    converted = (255 * (converted/ np.max(converted))).astype('uint8')
    return converted


# Use openCV to display your image"
# Remember: normalize binary masks and convert FFT matrices to be able to see and save them"
def displayImage(image):
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def getDFT(image):
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    return dft_shift


# Convert from fft matrix to an image"
def getImage(dft_img):
    f_ishift = np.fft.ifftshift(dft_img)
    img_back = np.fft.ifft2(f_ishift).real
    #img_back = np.abs(img_back)
    return img_back




# Both input values must be raw values"
def applyMask(image_dft, mask):
    return image_dft * mask


def signalToNoise():
    # a = np.asanyarray(a)
    # m = a.mean(axis)
    # sd = a.std(axis=0, ddof=0)
    # return np.where(sd == 0, 0, m/sd)
    return False

#[Provide] Use this function to acomplish a good final image
def post_process_image(image):
    a = np.min(image)
    b = np.max(image)
    k = 255
    image = (image - a) * (k / (b - a))
    return image.astype('uint8')
