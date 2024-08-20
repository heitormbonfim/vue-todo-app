<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
  <main class="w-full h-screen flex flex-col justify-center items-center gap-5">
    <h2 class="text-2xl text-center font-bold">
      404 - Page Not Found
    </h2>
    <RouterLink to="/" class="text-center underline text-lg hover:opacity-50 duration-300">
      Go back
    </RouterLink>
  </main>
</template>