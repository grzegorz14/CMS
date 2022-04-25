<script>
    import Header from "./Header.svelte";
    import Slider from "./Slider.svelte";
    import News from "./News.svelte";
    import Photos from "./Photos.svelte";
    import Footer from "./Footer.svelte";
</script>

<Header/>

<div class="marginTop">
    <Slider />
    <News />
    <Photos />
</div>

<Footer />

<style>
    .marginTop {
        margin-top: 30px;
    }
</style>