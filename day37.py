import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#tf-idf algorithm helps in vectorisation of the dataset that further helps in recomendation system

data = [
  {
    "title": "Echoes of Eternity",
    "author": "Lena Frost",
    "genre": "Fantasy",
    "description": "A young mage discovers a forgotten prophecy that could reshape her entire kingdom."
  },
  {
    "title": "Shadows of Silicon",
    "author": "Mark Rivers",
    "genre": "Sci-Fi",
    "description": "In a world ruled by AI corporations, one hacker fights to restore human freedom."
  },
  {
    "title": "The Last Train North",
    "author": "Amira Voss",
    "genre": "Historical Fiction",
    "description": "A gripping tale of survival and friendship set during a war-torn winter."
  },
  {
    "title": "Whispers in the Pines",
    "author": "Caleb Stone",
    "genre": "Thriller",
    "description": "A detective returns to his hometown only to uncover dark secrets buried in the forest."
  },
  {
    "title": "Canvas of Dreams",
    "author": "Isabella Reed",
    "genre": "Romance",
    "description": "An aspiring painter and a writer find love and inspiration in a small coastal town."
  },
  {
    "title": "Fragments of Tomorrow",
    "author": "Noah Clarke",
    "genre": "Dystopian",
    "description": "After a cataclysmic event, a lone survivor pieces together the remnants of a shattered world to find hope again."
  }
]

df = pd.DataFrame(data)
df.to_csv("books.csv" , index=False)

print("books.csv created!")

vectoriser = TfidfVectorizer(stop_words='english')
#this returns us a matrix . stop_words means to ignore irrelevant words like a , an , the etc.

matrix = vectoriser.fit_transform(df['description'])
#as vectoriser gives us all the details , we will select only the description which matters the most for our suggestion maker

cosine_comparision = cosine_similarity(matrix , matrix)
#cosine similarity assigns certain values to key words
#we then compare those words by their values
#more closer the value to 1 , more they are related

indices = pd.Series(df.index , index=df['title'])

def give_recommendation(title , cosine_comparision):
    idx = indices[title]
    cosine_scores = list(enumerate(cosine_comparision[idx]))
    #listing the books (enumerating them)

    cosine_scores = sorted(cosine_scores , key=lambda x : x[1] , reverse=True)[1:6]
    #we sort books based on their cosine scores that is the first index(x[1]) , and we skip the first value because the first value is the book itself
    #so that is going to have cosine score of 1 

    book_indices = [i[0] for i in cosine_scores]
    #we are just extracting the book indices now after sorting them

    return df[['title' ,'author']].iloc[book_indices]
    #returning the corresponding author and title of the matching books