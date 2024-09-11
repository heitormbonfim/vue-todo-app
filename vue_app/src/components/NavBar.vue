<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="z-10 w-full h-10 p-3 shadow-md flex justify-between items-center sticky top-0">
    <RouterLink to="/" class="text-lg font-bold">Todo List</RouterLink>

    <ul class="flex justify-center items-center gap-3">
      <li>
        <RouterLink to="/" class="underline">home</RouterLink>
      </li>
      <li>
        <RouterLink to="/settings" class="underline">settings</RouterLink>
      </li>
      <li>
        <RouterLink to="/about" class="underline">about</RouterLink>
      </li>
      <li>
        <RouterLink to="/login" class="underline">logout</RouterLink>
      </li>
    </ul>
  </nav>
</template>
