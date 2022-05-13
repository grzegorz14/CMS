<script>
	import NotFound from './NotFound.svelte'
	import Comments from './../components/Comments.svelte'
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

    let articleName = window.location.href.split("/")[window.location.href.split("/").length - 1].replaceAll("%20", " ")

    let article = articles.find(article => article.header == articleName)
</script>

{#if article == undefined}
    <NotFound />
{:else}
    <div class="d-flex flex-column justify-content-center {colorTheme == "Light" ? 'bg-white t-black' :  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}" style="margin-left: 30%; margin-right: 30%; padding:1%; font-size:120%;">
        <p class="date">ARTICLE | December 15, 2022</p>
        <p class="mainHeadline">{article.header}</p>
        <p class="by">By Mollier Carter and Ernier Wrighter</p>

        <p>{article.content}</p>
    </div>

    <div class="commentSecton {colorTheme == "Light" ? 'bg-lightGray t-black' :  (colorTheme == "Dark" ? 'bg-darkerGray t-white' : "bg-black t-yellow")}">
        <div class="in">
            <div class="c">Comments</div>
            <Comments />
        </div>
    </div>
{/if}
