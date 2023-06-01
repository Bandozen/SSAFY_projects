<template>
  <li class="d-flex justify-content-bw order-item">
    <div class="d-flex">
      <img :src="order.menu.image" alt="" />
      <div
        class="d-flex flex-column justify-content-center"
        style="margin-left: 10px"
      >
        <p>{{ order.menu.title }}</p>
        <p>사이즈 : {{ order.size.name }}</p>
        <p v-for="(option, idx) in order.optionList" :key="idx" :option="option">
          {{ option.type }}
          횟수: {{ option.count }}
        </p>
      </div>
    </div>
    <div class="d-flex flex-column justify-content-center">
    <div>가격 : {{ totalPrice }} 원</div>
    </div>
  </li>
</template>

<script>
export default {
  name: "OrderListItem",
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      return (
        this.order.menu.price +
        this.order.size.price +
        this.order.optionList.reduce((sum, option) => {
          if (option.count > 0) {
            sum += option.count * option.price;
          }
          return sum;
        }, 0))
    },
  },
};
</script>

<style>
.order-item {
  padding: 10px;
}

.flex-column {
  flex-direction: column;
}
</style>
