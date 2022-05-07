<script>
  let userType = getUserType()

  async function getUserType() {
    let response = await fetch("./getUserType", { method: "POST" })
    response = await response.text()
    console.log("User type: " + response)
    userType = response
  }

  async function logOut() {
    let response = await fetch("./logOut", { method: "POST" })
    response = await response.text()
    console.log("User type: " + response)
    userType = response
  }
</script>

<nav class="navbar navbar-expand-md navbar-dark navbarColors ">
    <div class="container-fluid">
        <a class="navbar-brand ms-3" style="font-size: 150%;" href="#/">CMS</a>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav ms-1 me-auto mb-2 mb-md-0">
                <li class="nav-item me-1">
                    <a class="nav-link active" style="font-size: 120%;" aria-current="page" href="#/">Home</a>
                </li>
                <li class="nav-item me-1">
                    <a class="nav-link" style="font-size: 120%;" href="#/subPage/article">Article</a>
                </li>
                <li class="nav-item me-1">
                    <a class="nav-link" style="font-size: 120%;" href="#/subPage/gallery">Gallery</a>
                </li>
            </ul>
            <div class="text-end me-2 d-flex align-items-center">
              {#if userType == "none"}
                  <a href="#/logIn" type="button" class="btn btn-outline-light me-2">Log in</a>
                  <a href="#/signUp" type="button" class="btn signUp text-light">Sign up</a>
              {:else}
                  <a href="#/subPage/settings" type="button" class="text-light me-4 hover d-flex align-content-center" style="font-size: 30px;"><i class="fa-solid fa-gear"></i></a> 
                  <button on:click={logOut} class="btn btn-outline-light me-2">Log out</button>
              {/if}
            </div>
        </div>
    </div>
</nav>
