<script>
    import MainDashboardSettings from "./MainDashboardSettings.svelte";
</script>

<div class="wrapper">
    <!-- Sidebar  -->
    <nav id="sidebar">
        <div class="sidebar-header">
            <h3>CMS Settings</h3>
        </div>

        <ul class="list-unstyled components">
            
            <li>
                <a href="#pageSubmenu" >Main Dashboard</a>
                
            </li>
            
            <li>
                <a href="#pageSubmenu" >Articles</a>
                
            </li>
            <li>
                <a href="#pageSubmenu" >Gallery</a>
                
            </li>
            
            <li>
                <a href="#pageSubmenu" >Users</a>
                
            </li>
        </ul>

        
    </nav>

    <!-- Page Content  -->
    <div id="content">
        <MainDashboardSettings />    
    </div>
</div>

<style>
   /*
    DEMO STYLE
*/




p {
    font-family: 'Poppins', sans-serif;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1.7em;
    color: #999;
}

a,
a:hover,
a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
}

.wrapper {
    display: flex;
    width: 100%;
    align-items: stretch;
}

#sidebar {
    min-width: 250px;
    max-width: 250px;
    background: #00557c;
    color: #fff;
    transition: all 0.3s;
}

#sidebar .sidebar-header {
    padding: 20px;
    background: #004261;
}

#sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid #47748b;
}

#sidebar ul li a {
    padding: 10px;
    font-size: 1.1em;
    display: block;
}

#sidebar ul li a:hover {
    color: #00557c;
    background: #fff;
}

ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #00557c;
}

#content {
    width: 100%;
    padding: 20px;
    min-height: 100vh;
    transition: all 0.3s;
}

</style>
