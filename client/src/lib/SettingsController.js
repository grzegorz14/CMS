import json from "./Settings.json"
var root = document.querySelector(':root');
var rootStyle = getComputedStyle(root);

class Settings {
    //String array to array 
    stringToArray(string) {
        if (string == "[]") {
            return []
        }

        string = string.split(",")
        string[0] = string[0].substring(1)
        string[string.length - 1] = string[string.length - 1].substring(0, string[string.length - 1].length - 1)

        string.forEach((x, i) => {
            string[i] = string[i].includes('"') ? string[i].replaceAll('"', "").trim() : string[i].replaceAll("'", "").trim()
        })

        return string
    }

    //Root styles edit functions
    getStyle(name) {
        return rootStyle.getPropertyValue(name)
    }
    setStyle(name, value) {
        root.style.setProperty(name, value);
    }

    //Menu settings
    async addLink(link){
        let array = await this.getSetting("links")
        array = this.stringToArray(array)
        array.push(link)
        await this.updateSetting("links", array)
    }
    async deleteLink(link){
        let array = await this.getSetting("links")
        array = this.stringToArray(array)
        const indexToRemove = array.indexOf(link);
        if (indexToRemove > -1) {
            array.splice(indexToRemove, 1);
        }
        await this.updateSetting("links", array)
    }

    //Slider settings
    async addSlide(image, header, content, transition) {
        let array = await this.getSetting("slides")
        array = this.stringToArray(array)
        array.push(image)
        array.push(header)
        array.push(content)
        array.push(transition)
        await this.updateSetting("slides", array)

        // let array = await this.getSetting("slides")
        // console.log(array)
        // array = JSON.parse(array)
        // console.log(array)
        // array.push({ image, header, content, transition })
        // await this.updateSetting("slides", array)
        
    }
    async deleteSlide(header){
        let array = await this.getSetting("slides")
        array = this.stringToArray(array)
        console.log(array)
        if (array.length <= 4) {
            array = []
        }
        else {
            for (let i = 0; i < array.length - 3; i++) {
                if (array[i + 1] == header) {
                    array.splice(i, 4)
                }
            }
        }
        console.log(array)
        await this.updateSetting("slides", array)
        //await this.updateSetting("slides", []) 
    }

    //Article settings
    async addArticle(header, content) {
        let array = await this.getSetting("articles")
        array = this.stringToArray(array)
        array.push(header)
        array.push(content)
        await this.updateSetting("articles", array)
    }
    async deleteArticle(header){
        let array = await this.getSetting("articles")
        array = this.stringToArray(array)
        if (array.length == 2) {
            array = []
        }
        else {
            for (let i = 0; i < array.length - 1; i++) {
                if (array[i] == header) {
                    array.splice(i, 2)
                }
            }
        }
        await this.updateSetting("articles", array)
    }

    //Gallery settings
    setGalleryParameters(display, size) {
        json.galleryDisplay = display
        json.imagesSize = size
        this.saveJson()
    }

    //saves/updates settings in local storage
    saveJson() {
        localStorage.setItem("settingsJson", JSON.stringify(json))
    }

    updateJson(jsonArray) {
        let newJson = { 
            "pageName": jsonArray[0],
            "pageLayout": jsonArray[1],
            "colorTheme": jsonArray[2],
            "fontSize": jsonArray[3],
            "fontFamily": jsonArray[4],
            "menuVariant": jsonArray[5],
            "galleryDisplay": jsonArray[6],
            "imagesSize": jsonArray[7],
            "links": jsonArray[8],
            "slides": jsonArray[9],
            "articles": jsonArray[10],
        }
        localStorage.setItem("settingsJson", JSON.stringify(newJson))
    }

    //returns settings (or null) from local storage 
    getJson() {
        let settingsJson = localStorage.getItem("settingsJson")
        settingsJson = JSON.parse(settingsJson)
        // console.log("Settings JSON:")
        // console.log(settingsJson)
        return settingsJson
    }

    //gets single Settings from json in local storage
    async getSetting(settingName) {
        let settings = await this.getSettings()
        let index = this.getArrayIndex(settingName)
        return settings[index]
    }

    //get/update settings in database.sqlite
    async getSettings() {
        let response = await fetch("./getSettings", { method: "POST" })
        response = await response.text()
        response = JSON.parse(response)
        return response[0]
    }

    async getSettingsJson() {
        let settingsArray = await this.getSettings()
        let settingsJson = { 
            "pageName": settingsArray[0],
            "pageLayout": settingsArray[1],
            "colorTheme": settingsArray[2],
            "fontSize": settingsArray[3],
            "fontFamily": settingsArray[4],
            "menuVariant": settingsArray[5],
            "galleryDisplay": settingsArray[6],
            "imagesSize": settingsArray[7],
            "links": settingsArray[8],
            "slides": settingsArray[9],
            "articles": settingsArray[10],
        }
        return settingsJson 
    }

    async updateSettings(newJson) {
        let response = await fetch("./updateSettings", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                "newJson": JSON.stringify(newJson)
            }),
        })
        response = await response.text()
        newJson = await this.getSettings()
        this.updateJson(newJson)
    }

    async updateSetting(settingName, value) {
        let settings = await this.getSettings()
        let index = this.getArrayIndex(settingName)
        settings[index] = value
        await this.updateSettings(settings)
    }

    getArrayIndex(field) {
        switch(field) {
            case "pageName": 
                return 0
            case "pageLayout": 
                return 1 
            case "colorTheme": 
                return 2
            case "fontSize": 
                return 3
            case "fontFamily": 
                return 4
            case "menuVariant": 
                return 5
            case "galleryDisplay": 
                return 6
            case "imagesSize": 
                return 7
            case "links": 
                return 8
            case "slides": 
                return 9
            case "articles": 
                return 10
            default:
                console.log("error!")
                return -1  
        }
    }
}

export default Settings