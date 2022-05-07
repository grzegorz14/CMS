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
    setFontAttributes(size, family) {
        json.fontSize = size
        json.fontFamily = family
        this.setStyle("--font-size", size + "px")
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
        console.log("Settings JSON:")
        console.log(settingsJson)
        return settingsJson
    }
}

export default Settings