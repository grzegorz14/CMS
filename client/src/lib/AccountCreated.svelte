<script>
    import { push } from "svelte-spa-router";

    function goToLogIn() {
        push("#/logIn");
    }
</script>

<div class="gradient d-flex flex-column justify-content-center">
    <div class="container w-25 p-5 card bg-dark text-white align-items-center" style="border-radius: 1rem;">
        <h1>Account created!</h1>
        <button on:click={goToLogIn} class="btn btn-outline-light btn-lg px-5 mt-4" >Log in here</button>
    </div>
    
</div>

<style>
    .gradient {
        height: 100vh;
        background: linear-gradient(90deg, rgba(98,42,42,1) 0%, rgba(111,72,111,1) 29%, rgba(93,73,101,1) 55%, rgba(8,48,68,1) 100%);
    }
</style>