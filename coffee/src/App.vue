<template>
  <div id="app">
    <img class='starbucks' src="@/assets/스타벅스.png" alt="" />
    <h1 class='d-flex justify-content-center'>
      Coffee Order App
    </h1>
    <div class='order-board d-flex justify-content-bw'>
        <MenuList />
        <SizeList />
        <OptionList />
    </div>
    <OrderList />
  </div>
</template>

<script>
import MenuList from "@/components/MenuList.vue";
import SizeList from "@/components/SizeList.vue";
import OptionList from "@/components/OptionList.vue"
import OrderList from "@/components/OrderList.vue"

export default {
  name: "App",
  components: {
    MenuList,
    SizeList,
    OptionList,
    OrderList,
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

* {
  box-sizing: border-box;
  font-family: "Noto Sans KR", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

#app {
  text-align: center;
  width: 1300px;
  margin: 0 auto;
}

.justify-content-center {
  justify-content: center;
}

.order-board {
  margin-top: 100px;
  background-color: lightgray;
  padding: 20px;
  border-radius: 10px;
}

.starbucks {
  width: 400px;
  height: 400px;
}
</style>
