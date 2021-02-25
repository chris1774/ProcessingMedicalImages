import numpy as np
from PIL import Image

def convert_numpy_array_to_int_array(img_array):
    #print(len(img_array)) # will return number of pictures
    image_list = []
    i = 0
    while i < len(img_array):
        for photo_indiv in img_array[i]:
            image = photo_indiv.astype('float32')
            #image = image*255 # NOTE: for imgs_mask_test, the pixel value should be multiplied by 255
            image_list.append(image)
            # plot_image_save_to_file("jack", image)
            # print(image)
        i += 1
    return image_list

def averagesignaltonoise(noise):
    value = 0
    for i in noise:
        value = value + i
    value = value/noise.size
    return value

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

def idealLowpassFilter(emptymask, cutoff):
    # M = emptymask.shape[0]
    # N = emptymask.shape[1]
    M = emptymask[0]
    N = emptymask[1]
    center1 = M/2
    center2 = N/2
    Emask = np.ones((M, N))

    for i in range(1, M):
        for j in range(1, N):
            r1 = (i-center1)**2+(j-center2)**2
            r = np.sqrt(r1)
            if r > cutoff:
                # emptymask[i,j] = 0.0
                Emask[i, j] = 0.0

    mask = Image.fromarray(Emask)
    return mask


def idealHighpassFilter(emptymask, cutoff):
    # M = emptymask.shape[0]
    # N = emptymask.shape[1]
    M = emptymask[0]
    N = emptymask[1]
    center1 = M/2
    center2 = N/2
    Emask = np.ones((M, N))

    for i in range(1,M):
        for j in range(1,N):
            r1 = (i-center1)**2+(j-center2)**2
            r = np.sqrt(r1)
            if 0 < r < cutoff:
                #emptymask[i,j] = 0.0
                Emask[i,j] = 0.0

    # mask = Image.fromarray(emptymask) #you may need to comment this line out and just return the mask
    # return mask
    mask = Image.fromarray(Emask)
    return mask


def gaussianLowpassFilter(emptymask, cutoff):
    # M = emptymask.shape[0]
    # N = emptymask.shape[1]
    M = emptymask[0]
    N = emptymask[1]
    Emask = np.ones((M, N))

    center1 = M/2
    center2 = N/2
    t1 = 2*cutoff
    for i in range(1,M):
        for j in range(1,N):
            r1 = (i-center1)**2+(j-center2)**2
            r = np.sqrt(r1)
            if r > cutoff:
                # emptymask[i, j] = np.exp(-r**2/t1**2)
                Emask[i, j] = np.exp(-r**2/t1**2)

    # mask = Image.fromarray(emptymask)
    # return mask
    mask = Image.fromarray(Emask)
    return mask


def gaussianHighpassFilter(emptymask, cutoff):
    # M = emptymask.shape[0]
    # N = emptymask.shape[1]
    M = emptymask[0]
    N = emptymask[1]
    Emask = np.zeros((M, N))

    center1 = M/2
    center2 = N/2
    #t1 = 2*cutoff
    for i in range(emptymask[0]):
        for j in range(emptymask[1]):
            # r1 = (i-center1)**2+(j-center2)**2
            # r = np.sqrt(r1)
            # if 0 < r < cutoff:
            #     # emptymask[i, j] = 1 - np.exp(-r**2/t1**2)
            #     Emask[i, j] = 1 - np.exp(-r**2/t1**2)
            distance = np.sqrt((i - center1) ** 2 + (j - center2) ** 2)
            Emask[i, j] = 1 - np.exp(-(distance ** 2) / (2 * (cutoff ** 2)))

    # mask = Image.fromarray(emptymask)
    # return mask
    # mask = Image.fromarray(Emask)
    # return mask
    return Emask


def butterworthLowpassFilter(emptymask, cutoff, order):
    # M = emptymask.shape[0]
    # N = emptymask.shape[1]
    M = emptymask[0]
    N = emptymask[1]
    Emask = np.ones((M, N))
    center1 = M/2
    center2 = N/2

    for i in range(1, M):
        for j in range(1, N):
            r1 = (i-center1)**2+(j-center2)**2
            r = np.sqrt(r1)
            if r > cutoff:
                # emptymask[i, j] = 1/(1 + (r/cutoff)**order)
                Emask[i, j] = 1/(1 + (r/cutoff)**order)

    mask = Image.fromarray(Emask)
    return mask


def butterworthHighpassFilter(emptymask, cutoff, order):
    M = emptymask[0]
    N = emptymask[1]
    Emask = np.ones((M, N))
    center1 = M/2
    center2 = N/2
    for i in range(emptymask[0]):
        for j in range(emptymask[1]):
            distance = np.sqrt((i - center1) ** 2 + (j - center2) ** 2)
            Emask[i, j] = 1 / (1 + (cutoff / distance) ** (2*order))

    return Emask


def ringLowpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask


def ringHighpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask
