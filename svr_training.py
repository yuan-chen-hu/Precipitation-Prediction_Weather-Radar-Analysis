from numpy import load
import time
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from sklearn import metrics
print("load start")
import csv
data=np.zeros((5171,4))
print("data.shape",data.shape)            
with open('result.csv',"rU", newline='') as csvfile:
    rows = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
    count=0
    for row in rows:	
        if count==5171:
            break
        for i in range(1,5):
            temp=float(row[i])
            data[count][i-1]=temp
        count+=1
print("data.shape=",data.shape)  
print(data)

train_x=np.zeros((4500,3))
train_x=data[:4500,0:3]     
print("train_x.shape=",train_x.shape)	
print(train_x)

train_y=np.zeros((4500,1))	            
train_y=data[:4500,3]
print("train_y.shape=",train_y.shape)	
print(train_y)

test_x=np.zeros((671,3))
test_x=data[4500:5171,0:3]     
print("test_x.shape=",test_x.shape)	
print(test_x)

test_y=np.zeros((671,1))	            
test_y=data[4500:5171,3]
print("test_y.shape=",test_y.shape)	
print(test_y)
#train x =temp , hum,radar
#train y = rainfall


print("training start")
scaler=Normalizer()
Normalizer().fit(train_x)
new_train_x=scaler.transform(train_x)
print("new_train_x=",new_train_x)
new_test_x=scaler.transform(test_x)
joblib.dump(scaler,"scaler.pkl")
#scaler2=joblib.load("scaler.pkl")

print("train start")
svr=SVR()

t0 = time.time()
svr.fit(new_train_x, train_y)
joblib.dump(svr,"svr_model.pkl")
svr_fit_time = time.time() - t0
print("svr_fit_time",svr_fit_time)
output_y=svr.predict(test_x)
print(output_y)

print("end")

print("score")
print("explained_variance_score=",metrics.explained_variance_score(test_y,output_y))
#print(metrics.max_error(test_y,output_y))
print("mean_absolute_error=",metrics.mean_absolute_error(test_y,output_y))
print("mean_squared_error=",metrics.mean_squared_error(test_y,output_y))
print("mean_squared_log_error=",metrics.mean_squared_log_error(test_y,output_y))
print("median_absolute_error=",metrics.median_absolute_error(test_y,output_y))
print("r2=",metrics.r2_score(test_y,output_y))

def z_to_r(z, a=200., b=1.6):
    print("old z_to_r working")
    return (z / a) ** (1. / b)
traditional_output_y=z_to_r(test_x[:,2])
print("score")
print("explained_variance_score=",metrics.explained_variance_score(test_y,traditional_output_y))
#print(metrics.max_error(test_y,output_y))
print("mean_absolute_error=",metrics.mean_absolute_error(test_y,traditional_output_y))
print("mean_squared_error=",metrics.mean_squared_error(test_y,traditional_output_y))
print("mean_squared_log_error=",metrics.mean_squared_log_error(test_y,traditional_output_y))
print("median_absolute_error=",metrics.median_absolute_error(test_y,traditional_output_y))
print("r2=",metrics.r2_score(test_y,traditional_output_y))

