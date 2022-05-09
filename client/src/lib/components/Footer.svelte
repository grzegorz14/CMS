<script>
    import SettingsController from "./../SettingsController"  
    let settings = new SettingsController()
    let colorTheme = settings.getJson().colorTheme
</script>

<footer class="container {colorTheme == "Light" ? 'bg-white t-black' :  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black text-yellow")}">
    <p class="float-end"><a href={"#"}>Back to home</a></p>
    <p>© 2022–2022 Grzegorz Szewczyk & Mikołaj Zając · <a href={"#"}>Privacy</a> · <a href={"#"}>Terms</a></p>
</footer>