<template>
  <div class="font-Inter">
    <h1 class="text-2xl text-gray-700">Welcome To Your Profile</h1>
    <hr />
    <article class="w-2/3 bg-amber-200/80 rounded-xl p-6">
      <UIcon name="i-solar-danger-triangle-bold-duotone" class="text-amber-600 text-3xl" />
      <p class="text-slate-700">Dear Sudent Please Take a monent to fill the following form thoroughly</p>
      <p>
        The information you provide should be accurate to help case coordinators to find the best schedule for
        you and find clients who math you Ubuntu re
      </p>
    </article>
    <div class="field">
      <p class="text-base text-gray-700">Gender</p>
      <URadio
        color="cyan"
        v-for="option of gender_options"
        :key="option.name"
        v-model="selected_gender"
        v-bind="option"
      />
    </div>
    <section class="text-black bg-white border border-orange-300 p-6 rounded-lg max-w-2xl my-12">
      <div class="flex flex-row gap-3">
        <UIcon name="i-solar-phone-bold-duotone" class="text-2xl text-cyan-500 max-w-sm" />
        <p class="text-base text-gray-700">Phone Number</p>
      </div>
      <UInput color="cyan" i-solar-phone-bold-duotone type="text" placeholder="236-856-8684" size="md" />
      <UIcon name="i-solar-map-point-wave-bold-duotone" class="text-2xl" />
      <p class="text-base text-gray-700">Address</p>
      <UInput placeholder="1080 Addreley St, North Vancouver" color="cyan" size="md" />
      <UIcon name="i-solar-point-on-map-perspective-bold" class="text-2xl" />
      <p class="text-base text-gray-700">PostalCode</p>
      <UInput placeholder="V7D P69" color="cyan" size="md" />
      <UIcon name="i-solar-buildings-3-bold-duotone" class="text-2xl" />
      <p class="text-base text-gray-700">Colledge or University</p>
      <USelectMenu
        v-model="selected_school"
        :options="school_options"
        color="cyan"
        size="md"
        class="text-gray-500"
      />
      <UIcon name="i-solar-book-2-bold-duotone" class="text-2xl" />
      <p class="text-base text-gray-700">Current Programm</p>
      <USelectMenu
        v-model="selected_degree"
        :options="degree_options"
        color="cyan"
        size="md"
        class="text-gray-500"
      />
    </section>
    <hr />
    <section class="time-table mt-12">
      <div class="flex flex-row items-center gap-6 my-6 text-cyan-900">
        <UIcon name="i-solar-calendar-bold-duotone" class="text-4xl" />
        <h2>Time Table Ubuntu</h2>
      </div>
      <article
        class="w-2/3 bg-amber-200 rounded-xl p-6 my-6 transition-all duration-75 hover:scale-105 hover:bg-amber-300 hover:shadow-lg"
      >
        <UIcon name="i-solar-danger-triangle-bold-duotone" class="text-amber-500 text-3xl" />

        <p class="text-gray-500">
          The following table helps you determine your availability throughout the next 3 months. For each day
          of the week you will have to first activate the day by clicing the associated checkbox. By default
          you are assumed to have no days open to work. Notice that only after activating a day, can you set
          the desired time slots for work. Remeber to open the night-slot if you are willing to take night
          shifts.
        </p>
      </article>
      <div class="border border-cyan-300 font-Inter rounded-xl overflow-hidden max-w-7xl">
        <div class="grid grid-cols-6 text-gray-300 font-bold bg-cyan-600 py-4">
          <p class="px-3">
            <UTooltip text="check to open up a day to work">Open</UTooltip>
          </p>
          <p>Days</p>
          <p v-for="slot in slots" :key="slot.id" class="mx-auto">
            {{ slot.title }}
          </p>
        </div>
        <div
          v-for="day in days"
          :key="day.id"
          class="grid grid-cols-6 border-b-2 border-cyan-300/50 gap-3 items-center bg-white"
        >
          <p class="px-6 pt-2">
            <UCheckbox v-model="checkboxes[day.id - 1].status" color="amber" />
          </p>
          <p>{{ day.title }}</p>
          <p v-for="slot in slots" :key="`${slot.id}${day.id}`">
            <USelect
              :options="time_options"
              size="md"
              :disabled="!checkboxes[day.id - 1].status"
              v-model="schedule[day.id - 1].slots[slot.id - 1].status"
              color="cyan"
            />
          </p>
        </div>
      </div>
    </section>
    <section>
      <div></div>
    </section>
  </div>
</template>

<script setup>
let selected_gender = ref("female");
let gender_options = [
  { name: "male", value: "male", label: "Male" },
  { name: "female", value: "female", label: "Female" },
];

let school_options = [
  "Fairleigh Dickinsin University",
  "Simon Fraiser University",
  "Vancouver Career Colledge",
];
let selected_school = ref(school_options[0]);

let degree_options = ["MS", "MA", "BA", "MD"];
let selected_degree = ref(degree_options[1]);

let days = [
  { id: 1, title: "Monday" },
  { id: 2, title: "Tuseday" },
  { id: 3, title: "Wednesday" },
  { id: 4, title: "Thursday" },
  { id: 5, title: "Friday" },
  { id: 6, title: "Saturday" },
  { id: 7, title: "Sunday" },
];
let schedule = ref([
  {
    id: 1,
    day: "Monday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
  {
    id: 2,
    day: "Tuseday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
  {
    id: 3,
    day: "Wednesday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
  {
    id: 4,
    day: "Thursday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
  {
    id: 5,
    day: "Friday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
  {
    id: 6,
    day: "Saturday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
  {
    id: 7,
    day: "Saturday",
    slots: [
      { id: 1, status: "busy" },
      { id: 2, status: "busy" },
      { id: 3, status: "busy" },
      { id: 4, status: "busy" },
    ],
  },
]);
let slots = [
  { id: 1, title: "8-12 AM" },
  { id: 2, title: "12-4 PM" },
  { id: 3, title: "4-8 PM" },
  { id: 4, title: "8 PM- 8 AM" },
];

let time_options = [
  { name: "school", value: "school", label: "School" },
  { name: "free", value: "free", label: "Open to Work" },
  { name: "busy", value: "busy", label: "Leave me Alone" },
];

let chech_box_status = ref(true);

let checkboxes = ref([
  { id: 0, status: false },
  { id: 1, status: false },
  { id: 2, status: false },
  { id: 3, status: false },
  { id: 4, status: false },
  { id: 5, status: false },
  { id: 6, status: false },
]);

async function save_data() {
  let response = await $fetch("http://locahost:8000/studentusers");
}
</script>

<style></style>
