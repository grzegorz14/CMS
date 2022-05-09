<script>
    import SettingsController from "./../SettingsController"  

    let settings = new SettingsController()
    let pageName = settings.getJson().pageName
    let menuVariant = settings.getJson().menuVariant

    let userType = getUserType()

    async function getUserType() {
        let response = await fetch("./getUserType", { method: "POST" })
        response = await response.text()
        console.log("User type: " + response)
        userType = response
    }

    async function logOut() {
        let response = await fetch("./logOut", { method: "POST" })
        response = await response.text()
        console.log("User type: " + response)
        userType = response
    }

    let colorTheme ="Dark"
</script>

{#if menuVariant == "1"}
    <nav class="navbar navbar-expand-md navbar-dark {colorTheme == "Light" ? 'bg-blue-800 text-white':  (colorTheme == "Dark" ? 'bg-blue-900 text-white' : "bg-black text-yellow-500")}">
        <div class="container-fluid">
            <a class="navbar-brand ms-3" style="font-size: 150%;" href="#/">{pageName}</a>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ms-1 me-auto mb-2 mb-md-0">
                    <li class="nav-item me-1">
                        <a class="nav-link active" style="font-size: 120%;" aria-current="page" href="#/">BBBBB</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link" style="font-size: 120%;" href="#/subPage/article">Article</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link" style="font-size: 120%;" href="#/subPage/gallery">Gallery</a>
                    </li>
                </ul>
                <div class="text-end me-2 d-flex align-items-center">
                {#if userType == "none"}
                    <a href="#/logIn" type="button" class="btn btn-outline-light me-2">Log in</a>
                    <a href="#/signUp" type="button" class="btn signUp text-light  {colorTheme == "Light" ? 'bg-cyan-500 text-black':  (colorTheme == "Dark" ? 'bg-cyan-900 text-white' : "bg-yellow-500 color-black")}">Sign up</a>
                {:else}
                    <a href="#/subPage/settings" type="button" class="text-light me-4 hover d-flex align-content-center"><i style="font-size: 160%;" class="fa-solid fa-gear"></i></a> 
                    <button on:click={logOut} class="btn btn-outline-light me-2">Log out</button>
                {/if}
                </div>
            </div>
        </div>
    </nav>
{:else}
    <nav class="border-bottom">
        <div class="container">
            <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-2">
                <a class="d-flex align-items-center col-md-2 mb-2 mb-md-0 text-dark" style="font-size: 150%;" href="#/">{pageName}</a>
        
                <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
                    <li class="nav-item me-1">
                        <a class="nav-link active" style="font-size: 120%;" aria-current="page" href="#/">Home</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link" style="font-size: 120%;" href="#/subPage/article">Article</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link" style="font-size: 120%;" href="#/subPage/gallery">Gallery</a>
                    </li>  
                </ul>
        
                <div class="col-md-2 text-end d-flex align-items-center">
                    {#if userType == "none"}
                        <a href="#/logIn" type="button" class="btn btn-outline-dark me-2">Log in</a>
                        <a href="#/signUp" type="button" class="btn signUp text-light">Sign up</a>
                    {:else}
                        <a href="#/subPage/settings" type="button" class="text-dark me-4 hover d-flex align-content-center"><i style="font-size: 160%;" class="fa-solid fa-gear"></i></a> 
                        <button on:click={logOut} class="btn btn-outline-dark me-2">Log out</button>
                    {/if}
                </div>
            </div>
        </div>
    </nav>
{/if}
