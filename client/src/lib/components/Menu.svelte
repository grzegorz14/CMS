<script>
    import SettingsController from "./../SettingsController"  
    
    let settings = new SettingsController()
    let json =  settings.getJson()
    let pageName = json.pageName
    let menuVariant = json.menuVariant
    let colorTheme = json.colorTheme
    let links = json.links

    let logged = isLogged()

    async function isLogged() {
        let response = await fetch("./isLogged", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                "login": localStorage.getItem("login")
            }),
        })
        response = await response.text()
        console.log("User type: " + response)
        console.log("Login: " + localStorage.getItem("login"))
        logged = response
    }

    async function logOut() {
        let response = await fetch("./logOut", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                "login": localStorage.getItem("login")
            }),
        })
        logged = "false"
    }
</script>

{#if menuVariant == "1"}
    <nav class="navbar navbar-expand-md {colorTheme == "Light" ? 'bg-lightBlue t-white':  (colorTheme == "Dark" ? 'bg-darkBlue t-white' : "bg-black t-yellow")} ">
        <div class="container-fluid">
            <a class="navbar-brand ms-3 {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 150%;" href="#/">{pageName}</a>
            <div class="collapse navbar-collapse " id="navbarCollapse">
                <ul class="navbar-nav ms-1 me-auto mb-2 mb-md-0 ">
                    <li class="nav-item me-1">
                        <a class="nav-link active {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" aria-current="page" href="#/">Home</a>
                    </li>
                    <li class="nav-item me-1 ">
                        <a class="nav-link {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" href="#/subPage/article">Article</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" href="#/subPage/gallery">Gallery</a>
                    </li>
                    {#each links as link}
                        <li class="nav-item me-1">
                            <a class="nav-link {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} "  style="font-size: 120%;" href="#/subPage/gallery">{link}</a>
                        </li>
                    {/each}
                </ul>
                <div class="text-end me-2 d-flex align-items-center">
                {#if logged == "false"}
                    <a href="#/logIn" type="button" class="btn btn-outline-light me-2">Log in</a>
                    <a href="#/signUp" type="button" class="btn signUp text-light  {colorTheme == "Light" ? 'bg-lightCyan t-black':  (colorTheme == "Dark" ? 'bg-darkCyan t-white' : "bg-yellow t-black")}">Sign up</a>
                {:else}
                    <a href="#/subPage/settings" type="button" class="text-light me-4 hover d-flex align-content-center"><i style="font-size: 160%;" class="fa-solid fa-gear"></i></a> 
                    <button on:click={logOut} class="btn btn-outline-light me-2">Log out</button>
                {/if}
                </div>
            </div>
        </div>
    </nav>
{:else}
    <nav class="border-bottom {colorTheme == "Light" ? 'bg-lightBlue t-white':  (colorTheme == "Dark" ? 'bg-darkBlue t-white' : "bg-black t-yellow")}">
        <div class="container">
            <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-2 ">
                <a class="d-flex align-items-center col-md-2 mb-2 mb-md-0  {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 150%;" href="#/">{pageName}</a>
        
                <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
                    <li class="nav-item me-1">
                        <a class="nav-link active {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" aria-current="page" href="#/">Home</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" href="#/subPage/article">Article</a>
                    </li>
                    <li class="nav-item me-1">
                        <a class="nav-link {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" href="#/subPage/gallery">Gallery</a>
                    </li>  
                    {#each links as link}
                        <li class="nav-item me-1">
                            <a class="nav-link {colorTheme == "Light" ? ' t-white':  (colorTheme == "Dark" ? ' t-white' : " t-yellow")} " style="font-size: 120%;" href="#/subPage/gallery">{link}</a>
                        </li>
                    {/each}
                </ul>
        
                <div class="col-md-2 text-end d-flex align-items-center">
                    {#if logged == "false"}
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
