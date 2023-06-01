<template>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div
      class="col d-flex justify-content-center"
      v-for="(movie, idx) in movieList"
      :key="idx"
    >
      <div class="card" style="width: 18rem">
        <img
          :src="getImageUrl(movie.poster_path)"
          class="card-img-top"
          alt="..."
        />
        <div class="card-body">
          <h5 class="card-title">{{ movie.original_title }}</h5>
          <p class="card-text">
            {{ movie.overview }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "movieCard",
  methods: {
    getImageUrl(posterPath) {
      if (posterPath) {
        return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
      }
    },
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  }
};
</script>

<style>
</style>