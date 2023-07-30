<template>
  <div class="rounded-3xl">
    <form @submite.prevent class="flex flex-col gap-y-16 rounded-xl">
      <h1 class="text-2xl text-gray-700 p-4 mt-4 mx-auto">Welcome to Hero Appliconnect</h1>
      <hr />
      <div class="flex flex-col mx-auto gap-y-10 px-4">
        <div class="flex flex-col gap-3 sm:flex-row">
          <UInput
            size="xl"
            color="violet"
            placeholder="First Name"
            icon="i-solar-user-circle-bold-duotone"
            v-model="firstname"
            :required="true"
            trailing
            class="text-slate-600"
          />
          <UInput
            size="xl"
            color="violet"
            placeholder="Last Name"
            v-model="lastname"
            icon="i-solar-user-circle-bold-duotone"
            trailing
            class="text-slate-600"
          />
        </div>

        <UInput
          size="xl"
          color="violet"
          placeholder="Email Address"
          v-model="email"
          icon="i-solar-letter-broken"
          trailing
          class="text-slate-600"
        />
        <div class="flex flex-col gap-3 sm:flex-row">
          <UInput
            size="xl"
            color="violet"
            placeholder="More than 6 chracters"
            type="password"
            v-model="password"
            icon="i-solar-lock-password-bold-duotone"
            trailing
          />
          <UInput
            size="xl"
            color="violet"
            type="password"
            placeholder="Repeat Password"
            icon="i-solar-lock-password-bold-duotone"
            v-model="repeat_password"
            trailing
          />
        </div>
        <USelectMenu
          v-model="role"
          :options="roles"
          icon="i-solar-buildings-2-bold-duotone"
          size="xl"
          color="violet"
          placeholder="Select Your Role"
          trailing
          class="text-slate-500"
        />
      </div>
      <div class="flex flex-col items-center gap-6">
        <UButton size="xl" lable="Create Account" variant="solid" @click="createUser" color="violet"
          >Create Account</UButton
        >

        <NuxtLink to="/login"
          >Already a Member? <span class="text-violet-500 italic underline">Login here</span></NuxtLink
        >
      </div>
    </form>
  </div>
</template>

<script setup>
let userstate = useUser();
let firstname = ref("");
let lastname = ref("");
let email = ref("");
let password = ref("");
let repeat_password = ref("");
let role = ref("");
let roles = [
  { id: 0, name: "student", label: "Student" },
  { id: 1, name: "coordinator", label: "Care Coordinator" },
  { id: 2, name: "college", label: "University Coordinator" },
];

async function createUser() {
  console.log("user data about to be sent");
  console.log(firstname.value, lastname.value, email.value, password.value, role.value.name);
  try {
    let response = await fetch(`http://localhost:8000/${role.value.name}s/signup`, {
      method: "POST",
      body: JSON.stringify({
        firstname: firstname.value,
        lastname: lastname.value,
        email: email.value,
        password: password.value,
        role: role.value.name,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.status === 201) {
      console.log(userstate.value.role, role.value.name);
      userstate.value.role = role.value.name;
      console.log(userstate.value.role, role.value.name);
      return navigateTo("/login");
    }
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}
</script>

<style scoped></style>
