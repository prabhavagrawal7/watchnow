import requests
imdb_id = "tt0114709"
API_KEY = "62c56bbac67642762ecb788540b5888e"
url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={API_KEY}&external_source=imdb_id"
r = requests.get(url = url)
print(r.json()["movie_results"][0]['backdrop_path'])
    
# print(r.json())


