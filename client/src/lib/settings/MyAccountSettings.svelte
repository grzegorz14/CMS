<script>
    let login = "Grzesiek" //saved in local storage

    function saveLogin() {
        let newLogin = document.getElementById("newLoginInput").value
        //update login
    }

    function savePassword() {
        let newPassword = document.getElementById("newPasswordInput").value
        //update password
    }

    function deleteAccount() {
        let confirm = confirm("Delete your account?")
        if (confirm) {
            //deletes account with unique login "Grzesiek"
        }
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">My Account</p>

    <hr>

    <p class="headline">Profile data</p>
    <div style="width: 40%;">
        <div class="row align-items-center m-2">
            <div class="col text">Login: </div>
            <div class="col">
                <input id="newLoginInput" type="text" placeholder={login} class="form-control form-control-lg"/>
            </div>
            <div class="col">
                <button on:click={saveLogin} class="btn btn-primary">Save</button>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col text">New password: </div>
            <div class="col">
                <input id="newPasswordInput" type="password" class="form-control form-control-lg"/>
            </div>
            <div class="col">
                <button on:click={savePassword} class="btn btn-primary">Save</button>
            </div>
        </div>

        <hr>

        <p class="headline">Delete account</p>
        <button on:click={deleteAccount} class="btn btn-danger m-2 ms-3">Delete account</button>
    </div>


</div>
