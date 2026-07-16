# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Mac OS X x86 (64-bit) (July 8, 2025)
# Date: Thu 16 Jul 2026 22:50:39


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
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

FFVS1 = Lorentz(name = 'FFVS1',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(-2,3)*P(-1,4)*P(3,2)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*ProjM(-3,1) - P(-2,3)*P(-1,4)*P(3,2)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjM(-3,1) + P(-2,2)*P(-2,3)*P(-1,4)*Gamma(-1,2,-4)*Gamma(3,-4,-3)*ProjM(-3,1) - P(-2,2)*P(-2,3)*P(-1,4)*Gamma(-1,-4,-3)*Gamma(3,2,-4)*ProjM(-3,1)')

FFVS2 = Lorentz(name = 'FFVS2',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(-2,3)*P(-1,4)*P(3,1)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*ProjP(-3,1) - P(-2,3)*P(-1,4)*P(3,1)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjP(-3,1) + P(-2,1)*P(-2,3)*P(-1,4)*Gamma(-1,2,-4)*Gamma(3,-4,-3)*ProjP(-3,1) - P(-2,1)*P(-2,3)*P(-1,4)*Gamma(-1,-4,-3)*Gamma(3,2,-4)*ProjP(-3,1)')

FFVS3 = Lorentz(name = 'FFVS3',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(-2,3)*P(-1,4)*P(3,2)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*ProjM(-3,1) - P(-2,3)*P(-1,4)*P(3,2)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjM(-3,1) + P(-2,2)*P(-2,3)*P(-1,4)*Gamma(-1,2,-4)*Gamma(3,-4,-3)*ProjM(-3,1) - P(-2,2)*P(-2,3)*P(-1,4)*Gamma(-1,-4,-3)*Gamma(3,2,-4)*ProjM(-3,1) + P(-2,3)*P(-1,4)*P(3,1)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*ProjP(-3,1) - P(-2,3)*P(-1,4)*P(3,1)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*ProjP(-3,1) + P(-2,1)*P(-2,3)*P(-1,4)*Gamma(-1,2,-4)*Gamma(3,-4,-3)*ProjP(-3,1) - P(-2,1)*P(-2,3)*P(-1,4)*Gamma(-1,-4,-3)*Gamma(3,2,-4)*ProjP(-3,1)')

FFVV1 = Lorentz(name = 'FFVV1',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVV2 = Lorentz(name = 'FFVV2',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1)) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVV3 = Lorentz(name = 'FFVV3',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVV4 = Lorentz(name = 'FFVV4',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1)) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVV5 = Lorentz(name = 'FFVV5',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVV6 = Lorentz(name = 'FFVV6',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1)) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVV7 = Lorentz(name = 'FFVV7',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVV8 = Lorentz(name = 'FFVV8',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1)) + P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVV9 = Lorentz(name = 'FFVV9',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

FFVVS1 = Lorentz(name = 'FFVVS1',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = '-(P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS2 = Lorentz(name = 'FFVVS2',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = '-(P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1)) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS3 = Lorentz(name = 'FFVVS3',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'P(-1,5)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,5)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,5)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS4 = Lorentz(name = 'FFVVS4',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'P(-1,2)*P(-1,3)*Gamma(3,2,-2)*Gamma(4,-2,-3)*ProjM(-3,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS5 = Lorentz(name = 'FFVVS5',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = '2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS6 = Lorentz(name = 'FFVVS6',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVVS7 = Lorentz(name = 'FFVVS7',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-1,5)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,5)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) + P(-1,5)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,5)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS8 = Lorentz(name = 'FFVVS8',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = '-(P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1)) + P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVVS9 = Lorentz(name = 'FFVVS9',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = '2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + 2*P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + 2*P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - 2*P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS10 = Lorentz(name = 'FFVVS10',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + P(-1,5)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,5)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,5)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS11 = Lorentz(name = 'FFVVS11',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS12 = Lorentz(name = 'FFVVS12',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1)) - P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1)')

FFVVS13 = Lorentz(name = 'FFVVS13',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS14 = Lorentz(name = 'FFVVS14',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1)) + P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS15 = Lorentz(name = 'FFVVS15',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) - P(-1,5)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,5)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,5)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,5)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS16 = Lorentz(name = 'FFVVS16',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-1,5)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,5)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,5)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,5)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS17 = Lorentz(name = 'FFVVS17',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-1,4)*P(4,1)*Gamma(-1,-2,-3)*Gamma(3,2,-2)*ProjP(-3,1) - P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS18 = Lorentz(name = 'FFVVS18',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS19 = Lorentz(name = 'FFVVS19',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVVS20 = Lorentz(name = 'FFVVS20',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-1,5)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,5)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,5)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS21 = Lorentz(name = 'FFVVS21',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1)) + P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVVS22 = Lorentz(name = 'FFVVS22',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS23 = Lorentz(name = 'FFVVS23',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + 2*P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - 2*P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + 2*P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - 2*P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS24 = Lorentz(name = 'FFVVS24',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-1,5)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,5)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,5)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS25 = Lorentz(name = 'FFVVS25',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS26 = Lorentz(name = 'FFVVS26',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1)) - P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS27 = Lorentz(name = 'FFVVS27',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS28 = Lorentz(name = 'FFVVS28',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = 'P(-1,5)*P(3,4)*Gamma(-1,2,-2)*Gamma(4,-2,-3)*ProjM(-3,1) + P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) + P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) - P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) - P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) - P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS29 = Lorentz(name = 'FFVVS29',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + 2*P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + 2*P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - 2*P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - 2*P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + 2*P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - 2*P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + 2*P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVS30 = Lorentz(name = 'FFVVS30',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '2*P(-1,5)*P(3,4)*Gamma(-1,2,-2)*Gamma(4,-2,-3)*ProjM(-3,1) + 2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) + 2*P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - 2*P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjM(-3,1) - P(-1,4)*P(4,2)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1) + P(-1,4)*P(4,2)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,3)*P(3,2)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,2)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) - P(-1,2)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjM(-2,1) + P(-1,3)*P(3,2)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - 2*P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - P(-1,2)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) + P(-1,2)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjM(-2,1) - 2*P(-2,3)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) - 2*P(-2,4)*P(-1,5)*Gamma(-2,2,-4)*Gamma(-1,-4,-3)*Metric(3,4)*ProjP(-3,1) + 2*P(-2,3)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + 2*P(-2,4)*P(-1,5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Metric(3,4)*ProjP(-3,1) + P(-1,4)*P(4,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - 2*P(-1,5)*P(4,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,4)*P(4,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + 2*P(-1,5)*P(4,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1) + P(-1,3)*P(3,1)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - 2*P(-1,5)*P(3,4)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,1)*P(-1,3)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) + P(-1,1)*P(-1,4)*Gamma(3,2,-3)*Gamma(4,-3,-2)*ProjP(-2,1) - P(-1,3)*P(3,1)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + 2*P(-1,5)*P(3,4)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) + P(-1,1)*P(-1,3)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1) - P(-1,1)*P(-1,4)*Gamma(3,-3,-2)*Gamma(4,2,-3)*ProjP(-2,1)')

FFVVV1 = Lorentz(name = 'FFVVV1',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV2 = Lorentz(name = 'FFVVV2',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV3 = Lorentz(name = 'FFVVV3',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV4 = Lorentz(name = 'FFVVV4',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV5 = Lorentz(name = 'FFVVV5',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVVV6 = Lorentz(name = 'FFVVV6',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV7 = Lorentz(name = 'FFVVV7',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV8 = Lorentz(name = 'FFVVV8',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV9 = Lorentz(name = 'FFVVV9',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV10 = Lorentz(name = 'FFVVV10',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV11 = Lorentz(name = 'FFVVV11',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV12 = Lorentz(name = 'FFVVV12',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV13 = Lorentz(name = 'FFVVV13',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVV14 = Lorentz(name = 'FFVVV14',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV15 = Lorentz(name = 'FFVVV15',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV16 = Lorentz(name = 'FFVVV16',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV17 = Lorentz(name = 'FFVVV17',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV18 = Lorentz(name = 'FFVVV18',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV19 = Lorentz(name = 'FFVVV19',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV20 = Lorentz(name = 'FFVVV20',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV21 = Lorentz(name = 'FFVVV21',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV22 = Lorentz(name = 'FFVVV22',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV23 = Lorentz(name = 'FFVVV23',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV24 = Lorentz(name = 'FFVVV24',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(3,4)*Gamma(4,2,-1)*Gamma(5,-1,-2)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV25 = Lorentz(name = 'FFVVV25',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1)) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV26 = Lorentz(name = 'FFVVV26',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV27 = Lorentz(name = 'FFVVV27',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV28 = Lorentz(name = 'FFVVV28',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVVV29 = Lorentz(name = 'FFVVV29',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV30 = Lorentz(name = 'FFVVV30',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVVV31 = Lorentz(name = 'FFVVV31',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV32 = Lorentz(name = 'FFVVV32',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV33 = Lorentz(name = 'FFVVV33',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV34 = Lorentz(name = 'FFVVV34',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV35 = Lorentz(name = 'FFVVV35',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVV36 = Lorentz(name = 'FFVVV36',
                  spins = [ 2, 2, 3, 3, 3 ],
                  structure = 'P(3,5)*Gamma(4,-1,-2)*Gamma(5,2,-1)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS1 = Lorentz(name = 'FFVVVS1',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = 'P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS2 = Lorentz(name = 'FFVVVS2',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = 'P(5,2)*Gamma(3,-1,-2)*Gamma(4,2,-1)*ProjM(-2,1) - P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS3 = Lorentz(name = 'FFVVVS3',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS4 = Lorentz(name = 'FFVVVS4',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS5 = Lorentz(name = 'FFVVVS5',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS6 = Lorentz(name = 'FFVVVS6',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS7 = Lorentz(name = 'FFVVVS7',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS8 = Lorentz(name = 'FFVVVS8',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = '-2*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) - 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS9 = Lorentz(name = 'FFVVVS9',
                  spins = [ 2, 2, 3, 3, 3, 1 ],
                  structure = 'P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) - 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS10 = Lorentz(name = 'FFVVVS10',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS11 = Lorentz(name = 'FFVVVS11',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS12 = Lorentz(name = 'FFVVVS12',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '2*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS13 = Lorentz(name = 'FFVVVS13',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) - P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + (P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1))/2. - (P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1))/2. - (P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1))/2. + (P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1))/2.')

FFVVVS14 = Lorentz(name = 'FFVVVS14',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) - P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS15 = Lorentz(name = 'FFVVVS15',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,4)*Gamma(-1,2,-2)*Gamma(5,-2,-3)*Metric(3,4)*ProjM(-3,1)) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1)')

FFVVVS16 = Lorentz(name = 'FFVVVS16',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = 'P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS17 = Lorentz(name = 'FFVVVS17',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS18 = Lorentz(name = 'FFVVVS18',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS19 = Lorentz(name = 'FFVVVS19',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS20 = Lorentz(name = 'FFVVVS20',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS21 = Lorentz(name = 'FFVVVS21',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS22 = Lorentz(name = 'FFVVVS22',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS23 = Lorentz(name = 'FFVVVS23',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS24 = Lorentz(name = 'FFVVVS24',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = 'P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS25 = Lorentz(name = 'FFVVVS25',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS26 = Lorentz(name = 'FFVVVS26',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjM(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS27 = Lorentz(name = 'FFVVVS27',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-2*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS28 = Lorentz(name = 'FFVVVS28',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = 'P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(4,5)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(4,5)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS29 = Lorentz(name = 'FFVVVS29',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) - P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(4,3)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,3)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS30 = Lorentz(name = 'FFVVVS30',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,4)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) + P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1) - P(3,4)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS31 = Lorentz(name = 'FFVVVS31',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '2*P(-1,6)*Gamma(-1,2,-3)*Gamma(5,-3,-2)*Metric(3,4)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(5,2,-3)*Metric(3,4)*ProjP(-2,1) - P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,5)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - 4*P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,5)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + 4*P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + 2*P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - 2*P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(3,5)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(3,5)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS32 = Lorentz(name = 'FFVVVS32',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1)) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) + P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS33 = Lorentz(name = 'FFVVVS33',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1)) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + (P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1))/2. - (P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1))/2. - (P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1))/2. + (P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1))/2.')

FFVVVS34 = Lorentz(name = 'FFVVVS34',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) - P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,2)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,2)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(5,1)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,1)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) + P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1) - P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1)')

FFVVVS35 = Lorentz(name = 'FFVVVS35',
                   spins = [ 2, 2, 3, 3, 3, 1 ],
                   structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1)) - P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjM(-2,1) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjM(-2,1) + P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjM(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjM(-2,1) + P(5,3)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - P(5,3)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + (P(4,2)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1))/2. - (P(3,2)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjM(-1,1))/2. - (P(4,2)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1))/2. + (P(3,2)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjM(-1,1))/2. + P(-1,6)*Gamma(-1,2,-3)*Gamma(4,-3,-2)*Metric(3,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,-3,-2)*Gamma(4,2,-3)*Metric(3,5)*ProjP(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) - P(-1,6)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*Metric(4,5)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) + P(-1,6)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*Metric(4,5)*ProjP(-2,1) - P(5,4)*Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + P(5,4)*Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1) - (P(4,1)*Gamma(3,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1))/2. + (P(3,1)*Gamma(4,2,-2)*Gamma(5,-2,-1)*ProjP(-1,1))/2. + (P(4,1)*Gamma(3,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1))/2. - (P(3,1)*Gamma(4,-2,-1)*Gamma(5,2,-2)*ProjP(-1,1))/2.')

FFVVVV1 = Lorentz(name = 'FFVVVV1',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = 'Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1)')

FFVVVV2 = Lorentz(name = 'FFVVVV2',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '-2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1)')

FFVVVV3 = Lorentz(name = 'FFVVVV3',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '-(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1)) + Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVV4 = Lorentz(name = 'FFVVVV4',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVV5 = Lorentz(name = 'FFVVVV5',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '-2*Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVV6 = Lorentz(name = 'FFVVVV6',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVV7 = Lorentz(name = 'FFVVVV7',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVV8 = Lorentz(name = 'FFVVVV8',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/4. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVV9 = Lorentz(name = 'FFVVVV9',
                  spins = [ 2, 2, 3, 3, 3, 3 ],
                  structure = 'Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVV10 = Lorentz(name = 'FFVVVV10',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = 'Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVV11 = Lorentz(name = 'FFVVVV11',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = 'Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) - Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1)')

FFVVVV12 = Lorentz(name = 'FFVVVV12',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1)')

FFVVVV13 = Lorentz(name = 'FFVVVV13',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) - 2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) - Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV14 = Lorentz(name = 'FFVVVV14',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1)) + Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) - (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1))/2. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/2.')

FFVVVV15 = Lorentz(name = 'FFVVVV15',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = 'Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV16 = Lorentz(name = 'FFVVVV16',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) - 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV17 = Lorentz(name = 'FFVVVV17',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-2*Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) + 2*Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV18 = Lorentz(name = 'FFVVVV18',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV19 = Lorentz(name = 'FFVVVV19',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) - Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV20 = Lorentz(name = 'FFVVVV20',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1)) + Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV21 = Lorentz(name = 'FFVVVV21',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + (Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV22 = Lorentz(name = 'FFVVVV22',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-0.5*(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1)) + (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1))/2. + (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/2. + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV23 = Lorentz(name = 'FFVVVV23',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) + 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV24 = Lorentz(name = 'FFVVVV24',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-0.5*(Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1)) + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/2. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV25 = Lorentz(name = 'FFVVVV25',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1) - (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/2. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV26 = Lorentz(name = 'FFVVVV26',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-0.25*(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1)) + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/4. - (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1))/4. + (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV27 = Lorentz(name = 'FFVVVV27',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/4. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1) - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/4. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/4. - (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1))/4. + (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV28 = Lorentz(name = 'FFVVVV28',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = 'Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVV29 = Lorentz(name = 'FFVVVV29',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-2*Gamma(5,-1,-2)*Gamma(6,2,-1)*Metric(3,4)*ProjP(-2,1) + 2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVV30 = Lorentz(name = 'FFVVVV30',
                   spins = [ 2, 2, 3, 3, 3, 3 ],
                   structure = '-(Gamma(3,2,-1)*Gamma(4,-1,-2)*Metric(5,6)*ProjP(-2,1)) + (Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS1 = Lorentz(name = 'FFVVVVS1',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = 'Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1)')

FFVVVVS2 = Lorentz(name = 'FFVVVVS2',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '-2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1)')

FFVVVVS3 = Lorentz(name = 'FFVVVVS3',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '-(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1)) + Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVVS4 = Lorentz(name = 'FFVVVVS4',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVVS5 = Lorentz(name = 'FFVVVVS5',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '-2*Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVVS6 = Lorentz(name = 'FFVVVVS6',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1)')

FFVVVVS7 = Lorentz(name = 'FFVVVVS7',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVVS8 = Lorentz(name = 'FFVVVVS8',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/4. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVVS9 = Lorentz(name = 'FFVVVVS9',
                   spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                   structure = 'Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVVS10 = Lorentz(name = 'FFVVVVS10',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = 'Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1)')

FFVVVVS11 = Lorentz(name = 'FFVVVVS11',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = 'Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) - Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1)')

FFVVVVS12 = Lorentz(name = 'FFVVVVS12',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1)')

FFVVVVS13 = Lorentz(name = 'FFVVVVS13',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) - 2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) + 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) - Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVVS14 = Lorentz(name = 'FFVVVVS14',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = 'Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVVS15 = Lorentz(name = 'FFVVVVS15',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '2*Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1) - 2*Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVVS16 = Lorentz(name = 'FFVVVVS16',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-2*Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) + 2*Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVVS17 = Lorentz(name = 'FFVVVVS17',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVVS18 = Lorentz(name = 'FFVVVVS18',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) - Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1)')

FFVVVVS19 = Lorentz(name = 'FFVVVVS19',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1)) + Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) - 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS20 = Lorentz(name = 'FFVVVVS20',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjM(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1) + (Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1))/2. - (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1))/2. - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/2. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/2. - Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) + Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS21 = Lorentz(name = 'FFVVVVS21',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-0.5*(Gamma(5,2,-2)*Gamma(6,-2,-1)*Metric(3,4)*ProjP(-1,1)) + (Gamma(5,-2,-1)*Gamma(6,2,-2)*Metric(3,4)*ProjP(-1,1))/2. + (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/2. + Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS22 = Lorentz(name = 'FFVVVVS22',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1)) + Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1) + 2*Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1) - 2*Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS23 = Lorentz(name = 'FFVVVVS23',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-0.5*(Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1)) + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/2. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS24 = Lorentz(name = 'FFVVVVS24',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/2. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/2. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1) - (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/2. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/2. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/2. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS25 = Lorentz(name = 'FFVVVVS25',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '-0.25*(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1)) + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/4. - (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1))/4. + (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS26 = Lorentz(name = 'FFVVVVS26',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = '(Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjM(-1,1))/4. + (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjM(-1,1))/4. - (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjM(-1,1))/4. + (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjM(-1,1))/4. - (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjM(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjM(-1,1) - (Gamma(4,2,-2)*Gamma(6,-2,-1)*Metric(3,5)*ProjP(-1,1))/4. + (Gamma(4,-2,-1)*Gamma(6,2,-2)*Metric(3,5)*ProjP(-1,1))/4. - (Gamma(4,2,-2)*Gamma(5,-2,-1)*Metric(3,6)*ProjP(-1,1))/4. + (Gamma(4,-2,-1)*Gamma(5,2,-2)*Metric(3,6)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1))/4. - (Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1))/4. + (Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1))/4. + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

FFVVVVS27 = Lorentz(name = 'FFVVVVS27',
                    spins = [ 2, 2, 3, 3, 3, 3, 1 ],
                    structure = 'Gamma(3,2,-2)*Gamma(6,-2,-1)*Metric(4,5)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(6,2,-2)*Metric(4,5)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(5,-2,-1)*Metric(4,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(5,2,-2)*Metric(4,6)*ProjP(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*Metric(5,6)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*Metric(5,6)*ProjP(-1,1)')

