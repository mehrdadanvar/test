<template>
  <UContainer>
    <main>
      <div class="flex flex-row rounded-3xl border border-cyan-500 p-6 my-12 font-Inter">
        <div>
          <img src="" alt="" class="rounded-l-3xl" />
        </div>
        <form class="mx-auto mt-6 flex flex-col items-center" @submit.prevent="check_empty">
          <h1 class="text-2xl">Welcome to Hero Appliconnect</h1>
          <div class="flex flex-col gap-3 mx-auto mt-6">
            <UInput
              size="md"
              color="cyan"
              placeholder="Email Address"
              icon="i-solar-letter-broken"
              v-model="login_user.email"
            />
            <UInput
              size="md"
              color="cyan"
              placeholder="******"
              icon="i-solar-lock-password-bold-duotone"
              v-model="login_user.password"
            />
            <USelectMenu
              size="md"
              color="cyan"
              placeholder="select your role"
              v-model="role"
              :options="roles"
              icon="i-solar-users-group-rounded-line-duotone"
              v-if="user_role == 'guest'"
            />
          </div>
          <div class="mt-12">
            <UButton color="sky" size="xl" @click="login"><span class="px-4">Sign In</span></UButton>
          </div>
          <div class="text-gray-500 mt-6">
            <NuxtLink to="/register"
              >Dont have an account yet?
              <span class="underline italic text-sky-500">Create One Here</span></NuxtLink
            >
          </div>
        </form>
      </div>
      <div>{{ role }}</div>
    </main>
  </UContainer>
  <UNotifications />
</template>

<script setup>
let userstate = useUser();
console.log("user state is", userstate.value);
let user_role = userstate.value.role;
console.log(`role is ${user_role}`);

let role = ref("");
let roles = [
  { id: 0, name: "student", label: "Student" },
  { id: 1, name: "coordinator", label: "Care Coordinator" },
  { id: 2, name: "college", label: "University Coordinator" },
];
watch(role, (new_role) => {
  console.log("role changed to", role.value.name);
  userstate.value.role = role.value.name;
});
let login_user = ref({ email: "", password: "" });

async function check_empty() {
  let user = login_user.value;
  if ((user.email === "") | (user.password === "")) {
    console.log("either email or password is blank");
  }
}

async function login() {
  try {
    let user = login_user.value;
    console.log({ email: user.email, password: user.password });
    console.log(user);
    let response = await fetch(`http://localhost:8000/${userstate.value.role}s/login`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({ email: user.email, password: user.password }),
      headers: { "Content-Type": "application/json" },
    });
    let data = await response.json();
    console.log("fetch request resulted in", data);
    if (response.status === 200) {
      let retrived_user = data.user;
      userstate.value.role = retrived_user.role;
      userstate.value.firstname = retrived_user.firstname;
      userstate.value.lastname = retrived_user.lastname;
      userstate.value.identity = retrived_user.identity;
      userstate.value.email = retrived_user.email;
      userstate.value.has_account = true;
      userstate.value.logged_in = true;
      userstate.value.has_token = true;
      return navigateTo(`/students/${userstate.value.identity}`);
    } else {
      console.log("status not success");
    }
  } catch (error) {
    error ? console.log(error) : "";
  }
}
</script>

<style scoped></style>
