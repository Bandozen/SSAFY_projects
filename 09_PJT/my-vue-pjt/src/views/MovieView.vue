<template>
  <div class="justify-content-center">
    <MovieCard />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'movieView',
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },
  components: {
    MovieCard
  },
  created() {
    this.getMovies();
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  }
}
</script>


<style>

</style>
