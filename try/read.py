import os

log_path = "log.txt"
out_path = "out.txt"


def read(path):
    data=[]
    with open(path, "r") as f:  # 打开文件
        lines = f.readlines()  # 调用文件的 readline()方法
        for line in lines:
            if (line.find('Validation Loss') !=- 1) and (line.find('Validation Acc@1: ')!=-1):
                epoch_pos=line.find('Epoch[')
                epoch=line[epoch_pos+6:epoch_pos+9]
                loss_pos=line.find('Loss: ')
                loss=line[loss_pos+6:loss_pos+12]
                acc_pos=line.find('Acc@1: ')
                acc=line[acc_pos+7:acc_pos+13]
                data.append([epoch,loss,acc])
        return data

def write(data,out_path):
    with open(out_path, 'w') as f:
        for i in data:
            f.write(i[0]+' '+i[1]+' '+i[2]+'\n')



def main():
    data=read(log_path)
    write(data,out_path)

if __name__ == "__main__":
    main()
