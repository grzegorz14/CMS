<script>
    import { push } from "svelte-spa-router";

    function goHome() {
        push("#/");
    }

    let errorInfo = "Login and password are required."

    async function signUp() {
        let login = document.getElementById("loginInput").value
        let password = document.getElementById("passwordInput").value
        if (isEmptyOrWhiteSpace(login) || isEmptyOrWhiteSpace(password)){
            document.getElementById("errorInfo").classList.remove("d-none")
            document.getElementById("passwordBox").classList.remove("mb-4")
        }
        else {
            let response = await fetch("./signUp", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    "login": login,
                    "password": password,
                }),
            })
            response = await response.text()
            if (response == "accountCreated") {
                push("#/accountCreated")
            }
            else {
                errorInfo = response
            }
        }
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
</script>

<button on:click={goHome} class="goBack btn btn-outline-light position-absolute">HOME</button>

<div class="gradient d-flex justify-content-center">
    <div class="container w-50">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                <div class="card bg-dark text-white" style="border-radius: 1rem;">
                    <div class="card-body p-5 text-center">

                    <h2 class="fw-bold mb-2 text-uppercase mb-5">Sign up</h2>

                    <div class="form-outline form-white mb-4">
                        <input type="text" id="loginInput" class="form-control form-control-lg" />
                        <label class="form-label mt-1" for="loginInput">Login</label>
                    </div>

                    <div id="passwordBox" class="form-outline form-white mb-4">
                        <input type="password" id="passwordInput" class="form-control form-control-lg" />
                        <label class="form-label mt-1" for="passwordInput">Password</label>
                    </div>

                    <p id="errorInfo" class="form-label text-danger mb-4 d-none">{errorInfo}</p>
                    <button on:click={signUp} class="btn btn-outline-light btn-lg px-5 mb-4">Sign up</button>

                    <div>
                        <p class="mb-0">
                            Already have an account? 
                            <a href="/#/logIn" class="link-secondary fw-bold">Log in</a>
                        </p>
                    </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .goBack {
        top: 50px;
        left: 50px;
        width: 80px;
        height: 40px;
    }

    .gradient {
        height: 100vh;
        background: linear-gradient(90deg, rgba(98,42,42,1) 0%, rgba(111,72,111,1) 29%, rgba(93,73,101,1) 55%, rgba(8,48,68,1) 100%);
    }
</style>