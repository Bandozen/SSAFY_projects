import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.
    # 먼저 url주소를 가져와 준다!
    url = "https://api.themoviedb.org/3/movie/popular?api_key=a51700c7b5c0eac2db0ce7a959dcc750"
    # requests 모듈을 사용해 url안에 json파일을 요청해서 가져온다.
    # 그 다음 response라는 변수에 담아준다
    response = requests.get(url).json()
    # 거기서 results가 영화목록이므로 변수 results에 다시 담아준다
    results = response.get("results")
    # 길이를 return하면 끝!
    return len(results)
            


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
