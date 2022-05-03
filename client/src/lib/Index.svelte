<script>
	import Router from 'svelte-spa-router';

    import Menu from "./components/Menu.svelte";
    import Footer from "./components/Footer.svelte";

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
</script>

<a name="top" href="/" style="visibility: collapse; position: absolute;">top</a>

<Menu/>

<div class="marginTop">
    <Router {routes} />
</div>

<Footer />

<style>
    .marginTop {
        margin-top: 3.2%;
    }
</style>
