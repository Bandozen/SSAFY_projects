<template>
  <div>
    <div class="d-flex justify-content-bw align-items-center menu-item"
    :class="{selected : menu.selected}"
    @click="selectMenu">
      <img :src="menu.image" alt="이미지를 표시할 수 없습니다." />
      <p>{{ menu.title }}</p>
      <p>{{ menu.price }}원</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuListItem",
  props: {
    menu: Object,
  },
  methods:{
    selectMenu() {
      this.$store.dispatch("selectMenu", this.menu)
    }
  }
};
</script>

<style>
img {
  width: 50px;
  height: 50px;
  border-radius: 10px;
}

.menu-item {
  border: 1px solid black;
  border-radius: 10px;
  padding: 5px;
  margin-top: 5px;
  margin-bottom: 5px;
}

.selected{
  background-color: forestgreen;
  color: white
}

.d-flex {
  display: flex;
}

.justify-content-bw {
  justify-content: space-between;
}

.align-items-center {
  align-items: center;
}
</style>
