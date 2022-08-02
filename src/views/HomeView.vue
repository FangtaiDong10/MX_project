<script setup>
import { useAuthStore } from "../stores/auth";
import UserInfoCard from "../components/UserInfoCard.vue";
import { NGrid, NGridItem, NDivider } from "naive-ui";
import CoursesStatus from "../components/CoursesStatus.vue";
import CourseList from "../components/CourseList.vue";
import { ref, onMounted } from "vue";

import { getCourseList } from "../api/course";

const authStore = useAuthStore();
authStore.reload();

const enrolledCourses = ref({});

onMounted(async () => {
  if (authStore.getUserInfo?.enrolledCourses) {
    const response = await getCourseList();
    console.log(authStore.getUserInfo);
    const items = response.items.filter((course) =>
      authStore.getUserInfo.enrolled_courses
        .map((c) => c.id)
        .includes(course.id)
    );
    let new_response = {
      ...response,
      counts: items.length,
      items: items,
    };
    console.log(new_response);
    enrolledCourses.value = new_response;
  }
});
</script>

<template>
  <n-grid
    cols="1 m:2"
    :x-gap="12"
    :y-gap="8"
    responsive="screen"
    v-if="authStore.getUserInfo"
  >
    <n-grid-item>
      <user-info-card :user-info="authStore.getUserInfo"></user-info-card>
    </n-grid-item>
    <n-grid-item>
      <courses-status :user-info="authStore.getUserInfo" />
    </n-grid-item>
  </n-grid>
  <n-divider />
  <course-list :courseData="enrolledCourses"></course-list>
</template>
