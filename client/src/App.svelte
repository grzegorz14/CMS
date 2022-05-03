<script>
  

  import Router from "svelte-spa-router";

	import LogIn from './lib/pages/LogIn.svelte';
	import SignUp from './lib/pages/SignUp.svelte';
	import Index from './lib/Index.svelte';
  import NotFound from './lib/pages/NotFound.svelte';
  import AccountCreated from "./lib/pages/AccountCreated.svelte";

  const routes = {
    "/subPage/:page/:page": Index,
    "/subPage/:page": Index,
    "/signUp": SignUp,
    "/logIn": LogIn,
    "/accountCreated": AccountCreated,
    "/": Index,

    "*": NotFound
  };
</script>

<main>
  <Router {routes} />
</main>

