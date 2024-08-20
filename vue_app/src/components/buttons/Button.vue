<script setup lang="ts">
import type { PropType } from 'vue';

const props = defineProps({
  type: {
    type: String as PropType<'button' | 'submit' | 'reset'>,
    default: 'button',
  },
});
</script>

<template>
  <button :type="props.type" class="rounded-lg p-3 text-lg font-bold hover:opacity-50 bg-gray-900 text-white">
    <slot></slot>
  </button>
</template>


<!-- <script setup lang="ts">
import { defineProps, computed } from 'vue';

const props = defineProps({
  type: {
    type: String as () => "button" | "submit" | "reset",
    default: "button",
    validator: (value: string) => {
      return ["button", "submit", "reset"].includes(value);
    }
  },
});

const buttonType = computed(() => props.type);
</script>

<template>
  <button :type="buttonType" class="rounded-lg p-3 text-lg font-bold hover:opacity-50 bg-gray-900 text-white">
    <slot></slot>
  </button>
</template> -->
