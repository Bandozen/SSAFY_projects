<template>
  <div class="menu-list">
    <h1>3. 옵션을 고르세요.</h1>
    <ul>
      <OptionListItem
        v-for="(option, index) in optionList"
        :key="index"
        :option="option"
      />
    </ul>
  </div>
</template>

<script>
import OptionListItem from "@/components/OptionListItem.vue";

export default {
  name: "OptionList",
  components: {
    OptionListItem,
  },
  computed: {
    optionList: function () {
      // console.log(this.$store.state.optionList)
      return this.$store.state.optionList;
    },
  },
  methods: {
    increase() {},
    decrease() {},
  },
  // created() {
  //   console.log(11, this.$store.state.optionList);
  // },
};
</script>

<style></style>
