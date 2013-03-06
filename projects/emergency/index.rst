=============
Emergency Amp
=============

Quick Hits
----------

+ Schematic (:download:`PDF file <emergency.pdf>`, 
  :download:`JSCHEM file <emergency.jsch>`)

Beyond this point will be TL;DR for most people.  Fair warning.

Background
----------

This amp started out with a piece old radio equipment I bought off of Ebay 
because I liked the chassis.  The chassis came with a Dynamo label on it that 
just said "FOR EMERGENCY USE ONLY".  So I call it my emergency amp.  Later I 
found `this old magazine cover showing the same chassis
<http://www.rfcafe.com/references/popular-electronics/images/dec-1957-popular-electronics-cover.jpg>`_,
so I'm guessing this was a popular DIY chassis back in the day.  After drilling
any new holes, I took the chassis to `Tech Shop <http://www.techshop.ws/>`_ to
sandblast and powder coat it, which made it look pretty spiffy.  Not sure
exactly what the original circuit was, but it had an LRC tuning circuit, a giant
power transformer and a voltage doubler running a pair of 6JG6 power tubes at
something like 900V.  It also had some kind of preamp tube as a phase inverter,
but I don't remember which it was at the moment.  No output transformer since
it wasn't driving a speaker.

I started by ripping everything out of the chassis and then spending some time
thinking about what I could build in there.  The 6JG6 tubes used a somewhat
unusual 9 pin socket that was *almost* as big as a standard octal socket, so
something that used a pair of octal tubes seemed like the way to go.  It's a 
really small box that previously only had just enough room for the power 
transformer and the tubes.  I'd need to fit in an output transformer, too, which
meant using power and output transformers about as small as I could find.  I 
figured that since I had two octal sockets and a push pull transformer can be
made smaller than a single ended transformer with equivalent power, I could do
an output section with a pair of octal tubes in push pull, and a preamp crafted
from my stock of subminiature tubes.  The subminiature tubes were small enough
that they could soldered directly into the circuit and mounted inside the 
chassis.

I ended up going with the same power transformer used for the SE-1 project.
For the output transformer, I wound up going with an `Edcor 10W 8K:8 push pull 
output transformer <http://www.edcorusa.com/p/390/gxpp10-8-8k>`_.  It would work
in terms of specs and physical size, was a very reasonably priced made in the USA
product, and seemed to have happy customers.  I thought about using 6L6s for the
output, but found they would bust the budget in terms of heater current 
available from my power transformer, so I went with a pair of 6V6s.  The choice 
of power transformer and my desire to reuse the "sag resistor" trick from the 
SE-1 meant the voltage on the 6V6s would be pretty low, so the amp might be 
a little underpowered compared to other push pull 6V6 amps.  This was fine with
me as long as it sounded good.

I tried to reuse what I could of the original holes in the chassis.  The input
and output were originally two large coaxial connectors.  I ended making these
holes a little larger and using them to output a Neutrik Speak-on connector for
the speaker output and a Neutrik Power-con connector the power inlet.  This was
the first time I'd ever used a Power-con connector.  It's actually pretty nice,
compared to an IEC socket, since it uses a round hole, as opposed to the polygon
shape required for an IEC socket, so it could be drilled rather than routed.  
The downside, of course, is nobody else uses them, so you have to make your own
power cable and keep track of it, rather than just using one of dozens of IEC 
power cables we tend to have laying around.  The speak-on cable has similar 
compatibility issues, but at least there is some uptake of that connector on
equipment you're likely to encounter--mostly PA gear in my experience.  

It strangely already had two indicator lamps on the front panel, both being run
off the 6.3V heater tap.  Since I already had the holes, I left those there,
but I did replace the matte plastic diffusors for some nice jewel diffusors.
The two input jacks went where the power and standby switches had been, without
having to alter the holes.  The volume and tone knobs required some widening of
existing holes on the front panel.  I drilled new holes in the back for a rear
mounted power switch, fuse holder, and what was originally supposed to be a
hi/lo power switch, but which got scrapped for space.  There is currently
gaffer's tape covering that hole to prevent little fingers from reaching inside
and finding high voltage.  The top had to be drilled for screw holes to mount
the transformers and the two tube socket holes had to be widened a bit.

Due to space being at a premium, I had to get creative cramming all of the parts
in there.  I wound up with the power supply, preamp and phase inverter all being
built on their own Radio Shack pad-per-hole circuit board and mounted vertically
with an L bracket using one of the transformer screws.  The layout was not 
planned out in advance, nor could it have been easily, given the heavy use of
all three dimensions to get things to fit.  The wiring has ended up looking a
bit like a rat's nest, but despite the obvious potential for layout issues, the
amp is surprisingly quiet and well behaved.

Basic Design 
------------

Preamp
======

The preamp is a single 6948 tube, which is a military grade subminiature twin
triode with a mu of about 70, which puts it roughly in the ballpark of a 12at7
for gain and 12ax7 for current handling.  The `data sheet <http://frank.pocnet.net/sheets/084/6/6948.pdf>`_ is amusing, as it shows that this tube was intended for use in 
guided missiles, rated for altitudes up to 80,000 feet and impact acceleration
of 450G, the datasheet also specifies the max allowable radiation.  Probably 
this tube would hold up well in a rock club environment.  

Each stage is pretty much a textbook common cathode gain stage, with fully 
bypassed cathode resistor.  The second stage is biased a little cooler than the
first, in an attempt to get a little more clean headroom out of it.  Hard to say
if it worked or not, as swapping components back and forth isn't terribly easy
in the small box with ad-hoc layout.  The volume and tone control are lifted 
straight from a schematic of a Marshall 18watt.  I had never tried that tone 
control and was curious to hear what it sounded like.  I am pleased with how it
sounds--it seems to be able to get bright without turning into an icepick.  
There is enough gain here to overdrive the second stage, so it can get crunchy
as the volume is turned up.

Phase Inverter
==============

I felt like doing something different with the phase inverter, so I tried a DC
coupled split load inverter, using a 5703 subminiature tube, which is a low-mu 
(about 20) high current single triode, similar in specs to a 12au7.   The plate
voltage at V1b is still higher than we'd want to see at the grid of V2, so R12
and R13 divide the DC voltage down to bias V2 properly.  C5 bypasses R13 so that
AC signal is not also divided down.  (I initially wired this without C5--output
was quite low.)  

Power Amp
=========

The phase inverter feeds a pretty textbook cathode biased power amp.  Not really
that much to say about this.  With the cathode bias and low plate voltage, we
get about 8 watts out of this.  Compare with a max of about 15-18W for other
cathode biased PP 6V6 amps, or 20-22W for fixed bias 6V6 amps.  There is some 
negative feedback going from the output back to the second stage, through R17.
This does smooth things out and make it sound less ragged.

Conclusions
-----------

The Good
========

It sounds pretty darn good.  Especially in the clean to slightly dirty range.
Using the humdinger, I was able to dial heater hum down to almost nothing, and
despite what should be a pretty bad wiring situation, the amp is fairly quiet 
and doesn't have any major issues.  It also looks pretty darn cool in its shiny
red and black powder coat finish.  And it's teeny size makes it really light
and portable.

The Bad
=======

The overdriven sounds could be smoother.  It's fairly low output due to its 
fairly low voltages.  It's fantastic for home and studio, and could be good in 
quieter bands, but won't have enough power to be heard in even a moderately loud
rock band.  The chassis originally had a handle for the top but I can't find it.

The Ugly
========

The chassis is very cramped.  It was difficult to wire everything up and is
even more difficult to tweak.  The wiring is spaghetti and some components that
could theoretically be tweaked and buried too far down to make it worth the
while.  The power amp, for example, could be biased a little hotter if I could
get to the cathode resistor.  This limits the extent to which I can experiment
to, say, smooth out the overdrive, or squeeze out a little more headrooom.

While a fun project, I probably couldn't justify spending the time and effort on
rehabilitating another "cool" old chassis, given that I could fabricate 
something easier to work on at Tech Shop for fairly cheap.  Future projects will
focus on custom built chassis using the tools available at Tech Shop.
