<script>
    import Router from "svelte-spa-router";
    
    import HomeSettings from "../settings/HomeSettings.svelte";
    import ArticlesSettings from "../settings/ArticlesSettings.svelte";
    import GallerySettings from "../settings/GallerySettings.svelte";
    import UsersSettings from "../settings/UsersSettings.svelte";
    import EditUser from "../settings/EditUser.svelte";
    import NotFound from "./NotFound.svelte";   
    import MyAccountSettings from "../settings/MyAccountSettings.svelte";
    import MenuSettings from "../settings/MenuSettings.svelte";
    import SliderSettings from "../settings/SliderSettings.svelte";

    import SettingsController from "./../SettingsController"

    let settings = new SettingsController()
    let colorTheme = settings.getJson().colorTheme
    console.log(colorTheme)

    const routes = {
        "/subPage/settings": HomeSettings,
        "/subPage/settings/home": HomeSettings,
        "/subPage/settings/gallery": GallerySettings,
        "/subPage/settings/articles": ArticlesSettings,
        "/subPage/settings/users": UsersSettings,
        "/subPage/settings/editUser/:user": EditUser,
        "/subPage/settings/myAccount": MyAccountSettings,
        "/subPage/settings/menu": MenuSettings,
        "/subPage/settings/slider": SliderSettings,

        "*": NotFound
    };

    let userType = getUserType()

    async function getUserType() {
        let response = await fetch("./getUserType", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                "login": localStorage.getItem("login")
            }),
        })
        response = await response.text()
        userType = response
    }
    
</script>

<div class="wrapper ">
    <nav id="sidebar">
        <div class="sidebar-header">
            <h3>Settings</h3>
        </div>

        <ul class="list-unstyled">
            {#if userType == "admin"}
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/home" >Home</a>
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/menu" >Menu</a>            
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/slider" >Slider</a>            
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/articles" >Articles</a>              
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/gallery" >Gallery</a>            
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/users" >Users</a>            
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/myAccount" >My Account</a>            
                </li>
            {:else}
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/myAccount" >My Account</a>            
                </li>
                <li>
                    <a class="settingsNavText" href="#/subPage/settings/articles" >Articles</a>              
                </li>
            {/if}
        </ul>
    </nav>

    <div id="content">
        <Router {routes} />
    </div>
</div>
