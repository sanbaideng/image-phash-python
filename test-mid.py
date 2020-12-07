from cv2 import cv2
import numpy as np
import os
from PIL import Image
import math
import operator
from functools import reduce
import time
from ImageHash import compareIH
from FourPoint import FourPoint

g1 = os.walk(r"xjcy")
g2 = os.walk(r'muyu')
file_list1 = []
file_list2 = []
point  =   FourPoint()

def findSimilarPic(file_list1,file_list2,dic,index, low1,high1,low2,high2):
    #if(index<low or index > high or dic[index]>0):
    if(dic[index]>0):
        return False,dic,index,0,low,high
    file1_len = len(file_list1)
    file2_len = len(file_list2)

    mid = int(low + (high - low)/2)
    r = findSimiPic(file_list1, file_list2, dic, index, low, high)
    plus = True
    count = 0
    current = index
    if(r[index]>0):
        return True,r,index,low,0,high
    else:            
        while(index - count >= 0 or index +count <= file2_len):
            if(index - count <= low):
                plus = True
                current = index+count
                r = findSimiPic(file_list1, file_list2, dic, index+count, low, high)
                if(dic[current]>0):
                    return True,r,index+count,count,low,high
            elif(index + count >= high):
                plus = False
                current = index-count
                r = findSimiPic(file_list1, file_list2, dic, index-count, low, high)
                if(dic[current]>0):
                    return True,r,index-count,count,low,high
            elif(plus):
                current = index + count
                r = findSimiPic(file_list1, file_list2, dic, index+count, low, high)
                if(dic[current]>0):
                    return True,r,index+count,count,low,high
                else:
                    plus = not plus
            else:
                current = index - count
                r = findSimiPic(file_list1, file_list2, dic, index - count, low, high)                
                if(dic[current]>0):
                    return True,r,index-count,0-count,low,high
                else:
                    plus = not plus
              
            count+=1

    return False,r,current,count if plus else 0-count,low,high

def findSimiPic(file_list1,file_list2,fourPoint):
    file1_len = len(file_list1)
    file2_len = len(file_list2)
    file1_low = fourPoint.blow#dict[low]
    file1_high = fourPoint.bhigh#dict[high]

    file1_index = file1_low
    file2 = file_list2[fourPoint.index]
    while file1_index < file1_high:
        print(file1_index)
        file1 = file_list1[file1_index-1]
        if(index == 0 and file1_index/file1_len >0.33):
            return fourPoint
        
        # if(index!=0 and index/file2_len*2 <file1_index/file1_len):
        #     return dict

        if(compareIH(file1,file2,4)):
            print("找到相近的图片：", file2, file1, file1_index)
            #dict[index]=file1_index
            fourPoint.dic[index] = file1_index
            return fourPoint
        file1_index+=1
    fourPoint.setCurrentFalse()
    print(fourPoint.index,"没找到")
    return fourPoint


if __name__ == '__main__':
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
    #print(file_list1)
    #print(file_list2)
    dic = {i: -1 for i in range(file2_len)}
    dic[file2_len] = file1_len
    #print(dic)
    mid = int(file2_len/2)
    #flaga,dic,currenta,counta,lowa,higha=findSimilarPic(file_list1,file_list2,dic,0,0,file1_len)
    
    flagb,dic,currentb,countb,lowb,highb=findSimilarPic(file_list1,file_list2,dic,file2_len-1,0,file2_len,int(file1_len*2/3),file1_len)
    if(flag):
        low1 = low
        high1 = current
        low2 = 101
        high2 = high
        mid1 = int((low1+high1)/2)
        mid2 = int((low2+high2)/2)
    else:
        mid = int()

    
    if(count>0):
        high = current-count+1
        flag,dic,current,count,index,low,high=findSimilarPic(file_list1,file_list2,dic,mid,low,high)
    else:
        low = current+count+1
    flag,dic,current,count,index,low,high=findSimilarPic(file_list1,file_list2,dic,mid,low,high)


