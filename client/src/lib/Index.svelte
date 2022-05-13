<script>
	import Router from 'svelte-spa-router';

    import Menu from "./components/Menu.svelte";
    import Home from './pages/Home.svelte';
    import ArticlePage from './pages/ArticlePage.svelte';
    import Article from './pages/Article.svelte';
    import Gallery from './pages/Gallery.svelte';
    import Settings from './pages/Settings.svelte';
    import NotFound from './pages/NotFound.svelte';

    const routes = {
        "/subPage/settings/:page/:parameter": Settings,
        "/subPage/settings/:page": Settings,
        "/subPage/settings": Settings,
        "/subPage/article/:page": ArticlePage,
        "/subPage/article": Article,
        "/subPage/gallery": Gallery,
        "/": Home,

        "*": NotFound
    };

    //imports settings from json in local storage
    import json from "./Settings.json"
    import SettingsController from './SettingsController';

    //localStorage.setItem("settingsJson", null)
    let settings = new SettingsController()
    let settingsJson = settings.getJson()
    let colorTheme

    async function code() {
        let databaseSettings = await settings.getSettingsJson()
        console.log("DB Settings:")
        console.log(databaseSettings)

        localStorage.setItem("settingsJson", JSON.stringify(databaseSettings))

        colorTheme = databaseSettings.colorTheme
        settings.setStyle("--font-size", databaseSettings.fontSize + "px")
        settings.setStyle("--font-family", databaseSettings.fontFamily)

        // if (settingsJson == null) {
        //     localStorage.setItem("settingsJson", JSON.stringify(databaseSettings))
        //     databaseSettings = await settings.getSettingsJson()
        //     settings.setStyle("--font-size", databaseSettings.fontSize)
        //     settings.setStyle("--font-family", databaseSettings.fontFamily)
        // }
        // else {
        //     //set json fields
        //     let updateJson = []
        //     updateJson[settings.getArrayIndex("pageName")] = settingsJson.pageName
        //     updateJson[settings.getArrayIndex("pageLayout")] = settingsJson.pageLayout
        //     updateJson[settings.getArrayIndex("colorTheme")] = settingsJson.colorTheme
        //     updateJson[settings.getArrayIndex("fontSize")] = settingsJson.fontSize
        //     updateJson[settings.getArrayIndex("fontFamily")] = settingsJson.fontFamily
        //     updateJson[settings.getArrayIndex("menuVariant")] = settingsJson.menuVariant
        //     updateJson[settings.getArrayIndex("imagesSize")] = settingsJson.imagesSize
        //     updateJson[settings.getArrayIndex("galleryDisplay")] = settingsJson.galleryDisplay
        //     updateJson[settings.getArrayIndex("links")] = settingsJson.links
        //     updateJson[settings.getArrayIndex("slides")] = settingsJson.slides
        //     updateJson[settings.getArrayIndex("articles")] = settingsJson.articles

        //     settings.updateJson(updateJson)
        
        //     settings.setStyle("--font-size", settingsJson.fontSize)
        //     settings.setStyle("--font-family", settingsJson.fontFamily)
        // }
    }
    let promise = code()
</script>

{#await promise}
    Loading settings...
{:then} 
    <a name="top" href="/" style="visibility: collapse; position: absolute;">top</a>

    <Menu/>

    <div class="{colorTheme == "Light" ? 'bg-white t-black' :  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black text-yellow")}">
        <Router {routes} />
    </div>
{/await}
