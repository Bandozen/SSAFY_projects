import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    # f포맷팅을 시켜서 맨 마지막 쿼리부분에 타이틀을 시시각각으로 변하게 해줘야 함!
    url = f"https://api.themoviedb.org/3/search/movie?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR&query={title}"
    response = requests.get(url).json()
    # 검색할 수 없는 영화일 경우 total_results의 값이 0이기 때문에
    # 여기서 먼저 조건을 걸어줘서 None을 받아주고 아닌 경우에는 계속 코드를 돌린다.
    # 아니면 results가 빈 배열로 나오니 조건을 response.get("results") == [] 이렇게 해줘도 무방!
    if response.get("total_results") == 0:
        return None
    results_ = response.get("results")
    get_id = results_[0]["id"]
    # 두번째 url같은 경우에는 id값에 따라 주소가 변하므로 f포맷팅을 id값에 주었다.
    url2 = f"https://api.themoviedb.org/3/movie/{get_id}/recommendations?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR&page=1"
    response2 = requests.get(url2).json()
    results2 = response2.get("results")
    # 이후는 b번문제와 동일!
    title_list = []
    for i in range(len(results2)):
        title_list.append(results2[i]["title"])
    
    return title_list
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
