<script setup lang="ts">
import Button from '@/components/buttons/Button.vue';

async function signUp() {
  alert("signing up")
}

</script>

<template>
  <main class="w-full min-h-screen flex justify-center items-center bg-zinc-300">
    <form @submit.prevent="signUp" class="w-full max-w-md flex flex-col justify-center items-center gap-6 shadow-md p-5 rounded-lg bg-white">
      <input id="email" type="email" name="email" placeholder="Email">
      <input id="name" type="text" name="name" placeholder="Name">
      <Button type="submit">Submit</Button>
    </form>
  </main>
</template>