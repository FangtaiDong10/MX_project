<script setup>
import {
  NLayoutHeader,
  NBreadcrumb,
  NBreadcrumbItem,
  NSpace,
  NAvatar,
  NDropdown,
} from "naive-ui";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { storeToRefs } from "pinia";
import { computed } from "vue";

const router = useRouter();
const authStore = useAuthStore();
const auth = storeToRefs(authStore);
const options = [{ label: "Sign out", key: "logout" }];
const handleOptionSelect = async (key) => {
  if (key === "logout") {
    await authStore.logout();
    await router.push("/login");
  }
};
const displayName = computed(() => {
  return auth.userInfo?.value?.display_name || auth.userInfo?.value?.username;
});
</script>
<template>
  <n-layout-header bordered>
    <n-breadcrumb>
      <n-breadcrumb-item>Dashboard</n-breadcrumb-item>
      <n-breadcrumb-item>Home</n-breadcrumb-item>
    </n-breadcrumb>

    <n-space class="navs" :size="20" align="center">
      <span>Hello {{ displayName }}!</span>
      <n-dropdown
        placement="bottom-end"
        :options="options"
        @select="handleOptionSelect"
      >
        <n-avatar size="small" round>
          <img src="~@/assets/logo.jpg" alt="" />
        </n-avatar>
      </n-dropdown>
    </n-space>
  </n-layout-header>
</template>

<style scoped>
.n-layout-header {
  display: flex;
  align-items: center;
  font-size: 1.1em;
  padding: 8px 18px;
}

.navs {
  margin-left: auto;
  line-height: 1px;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>
