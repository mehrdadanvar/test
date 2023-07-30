<template>
  <div class="container flex flex-row mx-auto rounded-3xl">
    <div class="w-7/12">
      <IndexPlay />
    </div>
    <img src="touch.jpg" alt="" class="sm:absolute sm:rounded-full md:relative" />
  </div>
</template>

<script setup></script>

<style>
img {
  opacity: 50%;
  box-shadow: -1px -10px 20px 100px whitesmoke inset;
  border: 10px 10px solid;
  border-color: rgba(250, 255, 255, 0.5);
  z-index: 1;
}
</style>
