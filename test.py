from cv2 import cv2
import numpy as np
import os
from PIL import Image
import math
import operator
from functools import reduce
import time

from ImageHash import compareIH

def compare(pic1,pic2):
    '''
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果
    '''
    # image1 = Image.open(pic1)
    # image2 = Image.open(pic2)

    # histogram1 = image1.histogram()
    # histogram2 = image2.histogram()

    # differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))


    #print(differ)
    differ = PHash.score(pic1,pic2)
    return differ

def compareHist(stdimg, ocimg):
    stdimg = cv2.imread(str(stdimg), 0)
    ocimg = cv2.imread(str(ocimg), 0)
    stdimg = np.float32(stdimg)
    ocimg = np.float32(ocimg)
    stdimg = np.ndarray.flatten(stdimg)
    ocimg = np.ndarray.flatten(ocimg)
    imgocr = np.corrcoef(stdimg, ocimg)
    if imgocr[0, 1] > 0.6:
        print("imgocr",imgocr[0, 1])
    return imgocr[0, 1] > 0.90

g1 = os.walk(r"xjcy")
g2 = os.walk(r'muyu')
file_list1 = []
file_list2 = []

if __name__ == '__main__':
    # time_start = time.time()
    # for i in range(100):
    #     compare(r'.\\muyu\\27.jpg',r'.\\top\\23.jpg')
    # time_end = time.time()
    # print('time cost', time_end - time_start, 's')
    #
    # time_start1 = time.time()
    # for i in range(100):
    #     compareIH(r'.\\muyu\\27.jpg', r'.\\top\\23.jpg',4)
    # time_end1= time.time()
    # print('time cost', time_end1 - time_start1, 's')
    #
    # print('done')
    for path, dir_list, file_list in g1:
        for file_name in file_list:
            #print(os.path.join(path, file_name))
            file_list1.append(os.path.join(path, file_name))

    for path, dir_list, file_list in g2:
        for file_name in file_list:
            #print(os.path.join(path, file_name))
            file_list2.append(os.path.join(path, file_name))

    file_list1.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
    file_list2.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
    file1_len = len(file_list1)
    file2_len = len(file_list2)
    current = 0
    print(file_list1)
    print(file_list2)
    dic = {i: -1 for i in range(file2_len)}
    dic[file2_len] = file1_len
    print(dic)
    for idx, file2 in enumerate(file_list2):
        index=current+1
        while index<file1_len:
            file1 = file_list1[index-1]
            #二分法
            if idx/file2_len*2 <index/file1_len:
                break
            if(compareIH(file1,file2,4)):
                print("找到相近的图片：", idx, file2, file1, index, current)
                current = index
                break
            index+=1

def BinarySearch(dict,low,high,pic):

    return dict

def findSimiPic(file_list1,file_list2,dict,index,low,high):
    file1_len = len(file_list1)
    file2_len = len(file_list2)
    file1_low = dict[low]
    file1_high = dict[high]

    file1_index = file1_low
    while file1_index < file1_high:
        file1 = file_list1[index-1]

        if idx/file2_len*2 <index/file1_len:
            break
        if(compareIH(file1,file2,4)):
            print("找到相近的图片：", file2, file1, file1_index)
            dict[index]=file1_index
            return dict
        file1_index+=1
    dict[index]=-2
    return dict

def findSimilarPic(file_list1,file_list2,dict,index, low,high):
    if(index==low or index == high or dict[index]>0):
        return 
    file1_len = len(file_list1)
    file2_len = len(file_list2)
    file1_low = dict[low]
    file1_high = dict[high]
    mid = int(low + (high - low)/2)
    r = findSimiPic(file_list1, file_list2, dict, index, low, high)
    plus = True
    count = 1
    current = index
    if(r[index]>0):
        return r
    else:            
        while(index - count >= low and index + count <= high and dict[current] < 0):
            count+=count
            if(plus):
                r1 = findSimiPic(file_list1, file_list2, dict, index+count, low, high)
                if(dict[index]>0):
                    return r1
            else:
                r2 = findSimiPic(file_list1, file_list2, dict, index - count, low, high)
                if(dict[index]>0):
                    return r2

            plus = not plus
    return dict

def findByMid(file_list1, file_list2, dict, index, low, high):
    if(index==low or index == high or dict[index]>0):
        return dict,low,high,-2
    file1_len = len(file_list1)
    file2_len = len(file_list2)
    file1_low = dict[low]
    file1_high = dict[high]
    mid = int(low + (high - low)/2)
    disc,low,high,flag = findByMid(file_list1, file_list2, dict, mid, low, high)
    if(flag == -1):
        return 1
