from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv("Student_Marks.csv")

Y = data[["Marks"]]
X = data[["number_courses","time_study"]]

model = LinearRegression()

model.fit(X, Y)

# 3,6.335,32.357
model_tahmin = model.predict([[3, 6.335]]) # =  32.33884377
print("Tahmin :", model_tahmin)

print("Score :", model.score(X, Y))

