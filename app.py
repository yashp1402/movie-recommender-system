import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/'+str(movie_id)+'?api_key=cd5c8e600dfd93c0320258ee614248b5&language=en-US')
    print(response)
    data = response.json()
    print('Inside fetch_poster')
    print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    # sorting based on second index
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x : x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # Fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendor System')

selected_movie_name = st.selectbox( 
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    # for i in recommendations:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])