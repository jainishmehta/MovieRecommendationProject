import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index (index):
    return def[def.index ==-index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

#Read CSV file
df= pd.read_csv("movie_dataset.csv")

#Select Features
features = ['keywords', 'cast', 'genres', 'director']

#Create a column in DF to combine selected features
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
try: 
    return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " "+row["director"]
except:
    print "Error: ", row
df["combined_features"] = df.apply(combined_features, axis=1)

#step 4: create count matrix from this new combined column
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

#Cosine Similarilty based on count_matrix
cosine_sim = cosine_similarity(count_matrix)
movie_user_likes = "Avatar"

#Get index of this movie from its title
movie_index = get_index_from_title (movie_user_likes)

similar_movies = list(enumerate (cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies, key = Lambdax:x[1], reverse=True)

#Print titesl of first 50 movies
i=0
for element in sorted_similar_movies:
    print get_title_from_index(element[0])
    i = i+1
        if i>50:
            break
