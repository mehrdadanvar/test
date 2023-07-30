<template>
  <div class="register pt-36 pb-36">
    <div class="container mx-auto backdrop-blur-md py-6">
      <RegisterMain />
    </div>
    <div class="text-rose-500 w-96">some conct</div>
  </div>
</template>

<script setup>
let userstate = useUser();
console.log(userstate.value);
// let data = ref("");
// async function changeState() {
//   user_state.value = { name: "changed name", status: false };
// }
// changeState();
// console.log(user_state.value);
</script>

<style scoped>
.register {
  background-image: url("back6.svg");
  background-color: rgba(255, 255, 255, 0.5);
  background-repeat: no-repeat;
  background-size: cover;
  background-blend-mode: darken;
}
</style>
