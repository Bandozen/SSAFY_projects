# 01_pjt

## problem_a

**학습했던 내용**

- 딕셔너리의 형태 및 만드는 방법!(Key와 Value 값을 사용해서 나열한다.)
- json을 활용해 데이터를 불러오는 방법!(전에 api 실습 때 get을 사용했다.)

**어려웠던 부분**

- 첫 번째 문제에서는 딱히 어려웠던 부분은 없었다... json을 활용해서 나열만 했기 때문!!

**코드**

```python
import json
from pprint import pprint


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.
    # 나는 여기서 나열만 해준거다!
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
```

**느낀 점**
개념 정리 느낌이랄까... 흠... 첫번째를 기분좋게 시작해서 좋았다.

## problem_b

**학습했던 내용**

- 리스트 안에 딕셔너리 데이터를 가져오는 방법은 []를 두번 써주는 것이다!
- sort를 활용해 데이터를 오름차순 혹은 내림차순으로 정렬할 수 있다.
- append를 활용해 리스트에 데이터를 추가한다.
- update와 pop을 활용해 딕셔너리의 데이터를 추가하거나 삭제할 수 있다.

**어려웠던 부분**

- 데이터의 값들을 비교하는 부분에서 많이 헤맸다.
- 아직 함수들의 사용법을 제대로 파악하지 못해서 어떤 곳에 사용해야 하는지 판단이 느리다.

**코드**

```python
import json
from pprint import pprint

내가 했던 풀이
def movie_info(movie, genres):
    pass
    # 여기에 코드를 작성합니다.
    # 여기에 코드를 작성합니다.
    movie_data = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }

    genrename = []            # 일단 장르이름을 담아줄 빈 배열을 하나 생성!
    for i in range(len(genres_list)):
        # 처음 movie.json의 장르 아이디의 첫번째와 장르리스트의 아이디가 같거나
        # 두번째와 아이디가 같으면 장르이름 배열에
        # 장르리스트의 이름을 추가해준다!
        if movie.get('genre_ids')[0]  == genres_list[i]["id"] or movie.get('genre_ids')[1] == genres_list[i]["id"]:
            genrename.append(genres_list[i]["name"])
    # pprint로 인해 자동정렬되서 출력되므로 내림차순을 시켜준 다음
    genrename.sort(reverse=True)
    # 만들었던 배열을 기존 딕셔너리에 새로운 내용으로 추가해주고
    movie_data.update(genres_name=genrename)
    # 기존 아이디는 삭제 시키고 리턴해준다.
    movie_data.pop("genre_ids")
    return movie_data

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

```

**느낀 점**
나는 내 방식대로 고민해서 풀었는데 교수님의 간단한 풀이를 보고 약간 좌절감(?)을 느꼈었다...
그래도 뭐랄까... 일단 내가 만든 코드도 잘 나왔다는 것에 만족감을 느꼈고 계속 연습해서
교수님처럼 최대한 간단하게 코드를 짜내는 연습도 해봐야 할것 같다.

## problem_c

**학습했던 내용**

- 기존에 썼던 함수를 임포트해서 재사용하기!

**어려웠던 내용**

- 없음.

**코드**

```python
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

```

**느낀 점**
일단 b에서 교수님이 해주신 풀이법을 활용해 c에 그대로 임포트해주고 풀이했다. 나름대로 무난하게 풀었고 나중에 시간이 되면 내가 했던 풀이법을 c에 그대로 적용해야겠다.

## problem_d

**학습했던 내용**

- f포맷팅을 활용해서 제이슨 파일을 반복문을 돌려서 열었음
- max함수값을 사용해서 최댓값을 구함

**어려웠던 내용**

- 무비폴더 안에 있는 제이슨 파일들을 여는 방법부터 막혔다.
- 분명 숫자로만 이루어져있어서 방법이 있을 것 같았는데 id값이 동일한 것을 보고 해결했다.

**코드**

```python
import json


def max_revenue(movies):
    pass
    # 여기에 코드를 작성합니다.
    revenue_list = []
    for i in range(len(movies_list)):
        # 제이슨파일의 숫자랑 무비리스트의 아이디 숫자랑 동일하다!
        movies_id = movies_list[i]['id']
        # f포맷팅을 활용해서 제이슨파일을 열어주고 있음!
        movie = open(f'data/movies/{movies_id}.json', encoding='utf-8')
        movie_detail = json.load(movie)
        # 수익 내용을 빈배열에 담아주고
        revenue_list.append(movie_detail.get('revenue'))
        # 거기서 최댓값이 수익과 같다면 제목변수에 담아주었다!
        if max(revenue_list) == movie_detail.get('revenue'):
            title = movie_detail.get('title')

    movie_dict = {
        title : max(revenue_list)
    }
    # 마지막으로 제목을 리턴!
    return title



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))

```

**느낀 점**
역대급으로 막혀서 교수님의 도움과 성주님의 도움을 많이 받은 문제였다. 딕셔너리의 형태로도 접근을 해보고 리스트형태로도 접근을 해봤는데 결국에는 둘다 혼용해서 사용했다!
특히 마지막에 정답이 나왔을 때 너무나 기분이 좋았었다. 성취감이 이런건가....

## problem_e

**학습했던 내용**

- 리스트의 슬라이싱을 활용해 데이터를 추출해 낼 수 있다.

**어려웠던 점**

- d문제를 풀었다면 무리없이 접근할 수 있었던 문제다.

**코드**

```python
import json
import datetime

def dec_movies(movies):
    pass
    # 여기에 코드를 작성합니다.
    # 배열 형태로 답이 나와있기 때문에 빈 배열들을 생성!
    dec_list = []
    movie_dec = []
    for i in range(len(movies_list)):
        # 여기는 d와 동일하다!
        movies_id = movies_list[i]['id']
        movie = open(f'data/movies/{movies_id}.json', encoding='utf-8')
        movie_detail = json.load(movie)
        # 개봉날짜를 가져와 dec_list에 추가해주는 코드!
        dec_list.append(movie_detail.get('release_date'))
        # dec_list를 슬라이싱을 통해 12월달의 영화들을 movie_dec에 추가해주는 코드!
        if dec_list[i][5:7] == '12':
            movie_dec.append(movie_detail.get('title'))

    return movie_dec


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))

```

**느낀 점**
처음에는 datatime을 임포트해서 월만 출력해서 풀어볼까 하다가 그냥 배웠던 것을 활용해서 문제를 풀었다. 그리고 슬라이싱해서 나온 값을 그냥 12로 설정하다가 순간 리스트 안에 있는 값들은 문자열이라는 것을 인지하고 '12'로 변경해줘서 답을 출력했다.
