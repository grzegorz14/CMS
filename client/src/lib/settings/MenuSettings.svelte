<script>
    let pageName = "CMS" //get from db

    function changePageName() {

    }

    function addLink() {
        let link = document.getElementById("linkText").value
        if (isEmptyOrWhiteSpace(link)){
            alert("Your link is empty!")
            return
        }
        else {
            //add link and empty input fields
        }
    }

    function deleteLink() {
        let link = document.getElementById("linkToDelete").value
        if (confirm("Do you want to delete link \"" + link + "\"?")) {
            //delete link
        }
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">Menu settings</p>

    <hr>

    <p class="headline">Main</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-3 text">Page name </div>
            <div class="col">
                <input id="newPageNameInput" type="text" placeholder={pageName} class="form-control form-control-lg"/>
            </div>
            <div class="col">
                <button on:click={changePageName} class="btn btn-primary">Change page name</button>
            </div>
        </div>
        <p>checkbox or select how to display menu</p>
    </div>

    <hr>

    <p class="headline">Link managment</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-3 text">Add link</div>
            <div class="col">
                <input id="linkText" type="text" class="form-control form-control-lg"/>
            </div>
            <button on:click={addLink} class="btn btn-success me-5" style="width:fit-content;">Add new link</button>
        </div>
        <div class="row align-items-center m-2 mt-4">
            <div class="col-3 text">Delete link</div>
            <select id="linkToDelete" class="form-select form-select-lg col">
                <option selected>Home</option>
                <option>Article</option>
                <option>Gallery</option>
            </select>
            <button on:click={deleteLink} class="btn btn-danger ms-4" style="width:fit-content;">Delete link</button>
        </div>
    </div>
</div>
