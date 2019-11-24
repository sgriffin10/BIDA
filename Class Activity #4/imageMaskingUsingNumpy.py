# # Install scikit-image
# # "Dependencies" are installed
#
# # image read/write library
# from skimage import data
#
# # Use matplotlib to show the image
# import matplotlib.pyplot as plt
#
# # Built-in image provided by the library
# image = data.camera();
#
# # image is a numpy 2D array!
# print(type(image))
# print(image.shape)
# print(image)
# # See the image
# plt.imshow(image, cmap='gray')
# plt.show()
#
# # Mask - apply a transform across the entire image
# mask = image < 87
# print(mask)
#
# # Apply the mask
# image[mask]=255
# plt.imshow(image, cmap='gray')
# plt.show()