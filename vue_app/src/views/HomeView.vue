<script setup lang="ts">
import AddTaskButton from '@/components/buttons/AddTaskButton.vue'
import Button from '@/components/buttons/Button.vue'
import Modal from '@/components/Modal.vue'
import NavBar from '@/components/NavBar.vue'
import TodoItem from '@/components/TodoItem.vue'
import { ref } from 'vue'
import { toast } from 'vue3-toastify'

const tasks = [
  {
    id: '1',
    title: 'Todo 1',
    description: 'Description of the task',
    done: false
  },
  {
    id: '2',
    title: 'Todo 2',
    description: 'Description of the task',
    done: true
  },
  {
    id: '3',
    title: 'Todo 3',
    description: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus alias officiis dolor facilis omnis voluptatum nihil itaque quidem consectetur quos aut odio veritatis, iste fugiat delectus deleniti laborum quasi eius.
  Expedita accusamus saepe ipsa nam exercitationem quidem pariatur aspernatur, quasi natus harum repellendus molestias quisquam cupiditate. Consequuntur, tempore aliquam ipsum harum atque ab? Mollitia doloribus perspiciatis quaerat et doloremque voluptatum.
  Aspernatur, placeat iste pariatur dolorum sed voluptate quasi earum dolores iure odio illum nam neque amet laboriosam aperiam molestias ad minima minus maxime. Dolore quidem dolorem atque culpa, architecto inventore?
  Debitis, facilis quo voluptas magnam excepturi nesciunt soluta perspiciatis, quod omnis corporis, facere doloremque. Eius consequuntur laudantium unde a. Numquam incidunt cupiditate a in fugit sed minus culpa, optio similique.`,
    done: false
  }
]

const showAddTaskModal = ref(false)

function openAddTaskModal() {
  showAddTaskModal.value = true
}

function closeAddTaskModal() {
  showAddTaskModal.value = false
}

const taskTitle = ref('')
const taskDescription = ref('')

function handleAddTask() {
  toast.success(taskTitle.value)
}
</script>

<template>
  <NavBar />
  <main>
    <h1 class="text-3xl font-bold text-center py-5">Tasks</h1>

    <div class="container mx-auto">
      <ul class="flex flex-col justify-center items-center gap-2">
        <li v-for="item in tasks" class="w-full">
          <TodoItem :title="item.title" :description="item.description" :done="item.done" />
        </li>
      </ul>
    </div>

    <Transition name="fade">
      <Modal :showModal="showAddTaskModal" @close="closeAddTaskModal">
        <form @submit.prevent="handleAddTask">
          <h3 class="text-lg text-center font-bold mb-5">Add Task</h3>

          <fieldset class="border p-2">
            <legend class="font-bold">
              <label for="title">Task Title</label>
            </legend>
            <input
              type="text"
              id="title"
              class="w-full focus:outline-2 border-2"
              placeholder="ex: walk the dog"
              v-model="taskTitle"
            />
          </fieldset>

          <div class="flex justify-end mt-5">
            <Button type="submit">Confirm</Button>
          </div>
        </form>
      </Modal>
    </Transition>

    <AddTaskButton @click="openAddTaskModal" />
  </main>
</template>
