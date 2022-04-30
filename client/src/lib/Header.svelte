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
            <div class="text-end me-2">
                <a href="#/logIn" type="button" class="btn btn-outline-light me-2">Log in</a>
                <a href="#/signUp" type="button" class="btn signUp">Sign up</a>
            </div>
        </div>
    </div>
</nav>

<style>
  .background {
    background: #011936;
  }  

  .signUp {
    background-color: #71bcd5;
    transition: 300ms;
  }

  .signUp:hover {
    background-color: #b5dbe8;
  }
</style>
