<script setup>
import {
  NCard,
  NSpace,
  NInput,
  NButton,
  NGrid,
  NGridItem,
  NDivider,
  NList,
} from "naive-ui";
import { ref, reactive, computed, onMounted } from "vue";

const todo = ref("");
const todoList = ref([]);

function addTodo() {
  todoList.value.push({
    title: todo.value,
    complete: false,
  });

  todo.value = "";
}

const completeTotal = computed(() => {
  return todoList.value.filter((todo) => todo.complete).length;
});

const completeTodo = (index) => {
  todoList.value[index].complete = true;
};

function restart() {
  todo.value = "";
  todoList.value = [];
}
</script>

<template>
  <div class="greetings">
    <n-divider dashed> Todo List </n-divider>
    <n-space horizontal>
      <n-input v-model:value="todo" type="text" placeholder="Input what todo" />
      <!-- <n-input v-model:value="lastName" placeholder="Last Name" /> -->
      <n-button @click="addTodo" type="primary"> Add </n-button>

      <div>total tasks: {{ todoList.length }}</div>
      <div>completed: {{ completeTotal }}</div>

      <n-button @click="restart()">reset</n-button>
    </n-space>

    <n-divider dashed> Todo Info </n-divider>
    <n-space vertical>
      <n-grid :x-gap="12" :y-gap="8" :cols="4">
        <n-grid-item v-for="(todo, index) in todoList" :key="index">
          <n-card>
            <div>{{ todo.title }}</div>
            <div>{{ todo.complete ? "Done":"Not Done" }}</div>
            <n-button @click="completeTodo(index)">complete</n-button>
          </n-card>
        </n-grid-item>
      </n-grid>
    </n-space>
  </div>
</template>

<style scoped></style>
