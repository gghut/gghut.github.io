# -*- coding: UTF-8 -*-
from math import *
from numpy import *
from matplotlib import pyplot as plt
from MySQLdb import connect
from datetime import *

def sigmoid(x):
    return 1.0/(1+exp(-x))
    return x

def loadDatas():
    db = connect('localhost','root','emsysggh','spider', charset="utf8mb4")
    code = '600000'
    start = '2017-11-08'
    end = '2017-11-09'
    cursor = db.cursor()
    cursor.execute("select date,price,turnover from record where code = %s and date BETWEEN %s and %s",(code,start,end))
    datas = cursor.fetchall()
    array = {}
    for data in datas:    
        time1 = datetime.strptime('2017-11-08 09:30', '%Y-%m-%d %H:%M')
        offset = data[0] - time1
        seconds = offset.total_seconds()/60
        if seconds > 210:
            seconds -= 90
        array[seconds] = data
    return array

def formatDatas(mapDatas):
    dataMat = []
    labelMat = []
    for k in range(235):
        dataMat.append([mapDatas[k+4][1],mapDatas[k+3][1],mapDatas[k+2][1],mapDatas[k+1][1],mapDatas[k][1],mapDatas[k+4][2],mapDatas[k+3][2],mapDatas[k+2][2],mapDatas[k+1][2],mapDatas[k][2]])
        labelMat.append(mapDatas[k+5][1]-mapDatas[k+4][1])
    return dataMat,labelMat

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights) 
        error = labelMat - h 
        weights += alpha * dataMatrix.transpose() * error
    return weights

dataMatIn,classLabels = formatDatas(loadDatas())

coefficient = gradAscent(dataMatIn, classLabels) 

a = [12.6,12.6,12.6,12.59,12.59,372060,208145,314500,128900,242500]
b = [12.65,12.65,12.64,12.63,12.63,125200,140000,119500,178600,311890]
c = [12.61,12.6,12.62,12.61,12.61,32901,79100,142300,64100,209100]

aMat = mat(c);
print coefficient
print aMat
print sigmoid(aMat * coefficient)