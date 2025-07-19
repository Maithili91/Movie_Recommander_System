import streamlit as st
import pandas as pd
import pickle
# import requests

# def fetch_poster(id):
#     response=requests.get('Enter Your API key'.format(id))
#     data=response.json()
#     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommanded(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    
    recommanded_movies=[]
    recommanded_movies_poster=[]
    for i in movie_list:
        id=movies.iloc[i[0]].id
        recommanded_movies.append(movies.iloc[i[0]].title)
        # recommanded_movies_poster.append(fetch_poster(id))
    return recommanded_movies,recommanded_movies_poster


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommander System')
selected_movie_name= st.selectbox('How would you like to be connected',movies['title'].values)


if st.button('recommanded'):
    recommandation=recommanded(selected_movie_name)
    for i in recommandation:
        st.write(i)
