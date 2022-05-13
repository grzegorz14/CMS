<script>
    import SettingsController from "./../SettingsController"  

    let settings = new SettingsController()
    let slideObjects =  settings.stringToArray(settings.getJson().slides)
    let slides = []
    for(let i = 0; i < slideObjects.length; i += 4) {
        slides.push({ 
            "image": slideObjects[i],
            "header": slideObjects[i + 1],
            "content": slideObjects[i + 2],
            "transition": slideObjects[i + 3],
        })
    }
    let colorTheme = settings.getJson().colorTheme
</script>

<div id="myCarousel" class="carousel slide  " data-bs-ride="carousel">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-label="Slide 1" aria-current="true"></button>
        <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2" class=""></button>
        <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3" class=""></button>
        {#each slides as slide, i}
            <button type="button" data-bs-target="#myCarousel" data-bs-slide-to={3 + i} aria-label={"Slide " + (3 + i)} class=""></button>
        {/each}
    </div>
    <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="6000">
            <img src="./../images/fullMoon.jpg" alt="" width="100%" height="500" style="object-fit: cover;">

            <div class="container">
                <div class="carousel-caption text-center sliderColors {colorTheme == "Light" ? 't-white':  (colorTheme == "Dark" ? 't-white' : "t-yellow")}">
                    <h2>How the full moon affects your sleep?</h2>
                    <p>Many people have trouble falling asleep during the full moon phase...</p>
                </div>
            </div>
        </div>

        <div class="carousel-item" data-bs-interval="6000">
            <img src="./../images/airPollution.jpg" alt="" width="100%" height="500" style="object-fit: cover;">

            <div class="container">
                <div class="carousel-caption text-center sliderColors {colorTheme == "Light" ? 't-white':  (colorTheme == "Dark" ? 't-white' : "t-yellow")}">
                    <h2>How to fight with air pollution?</h2>
                    <p>High air pollution is one of the biggest problems of many...</p>
                </div>
            </div>
        </div>

        <div class="carousel-item" data-bs-interval="6000">
            <img src="./../images/shootingStars.jpg" alt="" width="100%" height="500" style="object-fit: cover;">

            <div class="container">
                <div class="carousel-caption text-center sliderColors {colorTheme == "Light" ? 't-white':  (colorTheme == "Dark" ? 't-white' : "t-yellow")}">
                    <h2>What "falling stars" really are?</h2>
                    <p>"Shooting stars" and "falling stars" are both names that describe meteors...</p>
                </div>
            </div>
        </div>

        {#each slides as slide}
            <div class="carousel-item" data-bs-interval={slide.transition * 1000}>
                <img src={slide.image} alt="" width="100%" height="500" style="object-fit: cover;">

                <div class="container">
                    <div class="carousel-caption text-center sliderColors {colorTheme == "Light" ? 't-white':  (colorTheme == "Dark" ? 't-white' : "t-yellow")}">
                        <h2>{slide.header}</h2>
                        <p>{slide.content}</p>
                    </div>
                </div>
            </div>
        {/each}
    </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Prev</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>

