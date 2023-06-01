import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

const API_URL =
"https://api.themoviedb.org/3/movie/top_rated?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=en-US";

const W_API_URL = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kor&appid=9cbe77b703b0c172de8e80ade55ae511"

export default new Vuex.Store({
  state: {
    movieList:[
    ],
    watchList:[
    ],
    weatherNow: null,
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movieList) {
      state.movieList = movieList
    },
    CREATE_MOVIE(state, movieName){
      state.watchList.push(movieName)
    },
    WEATHER_LOAD(state, weatherNow){
      state.weatherNow = weatherNow
    },
    UPDATE_MOVIE(state, watchitem) {
      console.log(watchitem)
      state.watchList = state.watchList.map((movie) => {
        if (movie === watchitem) {
          movie.is_canceled = !movie.is_canceled
        }
        return movie
      })
    },
    LOAD_MOVIES(state) {
      const localStorageMovies = localStorage.getItem('watchList')
      const parsedMovies = JSON.parse(localStorageMovies)
      console.log(localStorageMovies)
      state.watchList = parsedMovies
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: API_URL,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data.results)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    createMovie(context, movieTitle) {
      const movieName = {
        title: movieTitle,
        is_canceled: false
      }
      context.commit("CREATE_MOVIE", movieName)
      context.dispatch("savemoviesToLocalStorage")
    },
    weatherLoad(context) {
      axios({
        method: "get",
        url: W_API_URL,
      })
        .then((res) => {
          // console.log(res.data.weather[0].description)
          context.commit('WEATHER_LOAD', res.data.weather[0].main )
        })
    },
    updateitem(context, watchitem) {
      context.commit('UPDATE_MOVIE', watchitem)
      context.dispatch('savemoviesToLocalStorage')
    },
    savemoviesToLocalStorage(context) {
      const jsonMovies = JSON.stringify(context.state.watchList)
      localStorage.setItem('watchList', jsonMovies)
    },

    loadMovies(context) {
      context.commit('LOAD_MOVIES')
    }
  },
  modules: {
  }
})