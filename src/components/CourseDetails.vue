<script setup>
import { defineProps, ref } from "vue";
import {
  NCard,
  NSpace,
  NButton,
  NImage,
  NH3,
  NP,
  NTag,
  NIcon,
  NModal,
  useMessage,
} from "naive-ui";
import { People } from "@vicons/ionicons5";
import { createOrder } from "../api/order";
const props = defineProps(["course", "isPurchased"]);
const showPurchase = ref(false);
const message = useMessage();
const purchase = async () => {
  const response = await createOrder(props.course.id);
  showPurchase.value = false;
  message.success(`订购成功, 订单号: ${response.id}`);
};
</script>
<template>
  <n-card>
    <div class="course-card-body">
      <n-image :src="props.course.cover_image"></n-image>

      <n-space vertical class="course-info">
        <n-h3>{{ props.course.name }}</n-h3>
        <n-space>
          <n-p>
            价格: <span> ${{ props.course.original_price }}</span>
          </n-p>
          <n-p>
            老师: <span> {{ props.course.teacher.display_name }}</span>
          </n-p>
          <n-p>
            校区: <span> {{ props.course.campus.name }}</span>
          </n-p>
        </n-space>
        <n-tag type="success" round :bordered="false" class="count-tag">
          Enrolled: {{ props.course.students_count }}
          <template #icon>
            <n-icon :component="People"></n-icon>
          </template>
        </n-tag>
        <n-p class="desc"> {{ props.course.description }}</n-p>
        <n-button
          class="purchase-button"
          type="primary"
          @click="showPurchase = true"
          v-if="isPurchased === false"
        >
          购买课程
        </n-button>
      </n-space>
    </div>
  </n-card>
  <n-modal
    v-model:show="showPurchase"
    preset="dialog"
    title="购买课程"
    content="您是否要购买该课程"
    positive-text="下单"
    negative-text="取消"
    @positive-click="purchase"
  />
</template>

<style lang="less" scoped>
.course-card-body {
  display: flex;
}
.course-info {
  padding: 16px;
  padding-left: 32px;
  width: 100%;
  height: 100%;
  span {
    font-size: 16px;
    font-weight: 700;
    margin-left: 12px;
    margin-right: 16px;
  }
  .desc {
    margin-top: 16px;
  }
  .purchase-button {
    position: absolute;
    bottom: 28px;
    right: 28px;
  }
  .count-tag {
    margin-top: 1rem;
  }
}
</style>
