<script>
	import Comments from './../components/Comments.svelte';
</script>

<div class="d-flex flex-column justify-content-center " style="margin-left: 30%; margin-right: 30%; padding:1%;">
    <p class="date">NEWS | November 10, 2021</p>
    <p class="mainHeadline">An Almost Total Lunar Eclipse</p>
    <p class="by">By Molly Wasser and Ernie Wright</p>

    <p class="">On November 19, 2021 (late evening of the 18th in some time zones), the Moon passes into the shadow of the Earth, creating a partial lunar eclipse so deep that it can reasonably be called almost total. Credit: NASA's Scientific Visualization Studio</p>
    <hr>
    <p class="headline">What is an “almost total” lunar eclipse?</p>
    <p class="">A lunar eclipse occurs when the Sun, Earth, and Moon align so that the Moon passes into Earth’s shadow. In a total lunar eclipse, the entire Moon falls within the darkest part of Earth’s shadow, called the umbra. In this eclipse, up to 99.1% of the Moon’s disk will be within Earth’s umbra.</p>
    <hr>
    <p class="headline">How can I observe the eclipse?</p>
    <p class="">The best viewing will be right around the peak of the eclipse, on November 19th at 9:03 UTC/4:03 AM EST/1:03 AM PST. This part of the eclipse is visible in all of North America, as well as large parts of South America, Polynesia, eastern Australia, and northeastern Asia.</p>

    <p class="">
        A world map showing where the eclipse is visible at the time of greatest eclipse. Earlier parts of the eclipse are visible farther east, while later times are visible farther west.
        A world map showing where the eclipse is visible at the time of greatest eclipse. Earlier parts of the eclipse are visible farther east, while later times are visible farther west. Credit: NASA's Scientific Visualization Studio
    </p>
    <hr>
    <p class="headline">Is this the longest lunar eclipse of the century?</p>
    <p class="">
        Kind of. It’s actually the longest partial lunar eclipse in a millennium, clocking in at 3 hours, 28 minutes and 23 seconds. There hasn’t been a longer partial lunar eclipse since February 18, 1440 (3 hours, 28 minutes, 46 seconds) and it will remain the longest partial lunar eclipse for 648 years until February 8, 2669 (3 hours, 30 minutes, and 2 seconds). There will be a longertotal lunar eclipse on November 8, 2022.
    </p>
        <p>- Partial lunar eclipse of February 18, 1440: 3:28:46</p> 
        <p>- Partial lunar eclipse of November 18/19, 2021: 3:28:23</p>
        <p>- Partial lunar eclipse of February 8, 2669, 3:30:02</p>
    <hr>
    <p class="headline">Why is this eclipse so long?</p>
    <p class="">
        This is a long eclipse for two main reasons: 1) The Moon’s orbital speed and 2) The near-totality of the eclipse.

        First, the Moon’s orbit around the Earth is not a perfect circle, and the Earth is off-center within the orbit so sometimes the Moon is closer to the Earth and sometimes it is farther away. This change in distance impacts the Moon’s orbital speed. Closer to the Earth, the Moon moves faster, while further away, it travels more slowly. Right now, the Moon is near its farthest point in its orbit around the Earth and thus, moves slowly through Earth’s shadow.

        Second, since this eclipse is almost-total, the Moon spends a longer amount of time in the Earth’s umbra than it would in a ‘more-partial’ eclipse.
    </p>
    <hr>
    <p class="headline">What else can I see tonight?</p>
    <p class="">
        During the eclipse, the Moon moves through the western part of the constellation Taurus. The Pleiades star cluster is to the upper right, and the Hyades cluster ― including the bright star Aldebaran, eye of the bull ― is in the lower left. Here are some more skywatching tips for the month of November.
    </p>
    <hr>
</div>

<div class="commentSecton">
    <div class="in">
        <div class="c">Comments</div>
        <Comments />
    </div>
</div>

<style>
    .date{
        padding-top: 20px;
        font-size: 15px;
        font-weight: bold;
    }
    .mainHeadline{
        margin-top: -20px;
        margin-bottom: -10px;
        font-size: 50px;
        font-weight: bolder;
    }
    .headline{
        font-size: 30px;
        font-weight: bold;
    }
    .by{
        font-size: 20px;
        font-weight: bolder;
        text-align: center;
        padding-bottom: 10px;
    }
    p{
        font-size: 20px;
    }
    
    .commentSecton{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        background-color: #DEB1AC;
        width: 100%;
        padding:20px;
        text-align: left;
        
    }
    .in{
        display: flex;
        flex-direction: column;
        
        width: 40%;
        
    }
    .c{
        float: left;
        text-align: left;
        font-size: 30px;
        font-weight: bold;
        border-bottom: 1px solid gray;
    }

</style>