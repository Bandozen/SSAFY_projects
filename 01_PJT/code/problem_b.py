import json
from pprint import pprint

# 내가 했던 풀이
# def movie_info(movie, genres):
#     pass 
#     # 여기에 코드를 작성합니다.  
#     # 여기에 코드를 작성합니다.
#     movie_data = {
#         'id' : movie.get('id'),
#         'title' : movie.get('title'),
#         'poster_path' : movie.get('poster_path'),
#         'vote_average' : movie.get('vote_average'),
#         'overview' : movie.get('overview'),
#         'genre_ids' : movie.get('genre_ids')
#     }
    
#     genrename = []
#     for i in range(len(genres_list)):
#         if movie.get('genre_ids')[0]  == genres_list[i]["id"] or movie.get('genre_ids')[1] == genres_list[i]["id"]:
#             genrename.append(genres_list[i]["name"])
#     genrename.sort(reverse=True)
#     movie_data.update(genres_name=genrename)
#     movie_data.pop("genre_ids")
#     return movie_data

# 교수님 풀이!
def movie_info(movie, genres):
    movie_dict = {'genre_names' : movie.get('genre_ids'), 'id' : movie.get('id'), 'overview' : movie.get('overview'), 'poster_path' : movie.get('poster_path'), 'title' : movie.get('title'), 'vote_average' : movie.get('vote_average')}
    genre_ids = movie["genre_ids"]
    movie_dict["genre_names"] = []

    for id in genre_ids:
        for genre in genres:
            if id == genre["id"]:
                movie_dict["genre_names"].append(genre["name"])
    return movie_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
