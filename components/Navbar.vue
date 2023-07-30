<template>
  <div class="bg-gray-800 border-b border-violet-700">
    <nav
      class="sm:px-1 sm:py-1 md:flex md:flex-row md:gap-6 md:justify-between md:text-white md:px-12 md:py-4"
    >
      <div class="">
        <h1
          class="sm:font-normal sm:text-xl md:font-semibold lg:font-bold lg:text-3xl text-amber-600"
        >
          Hero AppliConnect
        </h1>
      </div>
      <div class="flex flex-row gap-6 text-slate-300">
        <div
          v-for="item in menuItems"
          :key="item.id"
          class="rounded-md p-2 hover:bg-violet-500/70"
        >
          <NuxtLink :to="item.path">{{ item.title }}</NuxtLink>
        </div>
      </div>
      <div class="flex flex-row gap-4">
        <NuxtLink to="/register">
          <UButton color="purple">Register</UButton>
        </NuxtLink>
        <NuxtLink to="/login">
          <UButton color="purple">Login</UButton>
        </NuxtLink>
      </div>
    </nav>
  </div>
</template>

<script setup>
let menuItems = [
  { id: 0, title: "Home", path: "/" },
  { id: 1, title: "About", path: "/about" },
  { id: 2, title: "Care Coordinators", path: "/coordinators" },
  { id: 3, title: "Colleges", path: "/colleges" },
  { id: 4, title: "Students", path: "/students" },
];
</script>

<style lang="scss" scoped></style>
