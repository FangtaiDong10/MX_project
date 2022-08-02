import axios from "axios";
import { useAuthStore } from "../stores/auth";
import router from "../router";
axios.defaults.timeout = 5000;

axios.defaults.baseURL = import.meta.env.VITE_API_BASE;
axios.interceptors.request.use((config) => {
  const authStore = useAuthStore();
  const token = authStore.getToken;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

axios.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response) {
      const message = window["$message"];
      switch (error.response.status) {
        case 401:
          if (router.currentRoute.name !== "login") {
            const authStore = useAuthStore();
            authStore.logout();
            router.replace({
              path: "/login",
              query: { redirect: router.currentRoute.fullPath },
            });
          }
          break;
        default:
          message.error(error.response?.data?.message || "Unkown error");
      }
    }
  }
);

export default axios;
