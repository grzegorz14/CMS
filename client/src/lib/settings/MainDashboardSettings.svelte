<script>
    
</script>

<div class="d-flex flex-column justify-content-center">
    <p class="mainHeadline">Main Dashboard Settings</p>
    <hr>
    <p class="headline">Site Theme</p>
    <div class="colorBox"><!--Fajna nazwa klasy :)  (tylko tymczasowa)-->
        <button style="width: 100px;">Jakis ukłąd strony obrazek w butonie czy cos</button>
        <button style="width: 100px;">Jakis ukłąd strony obrazek w butonie czy cos</button>
        <button style="width: 100px;">Jakis ukłąd strony obrazek w butonie czy cos</button>
    </div>
        
    <hr>
    <p class="headline">Font Settings</p>
        <p style="font-weight: bold;">Font Size</p>
        <div class="d-flex pr-1">
            <input  style="width: 100px;" type="number">
            <p>Automatyczny pokaz rozmiaru fonta :) alob że te fonty na dole się zmieniają też spoko by było</p>
        </div>
        <hr>
        <p style="font-weight: bold;">Font</p>
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
        
        
    <hr>
    <p class="headline">Color Theme</p>
    <div class="colorBox">
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
    </div>
    
    <hr>
    <p class="headline">Slider</p>
    <p>Zdjęcia nw ??</p>
    
    <hr>
    <p class="headline">Articles Section</p>
    <p>Pewnie wybór tekstu i układu ??</p>
    <hr>
    <p class="headline">To takie coś na dole</p>
    <p>dodawanie nowych i te gify obok</p>
    <hr>
</div>


<style>
    .mainHeadline{
        font-size: 50px;
        font-weight: bolder;
    }
    .headline{
        font-size: 30px;
        font-weight: bold;
    }

    p{
        font-size: 20px;
    }
    .preColorBtn{
        height: 25px;
        margin-right: 5px;
        margin-top: -10px;
        /* xd, musiałem usunąć i zobaczyć */
        border: 0px;
        background-color: white;
        /* ----- */
    }
    .subColorBtn{
        width: 25px;
        height: 25px;
    }
    .colorBtn{
        width: 25px;
        height: 25px;
        border: 1px solid black;
        border-radius: 50%;
        margin-right: 5px;
        margin-top: -10px;
    }
    .colorBox{
        display: flex;
        flex-direction: row;
        
    }
    .box{
        margin-right: 10px;
        padding: 10px;
        border: 1px solid black;
    }
    .fontBox{
        width: 250px;
        
        background-color:white ;
    }

</style>