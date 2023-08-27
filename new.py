import pandas as pd
data = pd.read_csv('sets/arr.txt', encoding='utf-8')
data.head()

# clean columns
data.columns = ['output', 'input']
data.head()

data.isna().sum()

data.shape

# Create Feature and Label sets
X = data['input']
y = data['output']

# train test split (66% train - 33% test)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123)

print('Training Data :', X_train.shape)
print('Testing Data : ', X_test.shape)

# Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train)
X_train_cv.shape

# Training Logistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train_cv, y_train)

# prediction

from sklearn import metrics

# transform X_test using CV
X_test_cv = cv.transform(X_test)

# Create a prediction set:
predictions = lr.predict(X_test_cv)
#print(predictions)
index=0
xlist=X_test.tolist()
predictionlist=predictions.tolist()
index=0
while (index<500):
    print(xlist[index]+" Предсказание типа: "+predictionlist[index])
    index+=1
while True:
    inputs = input("Введите адрес: ")
    print(inputs)
    inputs=pd.Series(inputs)
    inputs= cv.transform(inputs)
    predictions = lr.predict(inputs)
    print(predictions.tolist())
