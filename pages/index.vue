<template>
  <div class="bg-gray-800 h-screen relative">
    <div class="pt-12">
      <IndexHero />
    </div>
    <div class="text-white w-36 border border-red-600">{{ userstate }}</div>
  </div>
</template>

<script setup>
let userstate = useUser();
console.log(userstate.value);
</script>

<style></style>
