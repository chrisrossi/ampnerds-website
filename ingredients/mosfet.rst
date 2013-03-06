-------
Mosfets
-------

The mosfet is a a kind of field effect transistor and is the most common type 
of transistor in modern electronics.  It is a three terminal device consisting 
of a source, a drain and a gate.  A semiconductive channel spans the source and 
the drain while the gate sits over the channel separated by a layer of 
dielectric.  By varying the voltage at the gate, the channel becomes more or 
less conductive and can be used to control the amount of current that flows
through the channel from the drain to the source.  

Mosfets come in two basic flavors, N-channel and P-channel.  In an N-channel
mosfet, the channel is doped such that it has extra electrons.  A forward bias
is applied from the drain to the source (meaning the drain is at a higher 
voltage than the source) and a forward bias from the gate to the source causes
electrons to move into the conduction band in the channel and flow from the 
source to the drain.  This is the type of mosfet most analogous to a vacuum 
tube, since the flow of current is from the flow of negatively charged 
electrons.  You can think of the source as the cathode, the drain as the anode 
and the gate is analogous to the control grid in a vacuum tube.  

P-channel mosfets have a channel doped such that it has extra "holes", ie an
absence of electrons that behave like positively charged particles.  It is 
complementary to and opposite an N-channel mosfet, in that you reverse bias the 
drain to the source (the drain is at a lower voltage than the source) and 
applying a reverse bias from gate to source causes positively current, as 
"holes", to flow from source to drain.  

I tend to find N-channel mosfets a little easier to wrap my mind around, 
probably because there is no analog to a P-channel mosfet in the vacuum tube 
world.  I will therefore tend to prefer N-channel to P-channel mosfets for 
applications where there is some choice between one or the other.  The ability
to combine N-channel and P-channel devices in complementary pairs, though, 
allows you to do some things you can't do with tubes, like implementing a 
push-pull amplifier without a phase inverter.

Here are some `schematic symbols for mosfets 
<http://en.wikipedia.org/wiki/Mosfet#Circuit_symbols>`_.

Mathematical model
------------------

.. math:: I_{DS} = \frac{K}{2} (V_{GS} - V_{TH})^2
    :label: 1

