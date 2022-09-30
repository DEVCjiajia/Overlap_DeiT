import paddle
import paddle.nn.functional as F
import paddle.vision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import paddle
from paddle.vision.models import ResNet
from paddle.vision.models.resnet import BottleneckBlock, BasicBlock
import paddle
import paddle.vision.transforms as T
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import cv2

model_state_dict = paddle.load(r"D:\A.python文件\Overlap_DeiT\60.pdparams")
net = ResNet(BottleneckBlock, 50, 10)
net.set_dict(model_state_dict)
net.eval()

def get_train_transforms():
    aug_op_list = []
    aug_op_list.append(transforms.ToTensor())
    transforms_train = transforms.Compose(aug_op_list)
    return transforms_train


dataset = paddle.vision.datasets.Cifar10(mode = 'train', transform = get_train_transforms())
print('图片：')
t = dataset[3]
plt.imshow(t[0].transpose([1,2,0]).numpy())
plt.show()
ans = net(t[0])
print(np.argmax(ans.numpy()))
