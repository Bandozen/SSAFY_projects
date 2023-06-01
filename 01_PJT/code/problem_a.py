import json
from pprint import pprint


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.
    movie_data = {
        'id' : movie_dict.get('id'),
        'title' : movie_dict.get('title'),
        'poster_path' : movie_dict.get('poster_path'),
        'vote_average' : movie_dict.get('vote_average'),
        'overview' : movie_dict.get('overview'),
        'genre_ids' : movie_dict.get('genre_ids')
    }
    return movie_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
