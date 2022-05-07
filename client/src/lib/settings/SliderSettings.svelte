<script>
    function addSlide() {
        let image = document.getElementById("slideImage").files[0]
        let header = document.getElementById("slideHeader").value
        let content = document.getElementById("slideContent").value
        let transition = document.getElementById("transitionTime").value
        console.log(transition)
        if (image == undefined) {
            alert("Select the slide image!")
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
            //add slide and empty input fields
        }
    }

    function deleteSlide() {
        let slide = document.getElementById("slideToDelete").value
        if (confirm("Do you want to delete slide \"" + slide + "\"?")) {
            //delete slide
        }
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">Slider settings</p>

    <hr>

    <p class="headline">Add slide</p>
    <div class="w-75">
        <div class="row align-items-center m-2">
            <div class="col-2 text">Image</div>
            <div class="col">
                <input class="form-control form-control-lg" type="file" id="slideImage" accept="image/png, image/gif, image/jpeg, image/jpg, image/webp" >
            </div>
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
                <input id="imageTransitionTime" type="number" onKeyDown="return false" min="2" max="9" value="7" class="form-control form-control-lg" style="width: 90px;"/>
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
                <option selected>Air pollution</option>
                <option>Phases of the moon</option>
                <option>People on Mars in 2029</option>
            </select>
            <button on:click={deleteSlide} class="btn btn-danger ms-4" style="width:fit-content;">Delete selected</button>
        </div>
    </div>
</div>