<template>
  <div>
    <WatchListForm />
    <WatchListItem v-for="(watch, idx) in watchList" :key="idx" :watchitem="watch" />
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'
import WatchListForm from '@/components/WatchListForm.vue'
export default {
  name: 'WatchListView',
  components: {
    WatchListItem,
    WatchListForm
  },
  computed: {
    watchList() {
      return this.$store.state.watchList
    }
  },
  created() {
    this.$store.dispatch('loadMovies')
  }
}
</script>

<style>

</style>