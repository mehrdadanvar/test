<template>
  <aside
    class="ml-1 py-52 bg-gradient-to-r from-cyan-950 from-10% via-cyan-800 via-85% to-cyan-800 text-white rounded-2xl overflow-hidden transition-all duration-150 border-white"
    :class="{ 'w-16': !isopen, 'w-2/12': isopen }"
  >
    <div>
      <div @click="toggle_button" class="text-white">
        <UButton icon="i-solar-map-arrow-right-bold-duotone" color="purple" size="sm"></UButton>
      </div>
      <div class="flex flex-row items-center">
        <UIcon name="i-solar-user-circle-bold-duotone" class="text-2xl sticky top-6" />
        <div class="flex flex-col"></div>
      </div>
      <hr />
    </div>
    <div class="ml-6 space-y-8 sticky top-9">
      <div v-for="item in menuItems" :key="item.id" class="">
        <NuxtLink
          :to="item.path"
          class="w-full flex flex-row gap-4 rounded-lg p-2 transition-all duration-150 ease-linear hover:backdrop-brightness-150"
        >
          <UIcon :name="item.iconName" class="text-2xl rotate-90" />
          <p class="text-lg">{{ item.title }}</p>
        </NuxtLink>
      </div>
    </div>
  </aside>
</template>

<script setup>
let isopen = ref(false);
function toggle_button() {
  isopen.value = !isopen.value;
}
let menuItems = [
  {
    id: "0",
    title: "Dashboard",
    iconName: "i-solar-qr-code-bold-duotone",
    path: "/",
  },
  {
    id: "1",
    title: "Cases",
    iconName: "i-solar-dna-bold-duotone",
    path: "",
  },
  {
    id: "2",
    title: "Create Code",
    iconName: "i-solar-sidebar-code-bold-duotone",
    path: "",
  },
  {
    id: "3",
    title: "Settings",
    iconName: "i-solar-settings-bold-duotone",
    path: "",
  },
  {
    id: "4",
    title: "Log Out",
    iconName: "i-solar-upload-bold-duotone",
    path: "",
  },
];
</script>

<style scoped></style>
