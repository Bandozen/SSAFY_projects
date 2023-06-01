# 02_pjt



## problem_a

**학습했던 내용**
- url안에 api주소를 불러와 json파일을 열 수 있다.
- json파일 안에 있는 데이터들을 불러와 출력할 수 있다.

**어려웠던 내용**
- 없었다!

**코드**
```python
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

```

**느낀 점**
복습은 정말 중요하다. api주소를 불러오는 걸 계속 반복해서 연습해야 할 것 같다!


## problem_b

**학습했던 내용**
- 반복문을 통해서 그 안에 조건에 해당하는 것들만 리스트에 추가해줄 수 있다.

**어려웠던 내용**
- 없었다!

**코드**
```python
import requests
from pprint import pprint


def vote_average_movies():
    pass 
    # 여기에 코드를 작성합니다.
    url = "https://api.themoviedb.org/3/movie/popular?api_key=a51700c7b5c0eac2db0ce7a959dcc750"
    response = requests.get(url).json()
    results = response.get("results")
    # title이라는 빈 배열하나를 만들어줍니다.
    title = []
    # 반복문을 results길이만큼 돌려줍니다.
    for i in range(len(results)):
      # 그 중 평점이 8점 이상인 것을 조건으로 걸어줍니다.
      if results[i]["vote_average"] >= 8:
        # 해당하는 것이 있다면 그 영화목록을 title리스트에 계속 추가해줍니다.
        title.append(results[i])
    
    return title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
```

**느낀 점**
여기까지도 충분히 잘해낼 수 있었다. 내가 원하고자 하는 데이터의 값을 정확히 인덱싱하는 능력을 길러야 할 것 같다.



## problem_c

**학습했던 내용**
- sort 혹은 sorted함수를 통해 리스트 안의 내용을 정렬할 수 있다.
- 새로운 모듈을 import해와서 적용시킬 수 있다.

**어려웠던 내용**
- 새로운 모듈인 itemgetter 사용법이 익숙치 않아 구글링을 통해서 배웠다.

**코드**
```python
import requests
from pprint import pprint
from operator import itemgetter


def ranking():
    pass 
    # 여기에 코드를 작성합니다.
    url = "https://api.themoviedb.org/3/movie/popular?api_key=a51700c7b5c0eac2db0ce7a959dcc750"

    response = requests.get(url).json()
    
    results = response.get("results")
    

    # 교수님이 알려주셨던 lambda를 이용해 정렬하는 방법!
    # 뒤에 reverse를 통해 내림차순을 시켜주었다.
    results.sort(key = lambda x : x['vote_average'], reverse = True)
    title = []
    for i in range(5):
      title.append(results[i])
    
    # itemgetter를 사용해서 정렬하는 방법!
    # results_sorted = sorted(results, key = itemgetter('vote_average'), reverse = True)
    # for i in range(5):
    #   title.append(results_sorted[i])
    
    return title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
```

**느낀 점**
교수님이 알려주셨던 lambda를 통해서도 해보고 더 쉬운 방법이 없을까하고 찾아보던 중 itemgetter라는 모듈을 발견했다. sorted와 함께 쓰이는 모듈이었는데 가지고 와야하는 데이터의 제목만 써주면 되는 거였다. lambda안에 썼던 함수와 비슷한 결로 작동했다.
그래도 확실히 편한것만 추구하다보면 코딩실력이 비약적으로 늘어나는 건 아닌것 같다. 생각하는 힘을 더 길러보고 나서 라이브러리 모듈의 힘을 빌려야겠다.



## problem_d

**학습했던 내용**
- b번문제와 동일(심화 버전이라고 생각)

**어려웠던 내용**
- url을 2개 가지고 와서 변수에 담아줘야 한다.
- url 그대로 붙여넣기하면 안되고 f포맷팅을 시켜주어 시시각각으로 값을 변하게 만들어줘야 함
- id 검색에 실패할 경우 None을 반환하는 케이스에서 조건을 설정하는데 어려움을 겪었다.

**코드**
```python
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
```

**느낀 점**
url을 2개나 만들어줘서 변수를 지정하는데 많이 헷갈렸다. 특히 두번째 results를 출력할때 response2라고 해줘야 하는데 계속 첫번째 response값을 넣어서 오답이 출력됐다.
f포맷팅을 어디에다가 넣어야하는지 파악하는 것도 중요!



## problem_e

**학습했던 내용**
- d번 문제와 동일!
- 반복문 안에 조건을 걸어서 해당하는것만 리스트에 추가해준다.
- 딕셔너리 안에 value값을 리스트형태로 넣어줄 수 있다.

**어려웠던 내용**
- d번 문제를 풀었다면 무난히 풀 수 있을 것이다.
- 딕셔너리화하는 부분 다시 공부!

**코드**
```python
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
```

**느낀 점**
처음했던 1차 관통보다는 빨리 끝낼 수 있어서 다행이었다. url주소를 요청하고 데이터를 가져오는 것이 익숙했다면 5문제 모두 쉽게 풀 수 있을 것이다.

## problem_f

#### 날짜를 입력받아 해당 날짜의 영화랭킹을 알아보자!

**코드**
```python
import requests
from pprint import pprint
import time

def ranking():
    pass
    # 무한 반복문을 계속 돌려주기 위해서 while문을 사용!
    while True:
        # 먼저 date값을 입력해줍니다. 예시형태를 참고하세요!
        date = int(input())
        url = f"https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={date}"
        # date 범위를 설정해줍니다.
        if date >= 20120101 and date <= 20230127:
            response = requests.get(url).json()
            results = response.get("boxOfficeResult")
            boxoffice = results.get("dailyBoxOfficeList")
            print("잠시만 기다려주세요...")
            # time 모듈을 import해서 긴장감있게(?) 출력을 해보았다.
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("결과는????")
            time.sleep(1)
            for i in range(len(boxoffice)):
                # 1~10위까지 저장되있어서 10위까지 출력이 나온다.
                print(f"{int(boxoffice[i]['rank'])}위 : {boxoffice[i]['movieNm']}")
            break
        else:
            # 만약 날짜형식이 잘못됐다면 다시 입력하라는 문구와 함께 처음부터 돌아가기!
            print("날짜를 다시 입력해주세요!!")

            
    

print("====================================")
print("날짜별 영화 랭킹을 알고 싶으신가요??")
print("====================================")
print("원하는 날짜를 입력해주세요!(Ex. 20120101)")
ranking()
```

**느낀 점**
처음으로 선택 과제까지 끝냈다! 일단 제대로 작동은 돼서 매우 뿌듯하다. 근데 date 설정해줄때 기본 날짜 형식을 맞춰서 입력값을 받아야하는데 아직 부족하다. 지금은 사이 범위값으로 어떻게든 메꿨지만 예를 들어서 입력값이 '20169999' 일 경우 가장 최근 영화 순위를 출력하게 된다. 이런 오류가 나면 사고다. 더 공부해서 고쳐봐야겠다.

### 주의해야 할 점!
```python
# Falsy
# False로 취급되는 값들
# 0, "", [], ...
result = []

# result에 값이 있다라고 조건을 걸어줌
if result :
    # 만약 리스트가 비어있지 않으면 여기 실행
    print(result[0])
else:
    # 리스트가 비어있으면 여기가 실행된다.
    print("리스트가 비었습니다.")
```

**알아야 할점**
- 앞으로 알고리즘 문제를 파이썬으로 풀텐데 위에 있는 코드를 습관화 하자!