<script>
  let userType = getUserType()

  async function getUserType() {
    let response = await fetch("./getUserType", { method: "POST" })
    response = await response.text()
    console.log(response)
    userType = response
  }

  async function logOut() {
    let response = await fetch("./logOut", { method: "POST" })
    response = await response.text()
    console.log(response)
    userType = response
  }
</script>

<nav class="navbar navbar-expand-md navbar-dark fixed-top background">
    <div class="container-fluid">
        <a class="navbar-brand ms-3" style="font-size: 150%;" href="/">CMS</a>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav ms-1 me-auto mb-2 mb-md-0">
                <li class="nav-item me-1">
                    <a class="nav-link active" style="font-size: 120%;" aria-current="page" href="#/">Home</a>
                </li>
                <li class="nav-item me-1">
                    <a class="nav-link" style="font-size: 120%;" href="#/subPage/article">Article</a>
                </li>
                <li class="nav-item me-1">
                    <a class="nav-link" style="font-size: 120%;" href="#/subPage/gallery" tabindex="-1" aria-disabled="true">Gallery</a>
                </li>
            </ul>
            <div class="text-end me-2 d-flex align-items-center">
              {#if userType == "none"}
                  <a href="#/logIn" type="button" class="btn btn-outline-light me-2">Log in</a>
                  <a href="#/signUp" type="button" class="btn signUp">Sign up</a>
              {:else}
                  <a href="#/subPage/settings" type="button" class="text-light me-4 hover" style="font-size: 30px;"><i class="fa-solid fa-gear"></i></a> 
                  <button on:click={logOut} class="btn btn-outline-light me-2">Log out</button>
              {/if}
            </div>
        </div>
    </div>
</nav>

<style>
  .background {
    background: #021D47;
  }  

  .signUp {
    background-color: #71bcd5;
    transition: 300ms;
  }

  .signUp:hover {
    background-color: #618bba;
  }

  .hover:hover {
    animation: spin 0.8s ease-in-out infinite;
    animation-iteration-count: 1;
  }

  @keyframes spin { 
    0% {
      transform:rotate(0deg); 
    }
    100% { 
        transform:rotate(360deg); 
    } 
}
</style>
