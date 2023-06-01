<template>
  <div class="">
    <div>
      <h1 v-if="weather">{{ weather }}한 날씨에는 이런 영화 보세요!</h1>
      <button @click="randomMovie">PICK</button>
      <hr>
      <div class="d-flex justify-content-center">
        <div class="card" style="width: 18rem">
          <img :src="getImageUrl(movieImgsrc)" alt="" />
          <div class="card-body">
            <h3>{{ movieTitle }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: "RandomView",
  data() {
    return {
      movieTitle: null,
      movieImgsrc: null,
      genre_ids: null,
      recommand: {
        Clouds: [18, 10749, 53, 10751],
        Clear: [80, 36, 28, 27],
        Snow: [35, 10752, 37, 99],
        Rain: [14, 16, 12, 9648],
      }
    }
  },
  methods: {
    randomMovie() {
      // const index = _.random(0, 19)
      // this.movieTitle = this.movieList[index].original_title
      // this.movieImgsrc = this.movieList[index].poster_path

      const weatherGenre = this.recommand[this.weather]
      const filterMovie = this.movieList.filter(movie => {
        return movie.genre_ids.some(genreId => weatherGenre.includes(genreId))
      })
      
      if (filterMovie) {
        const randomIdx = _.random(0, filterMovie.length-1)
        this.movieTitle = filterMovie[randomIdx].original_title
        this.movieImgsrc = filterMovie[randomIdx].poster_path
        console.log(this.movieTitle)
      } else {
        this.movieTitle = "추천 영화 없습니다."
        this.movieImgsrc = null
      }
    },
    getImageUrl(posterPath) {
        if (posterPath) {
          return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
        }
    },
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    },
    weather() {
      return this.$store.state.weatherNow
    }
  },
}
</script>
