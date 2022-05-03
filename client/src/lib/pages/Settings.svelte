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
                <a href="#/subPage/settings/mainDashboard" >Main Dashboard</a>
            </li>
            <li>
                <a href="#/subPage/settings/menu" >Menu</a>            
            </li>
            <li>
                <a href="#/subPage/settings/slider" >Slider</a>            
            </li>
            <li>
                <a href="#/subPage/settings/articles" >Articles</a>              
            </li>
            <li>
                <a href="#/subPage/settings/gallery" >Gallery</a>            
            </li>
            <li>
                <a href="#/subPage/settings/users" >Users</a>            
            </li>
            <li>
                <a href="#/subPage/settings/myAccount" >My Account</a>            
            </li>
        </ul>
    </nav>

    <div id="content">
        <Router {routes} />
    </div>
</div>

<style>
    a,
    a:hover,
    a:focus {
        color: inherit;
        text-decoration: none;
        transition: all 0.3s;
    }

    .wrapper {
        display: flex;
        width: 100%;
        align-items: stretch;
    }

    #sidebar {
        min-width: 250px;
        max-width: 250px;
        background: #cf8c85;
        color: #fff;
        transition: all 0.3s;
    }

    #sidebar .sidebar-header {
        padding: 20px;
        padding-bottom: 15px;
        background: #c27167;
    }

    #sidebar ul li a {
        padding: 20px;
        font-size: 1.1em;
        display: block;
    }

    #sidebar ul li a:hover {
        color: #00557c;
        background: #fff;
    }

    #content {
        width: 100%;
        padding: 40px;
        padding-left: 70px;
        padding-right: 70px;
        min-height: 100vh;
        transition: all 0.3s;
    }
</style>
