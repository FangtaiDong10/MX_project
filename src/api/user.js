import axios from "../utils/http";

export const getUser = async (username) => {
  const response = await axios.get("/users/" + username);
  return response.data;
};

export const createStudent = async (user) => {
  const response = await axios.post("/students", user);
  return response.data;
};
