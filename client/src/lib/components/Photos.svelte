<script>
  import SettingsController from "./../SettingsController"  

  let settings = new SettingsController()
  let colorTheme = settings.getJson().colorTheme
</script>

<div class="container {colorTheme == "Light" ? 'bg-white t-black' :  (colorTheme == "Dark" ? 'bg-dark t-white' : "bg-black t-yellow")}">
  <h1 class="text-justify m-4 mb-4 text-center">GIF News</h1>

  <hr>

  <div class="row">
    <div class="col-md-7 p-5 ">
      <h2>The Rise of Donuts</h2>
      <p class="lead">
        Glazed, powdered and jelly-filled donuts are timeless, but the
        industry’s come a long way from offering just the classics. Today,
        artisanal bakeries are attracting massive crowds with innovative flavor
        profiles (like brown butter hazelnut), unexpected add-ons and hybrid
        creations. But when—and how—did the bakery donut become so cool?
      </p>
      <p class="lead">
        “The donut has always been an affordable indulgence for Americans, but
        over the past 10 years, it’s become much more premiumized into
        higher-quality and more inventive offerings,” says Darren Tristano,
        president of the restaurant industry research firm Technomic. “You could
        say the donut has become a canvas for innovation. We’re really seeing a
        donut renaissance.”
      </p>
    </div>
    <div class="col-md-5">
      <img
        src="./../images/donut.webp"
        alt="An animated donut"
        width="500"
        height="500"
        style="object-fit: cover;"
      />
    </div>
  </div>

  <hr>

  <div class="row">
    <div class="col-md-5">
      <img
        src="./../images/plant.webp"
        alt="A cute plant"
        width="500"
        height="500"
        style="object-fit: cover;"
      />
    </div>
    <div class="col-md-7 p-5">
      <h2>Protect the Trees we have!</h2>
      <p class="lead">
        Between a death and a burial was hardly the best time to show up in a
        remote village in Madagascar to make a pitch for forest protection. Bad
        timing, however, turned out to be the easy problem. This forest was the
        first one that botanist Armand Randrianasolo had tried to protect. He’s
        the first native of Madagascar to become a Ph.D. taxonomist at Missouri
        Botanical Garden, or MBG, in St. Louis. So he was picked to join a 2002
        scouting trip to choose a conservation site.
      </p>
      <p class="lead">
        Other groups had already come into the country and protected swaths of
        green, focusing on “big forests; big, big, big!” Randrianasolo says.
        Preferably forests with lots of big-eyed, fluffy lemurs to tug
        heartstrings elsewhere in the world.
      </p>
    </div>
  </div>

  <hr>

  <div class="row">
    <div class="col-md-7 p-5">
      <h2>The Influence of Loud Music on Health</h2>
      <p class="lead">
        Music and noise can be considered as a collection of vibrational events
        which may impinge upon the body and the mind. As such they can induce
        beneficial or harmful bodily and psychological reactions. Much
        contemporary music production and consumption, however, produces sensory
        saturation and/or overload with sounds being manipulated in terms of
        spectrum and dynamic range. Such manipulation is not harmful by
        definition, but the manipulations may increase the potential for harm.
        Much research has been devoted to the risk of auditory overstimulation,
        but the topic is still relevant as listening to music is a significant
        form of leisure noise exposure. Listening habits and attitudes toward
        loud music may even promote behaviors that could cause harm to
        listeners, both in a direct and indirect way.
      </p>
    </div>
    <div class="col-md-5">
      <img
        src="./../images/speaker.gif"
        alt="A speaker playing music"
        width="500"
        height="500"
        style="object-fit: cover;"
      />
    </div>
  </div>

  <hr>
</div>
