import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    revenue_list = []
    for i in range(len(movies_list)):
        movies_id = movies_list[i]['id']
        movie = open(f'data/movies/{movies_id}.json', encoding='utf-8')
        movie_detail = json.load(movie)
        revenue_list.append(movie_detail.get('revenue'))
        if max(revenue_list) == movie_detail.get('revenue'):
            title = movie_detail.get('title')
           
    movie_dict = {
        title : max(revenue_list)
    }
    return title
    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
