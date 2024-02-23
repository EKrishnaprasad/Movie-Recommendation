import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://www.omdbapi.com/?t={}&apikey=cb0f076c'.format(movie_id))
    data=response.json()
    return data['Poster']
new = pickle.load(open('movies.pkl','rb'))
movies_list=new['title'].values
st.title('Movie Recommender System ')
def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in distances[1:6]:
        recommended_movies.append(new.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(new.iloc[i[0]].title)
        )
    return recommended_movies,recommended_movies_posters

similarity = pickle.load(open('similarity.pkl','rb'))

option = st.selectbox(
    'Enter your favourite movie ', movies_list )

if st.button('Recommend'):
    recommendation,posters =recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendation[0])
        st.image(posters[0])
    with col2:
        st.text(recommendation[1])
        st.image(posters[1])

    with col3:
        st.text(recommendation[2])
        st.image(posters[2])
    with col4:
        st.text(recommendation[3])
        st.image(posters[3])
    with col5:
        st.text(recommendation[4])
        st.image(posters[4])
