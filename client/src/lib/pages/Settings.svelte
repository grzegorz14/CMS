<script>
    import Router from "svelte-spa-router";
    
    import MainDashboardSettings from "../settings/MainDashboardSettings.svelte";
    import ArticlesSettings from "../settings/ArticlesSettings.svelte";
    import GallerySettings from "../settings/GallerySettings.svelte";
    import UsersSettings from "../settings/UsersSettings.svelte";
    import NotFound from "./NotFound.svelte";   
    import MyAccountSettings from "../settings/MyAccountSettings.svelte";
    import MenuSettings from "../settings/MenuSettings.svelte";
    import SliderSettings from "../settings/SliderSettings.svelte";

    const routes = {
        "/subPage/settings": MainDashboardSettings,
        "/subPage/settings/mainDashboard": MainDashboardSettings,
        "/subPage/settings/gallery": GallerySettings,
        "/subPage/settings/articles": ArticlesSettings,
        "/subPage/settings/users": UsersSettings,
        "/subPage/settings/myAccount": MyAccountSettings,
        "/subPage/settings/menu": MenuSettings,
        "/subPage/settings/slider": SliderSettings,

        "*": NotFound
    };
</script>

<div class="wrapper">
    <nav id="sidebar">
        <div class="sidebar-header">
            <h3>Settings</h3>
        </div>

        <ul class="list-unstyled">
            <li>
                <a class="settingsNavText" href="#/subPage/settings/mainDashboard" >Main Dashboard</a>
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
        </ul>
    </nav>

    <div id="content">
        <Router {routes} />
    </div>
</div>
