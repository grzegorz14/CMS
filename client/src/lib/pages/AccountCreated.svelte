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
