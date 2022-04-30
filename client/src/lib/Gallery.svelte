<script>
    let images = []
    let imagesLength = getImagesLength()

    async function getImagesLength() {
        let response = await fetch("./getImagesLength")
        response = await response.text()
        imagesLength = response
        await getImages()
    }

    async function getImages() {
        for (let i = 0; i < imagesLength; i++) {
            let response = await fetch("./getImage?id=" + i)
            response = await response.text()
            images = [...images, response.split("\\")[1]]
        }
    }
</script>

{#await images}
    <h1 class="text-center">Looking for photos...</h1>
{:then}
    <div class="mt-5 p-5">
        <h1 class="text-center">Images</h1>
        <div class="d-flex flex-row flex-wrap m-5 mb-0 justify-content-center">
            {#each images as image}
                <img
                src={"./../images/" + image}
                alt="An image"
                height="300px"
                class="rounded-3 m-3"
                style="object-fit: cover;"
                />
            {/each}
        </div>
    </div>
{/await}
