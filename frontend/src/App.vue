<script setup>
import { ref, onMounted } from 'vue';

const message = ref('');

onMounted(async () => {
  const response = await fetch('/api/');
  const data = await response.json();
  message.value = data.message;
});
</script>

<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>