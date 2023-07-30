let userstate = useUser();
export default defineNuxtRouteMiddleware(() => {
  console.log(userstate.value);
  if (userstate.value.logged_in == false) {
    return navigateTo("/login");
  }
});
