import PIL.ImageFilter
import cv2
import numpy as np
import matplotlib.pylab as pylab

pylab.rcParams['font.sans-serif'] = ['SimHei']


def conv2d(img):
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    img_edge = cv2.filter2D(img, -1, kernel)
    return img_edge
    # lena_noise = np.concatenate((np.expand_dims(img, axis = 2), np.expand_dims(img, axis = 2), np.expand_dims(img, axis = 2)),
    #                          axis = -1)
    # img_edge = np.concatenate((np.expand_dims(img_edge, axis = 2), np.expand_dims(img_edge, axis = 2), np.expand_dims(img_edge,axis = 2)),
    #                          axis = -1)


# # path = "img-47647-dog.png"
# path = "img-45275-cat.png"
# # img = cv2.imread("img-45275-cat.png", 1)
# img = cv2.imread(path, 1)
# b, g, r = cv2.split(img)
# img = cv2.merge([r, g, b])
# x = conv2d(b)
# y = conv2d(g)
# z = conv2d(r)
# img_edge = cv2.merge([z, y, x])
# 
# pylab.imshow(img)
# pylab.axis('off')
# pylab.show()
# 
# print(img.shape)
# pylab.imshow(img_edge)
# pylab.axis('off')
# pylab.show()
# 
# print(img_edge.shape)
# img_edge = img_edge * 0.45
# img = img * 0.55
# img = img + img_edge
# pylab.imshow(img.astype('int'))
# pylab.axis('off')
# pylab.show()

from PIL import Image, ImageFilter


#
# def conv2d(img):
#     # Roberts算子
#     # kernelx = np.array([[-1, 0], [0, 1]], dtype = int)
#     # kernely = np.array([[0, -1], [1, 0]], dtype = int)
#     # x = cv2.filter2D(img, cv2.CV_16S, kernelx)
#     # y = cv2.filter2D(img, cv2.CV_16S, kernely)
#     # # 转uint8
#     # absX = cv2.convertScaleAbs(x)
#     # absY = cv2.convertScaleAbs(y)
#     #
#     # Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
#     return Roberts


def roberts():
    path = "img-45275-cat.png"
    # # path = "F:\手机照片\zhuanzhuan\1300016554.png"
    # # path = "825033661.png"
    img = Image.open(path)
    img = np.array(img)
    # # img = cv2.imread(path, 1)
    # #
    # # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # #
    # # img = cv2.resize(img, (224, 224))
    # #
    r, g, b = cv2.split(img)
    x = conv2d(r)
    x = (x).astype('int')
    y = conv2d(g)
    y = (y).astype('int')
    z = conv2d(b)
    z = (z).astype('int')
    img_edge = cv2.merge([x, y, z])
    # #
    pylab.subplot(1, 2, 1), pylab.imshow(img), pylab.title('原始图像'), pylab.axis('off')  # 坐标轴关闭
    pylab.subplot(1, 2, 2), pylab.imshow(img_edge), pylab.title('锐化'), pylab.axis('off')
    pylab.show()
    # #
    # # pylab.show()
    #
    # # for i in range(img.shape[0]):
    # #     for j in range(img.shape[1]):
    # #         if (img_edge[i][j].mean() > 10):
    # #             img_edge[i][j] = img_edge[i][j] * 0.80 * 15
    # #             img[i][j] = img[i][j] * 0.20
    # #             img[i][j] = img[i][j] + img_edge[i][j]
    # #
    # img_edge = img.filter(ImageFilter.SHARPEN)
    # img_edge = img_edge.filter(ImageFilter.SHARPEN)
    #
    # pylab.subplot(1, 2, 1)
    # pylab.imshow(img)
    #
    # a = np.array(img)
    # b = np.array(img_edge)
    #
    # img_edg = a * 0.75 + b * 0.25
    # img_edg = img_edg.astype('int')
    #
    # print(img_edg.shape)
    #
    # pylab.subplot(1, 2, 2)
    # pylab.imshow(img_edg)
    # pylab.show()


def ruihua_PIL():
    pylab.gca().xaxis.set_major_locator(pylab.NullLocator())
    pylab.gca().yaxis.set_major_locator(pylab.NullLocator())
    pylab.subplots_adjust(top = 1, bottom = 0, left = 0, right = 1, hspace = 0, wspace = 0)

    path = "img-45275-cat.png"
    # path = "F:\手机照片\zhuanzhuan\1300016554.png"
    # path = "825033661.png"
    img = Image.open(path)


    # kernel = [-2, -2, -2,-2, 32, -2,-2, -2, -2]

    # kernel=PIL.ImageFilter.Kernel((3, 3),(
    #     -2, -2, -2,
    #     -2, 32, -2,
    #     -2, -2, -2,
    # ), None, 1)

    kernel=PIL.ImageFilter.Kernel((3, 3),(
        -2, -2, -2,
        -2, 32, -2,
        -2, -2, -2,
    ), 16, 1)
    #  img_edge = img.filter(ImageFilter.SHARPEN)
    # img_edge = img_edge.filter(ImageFilter.SHARPEN)
    img_edge1 = img.filter(kernel)
    img_edge = img_edge1.filter(kernel)

    img = img.resize((224, 224))
    img_edge1=img_edge1.resize((224,224))
    img_edge=img_edge.resize((224, 224))
    # pylab.subplot(1, 5, 1)
    pylab.imshow(img),pylab.title('原始图像,λ为100%'), pylab.axis('off')
    pylab.show()
    pylab.gca().xaxis.set_major_locator(pylab.NullLocator())
    pylab.gca().yaxis.set_major_locator(pylab.NullLocator())
    pylab.subplots_adjust(top = 1, bottom = 0, left = 0, right = 1, hspace = 0, wspace = 0)

    a = np.array(img)
    b = np.array(img_edge)

    # pylab.subplot(1, 5, 2)
    pylab.imshow(img_edge1),pylab.title('单锐化，λ为0%'), pylab.axis('off')
    pylab.show()
    pylab.gca().xaxis.set_major_locator(pylab.NullLocator())
    pylab.gca().yaxis.set_major_locator(pylab.NullLocator())
    pylab.subplots_adjust(top = 1, bottom = 0, left = 0, right = 1, hspace = 0, wspace = 0)

    img_edg = a * 0.25 + b * 0.75
    img_edg = img_edg.astype('int')

    # pylab.subplot(1, 5, 3)
    pylab.imshow(img_edge),pylab.title('双锐化，λ为0%'), pylab.axis('off')
    pylab.show()
    pylab.gca().xaxis.set_major_locator(pylab.NullLocator())
    pylab.gca().yaxis.set_major_locator(pylab.NullLocator())
    pylab.subplots_adjust(top = 1, bottom = 0, left = 0, right = 1, hspace = 0, wspace = 0)

    b=np.array(img_edge1)
    img_edg = a * 0.5 + b * 0.5
    img_edg = img_edg.astype('int')

    # pylab.subplot(1, 5, 4)
    pylab.imshow(img_edg), pylab.title('单锐化，λ为50%'), pylab.axis('off')
    pylab.show()
    pylab.gca().xaxis.set_major_locator(pylab.NullLocator())
    pylab.gca().yaxis.set_major_locator(pylab.NullLocator())
    pylab.subplots_adjust(top = 1, bottom = 0, left = 0, right = 1, hspace = 0, wspace = 0)

    b=np.array(img_edge)
    img_edg = a * 0.5 + b * 0.5
    img_edg = img_edg.astype('int')

    # pylab.subplot(1, 5, 5)
    pylab.imshow(img_edg), pylab.title('双锐化，λ为50%'), pylab.axis('off')
    pylab.show()



ruihua_PIL()
# roberts()
# filterargs = (3, 3), 16, 0, (
#         -2, -2, -2,
#         -2, 32, -2,
#         -2, -2, -2,
#     )
# print(filterargs)
