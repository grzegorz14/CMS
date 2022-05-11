<script>
  import Article from "../pages/Article.svelte"
import SettingsController from "./../SettingsController"  
  
  let settings = new SettingsController()
  let colorTheme = settings.getJson().colorTheme
  let articles = settings.getJson().articles

  let trios = [] //all articles
  for (let i = 1; i <= (articles.length / 3) + 1; i++) {
    let trio = [] //one article row
    for (let j = 1; j <= 3 && (i * 3 + j - 4) < articles.length; j++) {
      trio.push({ header: articles[i * 3 + j - 4].header, content: articles[i * 3 + j - 4].content.substring(0, 250) + "..." })
    }
    trios.push(trio)
  }
</script>

<div class="container mt-5 mb-5 {colorTheme == "Light" ? 'bg-white t-black' :  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
  <h1 class="text-justify mb-4 text-center">Articles</h1>
  <div class="row gap-4">
    <div class="col mb-5" style="max-width: 50%; max-height: 250px">
      <h3 class="mb-3">Air pollution</h3>
      <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
      <p><a class="btn {colorTheme == "Light" ? 'bg-cyan t-black':  (colorTheme == "Dark" ? 'bg-indygo t-white' : "bg-yellow t-black")}" href="/#/subPage/article" role="button">Read article »</a></p>
    </div>
    <div class="col mb-5" style="max-width: 50%; max-height: 250px;">
      <h3 class="mb-3">Phases of the moon</h3>
      <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
      <p><a class="btn {colorTheme == "Light" ? 'bg-cyan t-black':  (colorTheme == "Dark" ? 'bg-indygo t-white' : "bg-yellow t-black")}" href="/#/subPage/article" role="button">Read article »</a></p>
    </div>
    <div class="col mb-5" style="max-width: 50%; max-height: 250px;">
      <h3 class="mb-3">Falling stars</h3>
      <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
      <p><a class="btn {colorTheme == "Light" ? 'bg-cyan t-black':  (colorTheme == "Dark" ? 'bg-indygo t-white' : "bg-yellow t-black")}" href="/#/subPage/article" role="button">Read article »</a></p>
    </div>
  </div>
  <div class="row gap-4">
    <div class="col" style="max-width: 50%; max-height: 250px;">
      <h3 class="mb-3">People on Mars in 2029</h3>
      <p>Donec id elit non mi porta gravida at eget I love Elon Musk metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
      <p><a class="btn {colorTheme == "Light" ? 'bg-cyan t-black':  (colorTheme == "Dark" ? 'bg-indygo t-white' : "bg-yellow t-black")}" href="/#/subPage/article" role="button">Read article »</a></p>
    </div>
    <div class="col" style="max-width: 50%; max-height: 250px;">
      <h3 class="mb-3">Graphene technology</h3>
      <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
      <p><a class="btn {colorTheme == "Light" ? 'bg-cyan t-black':  (colorTheme == "Dark" ? 'bg-indygo t-white' : "bg-yellow t-black")}" href="/#/subPage/article" role="button">Read article »</a></p>
    </div>
  </div>
  {#if articles.length > 0}
    <h1 class="text-justify mb-4 text-center">Your Articles</h1>
    {#each trios as trio}
    <div class="row gap-4">
      {#each trio as article}
        <div class="col mb-5" style="max-width: 50%; max-height: 250px">
          <h3 class="mb-3">{article.header}</h3>
          <p>{article.content}</p>
          <p><a class="btn {colorTheme == "Light" ? 'bg-cyan t-black':  (colorTheme == "Dark" ? 'bg-indygo t-white' : "bg-yellow t-black")}" href="/#/subPage/article" role="button">Read article »</a></p>
        </div>
      {/each}
    </div>
  {/each}
  {/if}
</div>
