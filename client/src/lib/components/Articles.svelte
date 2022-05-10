<script>
  import SettingsController from "./../SettingsController"  
  
  let settings = new SettingsController()
  let colorTheme = settings.getJson().colorTheme
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
</div>
