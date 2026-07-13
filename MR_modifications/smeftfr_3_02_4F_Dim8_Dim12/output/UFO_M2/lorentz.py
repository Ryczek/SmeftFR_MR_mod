# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Fri 27 Jun 2025 17:02:37


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
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(-1,3)*P(-1,4)*P(1,2)*P(2,1) - P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2)*Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,4)*P(4,3)*Metric(1,2) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,3)*Metric(1,2) + P(2,4)*P(4,2)*Metric(1,3) + P(2,3)*P(3,2)*Metric(1,4) + P(1,4)*P(4,1)*Metric(2,3) - P(-1,2)*P(-1,3)*Metric(1,4)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) - P(-1,2)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVS1 = Lorentz(name = 'VVVVS1',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3)')

VVVVS2 = Lorentz(name = 'VVVVS2',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVVS3 = Lorentz(name = 'VVVVS3',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVVS4 = Lorentz(name = 'VVVVS4',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(3,4)*P(4,3)*Metric(1,2) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVS5 = Lorentz(name = 'VVVVS5',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(3,4)*P(4,3)*Metric(1,2) + P(2,4)*P(4,2)*Metric(1,3) + P(2,3)*P(3,2)*Metric(1,4) + P(1,4)*P(4,1)*Metric(2,3) - P(-1,2)*P(-1,3)*Metric(1,4)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) - P(-1,2)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVSS1 = Lorentz(name = 'VVVVSS1',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3)')

VVVVSS2 = Lorentz(name = 'VVVVSS2',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVVSS3 = Lorentz(name = 'VVVVSS3',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVVSS4 = Lorentz(name = 'VVVVSS4',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(3,4)*P(4,3)*Metric(1,2) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVSS5 = Lorentz(name = 'VVVVSS5',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(3,4)*P(4,3)*Metric(1,2) + P(2,4)*P(4,2)*Metric(1,3) + P(2,3)*P(3,2)*Metric(1,4) + P(1,4)*P(4,1)*Metric(2,3) - P(-1,2)*P(-1,3)*Metric(1,4)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) - P(-1,2)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

