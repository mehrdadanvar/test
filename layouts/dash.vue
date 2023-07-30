<template>
  <div class="dash flex flex-row mt-6 mb-6">
    <DashboardSidebar />
    <div class="-mt-3">
      <slot />
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
/* .dash {
  background-image: url("/dash6.png");
} */
</style>
