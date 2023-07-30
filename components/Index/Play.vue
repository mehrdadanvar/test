<template>
  <div class="rounded-lg h-auto p-4 mx-auto">
    <div class="terminal p-2 mb-6">
      <div class="flex flex-col gap-12">
        <p class="text-4xl text-white test">{{ rendered_text[0] }}</p>
        <p class="text-3xl text-gray-400">{{ rendered_text[1] }}</p>
        <p class="text-2xl text-slate-300 shodow-2xl shadow-black">
          {{ rendered_text[2] }}
        </p>
      </div>
    </div>
    <!-- <div class="flex flex-row gap-3 mt-24">
      <button class="bg-teal-400 text-lg text-white rounded-full w-2/5 h-12">
        How ?
      </button>
      <button
        class="bg-white border border-slate-200 text-lg text-slate-700 rounded-full w-2/5"
      >
        <NuxtLink to="register">Register</NuxtLink>
      </button>
    </div> -->
    <!-- <p>{{ rendered_text }}</p> -->
  </div>
</template>
<script setup>
let major_text = [
  "Unite Serve Thrive",
  "Connecting Healthcare Students with Businesses",
  "For a Better Tomorrow",
];
let minor_text = ref("");

let rendered_text = ref(["", "", ""]);

const timer = (ms) => new Promise((res) => setTimeout(res, ms));

async function minor_render(input, time, index) {
  for (let i = 0; i < input.length; i++) {
    rendered_text.value[index] += input[i];
    await timer(time);
  }
}

async function order(main_array) {
  for (let i = 0; i < main_array.length; i++) {
    await minor_render(main_array[i], 20, i);
  }
}

async function delay() {
  await timer(100);
  order(major_text);
}

delay();
async function show_bottons() {
  setTimeout(() => {
    console.log("time out working");
  }, 2000);
}
show_bottons();
</script>

<style scoped>
.test {
  color: #f7e1ff;
  text-shadow: 0 0 5px #fff;
}
</style>
