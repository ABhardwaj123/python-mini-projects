import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv("comments.csv")
x_train , x_test , y_train , y_test = train_test_split(df['comment'] , df['label'] , test_size=0.2 , random_state=30)
#here we split the data : training data and testing data
#test size tells in what ratio to divide into training and testing data
#random state decides randomness of picking data

model = Pipeline([
    ('tfidf' , TfidfVectorizer()) ,
    ('classification' , LogisticRegression())
])

model.fit(x_train , y_train)

score = model.score(x_test , y_test)
print(f"accuracy of the trained model: {round(score * 100, 2)}")