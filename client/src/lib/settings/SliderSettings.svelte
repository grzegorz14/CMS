<script>
    import SettingsController from "./../SettingsController"  

    let settings = new SettingsController()
    let slideObjects =  settings.stringToArray(settings.getJson().slides)
    let slides = []
    for(let i = 0; i < slideObjects.length; i += 4) {
        slides.push({ 
            "image": slideObjects[i],
            "header": slideObjects[i + 1],
            "content": slideObjects[i + 2],
            "transition": slideObjects[i + 3],
        })
    }


    let colorTheme = settings.getJson().colorTheme

    async function addSlide() {
        //let image = document.getElementById("slideImage").files[0]
        let image = document.getElementById("image").value
        let header = document.getElementById("slideHeader").value
        let content = document.getElementById("slideContent").value
        let transition = document.getElementById("imageTransitionTime").value
        // if (image == undefined) {
        //     alert("Select the slide image!")
        //     return
        // }
        if (isEmptyOrWhiteSpace(image)){
            alert("Your image url is empty!")
            return
        }
        else if (isEmptyOrWhiteSpace(header)){
            alert("Your slide header is empty!")
            return
        }
        else if (isEmptyOrWhiteSpace(content)) {
            alert("Your slide content is empty!")
            return
        }
        else {
            await settings.addSlide(image, header, content, transition)
            window.location.reload()
        }
    }

    async function deleteSlide() {
        let slide = document.getElementById("slideToDelete").value
        if (isEmptyOrWhiteSpace(slide)) {
            return
        }
        if (confirm("Do you want to delete slide \"" + slide + "\"?")) {
            await settings.deleteSlide(slide)
            window.location.reload()
        }
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
</script>

<div class="d-flex flex-column justify-content-center {colorTheme == "Light" ? 'bg-white t-black':  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
    <p class="mainHeadline">Slider settings</p>

    <hr>

    <p class="headline">Add slide</p>
    <div class="w-75">
        <div class="row align-items-center m-2">
            <div class="col-2 text">Image</div>
            <div class="col">
                <input id="image" placeholder="Paste here an url to image (with high resolution)" type="text" class="form-control form-control-lg"/>
            </div>
            <!-- <div class="col">
                <input class="form-control form-control-lg" type="file" id="slideImage" accept="image/png, image/gif, image/jpeg, image/jpg, image/webp" >
            </div> -->
        </div>
        <div class="row align-items-center m-2">
            <div class="col-2 text">Slide header</div>
            <div class="col">
                <input id="slideHeader" type="text" class="form-control form-control-lg"/>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-2 text">Short content</div>
            <div class="col">
                <textarea id="slideContent" class="form-control form-control-lg" rows="1"></textarea>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-2 text">Transition time </div>
            <div class="col d-flex flex-row align-items-center">
                <input id="imageTransitionTime" type="number" onKeyDown="return false" min="2" max="9" value="6" class="form-control form-control-lg" style="width: 90px;"/>
                <p class="ms-1 mb-0 text">s</p>
            </div>
        </div>
        <div class="row justify-content-end mt-3">
            <button on:click={addSlide} class="btn btn-success me-5" style="width:fit-content;">Add new slide</button>
        </div>
    </div>

    <hr>

    <p class="headline">Delete slide</p>
    <div class="w-75">
        <div class="row align-items-center m-2">
            <div class="col-2 text">Slide header</div>
            <select id="slideToDelete" class="form-select form-select-lg col">
                {#each slides as slide}
                    <option>{slide.header}</option>
                {/each}
            </select>
            <button on:click={deleteSlide} class="btn btn-danger ms-4" style="width:fit-content;">Delete selected</button>
        </div>
    </div>
</div>