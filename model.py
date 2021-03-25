import pandas as pd
import numpy as np 
from sklearn.utils import shuffle 
from sklearn.neighbors import  KNeighborsClassifier 
from sklearn import preprocessing
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
def knnmodel(inn):
   train=pd.read_csv(r"E:\lemon-dataset\train1.csv")
   test=pd.read_csv(r"E:\lemon-dataset\test.csv")
   trainlabel=train.Result.values
   testlabel=test.Result.values
   encode=preprocessing.LabelEncoder()
   train['Result']=encode.fit_transform(train['Result'])
   test['Result']=encode.fit_transform(test['Result'])
   train=train.drop('Result',axis=1).values
   test=test.drop('Result',axis=1).values
   tr=np.zeros(20)
   s=-11111
   k_max=0
   for i in range(5,20):
      knn=KNeighborsClassifier(n_neighbors=i)
      knn.fit(train,trainlabel)
      tr[i]=knn.score(test,testlabel)
      if(tr[i]>s):
          s=tr[i]
          k_max=i
   knn=KNeighborsClassifier(n_neighbors=k_max)
   knn.fit(train,trainlabel)
   plot_confusion_matrix(knn,test,testlabel)
   #plt.show()
   r=knn.predict(inn)
   return r
'''arr=np.array(['3','4','1','45'])
arr=arr.reshape(1,-1)
s=knnmodel(arr)
print(s)'''


