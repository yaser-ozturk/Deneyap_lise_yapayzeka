from sklearn.datasets import load_iris 

iris = load_iris() # iris veri setini yükle

#print (iris.feature_names) # Girdi özellikleri (bağımsız değişkenler)   bunler liste mi ? iris bi nesne mi ?
#print (iris.target_names)  # Çiçek sınıfları (etiketler)
#print (iris.target)        # Her veri satırının hangi sınıfa ait olduğunu gösteren sayısal etiketler
#print (iris.data)          # veri setini yazdır


X = iris.data  # Modelin öğreneceği özellikler
Y = iris.target  # Modelin tahmin etmeye çalışacağı sınıf etiketleri



from sklearn.model_selection import train_test_split 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0) ## random state nedir ? 
print("Eğitim veri seti boyutu=",len(X_train)) 
print("Test veri seti boyutu=",len(X_test)) 


"""
from sklearn.tree import DecisionTreeClassifier 
model = DecisionTreeClassifier() 
"""

from sklearn.neighbors import KNeighborsClassifier 
model =  KNeighborsClassifier () 
model.fit(X_train,Y_train) 



Y_tahmin = model.predict( X_test ) 
print("Yolanan x=",X_test[0])
print("Gerçek etiketler=",Y_test) 
print("Tahmin edilen etiketler=",Y_tahmin)



from sklearn.metrics import confusion_matrix 
hata_matrisi = confusion_matrix(Y_test, Y_tahmin) 
print(hata_matrisi)   # bunu yorumla


import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 
index = ['setosa','versicolor','virginica']  
columns = ['setosa','versicolor','virginica']  
hata_goster = pd.DataFrame(hata_matrisi,columns,index)  


plt.figure(figsize=(10,6))  
sns.heatmap(hata_goster, annot=True) 
plt.show()




"""

"""