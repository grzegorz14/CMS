<script>
	import Router from 'svelte-spa-router';

    import Menu from "./components/Menu.svelte";

    import Home from './pages/Home.svelte';
    import Article from './pages/Article.svelte';
    import Gallery from './pages/Gallery.svelte';
    import Settings from './pages/Settings.svelte';
    import NotFound from './pages/NotFound.svelte';

    const routes = {
        "/subPage/settings/:page": Settings,
        "/subPage/settings": Settings,
        "/subPage/article": Article,
        "/subPage/gallery": Gallery,
        "/": Home,

        "*": NotFound
    };

    //imports settings from json in local storage
    import json from "./Settings.json"
    import SettingsController from './SettingsController';

    let settings = new SettingsController()
    let settingsJson = settings.getJson()
    
    if (settingsJson != null) {
        //do that for each setting
        json.fontSize = settingsJson.fontSize
        settings.setFontAttributes(settingsJson.fontSize, "")
    }
</script>

<a name="top" href="/" style="visibility: collapse; position: absolute;">top</a>

<Menu/>

<div class="marginTop">
    <Router {routes} />
</div>
