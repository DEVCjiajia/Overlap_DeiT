import paddle
import paddle.nn.functional as F
import paddle.vision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import cv2

print(paddle.__version__)#打印版本号
paddle.set_device('cpu')

def get_train_transforms():
    aug_op_list = []
    aug_op_list.append(transforms.ToTensor())
    transforms_train = transforms.Compose(aug_op_list)
    return transforms_train



dataset = paddle.vision.datasets.Cifar10(mode='train', transform=get_train_transforms())
print('图片：')
t=dataset[3]
print(type(t[0]))
print(t[0].shape)
print(t[1])
a=t[0]
a=a.transpose([1,2,0])
a=a.numpy().astype('float')*255
print(type(a))
print(a.shape)
cv2.imwrite("filename.png", a)