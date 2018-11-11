__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

for i in range(208):
    #assign color based on color based on "M" or "R" labels
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"

    #plot rows of data as if they were series data
    dataRow = rocksVMines.iloc[i,0:60]
    dataRow.plot(color=pcolor, alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()

##绘制烟花iris数据集的平行坐标图（可视化）
#from sklearn import datasets
#import pandas as pd
#import matplotlib.pyplot as plot
#iris=datasets.load_iris()
#Xdata=pd.DataFrame(iris.data)
#ydata=pd.DataFrame(iris.target)
#data=pd.concat([Xdata,ydata],axis=1)
#data.columns=[0,1,2,3,4]
#for j in range(150):
#    if data.iat[j,4] ==0:
#        pcolor = 'red'
#    elif data.iat[j,4] == 1:
#        pcolor ='blue'
#    else:
#        pcolor ='green'
#    datarow=data.iloc[j,0:4]
#    datarow.plot(color=pcolor,alpha=0.5)
#    
#plot.xlabel("Attribute Index")
#plot.ylabel("Attribute value")
#plot.show()