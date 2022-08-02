import axios from "../utils/http";
import { getUser } from "../api/user";
import { defineStore } from "pinia";
const prefix = import.meta.env.VITE_STORAGE_PREFIX;
export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    token: localStorage.getItem(prefix + "token"),
    userInfo: JSON.parse(localStorage.getItem(prefix + "user_info")),
  }),
  getters: {
    getToken: (state) => state.token,
    getUserInfo: (state) => state.userInfo,
    isLoggedIn: (state) => state.token !== null,
  },
  actions: {
    async login(username, password) {
      const response = await axios.post("/auth/login", {
        username,
        password,
      });
      const { data } = response;
      localStorage.setItem(prefix + "token", data.token);
      localStorage.setItem(prefix + "user_info", JSON.stringify(data.user));
      this.token = data.token;
      this.userInfo = data.user;
    },
    async reload() {
      this.userInfo = await getUser(this.userInfo.username);
      localStorage.setItem(prefix + "user_info", JSON.stringify(this.userInfo));
    },
    async logout() {
      localStorage.removeItem(prefix + "token");
      localStorage.removeItem(prefix + "user_info");
      this.token = null;
      this.userInfo = null;
    },
  },
});
