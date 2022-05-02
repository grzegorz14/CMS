<script>
  import Router from "svelte-spa-router";

	import LogIn from './lib/LogIn.svelte';
	import SignUp from './lib/SignUp.svelte';
	import Index from './lib/Index.svelte';
  import NotFound from './lib/NotFound.svelte';
  import AccountCreated from "./lib/AccountCreated.svelte";
  import Settings from "./lib/Settings.svelte";

  const routes = {
    "/": Index,
    "/subPage/:page": Index,
    "/settings": Settings,
    "/signUp": SignUp,
    "/logIn": LogIn,
    "/accountCreated": AccountCreated,

    "*": NotFound
  };
</script>

<main>
  <Router {routes} />
</main>

