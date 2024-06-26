import requests
movie_id = 19995

response = requests.get('https://api.themoviedb.org/3/movie/' + str(movie_id) +'?api_key=cd5c8e600dfd93c0320258ee614248b5&language=en-US')
data = response.json()
print(data['poster_path'])