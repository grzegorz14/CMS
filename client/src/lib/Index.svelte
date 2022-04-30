<script>
	import Router from 'svelte-spa-router';

    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";

    import Home from './Home.svelte';
    import Article from './Article.svelte';
    import Gallery from './Gallery.svelte';
    import NotFound from './NotFound.svelte';

    const routes = {
    "/": Home,
    "/subPage/article": Article,
    "/subPage/gallery": Gallery,

    "*": NotFound
  };
</script>

<a name="top" href="/" style="visibility: collapse; position: absolute;">top</a>

<Header/>

<div class="marginTop">
    <Router {routes} />
</div>

<Footer />

<style>
    .marginTop {
        margin-top: 3%;
    }
</style>
