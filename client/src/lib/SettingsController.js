import json from "./Settings.json"
var root = document.querySelector(':root');
var rootStyle = getComputedStyle(root);

class Settings {
    //Root styles edit functions
    getStyle(name) {
        return rootStyle.getPropertyValue(name)
    }
    setStyle(name, value) {
        root.style.setProperty(name, value);
    }

    //Main settings
    setPageThemes(layout, theme) {
        json.pageLayout = layout
        json.colorTheme = theme
        this.saveJson()
    }  
    setFontAttributes(size, family) {
        json.fontSize = size
        json.fontFamily = family
        this.setStyle("--font-size", size + "px")
        this.setStyle("--font-family", family)
        this.saveJson()
    }  

    //Menu settings
    setPageName(name) {
        json.pageName = name
        this.saveJson()
    } 
    setMenuVariant(variant) {
        json.menuVariant = variant
        this.saveJson()
    } 
    addLink(link){
        json.links.push(link)
        this.saveJson()
    }
    deleteLink(link){
        const indexToRemove = json.links.indexOf(link);
        if (indexToRemove > -1) {
            json.links.splice(indexToRemove, 1);
        }
        this.saveJson()
    }

    //Slider settings
    addSlide(image, header, content, transition) {
        json.slides.push({ image, header, content, transition })
        this.saveJson()
    }
    deleteSlide(header){
        for (let i = 0; i < json.slides.length; i++) {
            if (json.slides[i].header == header) {
                json.slides.splice(i, 1)
            }
        }
        this.saveJson()
    }

    //Article settings
    addArticle(header, content) {
        json.articles.push({ header, content })
        this.saveJson()
    }
    deleteArticle(header){
        for (let i = 0; i < json.articles.length; i++) {
            if (json.articles[i].header == header) {
                json.articles.splice(i, 1)
            }
        }
        this.saveJson()
    }

    //Gallery settings
    setGalleryParameters(display, size) {
        json.galleryDisplay = display
        json.imagesSize = size
        this.saveJson()
    }

    //saves settings in local storage
    saveJson() {
        localStorage.setItem("settingsJson", JSON.stringify(json))
    }

    //returns settings (or null) from local storage 
    getJson() {
        let settingsJson = localStorage.getItem("settingsJson")
        settingsJson = JSON.parse(settingsJson)
        // console.log("Settings JSON:")
        // console.log(settingsJson)
        return settingsJson
    }

    getSettings() {
        let response = await fetch("./getSettings", { method: "POST" })
        response = await response.text()
        let set = JSON.parse(response)
        console.log(set)
        return set
    }
}

export default Settings