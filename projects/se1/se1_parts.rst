=====================
Rossi SE-1 Parts List
=====================

:Author: Chris Rossi
:Last-modified: 2012/07/02

This list aims to include most of the parts to build a particular version of 
the Rossi SE-1 amplifier.  Some options will be included.  Many parts could 
potentially be substituted with others and could be sourced from other vendors.
But this list should get you there.

The output transformer options are both 4k which should work fine with an EL-84
or a 6GM5.  Use of the 6GM5 is an experiment I want to do which may sound bad.
Switching to EL-84 if I don't like the 6GM5 should be as simple as rewiring 
the tube socket (different pinout) and decreasing the value of the cathode
resistor.

The power transformer here, using a diode bridge rectifier, has a theoretical
DC output max of 354V (sqrt(2) * Vrms).  In practice, due to transformer losses,
it's been suggested that 1.2 * Vrms is a good rule of thumb, which would put us
at 300V, our target voltage.  The "sag" resistor can be used to drop the voltage
in the event that it is higher than we expect, which, in turn, can add some nice
compression.  And actually, since that transformer is spec'ed for 115V input and
we all have 120V coming out of our walls these days, those numbers would be 
closer to 369V and 313V respectively.

Tubes are not included in this list.  If you need tubes they are easy to find.

Output Transformer
------------------

- Mercury Magnetics Axiom Series, 4K:8 10W
  (`Mercury Price Sheet <http://www.mercurymagnetics.com/pages/catalog/manufacturers/MM_boutique.htm>`_,
  `Chris G's source <http://www.jmimusic.com/>`_) 
- `Allen TO11C <http://www.allenamps.com/parts.php#transformers>`_ $45

In email correspondence Chris G's source offered the MM transformer for $80 +
drop shipping.

Mouser
------

Power Transformer
+++++++++++++++++

- `Power Transformer, Hammond 250VAC 40VA, 269AX 
  <http://www.mouser.com/ProductDetail/Hammond/269AX/?qs=%252bHhoWzUJg4LsIANOOQQymA%3d%3d>`_

1/2 Watt Metal Film Resistors
+++++++++++++++++++++++++++++

- `47R <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC47R0F/?qs=sGAEpiMZZMu61qfTUdNhG03wcFPUdIEWrt0B%2f0YVx48%3d>`_, 
  R21
- `1.5K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC1501F/?qs=sGAEpiMZZMu61qfTUdNhG2%252byzAc6g0mPEarHlK0GjPY%3d>`_, 
  R24, R20, R16
- `2.2K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC2201F/?qs=sGAEpiMZZMu61qfTUdNhG2r2Nmyl%2fOMiHmtaCQSEr%2fs%3d>`_, 
  R24, R20, R19
- `2.74K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC2741F/?qs=sGAEpiMZZMu61qfTUdNhG76aOwthnk9z7mw8OVh6Fh0%3d>`_, 
  R19
- `3.32K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC3321F/?qs=sGAEpiMZZMu61qfTUdNhG0pMwnAa95VwIXbDHFZ6qMA%3d>`_, 
  R19
- `4.7K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC4701F/?qs=sGAEpiMZZMu61qfTUdNhG0RUkTLGOdTM7%2fUyFw12Zik%3d>`_, 
  R24, R20, R19
- `22.1K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC2212F/?qs=sGAEpiMZZMu61qfTUdNhG4exJO9ReX867F0200EC2%252bg%3d>`_, 
  R23
- `68.1K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC6812F/?qs=sGAEpiMZZMu61qfTUdNhG4exJO9ReX86%2fLsR%2fVMXpFQ%3d>`_, 
  R25, R14
- `100K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC1003F/?qs=sGAEpiMZZMu61qfTUdNhG6w4bcG3pUGgppBvvmLXXHg%3d>`_,
  R26, R22
- `150K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC1503F/?qs=sGAEpiMZZMu61qfTUdNhG2%252byzAc6g0mPmm13FEw5lkg%3d>`_, 
  R12
- `221K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC2213F/?qs=sGAEpiMZZMu61qfTUdNhG4exJO9ReX86iNgOuAo%2fTMU%3d>`_, 
  R26, R22, R15, R8
- `470K <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC4703F/?qs=sGAEpiMZZMu61qfTUdNhG0RUkTLGOdTM5DyxqIWh2qA%3d>`_, 
  R26, R22
- `1M <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC1004F/?qs=sGAEpiMZZMu61qfTUdNhG6w4bcG3pUGgBaeVXZSNcx4%3d>`_, 
  R27, R17
- `2.21M <http://www.mouser.com/ProductDetail/KOA-Speer/MF1-2CC2214F/?qs=sGAEpiMZZMu61qfTUdNhG4exJO9ReX86T10tko6TNi8%3d>`_, 
  R13, R18

3 Watt Metal Film Resistors
+++++++++++++++++++++++++++

- `470R <http://www.mouser.com/ProductDetail/Vishay/PR03000204700JAC00/?qs=6J1u%252bx0LbWCXA6b85Z9lBw%3d%3d>`_,
  R4, R6, R9
- `22K <http://www.mouser.com/ProductDetail/Vishay-BC-Components/PR03000202202JAC00/?qs=sGAEpiMZZMu61qfTUdNhG%2f4r7Iw6CIkydAatbeBLwgE%3d>`_,
  R11
- `24K <http://www.mouser.com/ProductDetail/Vishay-BC-Components/PR03000202402JAC00/?qs=sGAEpiMZZMu61qfTUdNhGxOtoaS4p7nEEACppQS6tvA%3d>`_,
  R11
- `27K <http://www.mouser.com/ProductDetail/Vishay-BC-Components/PR03000202702JAC00/?qs=sGAEpiMZZMu61qfTUdNhG%2f4r7Iw6CIkyw%252b9vEz%2fgbYw%3d>`_,
  R11
- `200K <http://www.mouser.com/ProductDetail/Vishay/PR03000202003JAC00/?qs=LCMWAU1DZcxDaMRbGl9EBQ%3d%3d>`_,
  R10
  
3 Watt Wirewound Resistors
++++++++++++++++++++++++++

- `100R <http://www.mouser.com/ProductDetail/Vishay-Draloric/AC03000001000JAC00/?qs=sGAEpiMZZMtbXrIkmrvidMh8qIR%252bmwjwx0X40JT0%252bR4%3d>`_,
  R3, R7 
- `150R <http://www.mouser.com/ProductDetail/Vishay-Draloric/AC03000001500JAC00/?qs=sGAEpiMZZMtbXrIkmrvidMh8qIR%252bmwjweoIbRrENexE%3d>`_,
  R3, R7 
- `180R <http://www.mouser.com/ProductDetail/Vishay-Draloric/AC03000001800JAC00/?qs=sGAEpiMZZMtbXrIkmrvidMh8qIR%252bmwjw8R8%2fVmog1n4%3d>`_,
  R3, R7 
- `200R <http://www.mouser.com/ProductDetail/Vishay-Draloric/AC03000002000JAC00/?qs=sGAEpiMZZMtbXrIkmrvidMh8qIR%252bmwjwXdLX4PNFk4U%3d>`_,
  R3, R7 
- `220R <http://www.mouser.com/ProductDetail/Vishay-Draloric/AC03000002200JAC00/?qs=sGAEpiMZZMtbXrIkmrvidMh8qIR%252bmwjwJ7JrXr86OMg%3d>`_,
  R3, R7 
- `240R <http://www.mouser.com/ProductDetail/Vishay-Draloric/AC03000002400JAC00/?qs=sGAEpiMZZMtbXrIkmrvidMh8qIR%252bmwjw1ynoXGlLVH4%3d>`_,
  R3, R7
  
Small Electrolytic Caps
+++++++++++++++++++++++

- `25uF @ 50V <http://www.mouser.com/ProductDetail/Vishay-Sprague/TVA1306/?qs=sGAEpiMZZMtZ1n0r9vR22UzXQwAPJeqECXFITVQbZQM%3d>`_,
  C3, C13
- `100uF @ 50V <http://www.mouser.com/ProductDetail/Vishay-Sprague/516D107M050MM6AE3/?qs=sGAEpiMZZMtZ1n0r9vR22fPWwtj8kO8ayUNK78D3b3I%3d>`_,
  C3
- `2uF @ 50V <http://www.mouser.com/ProductDetail/Vishay-Sprague/TVA1301-E3/?qs=sGAEpiMZZMtZ1n0r9vR22beeiJoI0EpCw%2ftqZOItGaw%3d>`_,
  C12
- `4uF @ 50V <http://www.mouser.com/ProductDetail/Vishay-Sprague/TE13021-E3/?qs=sGAEpiMZZMtZ1n0r9vR22beeiJoI0EpCZfexeJLBHfY%3d>`_,
  C12
  
Mallory 150 Polyester Film Capacitors
+++++++++++++++++++++++++++++++++++++

- `.01uF @ 630V <http://www.mouser.com/ProductDetail/Cornell-Dubilier/150103J630BB/?qs=sGAEpiMZZMvOcEq4GH1AAkGjFdHWMsoDViQ222vXjfE%3d>`_,
  C14
- `.02uF @ 630V <http://www.mouser.com/ProductDetail/Cornell-Dubilier/150223J630DB/?qs=gZ69X08SqGh3hdEJ%252bMh8vg%3d%3d>`_,
  C11, C14
- `.047uF @ 630V <http://www.mouser.com/ProductDetail/Cornell-Dubilier/150473J630EC/?qs=u7ZFOgOpR2uW68R4iCgJhg%3d%3d>`_,
  C4
- `.1uF @ 630V <http://www.mouser.com/ProductDetail/Cornell-Dubilier/150104J630FE/?qs=u7ZFOgOpR2t2UDqECMwCLw%3d%3d>`_,
  C4
  
Orange Drop Polypropylene Capacitors
++++++++++++++++++++++++++++++++++++

- `.01uF @ 600V <http://www.mouser.com/ProductDetail/Vishay-Sprague/715P10356KD3/?qs=sGAEpiMZZMvCt%252bwg%252braTunzkLZq3Qunnjycuk68EpUQ%3d>`_,
  C14
- `.022uF @ 600V <http://www.mouser.com/ProductDetail/Vishay/715P22356KD3/?qs=FMw9dFbUF2tzs0iy7omQ6g%3d%3d>`_,
  C11, C14
- `.047uF @ 600V <http://www.mouser.com/ProductDetail/Vishay/715P47356LD3/?qs=4rkkKKSASjsW8pyG8isxzQ%3d%3d>`_,
  C4
- `.1uF @ 600V <http://www.mouser.com/ProductDetail/Vishay-Sprague/715P10456LD3/?qs=sGAEpiMZZMvCt%252bwg%252braTuqwrQx3d0hmsdbVPYyF1Too%3d>`_,
  C4

Ceramic Disk and Silver Micah Capacitors
++++++++++++++++++++++++++++++++++++++++

- `500pF @ 500V <http://www.mouser.com/ProductDetail/Cornell-Dubilier/CD19FD501J03F/?qs=sGAEpiMZZMtLiKaZgV7flft2%252biwd2UtDS0Pv7JNuntI%3d>`_,
  C10
- `.022uF @ 1KV <http://www.mouser.com/ProductDetail/Vishay-Draloric/HAX223SBACFGKR/?qs=sGAEpiMZZMuMW9TJLBQkXlmaccbwtG8b%252bXEiEUld2sQ%3d>`_,
  C6
- `.01uF @ 1KV <http://www.mouser.com/ProductDetail/Vishay-BC-Components/S103M47Z5UN63J7R/?qs=sGAEpiMZZMuMW9TJLBQkXrp1494b0sF2vcVtJ2x90Nw%3d>`_,
  C7, C8, C9
  
Misc
++++

- `1N4007 Rectifier Diode <http://www.mouser.com/ProductDetail/Fairchild-Semiconductor/1N4007/?qs=sGAEpiMZZMuQUXCJI7Y4lvWy%252b1U8RtCq>`_,
  D1, D2, D3, D4
- `Blue LED Panel Mount Indicator <http://www.mouser.com/ProductDetail/Shin-Chin/R9-122L1-01-UU3/?qs=doVol%252bVFxJoMGS5Qzwotyw%3d%3d>`_,
  LED1
  
Watts Audio
-----------

Filter Caps
+++++++++++

http://www.turretboards.com/guitar_amplifier_capacitors_electrolytic_f&t_axial.htm

- 100uF @ 450V, C1
- 47uF @ 500V, C2, C5

Potentiometers
++++++++++++++

- `500KA w/rotary switch <http://www.turretboards.com/guitar_amplifier_potentiomers_alpha_24_switched.html>`_,
  Depth
- `500KL <http://www.turretboards.com/guitar_amplifier_potentiomers_alpha_24.html>`_,
  Tone
- `1MA <http://www.turretboards.com/guitar_amplifier_potentiomers_alpha_24.html>`_,
  Volume, Rate
  
Chassis
+++++++

http://www.turretboards.com/guitar_amplifier_chassis_blank.htm

- PROJECT BOX 17.5"w x 6.5"d x 2.5"h
- Shielding plate for 17.5 x 6.5 x 2.5 outward lip project box.

Not sure if screws for mounting shield plate onto project box are included.  
Might require a quick run to the hardware store.

Hardware
++++++++

http://www.turretboards.com/guitar_amplifier_hardware.htm

- 4x 1/2" standoffs, for mounting circuit board
- 4x Chassis Bolts, for eventually mounting chassis in a cabinet
- 1x Size 4 crimp style solder lug, 1x 1/4" 4-40 screw and 1x 4-40 kep nut, 
  for making chassis ground connection
 
Wire
++++

www.turretboards.com/wire_pvc_hook_up.htm

Get some wire if you don't it already.  20awg for most stuff, 18awg for heaters

Switch
++++++

http://www.turretboards.com/guitar_amplifier_switches.html

- SPST Carling Switch, for the power switch

Weber
-----

- `200 Ohm Linear Potentiometer, screwdriver slot2 watts <https://taweber.powweb.com/store/potsord.htm>`_,
  Humdinger
  
Hoffman Amps
------------

http://www.hoffmanamps.com/MyStore/perlshop.cgi

Fuses/Cords/AC
++++++++++++++

- Fender Fuse Holder
- 2A standard size slo blo fuse
- Power Cord Receptacle
- 12 foot removable power cord

Board Building Parts
++++++++++++++++++++

- 12" x 3.125" Glass Epoxy board
- 53x Turret Lugs (buy some extras)
- 3/32 Drill bit
- Lug and Eyelet install tool
- Lead benders might be nice but certainly not required


Antique Electronics Supply
--------------------------

http://www.tubesandmore.com

- Rubber Feet: P-H253
- 9 pin sockets: P-ST9-600
- 8 pin socket: P-ST8-209MIP

Will need some small machine screws with nuts to mount the sockets.  I'll 
probably just run to the hardware store once I have sockets in hand to see
what fits.

**History**::

    2012/07/02, Chris Rossi, Initial Publication
