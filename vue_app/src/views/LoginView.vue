<script setup lang="ts">
import Button from '@/components/buttons/Button.vue'
import { ref } from 'vue'

const email = ref<string>('')
const password = ref<string>('')

async function handleLogin() {
  alert('signing up' + email.value + password.value)
}
</script>

<template>
  <main class="w-full min-h-screen flex justify-center items-center bg-zinc-300 p-">
    <form
      @submit.prevent="handleLogin"
      class="w-full max-w-md flex flex-col justify-center items-center gap-6 shadow-md p-5 rounded-lg bg-white"
    >
      <h2 class="text-2xl font-bold">Login</h2>

      <input
        required
        v-model="email"
        id="email"
        type="email"
        name="email"
        placeholder="Email"
        class="w-full border border-zinc-300 text-lg p-3 rounded-lg"
      />

      <input
        required
        v-model="password"
        id="name"
        type="password"
        name="name"
        placeholder="Name"
        class="w-full border border-zinc-300 text-lg p-3 rounded-lg"
      />

      <Button class="w-full" type="submit">Confirm</Button>

      <div>
        don't have an account?
        <RouterLink to="/register" class="underline font-bold">sign up</RouterLink>
      </div>
    </form>
  </main>
</template>
