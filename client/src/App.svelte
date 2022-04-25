<script>
  import Router from "svelte-spa-router";

	import LogIn from './lib/LogIn.svelte';
	import SignUp from './lib/SignUp.svelte';
	import Index from './lib/Index.svelte';
  import NotFound from './lib/NotFound.svelte';

  const routes = {
    "/": Index,
    "/signUp": SignUp,
    "/logIn": LogIn,

    "*": NotFound
  };
</script>

<main>
  <Router {routes} />
</main>

