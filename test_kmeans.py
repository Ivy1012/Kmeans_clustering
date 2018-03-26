
# coding: utf-8

# In[11]:


# coding=utf-8   
'''
Using kmeans to cluster a matrix and illustrate the result meanwhile.
'''

from sklearn.cluster import Birch  
from sklearn.cluster import KMeans  
from numpy import *  
import time  
import matplotlib.pyplot as plt 

## step 1: load data  
print ("step 1: load data..." ) 
dataSet = []   
fileIn = open("C:\\Users\\Administrator\\Desktop\\P2V\\kmeans-master\\testSet.txt")  
for line in fileIn.readlines(): 
	temp=[]
	lineArr = line.strip().split('\t')  #dismiss the '\n' at the end using line.strip
	temp.append(float(lineArr[0]))
	temp.append(float(lineArr[1]))
	dataSet.append(temp)
    #dataSet.append([float(lineArr[0]), float(lineArr[1])])  
fileIn.close()  
print(dataSet)
print('Data loading finished')

## step 2: clustering...  
print ("step 2: clustering..."  )
dataSet = mat(dataSet) 
clf = KMeans(n_clusters=3)  
y_pred = clf.fit_predict(dataSet)  
print(clf)
print(y_pred)
print('Clustering finished')
  
## step 3: show the result  
print ("step 3: show the result..."  )
x = [n[0,0] for n in dataSet]   
y = [n[0,1] for n in dataSet] 

plt.scatter(x, y, c=y_pred, marker='o')
plt.title("Kmeans-Basketball Data")
plt.legend(["A","B","C"]) 
plt.xlabel("test_x")        
plt.ylabel("test_y")        
plt.show()  

print('All done')

