<template>
  <StudentContent>
    <div>Welcome Student</div>
    <div class="text-red-500"></div>
    <StudentProfileInfo />
    <div class="border border-blue-600 h-screen">
      testing protected route
      <button @click="call_protected" class="bg-slate-500">press me</button>
      <div class="logout w-2/4 border border-slate-500">
        <p>you can log out by pressing this button</p>
        <button class="bg-red-500 rounded-xl w-24 text-white" @click="logout">log out</button>
      </div>
      <div class="logout w-2/4 border border-slate-500">
        <p>check headers</p>
        <button class="bg-cyan-500 rounded-xl w-24 text-white" @click="check_headers">check</button>
      </div>
    </div>
  </StudentContent>
</template>

<script setup>
definePageMeta({
  layout: "dash",
  middleware: "auth",
});
// let userstate = useUser();
// console.log(userstate.value);
// let route = useRoute();
// console.log(route);
// console.log(route.params);
// let { id } = route.params;
const token = document.cookie;
console.log(token);

async function call_protected() {
  let response = await fetch("http://localhost:8000/students/details", {
    method: "GET",
    headers: { Authorization: "Bearer" },
    credentials: "include",
  });
  let data = await response.json();
  console.log(data);
}
async function logout() {
  let response = await fetch("http://localhost:8000/students/logout", {
    method: "GET",
    credentials: "include",
    headers: { Authorization: "Bearer" },
  });
  console.log(response);
  let data = await response.json();
  console.log(data);
}
async function check_headers() {
  let response = await fetch("http://localhost:8000/students/test", {
    method: "GET",
    credentials: "include",
    headers: { Authorization: "Bearer" },
  });
  console.log(response);
  let data = await response.json();
  console.log(data);
}
</script>

<style></style>
