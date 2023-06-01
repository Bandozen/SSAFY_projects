<template>
  <div>
    <p :class="{'is-canceled': watchitem.is_canceled}"
    @click="cancel(watchitem)">{{watchitem.title}}</p>
  </div>
</template>

<script>
export default {
  name: 'WatvhListItem',
  props:{
    watchitem: Object
  },
  methods: {
    cancel(watchitem){
      return this.$store.dispatch('updateitem', watchitem)
      // watchitem.is_canceled = !watchitem.is_canceled
    }
  }
}
</script>

<style>
.is-canceled {
  text-decoration: line-through;
  color: rgb(112, 112, 112);
}
</style>