<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <div class="menu-box">
      <MenuListItem
        v-for="(menu, index) in menuList"
        :key="index"
        :menu="menu"
      />
    </div>
  </div>
</template>

<script>
import MenuListItem from "@/components/MenuListItem.vue";

export default {
  name: "MenuList",
  components: {
    MenuListItem,
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList;
    },
  },
  methods: {
    selectMenu: function () {},
  },
};
</script>

<style>
.menu-list {
  width: 400px;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  margin-left: 10px;
  margin-right: 10px;
}

.menu-box {
  height: 220px;
  overflow-y: scroll;
}
</style>
