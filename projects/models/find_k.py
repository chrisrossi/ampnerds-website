#
# Find K from tube datasheet parameters
#
# Device law for tube triode is: Ip = K(Vpk + u*Vgk)**1.5
#
# In small signal model, then:
#
# ip = 1.5*u*K * (VPK + u*VGK)**0.5 * vgk + 1.5*K * (VPK + u*VGK)**0.5 * vpk
#
# Let transconductance, gm = 1.5*u*K * (VPK + u*VGK)**0.5 and
# Let plate resistance, rp = 1/(1.5*K * (VPK + u*VGK)**0.5
#
# Then, ip = gm * vgk + vpk / rp
#
# gm and rp are dependent on operating point.  Tube data sheets usually include
# example values for gm and rp at different operating points.  u (mu, the
# "amplification factor") is usually included on the datasheet but not the
# device constant, K.
#
# For example, from the 12ax7 datasheet:
#
# VPK  100    250   volts
# VGK   -1     -2   volts
# mu   100    100
# rp   80k  62.5k   ohms
# gm  1250   1600   umhos
#
import math

gm = 1600.0e-6
u = 100.0
VPK = 250.0
VGK = -2.0
rp = 62.5e3

K = gm / (1.5*u * math.sqrt(VPK + u*VGK))
print "K, calculated from gm", K

K = 1.0 / (1.5*rp * math.sqrt(VPK + u*VGK))
print "K, calculated from rp", K
