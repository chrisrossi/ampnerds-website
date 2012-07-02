==============
Amp Nerds SE-1
==============

Amp Nerds Single Ended Amp Project
----------------------------------

This design grew out of the observation that nearly all small single ended
"practice" ampflifiers, ala Fender Champ, Fender Tweed Princeton, Gibson GA-5,
etc, share a nearly identical topology with part selection being the main 
difference from one amp to the next.  The goal of this design, then, is to 
design a turret board based physical layout that conforms to the basic common 
topology of this class of amplifier and allows for experimentation in terms of 
parts choice.  This amp could serve as a learning laboratory in which it is 
possible to  perform modifications and listen to the results, gaining some real 
world  experience as to the aesthetic tonal impact of electronic design 
decisions.

The amps consulted for this design are: Gibson GA-5, Fender 5F2 Tweed Princeton,
Fender Vibrochamp and the Dearmond R5T (aka Martin 112T).  The Dearmond amp 
served as the primary basis for this particular design.

- The unverified `Dearmond R5T schematic 
  <http://spacelabstudio.com/dearmondschematictx1.gif>`_
- The layout: :download:`QCad file <se1.dxf>`, 
  :download:`PNG file <se1_layout.png>`
- :doc:`Parts list <se1_parts>`
- The schematic: :download:`JSCHEM file <se1.jsch>`,
  :download:`PDF <se1.pdf>`

The basic design is two common cathode triode gain stages provided by a 12ax7
dual triode (V1).  Volume and tone controls, if any, come between the two gain 
stages.  The second gain stage feeds directly to the ouptput power tube which 
can be just about any tube you want.  Certain circuit choices will depend on
your choice of output tube.  6V6 and EL84 are the most common output tubes for
this style of amp.  

V2 is used for the tremolo circuit.  Tremolo is included because it sounds 
cool and isn't too hard to include.  If you really want to cut down on part
count and/or fit this in a tiny box, the tremolo could possibly be eliminated.

What follows is some words on each section of the amp and a stab at explaining
what some of your options are and what you might tweak.

First Gain Stage
++++++++++++++++

Guitar signal enters through input jack.  R27 is 1M resistor to ground and is
called the grid leak resistor.  It creates a path whereby the grid of the first
stage can come to idle at 0 volts.  R25 is the standard 68K grid stopper seen 
in nearly every guitar amp.  It's purpose is to form an RC filter with the 
internal tube capacitances which blocks very high frequency RF, which can spoil
the performance of the amp at audio frequencies.  Typically this resistor is
found hanging off the input jack, but here it has been moved to the tube grid, 
as recommended by Merlin Blencowe (MB) where it is more effective at filtering
RF due to the reduced amount of wire to the grid.   

R26 is the anode load resistor, R24 is the cathode resistor and C13 is the 
cathode bypass cap.  The values of R26 and R24 can be modified to change the
sound of the gain stage.  See MB for info on how to draw and interpret a load
line for desiging a triode gain stage.  Fender, and consequently much of the
rest of the world, uses 100K for R26 and 1.5K for R24.  Of the amps consulted
for this design, only the GA-5 uses different values: 220K for R26 and 2.2K for 
R24.  I also have a Gibson Scout which uses some very unsual values: 470K
for R26 and 4.7K for R24.  This amp sounds pretty cool.  Obviously, there is
lots of room for experimentation.  The values chosen here can have a dramatic
impact on the tone and feel of your amp.  It's not too hard to try a few
combinations and listen to find the one you prefer.

C13 is the cathode bypass capacitor.  In a cathode bias gain stage this acts
to prevent the gain loss that would be caused by the tube bias changing as a 
result of signal, by holding the voltage at the cathode constant at the 
frequencies of interest.  The boost is frequency dependent where the cutoff
frequency is a function of the size of the capacitor.  Frequencies below the
cutoff are passed but lower gain, where frequencies above the cutoff are passed
with full gain.  Usually this capacitor is large enough (25uF is standard) that
the cutoff frequency is subsonic, so that all audible frequencies are boosted.
If your amp has too much bass you can experiment with smaller values to raise
the cutoff frequency, which will de-emphasize the bass.  Chris G is reportedly
considering installing a way to switch in different values for this capacitor
for his Tremolux build.

C14 is the coupling capacitor.  Its job is to block the high voltage DC that
is on the plate of the tube and pass only the amplified AC signal component on 
to the next stage.  It also forms a high pass RC filter with the surrounding 
components, so depending on its value it can filter out more or less bass 
frequencies.  The amps consulted use either .01uF or .02uF.  Larger values will
yield more bass, smaller values less bass.  Unlike the cathode bypass cap above,
pretty much everything below the cutoff frequency is filtered out, as opposed
to just passed with lower gain.  Chris G's Tremolux that he built 
recently uses .1uF.  Chris G reports this is too much bass and has knocked his
down to .047uF.

Parts: 

- R27, Grid Leak, 1M
- R25, Grid Stopper, 68K
- R26, Anode Load, 100k, 220k or 470k (change with R26)
- R24, Cathode Bias, 1.5k, 2.2k or 4.7k (change with 24)
- C13, Cathode Bypass, 25uF-1uF (larger value==more bass, 25uF is standard)
- C14, Coupling Cap, Start with 0.01uF or 0.02uF (larger value==more bass)
- V1a, 1/2 of 12ax7
- Input Jack

Volume and Tone Control
+++++++++++++++++++++++

From the coupling cap of the first stage, the signal arrives at the volume and
tone controls.  The volume control is a straightforward 1M pot used as a 
voltage divider.  The tone circuit is about as basic as they come and is pretty
indicative of the state of the art in the 40s and 50s.  It is basically a 
variable brightness control.  If you're familiar with the "bright cap" on some
amps and you squint at the schematic just right you can see that with the tone
knob turned all the way up you can ignore C11 and the circuit with C10 is 
exactly equivalent to a basic volume control with bright cap.  The Gibson GA-5 does
not use a tone control.  This tone control is wired like the Dearmond schematic 
which uses 500pF for C10 and .02uF for C11.  The Fender 5F2 uses 500pF and .005
uF, instead.  Additionally in the Fender amp rather than the wipers of the two
pots being wired together the wiper (middle lug) of the tone pot is wired to 
the leftmost lug of the volume pot--a very simple modification.  I have no idea
what the tonal differences would be between those two variations, but it would 
be very easy to experiment and find out with a built amp.  The Vibrochamp uses
a 60s blackface style tone stack which is very different.

Parts: 

- C10, Bright Cap, 500pf
- C11, Mellow Cap, .02uF (Dearmond) or .005uF(Fender) 
- Vol Pot, 1M audio taper
- Tone Pot, 500k or 1M linear

Second Gain Stage
+++++++++++++++++

Second stage, same as the first.  R23 is a grid stopper like R25 above.  A grid
stopper is not typically used in preamp stages other than the first stage in 
vintage amps.  MB makes a compelling argument for their inclusion, though, 
since they can help to prevent blocking distortion (which sounds terrible) when
the tube is being overdriven by the first stage.  Vintage amps were not 
typically designed to be overdriven, so the inclusion of the grid stopper can 
improve the tone for guitarists looking to exploit rather than avoid the 
distortion available in their amp.  Anything in the 10k-100k range should give
some protection against blocking distortion without changing the tone of the 
amp.  If the value is too high, it can start to roll off some high end in the
audible band.  This resistor won't have much effect unless the volume control
is dimed.  Otherwise part of the volume control itself is in series with the
grid and provides some measure of grid stop. The volume control also provides
a grid leakage path, so no separate grid leak resistor is needed.

R22 and R20 are the anode load and cathode resistors respectively.  They serve
the same function as in the first gain stage, and the considerations for 
choosing their values is the same.  R21 is a small value compared to R20 and is
there just to have a point to inject negative feedback.  If no negative 
feedback is used this could just as easily be jumpered.  Since R21 is in series
with R20 it does add to the total cathode resistance which will change the bias
somewhat of the stage.  But if it's small enough with respect to R20, the 
difference will be negligible.

C12 is the cathode bypass cap.  None of the amps I looked at actually have this
cap, so it is very optional.  If included, it will boost the gain of this stage.
Since the tremolo signal is injected at this point, the value here, if used at
all, must be small enough that the cutoff frequency is higher than the 
frequency of the Tremolo LFO, or else it will siphon off the tremolo signal.
(Thanks HotBluesPlate for the explanation.)  Since the the value of this cap
will have to be small, the cutoff frequency should be in the audible range, so
it would act like a treble boost.  

C4 us the coupling cap, same as for the first stage.  Assuming you've done your
tone shaping in earlier stages, this can be arbitrarily large for transparency.

Parts: 

- R23, Grid Stopper, 22K (10k-100k should be fine)
- R22, Anode Load, 100k, 220k or 470k (change with R26)
- R20, Cathode Bias, 1.5k, 2.2k or 4.7k (change with 24)
- C12, Cathode Bypass, 2uF-1uF (larger value==more bass, 
  go smaller if tremolo doesn't work)
- C4, Coupling Cap, .047uF or .1uF
- V1b, 1/2 of 12ax7

Negative Feedback
+++++++++++++++++

Negative feedback is a little bit of electronics voodoo that reduces distortion
at the cost of some gain in an amp by feeding back a little bit of the output
signal out of phase into an earlier gain stage.  Here, feedback is taken from 
the speaker output and fed into the second gain stage through R19, which is 
the feedback resistor.  The feedback is not strictly necessary and can easily 
be ommitted.  The Dearmond amp does not use it at all.  The 5F2 and GA5 both 
inject negative feedback  right at the cathode, but they both also lack tremolo 
which, in this design, is fed into that spot.  The Vibrochamp is the only amp 
looked with both negative feedback and tremolo, so the basic topology for this
amp is stolen from the Vibrochamp.  Increasing the size of R19 decreases 
negative feedback.  The amount of negative feedback can dramatically effect 
the tone and responsiveness of the amp, so some amount of experimentation and 
seasoning to taste is warranted here.  Many people seem to prefer some amount
of negative feedback, but often less than the amount used by amp manufacturers
of the day.  Again, back in the day the design goal was usually to reduce 
distortion, rather than deliberately drive amps into distortion.

Parts: 

- R19, Feedback, Start with 2.7K (like Vibrochamp), adjust or omit to taste
- R21, Feedback tail, 47R or jumper if negative feedback is omitted

Tremolo
+++++++

The tremolo is cargo culted without modification from the Dearmond schematic.
Basically it is an LFO (low frequency oscillator) the output of which is fed 
into the cathode of the second gain stage, modulating its bias.  Graham gave
an excellent presentation on how the LFO works.  For the most part, though, you
should just be able to copy it and it 
should work.  (Knock on wood.)  What would be the footswitch I've just 
incorporated into the switch portion of a combo potentiometer and 
SPST switch.  With the depth knob full counter-clockwise there should be a 
click, shutting off the tremolo.  If you like the idea of a pedal you could 
always just install a jack for a foot pedal in combination with or instead of
the switch.  

Parts: 

- R12, 150K
- R13, 2.2M
- R14, 68K
- R15, 220K
- R16, 1.5K
- R17, 1M
- R18, 2.2M
- C6, .022uF ceramic disk
- C7,C8,C9, .01uF ceramic disk
- Depth Pot, 500K w/SPST switch
- Rate Pot, 1M
- V2, 12ax7

Power Stage
+++++++++++

This stage is very simple.  You can pretty much use any power tube you want.
I'm thinking of building mine using a 6GM5 which is a 9 pin
version of the much more common 7591A tube.  This might be a stupid thing to do,
since technically this tube really isn't designed for class A operation
and is mostly intended for use in push pull power stages.  Generally speaking,
attempting to bias this tube up into class A you hit the limits for maximum
plate dissipation fairly quickly, so the bias points that will keep the tube
in a safe operating region will have fairly high distortion as a result of the 
signal having much more room to swing up than down.  This might end up
sounding really cool or sounding like ass.  If it really sounds like ass, it 
should be easy to rewire the 9 pin socket for an EL84 which should work just 
fine in the same circuit with a different cathode resistor (R7).  I have a 
couple of NOS GE 6GM5 tubes already that saw service briefly in my Ampeg
Reverberocket.  I wouldn't be considering trying this tube if I didn't already
have some.

Operation is just like your basic triode preamp stage, with the addition of a 
second grid called the screen.  R8 is the grid leak resistor.  220K seems to be 
standard, which is lower than the 1M is standard on the preamp.  Datasheet for
the power tube usually suggests a value.  R7 is the cathode resistor and sets 
the bias.  Fender uses a 470R here.  The Dearmond uses a 330R.  A lower value 
will bias the tube hotter.  C3 is the cathode bypass cap.  Output will be very 
low if you don't have it.  You could try to do tone shaping here, but usually 
that's been done in the preamp.  25uF seems to be standard in amps looked at 
here.  You can improve bass response a bit by going higher--I'll probably try a 
100uF.  Large value caps that used to be hard to come by then, are common and 
cheap nowadays.

R6 is the screen resistor.  It is used to limit the current the can flow through 
the screen to prevent it from exceeding limits.  This would be more critical if
we were feeding it from a choke rather than a dropping resistor in the power
supply, since the power supply dropping resistor offers some current limiting
of its own.  Including it also adds some compression to the output, which might
sound cool. R9 is the grid stopper resistor.  It also is not present on any of the 
amps considered but MB insists you should have one to prevent high frequency
oscillation and presumably also to prevent blocking distortion.

There is no anode load resistor.  Instead you have the output transformer.  
The tube wants to a see a load impedance that is much higher than the impedance
of the loud speaker you're hoping to drive, so a transformer is used to 
transform the impedance of the speaker into a usable range for the output tube.
The actual impedance ratio required differs according to output tube and there
is some room for using different values with the same tube.  Generally you can
just buy an output transformer sold as a single ended transformer that will work
with the tube you want to use.

More than you ever wanted to know about a single ended output stage:

http://www.freewebs.com/valvewizard1/se.html

Parts: (Values assuming 6GM5 power tube.  Adjust for other tubes.)

- R6, Screen Resistor, 470R, 2-3W
- R7, Cathode Resistor, 200R, 160R, 180R, 220R, 240R, 2-3W
- R8, Grid Leak, 220K
- R9, Grid Stopper, 470R, 2-3W
- C3, Cathode Bypass, 22uF-100uF
- V3, 6GM5
- Output Transformer, one of: 
  Mercury Magnetics Axiom Series, 4K:8 10W, 
  Allen TO11C, 4K:8,
  Edcor XSE15-8-3.5K or GXSE15-8-3.5K, both 3.5K:8 15W
- Output Jack

Power Supply
++++++++++++

Takes AC wall voltage and provides high voltage DC used by the tubes in the 
amp.  The power transformer steps up wall voltage, the four silicon diodes are
arranged as a bridge rectifier, which takes the AC that is flowing in and gets
it flowing out in a single direction.  C1 stores the
charge from the rectifier and doles it out as current to the rest of the amp.
The plate of the power tube is fed directly from this capacitor, giving it the
highest voltage in the amp.  

With the parts list I give below, I'm shooting for about about 300V at the 
plates of the power tubes and about 200V feeding the preamp tubes.  Most power 
tubes you might use can go higher on the plate voltage, which will result in a 
bit more clean headroom.  I've noticed that the older vintage sounding amps 
people tend to like run the power tubes at around 300V and I've read 
antectdotally that EL84s, specifically, tend to sound nicer at lower voltages.  
If you want to use a higher power tube like a 6L6, 6551, EL34, KT66, etc..., 
these can be run perfectly fine at 300V, but we can also certainly tweak the 
power supply to get higher plate voltage.  I would stick to 200V for the preamp, 
though.  

R4/C2 and R11/C5 act as high pass RC filters that
filter out ripple that remains in the line due to the conversion from AC.  R4
and R11 also develop voltage drops across them that feed progressively lower 
(but cleaner) supply voltages to downstream components.  R4/C2 provide the
screen voltage for the power tube and R11/C5 provide the plate voltages for
all preamp tubes.  Screen voltages seem to vary quite wildly from one design to
the next and I'm not sure really what the difference in tone is from one
approach to another.  A recent forum thread suggests there's not much difference
in tone, but higher screen voltages allow more output power, but also run the
tube closer to its limits.  Fender amps tend to have screen voltages that are very
nearly the plate voltage.  The Dearmond amp has a screen voltage about 75V 
lower than the plate voltage.  The MB article linked to from the "Power Stage" 
section explains how screen voltage will impact your bias point.
For the preamp, shoot for about 200V coming out of R11.

The power transformer will have a 6.3V winding that is meant for wiring to the
heaters of all the tubes.   The humdinger pot is there to create an artificial 
ground so that the EM fields generated by the AC in the heater wires will tend
to cancel and induce less hum in the rest of the circuit.  Just adjust the pot
until you hear the least amount of hum.

In this design I've opted 
for a silicon rectifier over a tube rectifier since there is little reason to
use a tube rectifier given the expense and extra heat they generate.  Also,
when arranged as a bridge rectifier (four diodes, no center tap) instead of the 
typical full wave rectifier (using two diodes and the center tap on the power 
transformer's secondary) we can use a smaller transformer as we only need half
the amount of voltage swing on the primary to get the same output voltage.  When 
people discuss differences in tone between a tube and a silicon rectifier, 
they're generally talking about the extra "sag", a kind of compression effect, 
that is caused by the higher internal resistance of the tube rectifier compared
to the solid state.  This is easily simulated by just placing a resistor in 
series with a solid state rectifier, which is the purpose of R3, the "sag"
resistor.  It can easily be jumpered, for the most forward response, or can be
chosen to mimic the internal resistances of various tube rectifiers, which will
soften up the attack somewhat and give a more "tweedy" response.  If your
chosen power transformer has a 5V winding, you could easily forego the silicon
rectifier and use a tube rectifier instead, if you feel you must totally 
recreate the authentic design of a vintage amp.

Parts, assuming 300V at the plate, using 6GM5.  Can be tweaked for other 
voltages/tubes. Should be fine largely unmodified for EL84 and 6V6 as well as
higher power tubes if you want to run them at lower than usual voltages: 

- C1, Reservoir Capacitor: 40uF-100uF, 400-500V
- C2,C5 Filter Capacitors, 40uF-100uF, 400-500V
- R3, Sag, 180R, 200R, 2-3W
- R4, Dropper, 470R, 1-2W
- R11, Dropper, 24K, 22K, 27K, 1-2W
- D1-4, Rectifier Diodes, IN4007
- Humdinger Pot, Heater Balance, 200R Linear
- Power Transformer, Hammond 250VAC 40VA, 269AX, Mouser 546-269AX
- Power Switch
- Fuse Holder
- 2A Slow blow fuse
- IEC Power Inlet
       
Filter Cap Drain/Status LED
+++++++++++++++++++++++++++

I've never seen one of these before but I don't see why it wouldn't work.
Basically for the status light, just feed an LED from the high voltage supply 
rail through a very big resistor, R10.  The interesting and useful thing about
this arrangement, is this creates a path for the large power supply capacitors
to drain to ground after the amp is shut off, reducing the risk of electric 
shock when servicing the amp.  Not only that, but the LED should continue to
glow until the filter caps are drained, making it useful as a safety status
indicator.

Assuming a worst case of 400V at the supply rail and average case of 200V, 
if we say we want to run no more than 1mA through the LED, then our resistor 
should be about 200V / 0.001A = 200K.  Since when amp is powered on no current
is flowing through the tubes, initial voltage might be as high as 400V, making
for a worst case current of 2mA.  Because the voltage drop across the 
resistor is fairly large, the worst case dissipation will be about 400V x 
0.002A = .8 watts, so we'd probably want a 1 watt resistor, or a 2 or 3 watt if 
we anticipate we might want to run the amp without tubes for any length of time,
which you might do when debugging a newly built amp.  The only thing I'm not  
really sure about, is since we're keeping the current fairly low so as to avoid  
having to dissipate too much heat in R10, I don't know how brightly the LED 
will actually glow and if it will be easily visible.  I guess I'll find out.

Parts: 

- LED1
- R10 200K, 2 or 3 watt.

**History**::

    2012/07/02, Chris Rossi, Initial Publication
