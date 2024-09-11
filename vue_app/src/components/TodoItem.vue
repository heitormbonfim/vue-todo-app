<script setup lang="tsx">
import { defineProps } from 'vue'

defineProps({
  title: {
    type: String,
    required: true
  },

  description: {
    type: String
  },

  done: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <div
    :class="`w-full p-2 border rounded-lg flex justify-between items-start duration-300 ${done && 'border-l-4 border-l-black'}`"
  >
    <div class="w-full">
      <h2 class="font-bold text-lg">{{ title }}</h2>
      <div class="p-2">{{ description }}</div>
    </div>
    <div class="border rounded-lg bg-black text-white">
      <button class="text-2xl font-bold px-2">&times;</button>
    </div>
  </div>
</template>
