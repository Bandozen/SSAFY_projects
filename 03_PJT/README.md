# 03 Pjt

## 01_nav_footer.html

첫 번째 문제는 Nav바와 footer를 잘 설정해주면 되는 거였다.
요즘은 부트스트랩이 너무나 친절하기 때문에 복사+붙여넣기를 한 후 약간의 margin과 padding을 넣어줘서 위치 조절만 잘해주면 된다.

- 모달 창 부분을 예전에 배웠었는데 헷갈렸다. 더 공부해야지
- sticky 와 fixed 의 차이점을 파악했다. 상단은 왠만하면 sticky를 주고 하단은 fixed를 줍시다.

*첫번째 문제에서 가장 중요한 점은 **모달창**이다. 모달창의 위치는 body바깥부분에 설치해줘야 한다. 다른 태그의 영향을 받지 않기 위해서다.
일단 코드를 한번 살펴보자.*


```html
<body>
    <!-- 상단 바 부분! -->
    <!-- 색깔은 navbar와 배경색 둘 다 dark를 넣어줬다. 그리고 상단에 고정하기 위해서 'sticky-top'를 사용했다! -->
    <nav
      class="navbar navbar-expand-md navbar-dark bg-dark sticky-top"
    >
      <div class="container-fluid bg-dark">
        <a class="navbar-brand" href="02_home.html">
          <img src="images/logo.png" width="130" />
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" aria-current="page" href="02_home.html"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <!-- 로그인 모달을 먼저 만든 다음에 body바깥에 modal창을 만들어 주자 -->
            <li class="nav-item">
              <a
                class="nav-link"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop"
                >Login</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- 바닥 부분 -->
    <!-- 바닥 부분은 'fixed-bottom'을 사용했다! -->
    <footer class="card-footer fixed-bottom">
      <div
        class="footer d-flex justify-content-center align-items-center text-black"
      >
        Web-bootstrap PJT by chanik
      </div>
    </footer>

    <!-- Bootstrap JS -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
      crossorigin="anonymous"
    ></script>
  </body>

  <!-- 로그인 모달 창 -->
  <!-- body가 끝난 바로 다음 줄에 해준다. 이 이유는 모달은 기본적으로 display가 none 인 상태에서 시작하는데 어떠한 동작으로 인해 나타나는 창이다. 즉, 다른 어떤 태그의 영향도 받지 않아야 하기 때문에 body 바깥에다가 설치해주는 것이 국룰! -->
  <div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label"
                >Email address</label
              >
              <input
                type="email"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
              />
              <div id="emailHelp" class="form-text">
                We'll never share your email with anyone else.
              </div>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label"
                >Password</label
              >
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
              />
            </div>
            <div class="mb-3 form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="exampleCheck1"
              />
              <label class="form-check-label" for="exampleCheck1"
                >Check me out</label
              >
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
```

## 02_home.html

2번 문제는 캐러셀과 그리드 카드를 이용하면 쉽게 풀 수 있다. 이미지를 넣고 navbar에 강조하는 색깔을 넣어주면 무난하게 해결!

```html
<body>
    <!-- 01_nav_footer에서 완성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <div class="container-fluid bg-dark">
        <a class="navbar-brand" href="02_home.html">
          <img src="images/logo.png" width="130" />
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <!-- 홈 화면이니까 홈 글자 강조해주기! -->
              <a class="nav-link text-light" aria-current="page" href="02_home.html"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop"
                >Login</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- 02_home.html -->
    <header>
      <div
        id="carouselExampleAutoplaying"
        class="carousel slide"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img
              src="images/header1.jpg"
              class="d-block w-100"
              alt="이미지 표시할수 없음!"
            />
          </div>
          <div class="carousel-item">
            <img
              src="images/header2.jpg"
              class="d-block w-100"
              alt="이미지 표시할수 없음!"
            />
          </div>
          <div class="carousel-item">
            <img
              src="images/header3.jpg"
              class="d-block w-100"
              alt="이미지 표시할수 없음!"
            />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleAutoplaying"
          data-bs-slide="prev"
        ></button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleAutoplaying"
          data-bs-slide="next"
        ></button>
      </div>
    </header>
    <div class="div1 d-flex justify-content-center align-items-center">
      <h1><b>Boxoffice</b></h1>
    </div>
    <div>
      <section style="margin-left: 40px; margin-right: 40px;">
        <div class="row row-cols-1 row-cols-sm-3 g-3">
          <div class="col">
            <article>
              <div class="card">
                <img src="images/movie1.jpg" class="card-img-top" />
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">
                    This is a longer card with supporting text below as a
                    natural lead-in to additional content. This content is a
                    little bit longer.
                  </p>
                </div>
              </div>
            </article>
          </div>
          <div class="col">
            <article>
              <div class="card">
                <img src="images/movie2.jpg" class="card-img-top" />
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">
                    This is a longer card with supporting text below as a
                    natural lead-in to additional content. This content is a
                    little bit longer.
                  </p>
                </div>
              </div>
            </article>
          </div>
          <div class="col">
            <article>
              <div class="card">
                <img src="images/movie3.jpg" class="card-img-top" />
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">
                    This is a longer card with supporting text below as a
                    natural lead-in to additional content. This content is a
                    little bit longer.
                  </p>
                </div>
              </div>
            </article>
          </div>
          <div class="col">
            <article>
              <div class="card">
                <img src="images/movie4.jpg" class="card-img-top" />
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">
                    This is a longer card with supporting text below as a
                    natural lead-in to additional content. This content is a
                    little bit longer.
                  </p>
                </div>
              </div>
            </article>
          </div>
          <div class="col">
            <article>
            <div class="card">
              <img src="images/movie5.jpg" class="card-img-top" />
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">
                  This is a longer card with supporting text below as a natural
                  lead-in to additional content. This content is a little bit
                  longer.
                </p>
              </div>
            </div>
            </article>
          </div>
          <div class="col">
            <article>
            <div class="card">
              <img src="images/movie6.jpg" class="card-img-top" />
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">
                  This is a longer card with supporting text below as a natural
                  lead-in to additional content. This content is a little bit
                  longer.
                </p>
              </div>
            </div>
          </div>
          </article>
        </div>
      </section>
    </div>

    <!-- Bootstrap JS -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
  </body>

  <!-- 로그인 모달 창 -->
  <div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label"
                >Email address</label
              >
              <input
                type="email"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
              />
              <div id="emailHelp" class="form-text">
                We'll never share your email with anyone else.
              </div>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label"
                >Password</label
              >
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
              />
            </div>
            <div class="mb-3 form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="exampleCheck1"
              />
              <label class="form-check-label" for="exampleCheck1"
                >Check me out</label
              >
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
```

## 03_community.html

3번 문제는 display 속성을 정확히 이해했는가에 대한 문제다. 크기에 따라 해당 영역의 크기를 변경해줘야 했으며 또한 기존 영역이 사라지고 새로운 테이블 영역을 나타내는 것이 포인트다!

- display none 속성을 이용해 처음에 보이지 않게 설정해놓는다.(모달과 같은 원리!)
- 테이블과 게시판 목록은 한 줄에 붙어있기 때문에 한 태그 안에 두개의 부분으로 나누어주어야 한다. 즉 row와 col 성질을 잘 이용하면 한 줄에 나타낼 수 있다!

```html
<body>
    <!-- 01_nav_footer에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
    <!-- 상단 바 부분 -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <div class="container-fluid bg-dark">
        <a class="navbar-brand" href="02_home.html">
          <img src="images/logo.png" width="130" />
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" aria-current="page" href="02_home.html"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <!-- 커뮤니티 글자 강조해주기!! -->
              <a class="nav-link text-light" href="03_community.html"
                >Community</a
              >
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop"
                >Login</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- 03_community.html -->
    <main class="main">
      <h1 class="title">Community</h1>
      <!-- Aside - 게시판 목록 -->
      <!-- row로 묶어준다!! -->
      <aside class="row">
        <!-- 첫번째 col은 12분의 2! -->
        <ul class="list-group col-lg-2">
          <a href="#" class="list-group-item text-primary" aria-current="true">
            Boxoffice
          </a>
          <a href="#" class="list-group-item text-primary">Movies</a>
          <a href="#" class="list-group-item text-primary">Genres</a>
          <a href="#" class="list-group-item text-primary">Actors</a>
        </ul>
        <!-- 두번째 col은 12분의 10! -->
        <div class="d-none d-lg-block col-lg-10">
          <table class="table">
            <thead class="table-dark">
              <tr>
                <td>영화 제목</td>
                <td>글 제목</td>
                <td>작성자</td>
                <td>작성 시간</td>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Great Movie Title</td>
                <td>Best Movie Ever</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <td>Great Movie Title</td>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <td>Great Movie Title</td>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
              <tr>
                <td>Great Movie Title</td>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minute ago</td>
              </tr>
            </tbody>
          </table>
        </div>
    <!-- 다시 태그를 닫아줌으로써 row 끝! -->
      </aside>

      <!-- Section - 게시판 -->
      <section class="section">
        <div class="d-lg-none">
          <hr />
          <div>
            <article>
              <h1>Best Movie Ever</h1>
              <h2>Great Movie Title</h2>
              <p>user</p>
              <p>1 minute ago</p>
            </article>
          </div>
          <hr />
          <div>
            <article>
              <h1>Movie Test</h1>
              <h2>Great Movie Title</h2>
              <p>user</p>
              <p>1 minute ago</p>
            </article>
          </div>
          <hr />
          <div>
            <article>
              <h1>Movie Test</h1>
              <h2>Great Movie Title</h2>
              <p>user</p>
              <p>1 minute ago</p>
            </article>
          </div>
        </div>
      </section>
      <div class="page d-flex justify-content-center align-items-center">
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
      </div>
    </main>

    <!-- 바닥 부분 -->
    <footer class="card-footer fixed-bottom">
      <div
        class="footer d-flex justify-content-center align-items-center text-black"
      >
        Web-bootstrap PJT by chanik
      </div>
    </footer>

    <!-- Bootstrap JS -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
  </body>

  <!-- 로그인 모달 창 -->
  <div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label"
                >Email address</label
              >
              <input
                type="email"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
              />
              <div id="emailHelp" class="form-text">
                We'll never share your email with anyone else.
              </div>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label"
                >Password</label
              >
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
              />
            </div>
            <div class="mb-3 form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="exampleCheck1"
              />
              <label class="form-check-label" for="exampleCheck1"
                >Check me out</label
              >
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
```