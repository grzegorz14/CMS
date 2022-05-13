<script>
    import SettingsController from "./../SettingsController"  
    
    let settings = new SettingsController()
    let colorTheme = settings.getJson().colorTheme
    let articleObjects =  settings.stringToArray(settings.getJson().articles)
    let articles = []
    for(let i = 0; i < articleObjects.length; i += 2) {
        articles.push({ 
            "header": articleObjects[i],
            "content": articleObjects[i + 1],
        })
    }

    async function addArticle() {
        let header = document.getElementById("articleHeader").value
        let content = document.getElementById("articleContent").value
        if (isEmptyOrWhiteSpace(header)){
            alert("Your article header is empty!")
            return
        }
        else if (isEmptyOrWhiteSpace(content)) {
            alert("Your article content is empty!")
            return
        }
        else {
            await settings.addArticle(header, content)
            window.location.reload()
        }
    }

    async function deleteArticle() {
        let article = document.getElementById("articleToDelete").value
        if (isEmptyOrWhiteSpace(article)) {
            return
        }
        if (confirm("Do you want to delete article \"" + article + "\"?")) {
            await settings.deleteArticle(article)
            window.location.reload()
        }
    }

    function isEmptyOrWhiteSpace(str){
        return str === null || str.match(/^ *$/) !== null
    }
</script>

<div class="d-flex flex-column justify-content-center ">
    <p class="mainHeadline">Article settings</p>

    <hr>

    <p class="headline">Add article</p>
    <div class="w-50">
        <div class="row align-items-center m-2 {colorTheme == "Light" ? 'bg-white t-black':  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
            <div class="col-2 text">Header</div>
            <div class="col">
                <input id="articleHeader" type="text" class="form-control form-control-lg"/>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-2 text">Content</div>
            <div class="col">
                <textarea id="articleContent" class="form-control form-control-lg" rows="5"></textarea>
            </div>
        </div>
        <div class="row justify-content-end mt-3">
            <button on:click={addArticle} class="btn btn-success me-5" style="width:fit-content;">Add new article</button>
        </div>
        
    </div>

    <hr>

    <p class="headline">Delete article</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-2 text">Header</div>
            <select id="articleToDelete" class="form-select form-select-lg col">
                {#each articles as article}
                    <option>{article.header}</option>
                {/each}
            </select>
            <button on:click={deleteArticle} class="btn btn-danger ms-4" style="width:fit-content;">Delete selected</button>
        </div>
    </div>
</div>