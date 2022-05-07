<script>
    function applyFontSettings() {
        let fontSize = document.getElementById("fontSize").value
        let fontFamily = document.getElementById("fontFamily").value
        //set font size and font family
    }

    function setThemes() {
        let pageLayout = document.getElementById("pageLayout").value
        let colorTheme = document.getElementById("colorTheme").value
        //set page theme and color theme
    }
    
    function defaultSettings() {
        //set all settings in this page by default
    }
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">Main settings</p>

    <hr>

    <p class="headline">Site themes</p>
    <div class="w-50">
        <div class="row align-items-center m-2">
            <div class="col-3 text">Page layout</div>
            <select id="pageLayout" class="form-select form-select-lg col">
                <option value="classic" selected>Classic - (slider, articles, GIFs)</option>
                <option value="imageLover">Image lover -  (slider, GIFs, articles)</option>
                <option value="newsFirst">News First - (articles, GIFs, slider)</option>
                <option value="middleSlider">Middle Slider -  (articles, slider, GIFs)</option>
                <option value="gifsFan">GIFs Fan - (GIFs, slider, articles)</option>
                <option value="reverse">Reverse - (GIFs, articles, slider)</option>
            </select>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-3 text">Color theme</div>
            <select id="colorTheme" class="form-select form-select-lg col">
                <option selected>Light</option>
                <option>Dark</option>
                <option>High Contrast</option>
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
                <input id="fontSize" type="number" min="10" max="30" value="20" class="form-control form-control-lg" style="width: 80px;"/>
                <p class="ms-1 mb-0 text">px</p>
            </div>
        </div>
        <div class="row align-items-center m-2">
            <div class="col-3 text">Font family</div>
            <select id="fontFamily" class="form-select form-select-lg col ms-3">
                <option style="font-family: 'Courier New', Courier, monospace;" selected>Courier New, Courier, monospace</option>
                <option style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;">Franklin Gothic Medium, Arial Narrow, Arial, sans-serif</option>
                <option style="font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Lucida Sans, Lucida Sans Regular, Lucida Grande, Lucida Sans Unicode, Geneva, Verdana, sans-serife</option>
                <option style="font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;">Trebuchet MS, Lucida Sans Unicode, Lucida Grande, Lucida Sans, Arial, sans-serife</option>
                <option>Default font family</option>
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
