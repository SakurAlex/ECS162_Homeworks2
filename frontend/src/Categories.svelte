<script>
  import arrow from './assets/arrow.svg';
</script>

<nav>
    <!--
        The navigation bar
    -->
    <ul>
        <!--
            Image source: veryicon
            https://www.veryicon.com/icons/system/zoomlion-linear-icon/drop-down-43.html
        -->
        <li>U.S. <img src={arrow} alt="arrow"></li> <!-- Dropdown icon -->
        <li>World <img src={arrow} alt="arrow"></li>
        <li>Business <img src={arrow} alt="arrow"></li>
        <li>Arts <img src={arrow} alt="arrow"></li>
        <li>Lifestyle <img src={arrow} alt="arrow"></li>
        <li>Opinion <img src={arrow} alt="arrow"></li>
    </ul>
    <div id="vline"></div> <!-- Vertical separator -->
    <ul> <!-- Right links -->
        <li>Audio <img src={arrow} alt="arrow"></li>
        <li>Games <img src={arrow} alt="arrow"></li>
        <li>Cooking <img src={arrow} alt="arrow"></li>
        <li>Wirecutter <img src={arrow} alt="arrow"></li>
        <li>The Athletic <img src={arrow} alt="arrow"></li>
    </ul>
</nav>

<style>
/* Flex layout for navigation: centered items with wrapping */
nav {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    padding: 0.75rem 1rem;
    border-bottom: 2px double grey; /* Double-lined bottom border */
}

/* Layout for each group of links */
nav ul {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem; /* Spacing between list items */
    list-style: none; /* Remove default bullets */
}

/* Style for each navigation item */
nav li {
    position: relative; /* For potential dropdown positioning */
    cursor: pointer; /* Pointer cursor on hover */
}

/* Size the dropdown arrow icon */
nav li img {
    width: 0.5rem;
}

/* Vertical line separator styling */
#vline {
    width: 1px;
    height: 1.2rem;
    background-color: rgb(175, 165, 165);
    margin: 1rem;
}
</style>