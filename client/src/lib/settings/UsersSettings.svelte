<script>
    import SettingsController from "./../SettingsController"  
    
    let settings = new SettingsController()
    let colorTheme = settings.getJson().colorTheme

    function editUser(login) {
        window.location.href =  "#/subPage/settings/editUser/" +  login; 
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
                    <th>Id</th>
                    <th>Login</th>
                    <th>Password</th>
                    <th>Edit</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th>0</th>
                    <th>Grzesiek</th>
                    <th>abcdgd</th>
                    <th><button on:click={() => editUser("Grzesiek")} class="btn btn-primary btn-sm">Edit</button></th>
                </tr>
                <tr>
                    <th>1</th>
                    <th>Drater</th>
                    <th>robieStonki</th>
                    <th><button on:click={() => editUser("Grzesiek")} class="btn btn-primary btn-sm">Edit</button></th>
                </tr>
            </tbody>
        </table>
    </div>
</div>
