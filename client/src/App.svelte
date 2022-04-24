<script>
  import Index from "./lib/Index.svelte";
  import SignUp from "./lib/SignUp.svelte";
  import LogIn from "./lib/LogIn.svelte";

  import Router from "svelte-spa-router";

  const routes = {
      '/': Index,
      '/signUp': SignUp,
      '/logIn': LogIn
  }

</script>

<Router routes={routes} />