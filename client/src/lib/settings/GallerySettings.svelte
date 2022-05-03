<script>
    function save() {
        //saves settings
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">Gallery settings</p>

    <hr>

    <p class="headline">Parameters</p>
    <div style="width: 40%;">
        <div class="row align-items-center m-2">
            <div class="col text">Display</div>
            <div class="col">
                <div>
                    <input id="rowRadioInput" type="radio" name="display" checked/>
                    <label for="rowRadioInput" class="radioLabel">Row</label>
                </div>
               <div>
                    <input id="columnRadioInput" type="radio" name="display"/>
                    <label for="columnRadioInput" class="radioLabel">Column</label>
               </div>
            </div>
        </div>
        <div class="row align-items-center m-2 mt-4">
            <div class="col text">Images width: </div>
            <div class="col d-flex flex-row align-items-center">
                <input id="imagesWidthInput" type="number" min="100" max="500" value="300" class="form-control form-control-lg" style="width: 100px;"/>
                <p class="ms-1 mb-0">px</p>
            </div>
        </div>
    </div>

    <button on:click={save} class="btn btn-primary btn-lg mt-4 ms-3" style="width:fit-content;">Save</button>
</div>