<script>
    let login = localStorage.getItem("login")

    async function updateLogin() {
        let newLogin = document.getElementById("newLogin").value
        if (isEmptyOrWhiteSpace(newLogin)) {
            alert("Your new login is empty!")
            return
        }
        let response = await fetch("./updateLogin", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                "login": login,
                "newLogin": newLogin
            }),
        })
        response = await response.text()
        console.log(response)
        if (response = "updated") {
            localStorage.setItem("login", newLogin)
        }
        window.location.reload()
    }

    async function updatePassword() {
        let newPassword = document.getElementById("newPassword").value
        if (isEmptyOrWhiteSpace(newPassword)) {
            alert("Your new password is empty!")
            return
        }
        //update
    }

    async function deleteAccount() {
        if (confirm("Delete your account?")) {
            //deletes account with unique login "Grzesiek"
        }        
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">My Account</p>

    <hr>

    <p class="headline">Profile data</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col text">Login</div>
            <div class="col">
                <input id="newLogin" type="text" placeholder={login} class="form-control form-control-lg"/>
            </div>
            <div class="col">
                <button on:click={updateLogin} class="btn btn-primary">Save</button>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col text">New password</div>
            <div class="col">
                <input id="newPassword" type="password" class="form-control form-control-lg"/>
            </div>
            <div class="col">
                <button on:click={updatePassword} class="btn btn-primary">Save</button>
            </div>
        </div>

        <hr>

        <p class="headline">Delete account</p>
        <button on:click={deleteAccount} class="btn btn-danger m-2 ms-3">Delete account</button>
    </div>
</div>
