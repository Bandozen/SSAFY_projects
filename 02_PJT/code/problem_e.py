import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    # 배열을 만드는 것까지는 d번문제와 동일하다!
    url = f"https://api.themoviedb.org/3/search/movie?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR&query={title}"
    response = requests.get(url).json()
    if response.get("total_results") == 0:
        return None
    results_ = response.get("results")
    get_id = results_[0]["id"]
    url2 = f"https://api.themoviedb.org/3/movie/{get_id}/credits?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=en-US"
    response2 = requests.get(url2).json()
    cast = response2.get("cast")
    crew = response2.get("crew")
    cast_list = []
    crew_list = []
    for i in range(len(cast)):
        # 문제에 나오듯이 10미만인 것들만 리스트에 담아줘야 한다!
        if cast[i]["cast_id"] < 10:
            cast_list.append(cast[i]["name"])
    for i in range(len(crew)):
        # department가 Directing인 것들만 리스트에 담아줘야 한다!
        if crew[i]["department"] == "Directing":
            crew_list.append(crew[i]["name"])

    # 예시답안을 보면 딕셔너리화 돼있으므로 딕셔너리 형태로 만들어줘야 한다.
    staff = {'cast' : cast_list,
            'directing' : crew_list}

    return staff


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
