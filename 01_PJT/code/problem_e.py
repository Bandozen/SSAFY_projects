import json
import datetime

def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.
    dec_list = []
    movie_dec = []
    for i in range(len(movies_list)):
        movies_id = movies_list[i]['id']
        movie = open(f'data/movies/{movies_id}.json', encoding='utf-8')
        movie_detail = json.load(movie)
        dec_list.append(movie_detail.get('release_date'))
        if dec_list[i][5:7] == '12':
            movie_dec.append(movie_detail.get('title'))

    return movie_dec
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
