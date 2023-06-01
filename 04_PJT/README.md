# 04_PJT

## Model 클래스 선정
- 관통프로젝트의 Model들은 단순히 Type설정만 해준 것이 아닌 요소마다 조건이 있었다.
- Genre 필드같은 경우에는 List와 Tuple 형식을 이용하여 choice를 활용해 선택할 수 있도록 하였다.
- Score 필드같은 경우에는 attr 안에 일일히 조건을 명시한대로 써주었다.
- 그리고 bootstrap5버전을 설치한 후 그대로 load해준 결과 형식에 맞게 잘 출력되었다.


## View 작업
- 허용 HTTP Method의 방법을 까먹어서 교재에 있던 것을 참고해 GET과 POST의 방식을 나눠서 적어줬다.
- GET 같은 경우에는 잘 쓰이지 않고 safe를 써주는 것이 바람직하니 참고!

```html
# get이 아닌 safe를 사용한 모습!
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)
```

## Admin 작업
- 관리자아이디를 생성한 후 Model만 참조해주면 끝!

## Template 작업
- 수업, 실습 내내 했던 CRUD 작업이라 손에 매우 익숙했다. 예전에는 외워서 그냥 손이 따라간 거였다면 지금은 어느정도 흐름을 파악해서 빠른 시간내에 Template을 작업할 수 있었다.

## 힘들었던 점
- 작업은 다 끝냈고 부트스트랩을 활용해 홈페이지를 꾸미는 것이 머리가 아팠다.
- 아무래도 개발자의 입장보단 사용자의 입장에서 생각해야 하기 때문에 더 그랬던 것 같다.
- 나름 프론트엔드에 관심이 있고 더 열심히 할려고 했지만 언제나 홈페이지를 꾸미는 건 쉽지 않다.