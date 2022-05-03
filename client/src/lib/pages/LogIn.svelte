<script>
    import { push } from "svelte-spa-router";

    function goHome() {
        push("#/");
    }

    let errorInfo = "Login and password are required."

    async function logIn() {
        let login = document.getElementById("loginInput").value
        let password = document.getElementById("passwordInput").value
        if (isEmptyOrWhiteSpace(login) || isEmptyOrWhiteSpace(password)){
            document.getElementById("errorInfo").classList.remove("d-none")
            document.getElementById("passwordBox").classList.remove("mb-4")
        }
        else {
            let response = await fetch("./logIn", {
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
            if (response == "admin" || response == "user") {
                //store somewhere user type info
                push("#/")
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
                    <div action="/logIn" method="post" class="card-body p-5 text-center">
                        <h2 class="fw-bold mb-2 text-uppercase mb-5">Log in</h2>

                        <div class="form-outline form-white mb-4">
                            <input type="text" id="loginInput" class="form-control form-control-lg" />
                            <label class="form-label mt-1" for="loginInput">Login</label>
                        </div>

                        <div id="passwordBox" class="form-outline form-white mb-4">
                            <input type="password" id="passwordInput" class="form-control form-control-lg" />
                            <label class="form-label mt-1" for="passwordInput">Password</label>
                        </div>

                        <p id="errorInfo" class="form-label text-danger mb-4 d-none">{errorInfo}</p>
                        <button on:click={logIn} class="btn btn-outline-light btn-lg px-5 mb-4">Log in</button>

                        <div>
                            <p class="mb-0">
                                Don't have an account? 
                                <a href="/#/signUp" class="text-white-50 fw-bold">Sign Up</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

