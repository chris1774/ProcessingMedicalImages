# Use this file as you wish to generate the images needed to answer the report
import src.project.Utilities as util
import src.project.SelectiveImageAcquisition as sia
#
# img = util.loadImage("images/cardiac.jpg")
# d = util.getDFT(img)

# img = util.loadImage("images/brain.png")
# d = util.getDFT(img)
# img_back1 = util.writableDFT(d)
# util.saveImage("images/CardiacDFT.png", img_back1)

array = (1000, 1000)
#mask = sia.ellipsePattern(array, 100, 1500, 0)
#mask = sia.circlePattern(array, 20)
mask = sia.bandPattern(array, 100, 200, 10)
#mask = sia.cartesianPattern(array, 1)
#mask = sia.radialPattern(array, 1)

mask_back = util.normalizeImage(mask)
util.saveImage("images/band_acquisition_pattern_10.png", mask_back)
#util.displayImage(mask_back)


# con = util.applyMask(d, mask)
# img_back = util.getImage(con)
# img_back = util.normalizeImage(img_back)
# img_back = util.post_process_image(img_back)
# util.saveImage("images/radial.png", img_back)
