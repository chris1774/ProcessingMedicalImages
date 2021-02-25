import numpy as np
import cv2


##
# Objective: Simulate different types of acquisition patterns by implementing the
# following functions.
##

def cartesianPattern(mask_size, percent):
    # M = mask_size.shape[0]
    # N = mask_size.shape[1]
    M = mask_size[0]
    N = mask_size[1]
    Emask = np.zeros((M, N))

    center1 = M/2
    center2 = N/2
    percent = percent*100
    increment = int(M*percent/100)
    increment = int(M/increment)
    j = 0
    for i in range(0, M, increment):
        if j == 0:
            # mask = cv2.line(mask_size, (0,i), ( M-1,i), (1,1,1), 1)
            mask = cv2.line(Emask, (0,i), ( M-1,i), (1,1,1), 1)
        else:
            # mask += cv2.line(mask_size, (0,i), ( M-1,i), (1,1,1), 1)
            mask += cv2.line(Emask, (0,i), ( M-1,i), (1,1,1), 1)

    return mask


def circlePattern(mask_size, radius):
    # M = mask_size.shape[0]
    # N = mask_size.shape[1]
    M = mask_size[0]
    N = mask_size[1]
    Emask = np.zeros((M, N))
    center1 = M/2
    center2 = N/2
    # x,y = np.ogrid[-center1: center1, -center2: center2]
    # mask = x*x+y*y <= radius*radius
    # mask = cv2.circle(mask_size, (int(center2), int(center1)), radius, (1,1,1), -1)
    mask = cv2.circle(Emask, (int(center2), int(center1)), radius, (1,1,1), -1)
    return mask

def ellipsePattern(mask_size, major_axis, minor_axis, angle):
    # M = mask_size.shape[0]
    # N = mask_size.shape[1]
    M = mask_size[0]
    N = mask_size[1]
    Emask = np.zeros((M, N))
    center1 = M/2
    center2 = N/2
    center = (center2, center1)
    axes = (major_axis, minor_axis)

    mask = cv2.ellipse(Emask, (center, axes, angle), (1,1,1), -1)
    return mask


def bandPattern(mask_size, width, length, angle):

    M = mask_size[0]
    N = mask_size[1]
    Emask = np.zeros((M, N))
    center1 = M/2
    center2 = N/2
    if(width < 0):
        width = width*-1
    x_min, y_min = center2-length/2, center1-width/2
    x_max, y_max = center2+length/2,center1+width/2
    mask = cv2.rectangle(Emask, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (1,1,1), -1)
    return rotate_image(mask, angle)


def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result





def radialPattern(mask_size, ray_count):
    # M = mask_size.shape[0]
    # N = mask_size.shape[1]
    M = mask_size[0]
    N = mask_size[1]
    Emask = np.zeros((M, N))
    center1 = M/2
    center2 = N/2
    angle = 180/ray_count
    # mask = cv2.line(mask_size, (0, int(center1)),(N, int(center1)),(1,1,1), 1)
    mask = cv2.line(Emask, (0, int(center1)),(N, int(center1)),(1,1,1), 1)
    img = rotate_image(mask, angle)

    for i in range(2, ray_count+1):
        img += rotate_image(mask, angle*i)

    return img




def spiralPattern(mask_size, sparsity):
    mask = None
    return mask
