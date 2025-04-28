<script>
  import logo from './assets/NewYorkTimes.svg';
</script>

<div id="logo">
    <!--
        The row in the header which includes the logo "New York Times"
    -->
    <div id="date"> 
        <!--
            The time of the current day
        -->
        <p id="day"></p> <!-- Populated in script.js -->
        <p>Today's Paper</p> <!-- Static label -->
    </div>
    <figure>
        <!--
            The logo "New York Time" in the center of the page
            Image source: wikipedia
            https://en.m.wikipedia.org/wiki/File:NewYorkTimes.svg
        -->
        <a href="https://www.nytimes.com/"><img src={logo} alt="NewYorkTimes"></a> <!-- Link to homepage -->
    </figure>
    <div id="trend"> 
        <!--
            The current trend (stock market)
        -->
        <p id="market"></p> <!-- Populated in script.js -->
    </div>
</div>

<style>
#logo {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1rem;
}
#date {
    display:flex;
    flex-direction: column;
    max-width: 20%;
    gap: 0.5rem;
    font-size: 0.85rem;
}
#logo img {
    height: 4rem;
    max-width: 100%;
}
#trend {
    width: 8rem;
    max-width: 12%;
}
</style>