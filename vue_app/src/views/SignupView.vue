<script setup lang="ts">
import Button from '@/components/buttons/Button.vue'
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { toast } from 'vue3-toastify'

const email = ref<string>('')
const name = ref<string>('')
const password = ref<string>('')
const showPass = ref<boolean>(false)

function handleTogglePasswordVisibility() {
  showPass.value = !showPass.value
}

async function handleSignUp() {
  toast.success(`${email.value} ${name.value} ${password.value}`)
}
</script>

<template>
  <main class="w-full min-h-screen flex justify-center items-center bg-zinc-300 p-3">
    <form
      @submit.prevent="handleSignUp"
      class="w-full max-w-md flex flex-col justify-center items-center gap-6 shadow-md p-5 rounded-lg bg-white"
    >
      <h2 class="text-2xl font-bold">Sign Up</h2>

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
        v-model="name"
        id="name"
        type="text"
        name="name"
        placeholder="Name"
        class="w-full border border-zinc-300 text-lg p-3 rounded-lg"
      />

      <input
        required
        v-model="password"
        id="password"
        :type="showPass ? 'text' : 'password'"
        name="password"
        placeholder="Password"
        class="w-full border border-zinc-300 text-lg p-3 rounded-lg"
      />

      <label for="pass-visibility" class="w-full flex justify-end items-center gap-2">
        <input
          id="pass-visibility"
          type="checkbox"
          @change="handleTogglePasswordVisibility"
          class="appearance-none w-5 h-5 border rounded-lg border-zinc-300 cursor-pointer checked:bg-black"
        />
        <span>show password</span>
      </label>

      <Button class="w-full" type="submit">Submit</Button>

      <div>
        already have an account?
        <RouterLink to="/login" class="underline font-bold">login</RouterLink>
      </div>
    </form>
  </main>
</template>
