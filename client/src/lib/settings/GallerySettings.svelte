<script>
    import SettingsController from "./../SettingsController";

    let settings = new SettingsController()
    let json = settings.getJson()

    //selects options
    let displays = [
        "Row", 
        "Column"
    ]

    //inputs
    let imagesSizeInput = json.imagesSize
    let displayTypeInput = json.galleryDisplay

    function save() {
        let displayType = document.getElementById("displayType").value
        let imagesSize = document.getElementById("imagesSize").value
        if (imagesSize > 800) {
            alert("Maximum images size is 800!")
            return
        }
        settings.setGalleryParameters(displayType, imagesSize)
        window.location.reload()
    }
    let colorTheme = settings.getJson().colorTheme
</script>

<div class="d-flex flex-column justify-content-center {colorTheme == "Light" ? 'bg-white t-black':  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
    <p class="mainHeadline">Gallery settings</p>

    <hr>

    <p class="headline">Parameters</p>
    <div class="w-25">
        <div class="row align-items-center m-2">
            <div class="col-6 text">Display</div>
            <select id="displayType" class="form-select form-select-lg col ms-3">
                {#each displays as display}
                    {#if display == displayTypeInput} 
                        <option selected>{display}</option>
                    {:else}
                        <option>{display}</option>
                    {/if}
                {/each}
            </select>
        </div>
        <div class="row align-items-center m-2 mt-4">
            <div class="col-6 text">Images size</div>
            <div class="col d-flex flex-row align-items-center ms-1">
                <input id="imagesSize" type="number" min="100" max="800" value={imagesSizeInput} class="form-control form-control-lg" style="width: 100px;"/>
                <p class="ms-1 mb-0 text">px</p>
            </div>
        </div>
    </div>

    <button on:click={save} class="btn btn-primary btn-lg mt-4 ms-3" style="width:fit-content;">Save</button>
</div>