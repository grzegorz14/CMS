<script>
    import SettingsController from "./../SettingsController";

    let settings = new SettingsController()
    let json = settings.getJson()

    //selects options
    let layouts = [
        { value: "classic", content: "Classic - (slider, articles, GIFs)" },
        { value: "imageLover", content: "Image lover -  (slider, GIFs, articles)" },
        { value: "newsFirst", content: "News First - (articles, GIFs, slider)" },
        { value: "middleSlider", content: "Middle Slider -  (articles, slider, GIFs)" },
        { value: "gifsFan", content: "GIFs Fan - (GIFs, slider, articles)" },
        { value: "reverse", content: "Reverse - (GIFs, articles, slider)" }
    ]
    let colorThemes = [
        "Light",
        "Dark",
        "High Contrast"
    ]
    let fonts = [
        "Arial, Helvetica, sans-serif",
        "'Courier New', Courier, monospace",
        "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif",
        "'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif",
        "'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif"
    ]


    //inputs
    let pageLayoutInput = json.pageLayout
    let colorThemeInput = json.colorTheme
    let fontSizeInput = json.fontSize
    let fontFamilyInput = json.fontFamily
    let colorTheme = json.colorTheme

    async function setThemes() {
        let pageLayout = document.getElementById("pageLayout").value
        let colorTheme = document.getElementById("colorTheme").value
        await settings.updateSetting("pageLayout", pageLayout)
        await settings.updateSetting("colorTheme", colorTheme)
        window.location.reload()
    }

    async function applyFontSettings() {
        let fontSize = document.getElementById("fontSize").value
        let fontFamily = document.getElementById("fontFamily").value
        await settings.updateSetting("fontSize", fontSize)
        settings.setStyle("--font-size", fontSize)
        await settings.updateSetting("fontFamily", fontFamily)
        window.location.reload()
    }
    
    async function defaultSettings() {
        document.getElementById("pageLayout").value = "classic"
        document.getElementById("colorTheme").value = "Light"
        document.getElementById("fontSize").value = "17"
        document.getElementById("fontFamily").value = "Arial, Helvetica, sans-serif"
        await settings.updateSetting("pageLayout", "classic")
        await settings.updateSetting("colorTheme", "Light")
        await settings.updateSetting("fontSize", 17)
        await settings.updateSetting("fontFamily", "Arial, Helvetica, sans-serif")
        window.location.reload()
    }
</script>

<div class="d-flex flex-column justify-content-center {colorTheme == "Light" ? 'bg-white t-black':  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
    <p class="mainHeadline">Page settings</p>

    <hr>

    <p class="headline">Site themes</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-3 text">Page layout</div>
            <select id="pageLayout" class="form-select form-select-lg col">
                {#each layouts as layout}
                    {#if layout.value == pageLayoutInput} 
                        <option selected value={layout.value}>{layout.content}</option>
                    {:else}
                        <option value={layout.value}>{layout.content}</option>
                    {/if}
                {/each}
            </select>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-3 text">Color theme</div>
            <select id="colorTheme" class="form-select form-select-lg col">
                {#each colorThemes as theme}
                    {#if theme == colorThemeInput} 
                        <option selected>{theme}</option>
                    {:else}
                        <option>{theme}</option>
                    {/if}
                {/each}
            </select>
        </div>
        <div class="row justify-content-end mt-3">
            <button on:click={setThemes} class="btn btn-primary me-5" style="width:fit-content;">Set themes</button>
        </div>
        <!-- <div class="colorBox">
            <div class="box">
                <p >Precoded Color Themes</p>
                <div class="colorBox">
                    <button class="preColorBtn d-flex" >
                        <div class="subColorBtn" style="background-color: red;"></div>
                        <div class="subColorBtn" style="background-color: blue;"></div>
                        <div class="subColorBtn" style="background-color: green;"></div>
                    </button>
                    <button class="preColorBtn d-flex" >
                        <div class="subColorBtn" style="background-color: magenta;"></div>
                        <div class="subColorBtn" style="background-color: yellow;"></div>
                        <div class="subColorBtn" style="background-color: cyan;"></div>
                        <div class="subColorBtn" style="background-color: black;"></div>
                    </button>
                    <button class="preColorBtn d-flex" >
                        <div class="subColorBtn" style="background-color: purple;"></div>
                        <div class="subColorBtn" style="background-color: brown;"></div>
                        <div class="subColorBtn" style="background-color: olive;"></div>
                        <div class="subColorBtn" style="background-color: aquamarine;"></div>
                        <div class="subColorBtn" style="background-color: wheat;"></div>
                        
                    </button>
    
                </div>
            </div>
            <div class="box">
                <p >Background Color</p>
                <div class="colorBox">
                    <button class="colorBtn" style="background-color: red;"></button>
                    <button class="colorBtn" style="background-color: blue;"></button>
                    <button class="colorBtn" style="background-color: green;"></button>
                    <input type="color">
                </div>
            </div>
            <div class="box">
                <p>Nav Bar Color</p>
                <div class="colorBox">
                    <button class="colorBtn" style="background-color: red;"></button>
                    <button class="colorBtn" style="background-color: blue;"></button>
                    <button class="colorBtn" style="background-color: green;"></button>
                    <input type="color">
                </div>
            </div>
        </div> -->

        <hr>

        <p class="headline">Font settings</p>
        <div class="row align-items-center m-2">
            <div class="col-3 text">Font size</div>
            <div class="col d-flex flex-row align-items-center ms-1">
                <input id="fontSize" type="number" onKeyDown="return false" min="15" max="25" value={fontSizeInput} class="form-control form-control-lg" style="width: 100px;"/>
                <p class="ms-1 mb-0 text">px</p>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-3 text">Font family</div>
            <select id="fontFamily" class="form-select form-select-lg col ms-3">
                {#each fonts as font}
                    {#if font == fontFamilyInput} 
                        <option selected style={"font-family: " + font}>{font}</option>
                    {:else}
                        <option style={"font-family: " + font}>{font}</option>
                    {/if}
                {/each}
            </select>
        </div>
        <div class="row justify-content-end mt-3">
            <button on:click={applyFontSettings} class="btn btn-primary me-5" style="width:fit-content;">Apply changes</button>
        </div>

        <hr>

        <p class="headline">Set by default</p>
        <button on:click={defaultSettings} class="btn btn-danger m-2 ms-3" >Reset main settings</button>
    </div>
</div>

<!-- <div class="d-flex flex-column justify-content-center">
    <div class="d-flex justify-content-start">
        <div class="p-1">
            <button class="fontBox m-1" style="font-family: 'Courier New', Courier, monospace;">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sint officia facere cupiditate adipisci quas placeat culpa quod quos. Id nemo ea accusantium, nisi magnam voluptatibus porro error a aut et.</button>
            <button class="fontBox m-1" style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sint officia facere cupiditate adipisci quas placeat culpa quod quos. Id nemo ea accusantium, nisi magnam voluptatibus porro error a aut et.</button>
        </div>
        <div class="p-1">
            <button class="fontBox m-1" style="font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sint officia facere cupiditate adipisci quas placeat culpa quod quos. Id nemo ea accusantium, nisi magnam voluptatibus porro error a aut et.</button>
            <button class="fontBox m-1" style="font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sint officia facere cupiditate adipisci quas placeat culpa quod quos. Id nemo ea accusantium, nisi magnam voluptatibus porro error a aut et.</button>
            
        </div>
        <div class="p-1">
            <button class="fontBox m-1">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sint officia facere cupiditate adipisci quas placeat culpa quod quos. Id nemo ea accusantium, nisi magnam voluptatibus porro error a aut et.</button>
        </div>
    </div>
</div> -->