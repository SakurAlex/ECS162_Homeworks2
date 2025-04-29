<script>
    import logo from './assets/NewYorkTimes.svg';
    
    //Keep current date on the top left corner
    const date = new Date();
    const currentDate = date.toLocaleString("en-US", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });

    //Trend data on the top right corner
    const data = [
        {
            name: "Sleep",
            value: "-0.19%↓",
            color: "red"
        },
        {
            name: "Study",
            value: "+0.31%↑",
            color: "green"
        },
        {
            name: "Social",
            value: "-0.45%↓",
            color: "red"
        }
    ];

    let index = 0;
    let currentTrend = data[0];

    function updateMarket() {
        index = (index + 1) % 3;
        currentTrend = data[index];
    }

    setInterval(updateMarket, 1500);
</script>

<div id="logo">
    <!--
        The row in the header which includes the logo "New York Times"
    -->
    <div id="date"> 
        <!--
            The time of the current day
        -->
        <p>{currentDate}</p>
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
        <p>{currentTrend.name} <span style="color: {currentTrend.color};">{currentTrend.value}</span></p>
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