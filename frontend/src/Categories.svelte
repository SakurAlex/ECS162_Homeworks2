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
nav {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    padding: 0.75rem 1rem;
    border-bottom: 2px double grey;
}
nav ul {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    list-style: none;
}
nav li {
    position: relative;
    cursor: pointer;
}
nav li img {
    width: 0.5rem;
}
#vline {
    width: 1px;
    height: 1.2rem;
    background-color: rgb(175, 165, 165);
    margin: 1rem;
}
</style>