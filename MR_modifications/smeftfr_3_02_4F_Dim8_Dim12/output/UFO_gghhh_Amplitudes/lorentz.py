# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Wed 9 Apr 2025 16:27:13


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

SSS2 = Lorentz(name = 'SSS2',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3)')

SSS3 = Lorentz(name = 'SSS3',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)**2 + P(-1,2)**2 + P(-1,3)**2')

SSS4 = Lorentz(name = 'SSS4',
               spins = [ 1, 1, 1 ],
               structure = 'P(-1,1)**2 - (2*P(-1,1)*P(-1,2))/3. + P(-1,2)**2 - (2*P(-1,1)*P(-1,3))/3. - (2*P(-1,2)*P(-1,3))/3. + P(-1,3)**2')

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
               structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4) + P(-1,3)*P(-1,4)')

SSSS3 = Lorentz(name = 'SSSS3',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)**2 + P(-1,2)**2 + P(-1,3)**2 + P(-1,4)**2')

SSSS4 = Lorentz(name = 'SSSS4',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-1,1)**2 + (2*P(-1,1)*P(-1,2))/3. + P(-1,2)**2 + (2*P(-1,1)*P(-1,3))/3. + (2*P(-1,2)*P(-1,3))/3. + P(-1,3)**2 + (2*P(-1,1)*P(-1,4))/3. + (2*P(-1,2)*P(-1,4))/3. + (2*P(-1,3)*P(-1,4))/3. + P(-1,4)**2')

SSSS5 = Lorentz(name = 'SSSS5',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,4)*P(2,3) + P(1,3)*P(2,4)')

VVSS3 = Lorentz(name = 'VVSS3',
                spins = [ 3, 3, 1, 1 ],
                structure = '-(Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4)) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4)')

VVSS4 = Lorentz(name = 'VVSS4',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVSS5 = Lorentz(name = 'VVSS5',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(-1,3)*P(-1,4)*Metric(1,2)')

VVSS6 = Lorentz(name = 'VVSS6',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVSS7 = Lorentz(name = 'VVSS7',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,4)*P(2,3) + P(1,3)*P(2,4) - P(-1,3)*P(-1,4)*Metric(1,2)')

VVSS8 = Lorentz(name = 'VVSS8',
                spins = [ 3, 3, 1, 1 ],
                structure = '-(P(-1,2)*P(-1,4)*P(1,3)*P(2,1)) - P(-1,2)*P(-1,3)*P(1,4)*P(2,1) - P(-1,1)*P(-1,4)*P(1,2)*P(2,3) + P(-1,1)*P(-1,2)*P(1,4)*P(2,3) - P(-1,1)*P(-1,3)*P(1,2)*P(2,4) + P(-1,1)*P(-1,2)*P(1,3)*P(2,4) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4)*Metric(1,2)')

VVSS9 = Lorentz(name = 'VVSS9',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(-1,3)*P(-1,4)*P(1,2)*P(2,1) - P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2)*Metric(1,2)')

VVVS1 = Lorentz(name = 'VVVS1',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVS3 = Lorentz(name = 'VVVS3',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(2,4)*Metric(1,3) - P(1,4)*Metric(2,3)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,2)*P(4,1)*Metric(1,2) + P(3,1)*P(4,2)*Metric(1,2) - P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(3,2)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) - P(1,2)*P(3,1)*Metric(2,4) + P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)*Metric(3,4)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)*Metric(3,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

SSSSS1 = Lorentz(name = 'SSSSS1',
                 spins = [ 1, 1, 1, 1, 1 ],
                 structure = '1')

SSSSS2 = Lorentz(name = 'SSSSS2',
                 spins = [ 1, 1, 1, 1, 1 ],
                 structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4) + P(-1,3)*P(-1,4) + P(-1,1)*P(-1,5) + P(-1,2)*P(-1,5) + P(-1,3)*P(-1,5) + P(-1,4)*P(-1,5)')

SSSSS3 = Lorentz(name = 'SSSSS3',
                 spins = [ 1, 1, 1, 1, 1 ],
                 structure = 'P(-1,1)**2 + (2*P(-1,1)*P(-1,2))/5. + P(-1,2)**2 + (2*P(-1,1)*P(-1,3))/5. + (2*P(-1,2)*P(-1,3))/5. + P(-1,3)**2 + (2*P(-1,1)*P(-1,4))/5. + (2*P(-1,2)*P(-1,4))/5. + (2*P(-1,3)*P(-1,4))/5. + P(-1,4)**2 + (2*P(-1,1)*P(-1,5))/5. + (2*P(-1,2)*P(-1,5))/5. + (2*P(-1,3)*P(-1,5))/5. + (2*P(-1,4)*P(-1,5))/5. + P(-1,5)**2')

VVSSS1 = Lorentz(name = 'VVSSS1',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSSS2 = Lorentz(name = 'VVSSS2',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,4)*P(2,3) + P(1,5)*P(2,3) + P(1,3)*P(2,4) + P(1,5)*P(2,4) + P(1,3)*P(2,5) + P(1,4)*P(2,5)')

VVSSS3 = Lorentz(name = 'VVSSS3',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'Metric(1,2)')

VVSSS4 = Lorentz(name = 'VVSSS4',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVSSS5 = Lorentz(name = 'VVSSS5',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,4)*P(2,3) + P(1,5)*P(2,3) + P(1,3)*P(2,4) + P(1,5)*P(2,4) + P(1,3)*P(2,5) + P(1,4)*P(2,5) - P(-1,3)*P(-1,4)*Metric(1,2) - P(-1,3)*P(-1,5)*Metric(1,2) - P(-1,4)*P(-1,5)*Metric(1,2)')

VVSSS6 = Lorentz(name = 'VVSSS6',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(-1,3)*P(-1,4)*Metric(1,2) + P(-1,3)*P(-1,5)*Metric(1,2) + P(-1,4)*P(-1,5)*Metric(1,2)')

VVVSS1 = Lorentz(name = 'VVVSS1',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVSS2 = Lorentz(name = 'VVVSS2',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = '-(Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,5)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,5)')

VVVSS3 = Lorentz(name = 'VVVSS3',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVSS4 = Lorentz(name = 'VVVSS4',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) - P(1,4)*Metric(2,3) - P(1,5)*Metric(2,3)')

VVVSS5 = Lorentz(name = 'VVVSS5',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(1,5)*P(2,4)*P(3,1) + P(1,4)*P(2,5)*P(3,1) - P(1,5)*P(2,4)*P(3,2) - P(1,4)*P(2,5)*P(3,2) - P(1,5)*P(2,1)*P(3,4) + P(1,5)*P(2,3)*P(3,4) + P(1,2)*P(2,5)*P(3,4) - P(1,3)*P(2,5)*P(3,4) - P(1,4)*P(2,1)*P(3,5) + P(1,4)*P(2,3)*P(3,5) + P(1,2)*P(2,4)*P(3,5) - P(1,3)*P(2,4)*P(3,5) + P(-1,1)*P(-1,5)*P(3,4)*Metric(1,2) - P(-1,2)*P(-1,5)*P(3,4)*Metric(1,2) + P(-1,1)*P(-1,4)*P(3,5)*Metric(1,2) - P(-1,2)*P(-1,4)*P(3,5)*Metric(1,2) - P(-1,1)*P(-1,5)*P(2,4)*Metric(1,3) + P(-1,3)*P(-1,5)*P(2,4)*Metric(1,3) - P(-1,1)*P(-1,4)*P(2,5)*Metric(1,3) + P(-1,3)*P(-1,4)*P(2,5)*Metric(1,3) + P(-1,2)*P(-1,5)*P(1,4)*Metric(2,3) - P(-1,3)*P(-1,5)*P(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*P(1,5)*Metric(2,3) - P(-1,3)*P(-1,4)*P(1,5)*Metric(2,3)')

VVVSS6 = Lorentz(name = 'VVVSS6',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(-1,4)*P(-1,5)*P(3,1)*Metric(1,2) - P(-1,4)*P(-1,5)*P(3,2)*Metric(1,2) - P(-1,4)*P(-1,5)*P(2,1)*Metric(1,3) + P(-1,4)*P(-1,5)*P(2,3)*Metric(1,3) + P(-1,4)*P(-1,5)*P(1,2)*Metric(2,3) - P(-1,4)*P(-1,5)*P(1,3)*Metric(2,3)')

VVVVS1 = Lorentz(name = 'VVVVS1',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVS2 = Lorentz(name = 'VVVVS2',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVVS3 = Lorentz(name = 'VVVVS3',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(3,2)*P(4,1)*Metric(1,2) + P(3,1)*P(4,2)*Metric(1,2) - P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(3,2)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) - P(1,2)*P(3,1)*Metric(2,4) + P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4)')

VVVVS4 = Lorentz(name = 'VVVVS4',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,2)*Metric(3,4)')

VVVVS5 = Lorentz(name = 'VVVVS5',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)*Metric(3,4)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)*Metric(3,4)')

VVVVS6 = Lorentz(name = 'VVVVS6',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVS7 = Lorentz(name = 'VVVVS7',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVS8 = Lorentz(name = 'VVVVS8',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVS9 = Lorentz(name = 'VVVVS9',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVVV1 = Lorentz(name = 'VVVVV1',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) - P(4,3)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,3)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) - P(4,1)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) + P(3,1)*Metric(1,4)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(5,1)*Metric(1,2)*Metric(3,4) - P(5,2)*Metric(1,2)*Metric(3,4) - P(2,1)*Metric(1,5)*Metric(3,4) + P(2,3)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,3)*Metric(2,4)*Metric(3,5)')

VVVVV2 = Lorentz(name = 'VVVVV2',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5)) - Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5) - Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5)')

VVVVV3 = Lorentz(name = 'VVVVV3',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(3,1)*Metric(1,2)*Metric(4,5) - P(3,2)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,3)*Metric(1,3)*Metric(4,5) + P(1,2)*Metric(2,3)*Metric(4,5) - P(1,3)*Metric(2,3)*Metric(4,5)')

SSSSSS1 = Lorentz(name = 'SSSSSS1',
                  spins = [ 1, 1, 1, 1, 1, 1 ],
                  structure = '1')

SSSSSS2 = Lorentz(name = 'SSSSSS2',
                  spins = [ 1, 1, 1, 1, 1, 1 ],
                  structure = 'P(-1,1)*P(-1,2) + P(-1,1)*P(-1,3) + P(-1,2)*P(-1,3) + P(-1,1)*P(-1,4) + P(-1,2)*P(-1,4) + P(-1,3)*P(-1,4) + P(-1,1)*P(-1,5) + P(-1,2)*P(-1,5) + P(-1,3)*P(-1,5) + P(-1,4)*P(-1,5) + P(-1,1)*P(-1,6) + P(-1,2)*P(-1,6) + P(-1,3)*P(-1,6) + P(-1,4)*P(-1,6) + P(-1,5)*P(-1,6)')

SSSSSS3 = Lorentz(name = 'SSSSSS3',
                  spins = [ 1, 1, 1, 1, 1, 1 ],
                  structure = 'P(-1,1)**2 + (2*P(-1,1)*P(-1,2))/5. + P(-1,2)**2 + (2*P(-1,1)*P(-1,3))/5. + (2*P(-1,2)*P(-1,3))/5. + P(-1,3)**2 + (2*P(-1,1)*P(-1,4))/5. + (2*P(-1,2)*P(-1,4))/5. + (2*P(-1,3)*P(-1,4))/5. + P(-1,4)**2 + (2*P(-1,1)*P(-1,5))/5. + (2*P(-1,2)*P(-1,5))/5. + (2*P(-1,3)*P(-1,5))/5. + (2*P(-1,4)*P(-1,5))/5. + P(-1,5)**2 + (2*P(-1,1)*P(-1,6))/5. + (2*P(-1,2)*P(-1,6))/5. + (2*P(-1,3)*P(-1,6))/5. + (2*P(-1,4)*P(-1,6))/5. + (2*P(-1,5)*P(-1,6))/5. + P(-1,6)**2')

VVSSSS1 = Lorentz(name = 'VVSSSS1',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSSSS2 = Lorentz(name = 'VVSSSS2',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(1,4)*P(2,3) + P(1,5)*P(2,3) + P(1,6)*P(2,3) + P(1,3)*P(2,4) + P(1,5)*P(2,4) + P(1,6)*P(2,4) + P(1,3)*P(2,5) + P(1,4)*P(2,5) + P(1,6)*P(2,5) + P(1,3)*P(2,6) + P(1,4)*P(2,6) + P(1,5)*P(2,6)')

VVSSSS3 = Lorentz(name = 'VVSSSS3',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'Metric(1,2)')

VVSSSS4 = Lorentz(name = 'VVSSSS4',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVSSSS5 = Lorentz(name = 'VVSSSS5',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(1,4)*P(2,3) + P(1,5)*P(2,3) + P(1,6)*P(2,3) + P(1,3)*P(2,4) + P(1,5)*P(2,4) + P(1,6)*P(2,4) + P(1,3)*P(2,5) + P(1,4)*P(2,5) + P(1,6)*P(2,5) + P(1,3)*P(2,6) + P(1,4)*P(2,6) + P(1,5)*P(2,6) - P(-1,3)*P(-1,4)*Metric(1,2) - P(-1,3)*P(-1,5)*Metric(1,2) - P(-1,4)*P(-1,5)*Metric(1,2) - P(-1,3)*P(-1,6)*Metric(1,2) - P(-1,4)*P(-1,6)*Metric(1,2) - P(-1,5)*P(-1,6)*Metric(1,2)')

VVSSSS6 = Lorentz(name = 'VVSSSS6',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(-1,3)*P(-1,4)*Metric(1,2) + P(-1,3)*P(-1,5)*Metric(1,2) + P(-1,4)*P(-1,5)*Metric(1,2) + P(-1,3)*P(-1,6)*Metric(1,2) + P(-1,4)*P(-1,6)*Metric(1,2) + P(-1,5)*P(-1,6)*Metric(1,2)')

VVVSSS1 = Lorentz(name = 'VVVSSS1',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVSSS2 = Lorentz(name = 'VVVSSS2',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVSSS3 = Lorentz(name = 'VVVSSS3',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(2,6)*Metric(1,3) - P(1,4)*Metric(2,3) - P(1,5)*Metric(2,3) - P(1,6)*Metric(2,3)')

VVVVSS1 = Lorentz(name = 'VVVVSS1',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(2,6)*P(4,5)*Metric(1,3) + P(2,5)*P(4,6)*Metric(1,3) - P(2,6)*P(3,5)*Metric(1,4) - P(2,5)*P(3,6)*Metric(1,4) - P(1,6)*P(4,5)*Metric(2,3) - P(1,5)*P(4,6)*Metric(2,3) + P(1,6)*P(3,5)*Metric(2,4) + P(1,5)*P(3,6)*Metric(2,4)')

VVVVSS2 = Lorentz(name = 'VVVVSS2',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVSS3 = Lorentz(name = 'VVVVSS3',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVVSS4 = Lorentz(name = 'VVVVSS4',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(3,2)*P(4,1)*Metric(1,2) + P(3,1)*P(4,2)*Metric(1,2) - P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(3,2)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) - P(1,2)*P(3,1)*Metric(2,4) + P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4)')

VVVVSS5 = Lorentz(name = 'VVVVSS5',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(-1,5)*P(-1,6)*Metric(1,4)*Metric(2,3) - P(-1,5)*P(-1,6)*Metric(1,3)*Metric(2,4)')

VVVVSS6 = Lorentz(name = 'VVVVSS6',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,2)*Metric(3,4)')

VVVVSS7 = Lorentz(name = 'VVVVSS7',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)*Metric(3,4)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)*Metric(3,4)')

VVVVSS8 = Lorentz(name = 'VVVVSS8',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(3,6)*P(4,5)*Metric(1,2) + P(3,5)*P(4,6)*Metric(1,2) - P(2,6)*P(3,5)*Metric(1,4) - P(2,5)*P(3,6)*Metric(1,4) - P(1,6)*P(4,5)*Metric(2,3) - P(1,5)*P(4,6)*Metric(2,3) + P(1,6)*P(2,5)*Metric(3,4) + P(1,5)*P(2,6)*Metric(3,4)')

VVVVSS9 = Lorentz(name = 'VVVVSS9',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'P(3,6)*P(4,5)*Metric(1,2) + P(3,5)*P(4,6)*Metric(1,2) - P(2,6)*P(4,5)*Metric(1,3) - P(2,5)*P(4,6)*Metric(1,3) - P(1,6)*P(3,5)*Metric(2,4) - P(1,5)*P(3,6)*Metric(2,4) + P(1,6)*P(2,5)*Metric(3,4) + P(1,5)*P(2,6)*Metric(3,4)')

VVVVSS10 = Lorentz(name = 'VVVVSS10',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVSS11 = Lorentz(name = 'VVVVSS11',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVSS12 = Lorentz(name = 'VVVVSS12',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVSS13 = Lorentz(name = 'VVVVSS13',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVVSS14 = Lorentz(name = 'VVVVSS14',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,4)*Metric(2,3) - P(-1,5)*P(-1,6)*Metric(1,2)*Metric(3,4)')

VVVVSS15 = Lorentz(name = 'VVVVSS15',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,3)*Metric(2,4) - P(-1,5)*P(-1,6)*Metric(1,2)*Metric(3,4)')

VVVVVS1 = Lorentz(name = 'VVVVVS1',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) - P(4,3)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,3)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) - P(4,1)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) + P(3,1)*Metric(1,4)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(5,1)*Metric(1,2)*Metric(3,4) - P(5,2)*Metric(1,2)*Metric(3,4) - P(2,1)*Metric(1,5)*Metric(3,4) + P(2,3)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,3)*Metric(2,4)*Metric(3,5)')

VVVVVS2 = Lorentz(name = 'VVVVVS2',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5)) - Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5) - Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5)')

VVVVVS3 = Lorentz(name = 'VVVVVS3',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(3,1)*Metric(1,2)*Metric(4,5) - P(3,2)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,3)*Metric(1,3)*Metric(4,5) + P(1,2)*Metric(2,3)*Metric(4,5) - P(1,3)*Metric(2,3)*Metric(4,5)')

VVVVVV1 = Lorentz(name = 'VVVVVV1',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,4)*Metric(2,6)*Metric(3,5) + Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,3)*Metric(2,5)*Metric(4,6)')

VVVVVV2 = Lorentz(name = 'VVVVVV2',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVV3 = Lorentz(name = 'VVVVVV3',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVV4 = Lorentz(name = 'VVVVVV4',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVV5 = Lorentz(name = 'VVVVVV5',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV6 = Lorentz(name = 'VVVVVV6',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

SSSSSSS1 = Lorentz(name = 'SSSSSSS1',
                   spins = [ 1, 1, 1, 1, 1, 1, 1 ],
                   structure = '1')

VVSSSSS1 = Lorentz(name = 'VVSSSSS1',
                   spins = [ 3, 3, 1, 1, 1, 1, 1 ],
                   structure = 'Metric(1,2)')

VVVSSSS1 = Lorentz(name = 'VVVSSSS1',
                   spins = [ 3, 3, 3, 1, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVSSSS2 = Lorentz(name = 'VVVSSSS2',
                   spins = [ 3, 3, 3, 1, 1, 1, 1 ],
                   structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVSSSS3 = Lorentz(name = 'VVVSSSS3',
                   spins = [ 3, 3, 3, 1, 1, 1, 1 ],
                   structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(2,6)*Metric(1,3) + P(2,7)*Metric(1,3) - P(1,4)*Metric(2,3) - P(1,5)*Metric(2,3) - P(1,6)*Metric(2,3) - P(1,7)*Metric(2,3)')

VVVVSSS1 = Lorentz(name = 'VVVVSSS1',
                   spins = [ 3, 3, 3, 3, 1, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVSSS2 = Lorentz(name = 'VVVVSSS2',
                   spins = [ 3, 3, 3, 3, 1, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVVSSS3 = Lorentz(name = 'VVVVSSS3',
                   spins = [ 3, 3, 3, 3, 1, 1, 1 ],
                   structure = 'Metric(1,2)*Metric(3,4)')

VVVVSSS4 = Lorentz(name = 'VVVVSSS4',
                   spins = [ 3, 3, 3, 3, 1, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVSSS5 = Lorentz(name = 'VVVVSSS5',
                   spins = [ 3, 3, 3, 3, 1, 1, 1 ],
                   structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVSSS6 = Lorentz(name = 'VVVVSSS6',
                   spins = [ 3, 3, 3, 3, 1, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVVSS1 = Lorentz(name = 'VVVVVSS1',
                   spins = [ 3, 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) - P(4,3)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,3)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) - P(4,1)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) + P(3,1)*Metric(1,4)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(5,1)*Metric(1,2)*Metric(3,4) - P(5,2)*Metric(1,2)*Metric(3,4) - P(2,1)*Metric(1,5)*Metric(3,4) + P(2,3)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,3)*Metric(2,4)*Metric(3,5)')

VVVVVSS2 = Lorentz(name = 'VVVVVSS2',
                   spins = [ 3, 3, 3, 3, 3, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5)) - Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5) - Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5)')

VVVVVSS3 = Lorentz(name = 'VVVVVSS3',
                   spins = [ 3, 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,1)*Metric(1,2)*Metric(4,5) - P(3,2)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,3)*Metric(1,3)*Metric(4,5) + P(1,2)*Metric(2,3)*Metric(4,5) - P(1,3)*Metric(2,3)*Metric(4,5)')

VVVVVVS1 = Lorentz(name = 'VVVVVVS1',
                   spins = [ 3, 3, 3, 3, 3, 3, 1 ],
                   structure = 'Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,4)*Metric(2,6)*Metric(3,5) + Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,3)*Metric(2,5)*Metric(4,6)')

VVVVVVS2 = Lorentz(name = 'VVVVVVS2',
                   spins = [ 3, 3, 3, 3, 3, 3, 1 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVVS3 = Lorentz(name = 'VVVVVVS3',
                   spins = [ 3, 3, 3, 3, 3, 3, 1 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVVS4 = Lorentz(name = 'VVVVVVS4',
                   spins = [ 3, 3, 3, 3, 3, 3, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVVS5 = Lorentz(name = 'VVVVVVS5',
                   spins = [ 3, 3, 3, 3, 3, 3, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVVS6 = Lorentz(name = 'VVVVVVS6',
                   spins = [ 3, 3, 3, 3, 3, 3, 1 ],
                   structure = 'Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

SSSSSSSS1 = Lorentz(name = 'SSSSSSSS1',
                    spins = [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                    structure = '1')

VVSSSSSS1 = Lorentz(name = 'VVSSSSSS1',
                    spins = [ 3, 3, 1, 1, 1, 1, 1, 1 ],
                    structure = 'Metric(1,2)')

VVVVSSSS1 = Lorentz(name = 'VVVVSSSS1',
                    spins = [ 3, 3, 3, 3, 1, 1, 1, 1 ],
                    structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVSSSS2 = Lorentz(name = 'VVVVSSSS2',
                    spins = [ 3, 3, 3, 3, 1, 1, 1, 1 ],
                    structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVVSSSS3 = Lorentz(name = 'VVVVSSSS3',
                    spins = [ 3, 3, 3, 3, 1, 1, 1, 1 ],
                    structure = 'Metric(1,2)*Metric(3,4)')

VVVVSSSS4 = Lorentz(name = 'VVVVSSSS4',
                    spins = [ 3, 3, 3, 3, 1, 1, 1, 1 ],
                    structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVSSSS5 = Lorentz(name = 'VVVVSSSS5',
                    spins = [ 3, 3, 3, 3, 1, 1, 1, 1 ],
                    structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVSSSS6 = Lorentz(name = 'VVVVSSSS6',
                    spins = [ 3, 3, 3, 3, 1, 1, 1, 1 ],
                    structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVVVSS1 = Lorentz(name = 'VVVVVVSS1',
                    spins = [ 3, 3, 3, 3, 3, 3, 1, 1 ],
                    structure = 'Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,4)*Metric(2,6)*Metric(3,5) + Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,3)*Metric(2,5)*Metric(4,6)')

VVVVVVSS2 = Lorentz(name = 'VVVVVVSS2',
                    spins = [ 3, 3, 3, 3, 3, 3, 1, 1 ],
                    structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVVSS3 = Lorentz(name = 'VVVVVVSS3',
                    spins = [ 3, 3, 3, 3, 3, 3, 1, 1 ],
                    structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVVSS4 = Lorentz(name = 'VVVVVVSS4',
                    spins = [ 3, 3, 3, 3, 3, 3, 1, 1 ],
                    structure = 'Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVVSS5 = Lorentz(name = 'VVVVVVSS5',
                    spins = [ 3, 3, 3, 3, 3, 3, 1, 1 ],
                    structure = 'Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVVSS6 = Lorentz(name = 'VVVVVVSS6',
                    spins = [ 3, 3, 3, 3, 3, 3, 1, 1 ],
                    structure = 'Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

