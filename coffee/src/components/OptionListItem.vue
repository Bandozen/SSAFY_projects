<template>
  <div class="d-flex justify-content-bw menu-item">
    <p class="size-item d-flex align-items-center justify-content-center">
      {{ option.type }}
    </p>
    <p class="size-item d-flex align-items-center justify-content-center">
      {{ option.price }}원
    </p>
    <div class="item d-flex align-items-center justify-content-bw">
      <button class="btn" @click="increase(option.type)">+</button>
      <p class="size-item d-flex align-items-center justify-content-center">
        {{ option.count }}
      </p>
      <button class="btn" @click="decrease(option.type)">-</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "OptionListItem",
  // created() {
  //   console.log(this.option);
  // },
  props: {
    option: Object,
  },
  methods: {
    increase(type) {
      this.$store.commit("increaseOption", type);
    },
    decrease(type) {
      this.$store.commit("decreaseOption", type);
    },
  },
};
</script>

<style>
.size-item {
  text-align: center;
  height: 50px;
  width: 50px;
}

.btn {
  width: 30px;
  height: 30px;
  border: 1px solid black;
  border-radius: 15px;
  padding: 5px;
  margin-left: 15px;
  margin-right: 15px;
}

.btn:hover {
  cursor: pointer;
  background-color: forestgreen;
  color: white;
}
</style>
