import Vue from "vue";
import Vuex from "vuex";
// 스토리지 사용하기 위해서 플러그인 설치
import createPersistedState from "vuex-persistedstate"
// 깊은 복사를 위한 lodash 설치
import _ from "lodash"

Vue.use(Vuex);

const orderState = createPersistedState({
  key: "coffee-app",
  // 명세서에는 로컬 스토리지가 아닌 세션 스토리지를 사용!
  storage: window.sessionStorage
});

export default new Vuex.Store({
  plugins: [orderState],
  state: {
    orderList: [],
    menuList: [
      {
        title: "아메리카노",
        price: 4500,
        selected: false,
        image: "https://source.unsplash.com/featured/?americano",
      },
      {
        title: "카페 라떼",
        price: 5000,
        selected: false,
        image: "https://source.unsplash.com/featured/?latte",
      },
      {
        title: "콜드 브루",
        price: 4800,
        selected: false,
        image: "https://source.unsplash.com/featured/?coldbrew",
      },
      {
        title: "초콜릿 모카",
        price: 5500,
        selected: false,
        image: "https://source.unsplash.com/featured/?mocha",
      },
    ],
    sizeList: [
      {
        name: "tall",
        price: 0,
        selected: false,
      },
      {
        name: "grande",
        price: 500,
        selected: false,
      },
      {
        name: "venti",
        price: 1000,
        selected: false,
      },
    ],
    optionList: [
      {
        type: "샷",
        price: 500,
        count: 0,
      },
      {
        type: "시럽",
        price: 500,
        count: 0,
      },
      {
        type: "휘핑 크림",
        price: 500,
        count: 0,
      },
    ],
    selectedMenu: {},
    selectedSize: {},
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length;
    },
    totalOrderPrice(state) {
      return state.orderList.reduce((sum, order) => {
        // console.log(order)
        // console.log(order.option)
        sum += order.menu.price + order.size.price;

        // 다시 한번 reduce를 사용해서 옵션 가격을 더해준다.
        sum += order.optionList.reduce((optionsum, option) => {
          if (option.count > 0) {
            optionsum += option.count * option.price;
            console.log(optionsum);
          }
          return optionsum;
        }, 0);
        return sum;
      }, 0);
    },
  },
  mutations: {
    addOrder(state) {
      // console.log(13, state.optionList)
      state.orderList.push({
        menu: state.selectedMenu,
        size: state.selectedSize,

        // 옵션은 그대로 불러와 버리면 주문 할 때 마다 값이 변경되버린다.
        // 그래서 깊은 복사를 통해 옵션리스트를 하나 더 만들어준다.
        optionList: _.cloneDeep(state.optionList),
      });

      // 옵션 정보를 초기화 해서 얕은 복사를 방지하기!
      state.optionList = state.optionList.map((option) => {
        option.count = 0;
        return option;
      });
    },
    updateMenuList(state, selectedMenu) {
      state.menuList = state.menuList.map((menu) => {
        if (menu.title == selectedMenu.title) {
          menu.selected = true;
          state.selectedMenu = selectedMenu;
        } else {
          menu.selected = false;
        }
        return menu;
      });
    },
    updateSizeList(state, selectedSize) {
      state.sizeList = state.sizeList.map((size) => {
        if (size.name == selectedSize.name) {
          size.selected = true;
          state.selectedSize = selectedSize;
        } else {
          size.selected = false;
        }
        return size;
      });
    },
    // increase 와 decrease 함수를 두개 만들어주어야 한다!
    increaseOption(state, optionType) {
      state.optionList = state.optionList.map((option) => {
        if (option.type == optionType) {
          option.count += 1;
        }
        return option;
      });
    },
    decreaseOption(state, optionType) {
      state.optionList = state.optionList.map((option) => {
        if (option.type == optionType && option.count > 0) {
          option.count -= 1;
        }
        return option;
      });
    },
  },
  actions: {
    selectMenu(context, selectedMenu) {
      context.commit("updateMenuList", selectedMenu);
    },
    selectSize(context, selectedSize) {
      context.commit("updateSizeList", selectedSize);
    },
    addOrder(context) {
      context.commit("addOrder");
    },
  },
  modules: {},
});
