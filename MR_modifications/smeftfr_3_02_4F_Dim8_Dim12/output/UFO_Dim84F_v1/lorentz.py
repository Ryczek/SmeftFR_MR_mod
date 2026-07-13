# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Thu 16 Oct 2025 16:32:28


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'Identity(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,2)*Metric(1,2)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = 'P(2,1)*Metric(1,3)')

VVV4 = Lorentz(name = 'VVV4',
               spins = [ 3, 3, 3 ],
               structure = 'P(2,3)*Metric(1,3)')

VVV5 = Lorentz(name = 'VVV5',
               spins = [ 3, 3, 3 ],
               structure = 'P(1,2)*Metric(2,3)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = 'P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

FFFF1 = Lorentz(name = 'FFFF1',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,3)*Gamma(-1,4,-2)*ProjM(-2,1)*ProjM(2,3)')

FFFF2 = Lorentz(name = 'FFFF2',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjM(-2,1)*ProjM(4,3)')

FFFF3 = Lorentz(name = 'FFFF3',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,1)*Gamma(-1,4,-2)*ProjM(-2,3)*ProjM(2,1)')

FFFF4 = Lorentz(name = 'FFFF4',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,3)*ProjM(4,1)')

FFFF5 = Lorentz(name = 'FFFF5',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(-2,3)*ProjP(2,1)')

FFFF6 = Lorentz(name = 'FFFF6',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(-2,1)*ProjP(2,3)')

FFFF7 = Lorentz(name = 'FFFF7',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,3)*ProjP(4,1)')

FFFF8 = Lorentz(name = 'FFFF8',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,1)*ProjP(4,3)')

FFFF9 = Lorentz(name = 'FFFF9',
                spins = [ 2, 2, 2, 2 ],
                structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(2,3)*ProjP(-2,1)')

FFFF10 = Lorentz(name = 'FFFF10',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(4,3)*ProjP(-2,1)')

FFFF11 = Lorentz(name = 'FFFF11',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,3)*Gamma(-1,4,-2)*ProjP(-2,1)*ProjP(2,3)')

FFFF12 = Lorentz(name = 'FFFF12',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjP(-2,1)*ProjP(4,3)')

FFFF13 = Lorentz(name = 'FFFF13',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(2,1)*ProjP(-2,3)')

FFFF14 = Lorentz(name = 'FFFF14',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(4,1)*ProjP(-2,3)')

FFFF15 = Lorentz(name = 'FFFF15',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,1)*Gamma(-1,4,-2)*ProjP(-2,3)*ProjP(2,1)')

FFFF16 = Lorentz(name = 'FFFF16',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,3)*ProjP(4,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,2)*Metric(3,4)')

FFFFS1 = Lorentz(name = 'FFFFS1',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,3)*Gamma(-1,4,-2)*ProjM(-2,1)*ProjM(2,3)')

FFFFS2 = Lorentz(name = 'FFFFS2',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjM(-2,1)*ProjM(4,3)')

FFFFS3 = Lorentz(name = 'FFFFS3',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,1)*Gamma(-1,4,-2)*ProjM(-2,3)*ProjM(2,1)')

FFFFS4 = Lorentz(name = 'FFFFS4',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,3)*ProjM(4,1)')

FFFFS5 = Lorentz(name = 'FFFFS5',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(-2,3)*ProjP(2,1)')

FFFFS6 = Lorentz(name = 'FFFFS6',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(-2,1)*ProjP(2,3)')

FFFFS7 = Lorentz(name = 'FFFFS7',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,3)*ProjP(4,1)')

FFFFS8 = Lorentz(name = 'FFFFS8',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,1)*ProjP(4,3)')

FFFFS9 = Lorentz(name = 'FFFFS9',
                 spins = [ 2, 2, 2, 2, 1 ],
                 structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(2,3)*ProjP(-2,1)')

FFFFS10 = Lorentz(name = 'FFFFS10',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(4,3)*ProjP(-2,1)')

FFFFS11 = Lorentz(name = 'FFFFS11',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,3)*Gamma(-1,4,-2)*ProjP(-2,1)*ProjP(2,3)')

FFFFS12 = Lorentz(name = 'FFFFS12',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjP(-2,1)*ProjP(4,3)')

FFFFS13 = Lorentz(name = 'FFFFS13',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,2)*Gamma(-1,4,-2)*ProjM(2,1)*ProjP(-2,3)')

FFFFS14 = Lorentz(name = 'FFFFS14',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(4,1)*ProjP(-2,3)')

FFFFS15 = Lorentz(name = 'FFFFS15',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,1)*Gamma(-1,4,-2)*ProjP(-2,3)*ProjP(2,1)')

FFFFS16 = Lorentz(name = 'FFFFS16',
                  spins = [ 2, 2, 2, 2, 1 ],
                  structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,3)*ProjP(4,1)')

FFFFV1 = Lorentz(name = 'FFFFV1',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,4,-1)*ProjM(-1,1)*ProjM(2,3)')

FFFFV2 = Lorentz(name = 'FFFFV2',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,2,-1)*ProjM(-1,1)*ProjM(4,3)')

FFFFV3 = Lorentz(name = 'FFFFV3',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,4,-1)*ProjM(-1,3)*ProjM(2,1)')

FFFFV4 = Lorentz(name = 'FFFFV4',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,2,-1)*ProjM(-1,3)*ProjM(4,1)')

FFFFV5 = Lorentz(name = 'FFFFV5',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,4,-1)*ProjM(-1,3)*ProjP(2,1)')

FFFFV6 = Lorentz(name = 'FFFFV6',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,4,-1)*ProjM(-1,1)*ProjP(2,3)')

FFFFV7 = Lorentz(name = 'FFFFV7',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,2,-1)*ProjM(-1,3)*ProjP(4,1)')

FFFFV8 = Lorentz(name = 'FFFFV8',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,2,-1)*ProjM(-1,1)*ProjP(4,3)')

FFFFV9 = Lorentz(name = 'FFFFV9',
                 spins = [ 2, 2, 2, 2, 3 ],
                 structure = 'Gamma(5,4,-1)*ProjM(2,3)*ProjP(-1,1)')

FFFFV10 = Lorentz(name = 'FFFFV10',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,2,-1)*ProjM(4,3)*ProjP(-1,1)')

FFFFV11 = Lorentz(name = 'FFFFV11',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,4,-1)*ProjP(-1,1)*ProjP(2,3)')

FFFFV12 = Lorentz(name = 'FFFFV12',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,2,-1)*ProjP(-1,1)*ProjP(4,3)')

FFFFV13 = Lorentz(name = 'FFFFV13',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,4,-1)*ProjM(2,1)*ProjP(-1,3)')

FFFFV14 = Lorentz(name = 'FFFFV14',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,2,-1)*ProjM(4,1)*ProjP(-1,3)')

FFFFV15 = Lorentz(name = 'FFFFV15',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,4,-1)*ProjP(-1,3)*ProjP(2,1)')

FFFFV16 = Lorentz(name = 'FFFFV16',
                  spins = [ 2, 2, 2, 2, 3 ],
                  structure = 'Gamma(5,2,-1)*ProjP(-1,3)*ProjP(4,1)')

FFFFVS1 = Lorentz(name = 'FFFFVS1',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,4,-1)*ProjM(-1,1)*ProjM(2,3)')

FFFFVS2 = Lorentz(name = 'FFFFVS2',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,2,-1)*ProjM(-1,1)*ProjM(4,3)')

FFFFVS3 = Lorentz(name = 'FFFFVS3',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,4,-1)*ProjM(-1,3)*ProjM(2,1)')

FFFFVS4 = Lorentz(name = 'FFFFVS4',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,2,-1)*ProjM(-1,3)*ProjM(4,1)')

FFFFVS5 = Lorentz(name = 'FFFFVS5',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,4,-1)*ProjM(-1,3)*ProjP(2,1)')

FFFFVS6 = Lorentz(name = 'FFFFVS6',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,4,-1)*ProjM(-1,1)*ProjP(2,3)')

FFFFVS7 = Lorentz(name = 'FFFFVS7',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,2,-1)*ProjM(-1,3)*ProjP(4,1)')

FFFFVS8 = Lorentz(name = 'FFFFVS8',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,2,-1)*ProjM(-1,1)*ProjP(4,3)')

FFFFVS9 = Lorentz(name = 'FFFFVS9',
                  spins = [ 2, 2, 2, 2, 3, 1 ],
                  structure = 'Gamma(5,4,-1)*ProjM(2,3)*ProjP(-1,1)')

FFFFVS10 = Lorentz(name = 'FFFFVS10',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,2,-1)*ProjM(4,3)*ProjP(-1,1)')

FFFFVS11 = Lorentz(name = 'FFFFVS11',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,4,-1)*ProjP(-1,1)*ProjP(2,3)')

FFFFVS12 = Lorentz(name = 'FFFFVS12',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,2,-1)*ProjP(-1,1)*ProjP(4,3)')

FFFFVS13 = Lorentz(name = 'FFFFVS13',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,4,-1)*ProjM(2,1)*ProjP(-1,3)')

FFFFVS14 = Lorentz(name = 'FFFFVS14',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,2,-1)*ProjM(4,1)*ProjP(-1,3)')

FFFFVS15 = Lorentz(name = 'FFFFVS15',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,4,-1)*ProjP(-1,3)*ProjP(2,1)')

FFFFVS16 = Lorentz(name = 'FFFFVS16',
                   spins = [ 2, 2, 2, 2, 3, 1 ],
                   structure = 'Gamma(5,2,-1)*ProjP(-1,3)*ProjP(4,1)')

