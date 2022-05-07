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
        //set all of the fields
        json.pageName = settingsJson.pageName
        settings.setPageName(settingsJson.pageName)
        json.pageLayout = settingsJson.pageLayout
        json.colorTheme = settingsJson.colorTheme
        settings.setPageThemes(settingsJson.pageLayout, settingsJson.colorTheme)
        json.fontSize = settingsJson.fontSize
        json.fontFamily = settingsJson.fontFamily
        settings.setFontAttributes(settingsJson.fontSize, settingsJson.fontFamily)
        json.menuVariant = settingsJson.menuVariant
        settings.setMenuVariant(settingsJson.menuVariant)
    }
</script>

<a name="top" href="/" style="visibility: collapse; position: absolute;">top</a>

<Menu/>

<div class="marginTop">
    <Router {routes} />
</div>
