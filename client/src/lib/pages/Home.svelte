<script>
	import Slider from './../components/Slider.svelte';
    import Articles from "./../components/Articles.svelte";
    import Photos from "./../components/Photos.svelte";
    import Footer from '../components/Footer.svelte';

    import SettingsController from "./../SettingsController"
    let settings = new SettingsController()
    let layout = settings.getJson().pageLayout
    console.log(layout)
    if (layout == undefined) {
        layout == "classic"
    }
</script>

{#if layout == "classic"}
    <Slider />
    <Articles />
    <Photos />
{:else if layout == "imageLover"}
    <Slider />
    <Photos />
    <Articles />
{:else if layout == "newsFirst"}
    <Articles />
    <Photos />
    <Slider />
{:else if layout == "middleSlider"}
    <Articles />
    <Slider />
    <Photos />
{:else if layout == "gifsFan"}
    <Photos />
    <Slider />
    <Articles />
{:else if layout == "reverse"}
    <Photos />
    <Articles />
    <Slider />
{/if}

<Footer />
