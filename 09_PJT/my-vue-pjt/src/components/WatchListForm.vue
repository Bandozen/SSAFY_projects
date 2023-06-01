<template>
  <div>
    <h1>보고싶은 영화</h1>
    <input type="text" v-model.trim="movieTitle" @keyup.enter="createMovie">
    <button @click="createMovie">ADD</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovie() {
      if (this.movieTitle) {
        this.$store.dispatch('createMovie', this.movieTitle)
      } else {
        alert("영화 제목을 입력하세요!")
      }
      this.movieTitle = null
    }
  }
}
</script>

<style>

</style>