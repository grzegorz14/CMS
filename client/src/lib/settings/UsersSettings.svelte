<script>
    import SettingsController from "./../SettingsController"  
    
    let settings = new SettingsController()
    let colorTheme = settings.getJson().colorTheme
    let users = getUsers()

    function editUser(login) {
        window.location.href =  "#/subPage/settings/editUser/" +  login; 
    }

    async function getUsers() {
        let response = await fetch("./getUsers", { method: "POST" })
        response = await response.text()
        users = JSON.parse(response)
    }
</script>

<div class="d-flex flex-column justify-content-center {colorTheme == "Light" ? 'bg-white t-black':  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
    <p class="mainHeadline">User settings</p>

    <hr>

    <p class="headline">Users</p>
    <div class="table-responsive w-50 ms-3">
        <table class="table">
            <thead>
                <tr>
                    <th>Counter</th>
                    <th>Login</th>
                    <th>Password</th>
                    <th>User type</th>
                    <th>Edit</th>
                </tr>
            </thead>
            <tbody>
                {#each users as user, i}
                    <tr>
                        <th>{i + 1}</th>
                        <th>{user[0]}</th>
                        <th>{user[1]}</th>
                        <th>{user[2]}</th>
                        <th><button on:click={() => editUser(user[0])} class="btn btn-primary btn-sm">Edit</button></th>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>
