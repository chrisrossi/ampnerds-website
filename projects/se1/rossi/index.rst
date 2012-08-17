==========
SE-1 ROSSI
==========

- The schematic: :download:`JSCHEM file <se1_rossi.jsch>`,
  :download:`PDF file <se1_rossi.pdf>`
- Audio recording: :download:`MP3 file <se1_rossi.mp3>`

Build notes
-----------

Assembly
~~~~~~~~

I have to say that assembly was fairly straightforward and problem free.  Since
this is the first time I've ever fabricated, much less designed, a turret board,
I have to say that I'm pretty happy with how it turned out.  That said, the 
spacing on some of the components was pretty long--mostly on things that spanned
most of the width of the board: R22, R24, and R26, for example, barely had 
enough lead to span the turret spacing.  A second revision of the layout would
likely look for some ways to use a little less space, in general.  Having a lot
of room to maneuver inside the chassis is pretty nice, though.

Initial Test
~~~~~~~~~~~~

My first test of the amp was done without any of the tremolo or tone circuitry
having been wired up yet, so none of that was in play.  The power transformer
actually has 115V and 125V taps for the primary, where the 115V tap is going to
give you a little higher voltage on the tubes.  I started out using the 115V
primary tap with just a jumper for the sag resistor, giving the highest
voltages possible with these components.  I also had not yet hooked up any
negative feedback, so the maximum amount of gain was on tap.  Initial
impression was that it was really darn loud for a little single ended amp, and
very raunchy.  With the volume dimed, extreme amounts of distortion were
available--approaching square wave territory.  Pretty fun to play around but
not my usual sound.

Tremolo
~~~~~~~

The tremolo turned out to be interesting.  My initial concerns were: I got no
tremolo for most of the depth pot range, and then it would cut on suddenly
towards the very top and be very strong.  I also got some scratchiness when
rotating the depth pot that is usually a sign that you're putting DC on a pot
which you're generally not supposed to do.  After examining the Dearmond
schematic that I ripped off the tremolo from, I saw that 10 there was DC on it.
It's basically sitting right in the cathode circuit of the tremolo output
triode.  So it's going to crackle when you turn it.  Oh well.  The other thing
I noticed is that the pot is specified as a 350K CCW.  Had pretty much glossed 
over the CCW.  I thought it might mean reverse log, but I wasn't sure, and 
reverse log isn't super common.  As it turns out, the taper makes a pretty big
difference, and they really did mean for it to be a reverse log taper.  I ended
up turning my regular audio taper 500K depth pot into a reverse taper pot by
just wiring it in reverse.  The downside is now that rotating the depth knob
counter-clockwise gives you more tremolo and rotating it clockwise gives you
less, which kind of makes my brain hurt.  But you get a much broader usable
range with the pot and can easily dial in subtle tremolo effects, which was
hard to do with the pot wired in the more intuitive way.  The switch seems to
be totally superfluous given that the tremolo has no noticeable effect with the
depth turned all the way down.

The next thing I noticed was that the tremolo was causing the second gain stage
to be biased very cold, even when the tremolo was not in operation.  This
would, of course, lower the gain of that stage (not necessarily a bad thing,
given how hot the amp is), as well as affect the tone.  Where typically the
cathode would be a little over 1 volt, the cathode was actually at closer to
2.3V, which makes a fairly big difference.  At this point I decided to go ahead
and try the Vibrochamp wiring, since it wasn't too far off from what I had.  I
managed to scrounge a 25KA pot to replace the depth pot, still wired backwards,
since I still actually ought to have had a reverse taper pot there.  With the
rewire, the bias on the second stage went right back to normal, making the whole
amp sound a little nicer to my ears.  So I left it that way, as noted on my 
schematic.  A rev2 of this project would use this wiring for the tremolo.

Dialing Things Back
~~~~~~~~~~~~~~~~~~~

The next thing I did was add the sag resistor.  A 200 ohm resistor for R3 made
a pretty big difference in overall feel of the amp.  While still capable of a
decent amount of distortion, the distortion available sounded smoother to my 
ears, where it had sounded harsher before.  I also added negative feedback and
found that the Vibrochamp parts worked pretty well to my ears.  I then tried
the 125V primary on the power transformer, which knocked voltages down a little
further.  This didn't have near as dramatic an effect on the sound--I'm not
sure I could really tell much difference at all, but it sounded pretty nice so
I didn't change it back.  Overall, voltage on the plate of the power tube went
from about 350V or so to closer to 275V.  To my ears, the lower voltage and
increased sag make it work much better as an instrument amplifier.  I didn't
experiment with changing the voltages on the power tube and preamp tubes
independently of each other, to see if the tone change I liked was coming more
from the preamp or more from the power amp.  I just got to a state where I
liked what I heard and stopped messing with it.

Tone Control
~~~~~~~~~~~~

Although I tend to keep the tone control turned pretty far down--around 9 or 10 
o'clock typically--I found that having the tone control still sounds a lot
better than not having it.  Without the tone control, the whole thing sounds way
too dark to me.  Even just a little bit of brightness from the tone control goes
a long way.  

I did experiment with putting a tilt tone control (aka Big Muff Pi tone control)
in there.  I thought I would probably prefer the tilt control over the stock 
control, based on some breadboard experimentation I had done.  In the context of
that amp, though, I found the tilt control to be kind of dead sounding overall.
I promptly changed back to the stock tone control and haven't messed with it 
since.

6GM5 Tube
~~~~~~~~~

I'm really digging the 6GM5 tube.  It is a 9 pin version of a 7591A used in 
several Ampegs in the 60s.  This tube isn't really designed for class A so 
ostensibly I'm getting more distortion than if I was using a tube designed to
be biased into class A.  But this is a guitar amp we're talking about, and we
don't necessarily shy away from distortion.  I think it sounds great, albeit
there isn't a ton of really clean headroom.

Conclusions
~~~~~~~~~~~

I'm very happy with how this has turned out.  This is the most from scratch that
I've built something so far, and it is certainly the most well put together amp
I've managed to pull off to date.  I haven't done as much experimenting with it
as I thought I might.  I basically tweaked it until it sounded good--as soon as
I got to a very happy place I just stopped, as I had a hard time imagining it
sounding any better.  That said, there are still plenty of easily reversible
mods that could be tried out on this thing, so the Amp Nerds may yet have a
hack night ahead of them where we change things around just to hear what those
changes might sound like.  Stay tuned.  
