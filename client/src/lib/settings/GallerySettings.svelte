<script>
    function save() {
        //saves settings
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">Gallery settings</p>

    <hr>

    <p class="headline">Parameters</p>
    <div class="w-25">
        <div class="row align-items-center m-2">
            <div class="col-6 text">Display</div>
            <select id="displayType" class="form-select form-select-lg col ms-3">
                <option selected>Row</option>
                <option>Column</option>
            </select>
        </div>
        <div class="row align-items-center m-2 mt-4">
            <div class="col-6 text">Images width</div>
            <div class="col d-flex flex-row align-items-center ms-1">
                <input id="imagesWidthInput" type="number" onKeyDown="return false" min="100" max="500" value="300" class="form-control form-control-lg" style="width: 100px;"/>
                <p class="ms-1 mb-0 text">px</p>
            </div>
        </div>
    </div>

    <button on:click={save} class="btn btn-primary btn-lg mt-4 ms-3" style="width:fit-content;">Save</button>
</div>