<script>    
    import SettingsController from "./../SettingsController";

    let settings = new SettingsController()
    let json = settings.getJson()

    //selects options
    let variants = [
        { value: "1", content: "Variant 1 (default)" },
        { value: "2", content: "Variant 2 (contentCenter)" }
    ]
    let links = json.links

    //inputs
    let pageNameInput = json.pageName
    let menuVariantInput = json.menuVariant

    function changePageName() {
        let newPageName = document.getElementById("pageName").value
        if (isEmptyOrWhiteSpace(newPageName)) {
            alert("New page name is empty!")
            return
        }
        settings.setPageName(newPageName)
        window.location.reload()
    }   

    function changeMenuVariant() {
        settings.setMenuVariant(document.getElementById("menuVariant").value)
        window.location.reload()
    }

    function addLink() {
        let link = document.getElementById("linkText").value
        if (isEmptyOrWhiteSpace(link)){
            alert("Your link is empty!")
            return
        }
        else {
            settings.addLink(link)
            window.location.reload()
        }
    }

    function deleteLink() {
        let link = document.getElementById("linkToDelete").value
        if (confirm("Do you want to delete link \"" + link + "\"?")) {
            settings.deleteLink(link)
            window.location.reload()
        }
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
    let colorTheme = settings.getJson().colorTheme
</script>

<div class="d-flex flex-column justify-content-center {colorTheme == "Light" ? 'bg-white t-black':  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
    <p class="mainHeadline">Menu settings</p>

    <hr>

    <p class="headline">Main</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-3 text">Page name</div>
            <div class="col ms-1">
                <input id="pageName" type="text" placeholder={pageNameInput} class="form-control form-control-lg"/>
            </div>
            <div class="col">
                <button on:click={changePageName} class="btn btn-primary">Change page name</button>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-3 text">Menu variant</div>
            <select id="menuVariant" class="form-select form-select-lg col ms-3">
                {#each variants as variant}
                    {#if variant.value == menuVariantInput} 
                        <option selected value={variant.value}>{variant.content}</option>
                    {:else}
                        <option value={variant.value}>{variant.content}</option>
                    {/if}
                {/each}
            </select>
            <div class="col">
                <button on:click={changeMenuVariant} class="btn btn-primary">Change menu variant</button>
            </div>
        </div>
    </div>

    <hr>

    <p class="headline">Link managment</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-3 text">Add link</div>
            <div class="col ms-1">
                <input id="linkText" type="text" class="form-control form-control-lg"/>
            </div>
            <button on:click={addLink} class="btn btn-success me-5" style="width:fit-content;">Add new link</button>
        </div>
        <div class="row align-items-center m-2 mt-4">
            <div class="col-3 text">Delete link</div>
            <select id="linkToDelete" class="form-select form-select-lg col ms-3">
                {#each links as link}
                    <option>{link}</option>
                {/each}
            </select>
            <button on:click={deleteLink} class="btn btn-danger ms-4" style="width:fit-content;">Delete link</button>
        </div>
    </div>
</div>
