<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

defineProps({
  showModal: Boolean
})

const emit = defineEmits(['close'])

function closeModal() {
  emit('close')
}
</script>

<template>
  <div
    v-if="showModal"
    @click.stop="closeModal"
    class="z-10 fixed inset-0 bg-black bg-opacity-50 p-3 backdrop-blur-sm flex items-end lg:items-center justify-center"
  >
    <div class="bg-white px-3 pb-3 rounded w-full max-w-md" @click.stop>
      <div class="flex justify-end">
        <button @click="closeModal" class="text-black text-3xl">&times;</button>
      </div>
      <slot></slot>
    </div>
  </div>
</template>
