<script setup>
import { NLayoutSider, NA, NMenu, NIcon } from "naive-ui";
import { ref, h, watchEffect } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { Home, Book, Grid, Cart } from "@vicons/ionicons5";
import { useAuthStore } from "../stores/auth";
import { storeToRefs } from "pinia";

const authStore = useAuthStore();
const auth = storeToRefs(authStore);

const route = useRoute();
const currentKey = ref("home");

watchEffect(() => {
  if (route.fullPath.split("/").includes("browse")) {
    currentKey.value = "browse";
  } else {
    currentKey.value = route.fullPath.slice(1);
  }
});

const createMenu = (coursesMenu) => {
  return [
    {
      label: "Home",
      key: "home",
      path: "/",
      icon: Home,
    },
    {
      label: "Orders",
      key: "orders",
      icon: Cart,
      path: "/orders",
    },
    {
      label: "All Courses",
      key: "browse",
      icon: Grid,
      path: "/browse",
    },
    {
      label: "My Courses",
      key: "courses",
      path: "/courses",
      icon: Book,
      children: coursesMenu,
    },
  ];
};

const menus = ref(createMenu([]));

watchEffect(() => {
  if (auth.userInfo?.value?.enrolled_courses) {
    menus.value = createMenu(
      auth.userInfo.value.enrolled_courses.map((item) => ({
        label: item.name,
        key: "courses/" + item.id,
        path: "/courses/" + item.id,
      }))
    );
  }
});

const renderMenu = (menus) =>
  menus.map((item) => ({
    label: () =>
      item.children
        ? item.label
        : h(
            RouterLink,
            { to: { path: item.path } },
            { default: () => item.label }
          ),
    key: item.key,
    icon:
      item.icon != null
        ? () => h(NIcon, null, { default: () => h(item.icon) })
        : undefined,
    children: item.children ? renderMenu(item.children) : undefined,
  }));
const menuOptions = renderMenu(menus.value);
const collapsed = ref(false);
</script>
<template>
  <n-layout-sider
    bordered
    :width="240"
    show-trigger
    collapse-mode="width"
    v-model:collapsed="collapsed"
    :native-scrollbar="false"
  >
    <router-link to="/" custom #="{ navigate, href }">
      <n-a class="logo" :href="href" @click="navigate">
        <img src="~@/assets/logo.jpg" />
        <span> ShangxueOnline </span>
      </n-a>
    </router-link>
    <n-menu
      :value="currentKey"
      :options="menuOptions"
      :collapsed="collapsed"
      @update:value="
        (k) => {
          currentKey = k;
        }
      "
    />
  </n-layout-sider>
</template>

<style lang="less" scoped>
.logo {
  position: sticky;
  top: 0;
  display: flex;
  padding: 20px;
  justify-content: center;
  align-items: center;
  font-size: 1.2em;
  font-weight: 300;
  text-decoration: none;
  transition: padding 0.3s, font-size 0.3s;

  img {
    height: 32px;
    margin-right: 8px;
    transition: margin 0.3s;
  }
}

.n-layout-sider--collapsed .logo {
  font-size: 0;
  padding: 12px;
  img {
    margin-right: 0px;
  }
}
</style>
