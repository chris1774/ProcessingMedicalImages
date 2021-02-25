# Use this file as you wish to generate the images needed to answer the report
import numpy as np
import cv2
import src.project.Utilities as util
import src.project.ImageSynthesisNoise as isn
from PIL import Image
from matplotlib import pyplot as plt
import src.project.SelectiveImageAcquisition as sia



# #
# b = util.loadImage("images/brain.png")
# #util.displayImage(b)
# d = util.getDFT(b)
# print(d)
# M = d.shape[0]
# N = d.shape[1]
# mask = np.ones((M, N))
# # #########################################################################################################
# # #Butterworth Lowpass Filter
# #
# #I reused this code to produce the images in question 6 but with different values
# mask = isn.butterworthLowpassFilter(mask, 120, 4)
# con = util.applyMask(d, mask)
# img_back = util.getImage(con)
# util.saveImage("images/BLF.png", img_back)
#
# #This is to get the SNR which you will need to comment out the displayImage line to get to work
# noise = isn.signaltonoise(img_back)
# print(isn.averagesignaltonoise(noise))
#
# #########################################################################################################
# #Gaussian Lowpass and Highpass
# #I reused this code to produce the images in question 7 but with different values
#mask = isn.gaussianHighpassFilter(mask, 100)
# con = util.applyMask(d, mask)
# img_back = util.getImage(con)
# util.saveImage("images/GHF.png", img_back)


#########################################################################################################
#Question 8

dataset = util.loadMatrix("images/noisyimage.npy")
# d = util.getImage(dataset)
# util.saveImage('images/noisyImage.png', d)
M = dataset.shape[0]
N = dataset.shape[1]

array = np.zeros((M,N))
mask1 = isn.butterworthHighpassFilter(array, 50, 1)
mask2 = isn.idealHighpassFilter(array, 20)
mask3 = isn.gaussianHighpassFilter(array, 10)
mask4 = isn.butterworthLowpassFilter(array, 75, 1)
mask5 = isn.idealLowpassFilter(array, 50)
mask6 = isn.gaussianLowpassFilter(array, 50)
mask7 = sia.cartesianPattern(array, 0.05)
mask8 = sia.bandPattern(array, 100, 200, 0)
mask9 = sia.ellipsePattern(array, 50, 100, 0)
mask0 = sia.circlePattern(array, 150)

con = util.applyMask(dataset, mask8)
img_back = util.getImage(con)
img_back = util.normalizeImage(img_back)
util.saveImage('images/noisyImage.png', img_back)
#d = util.getDFT(img_back)


# con = util.applyMask(d, mask5)
# #con = util.applyMask(con, mask8)
# img_back = util.getImage(con)
# img_back = util.normalizeImage(img_back)
# #
# util.saveImage('images/noisyImage.png', img_back)


#util.displayImage(img)
# M = img.shape[0]
# N = img.shape[1]
#
# array = np.zeros((M,N))
#util.saveImage('images/noisyImage.png', img)





# m, n = img_noisy1.shape
# #
# # mask = np.ones([3,3], dtype=int)
# # mask = mask/9
#
# img_new1 = np.zeros([m, n])
#
# for i in range(1, m-1):
#     for j in range(1, n-1):
#         temp = [img_noisy1[i-1, j-1],
#                img_noisy1[i-1, j],
#                img_noisy1[i-1, j + 1],
#                img_noisy1[i, j-1],
#                img_noisy1[i, j],
#                img_noisy1[i, j + 1],
#                img_noisy1[i + 1, j-1],
#                img_noisy1[i + 1, j],
#                img_noisy1[i + 1, j + 1]]
#
#         temp = sorted(temp)
#         img_new1[i, j]= temp[4]
#
# img_new1 = img_new1.astype(np.uint8)
# util.saveImage('images/new_median_filter.png', img_new1)





# util.saveImage('images/noisyImage.png', dataset)
