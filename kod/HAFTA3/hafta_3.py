import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.naive_bayes import GaussianNB ,CategoricalNB # CategoricalNB yerine GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 1. Veri Yükleme
# Not: Dosya yollarının doğru olduğundan emin olun
train = pd.read_csv("mitbih_train.csv", header=None) # Genelde bu veri setinde header yoktur
test = pd.read_csv("mitbih_test.csv", header=None) 

# Pandas dataframe'i numpy array'e çevirme
train_arr = train.values
test_arr = test.values

# 2. Veriyi Özellik (X) ve Etiket (y) olarak ayırma
# İlk 187 sütun sinyal verisi, son sütun (187. index) sınıftır.
X_train = train_arr[:, :187] 
y_train = train_arr[:, 187] 

X_test = test_arr[:, :187] 
y_test = test_arr[:, 187] 


gnb = CategoricalNB()
gnb.fit(X_train, y_train) 

# 4. Tahmin
y_pred = gnb.predict(X_test) 

# 5. Değerlendirme ve Görselleştirme
cm = confusion_matrix(y_test, y_pred) 


index = ['N', 'S', 'V', 'F', 'Q']  # MIT-BIH sınıfları (Normal, Supraventricular, vs.)
columns = ['N', 'S', 'V', 'F', 'Q']    

cm_df = pd.DataFrame(cm, columns, index)        

plt.figure(figsize=(10,6))   
sns.heatmap(cm_df, annot=True, fmt="d", cmap="YlGnBu") 
plt.title("Confusion Matrix - Gaussian Naive Bayes")
plt.ylabel("Gerçek Değerler")
plt.xlabel("Tahmin Edilen Değerler")
plt.show()

# Metrikler
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nSınıflandırma Raporu:\n")
print(classification_report(y_test, y_pred, target_names=index))