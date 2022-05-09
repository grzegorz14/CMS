<script>
    import Footer from "../components/Footer.svelte"
    import SettingsController from "./../SettingsController"  

    let settings = new SettingsController()
    let json = settings.getJson()
    let imagesSize = json.imagesSize
    let displayType = json.galleryDisplay
    let colorTheme = json.colorTheme


    let images = []
    let imagesLength = getImagesLength()

    async function getImagesLength() {
        let response = await fetch("./getImagesLength", { method: "POST" })
        response = await response.text()
        imagesLength = response
        await getImages()
    }

    async function getImages() {
        for (let i = 0; i < imagesLength; i++) {
            let response = await fetch("./getImage?id=" + i, { method: "POST" })
            response = await response.text()
            images = [...images, response.split("\\")[1]]
        }
    }
</script>

{#await images}
    <h1 class="text-center">Looking for photos...</h1>
{:then}
    <div class="p-5">
        <h1 class="text-center">Images</h1>
        {#if displayType == "Row"}
            <div class="d-flex flex-row flex-wrap m-5 mb-0 justify-content-center">
                {#each images as image}
                    <img
                    src={"./../images/" + image}
                    alt="An image"
                    height={imagesSize + "px"}
                    class="rounded-3 m-3"
                    style="object-fit: cover;"
                    />
                {/each}
            </div>
        {:else}
            <div class="d-flex flex-column m-5 mb-0 align-items-center">
                {#each images as image}
                    <img
                    src={"./../images/" + image}
                    alt="An image"
                    width={imagesSize + "px"}
                    class="rounded-3 m-3"
                    style="object-fit: cover;"
                    />
                {/each}
            </div>
        {/if}
    </div>

    <hr>
    <Footer />
{/await}
