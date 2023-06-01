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


