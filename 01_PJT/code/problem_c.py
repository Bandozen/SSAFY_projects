import json
from pprint import pprint
import problem_b

# 교수님 풀이!
def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.
    movie_list = []
    

    # 함수 재사용
    for movie in movies:
        movie_list.append(problem_b.movie_info(movie, genres))

    return movie_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
