# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Mac OS X x86 (64-bit) (July 8, 2025)
# Date: Thu 16 Jul 2026 22:50:39



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
alphas = Parameter(name = 'alphas',
                   nature = 'external',
                   type = 'real',
                   value = 0.1176,
                   texname = '\\alpha _s',
                   lhablock = 'FRBlock',
                   lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011638081097590524,
               texname = 'G_F',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

AEM = Parameter(name = 'AEM',
                nature = 'external',
                type = 'real',
                value = 0.0072973525692838015,
                texname = '\\alpha _{\\text{em}}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

Zmass = Parameter(name = 'Zmass',
                  nature = 'external',
                  type = 'real',
                  value = 91.1876,
                  texname = 'M_Z',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

Wmass = Parameter(name = 'Wmass',
                  nature = 'external',
                  type = 'real',
                  value = 80.379,
                  texname = 'M_W',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

Hmass = Parameter(name = 'Hmass',
                  nature = 'external',
                  type = 'real',
                  value = 125.35,
                  texname = 'M_H',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

tmass = Parameter(name = 'tmass',
                  nature = 'external',
                  type = 'real',
                  value = 172.76,
                  texname = 'm_t',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

cmass = Parameter(name = 'cmass',
                  nature = 'external',
                  type = 'real',
                  value = 1.27,
                  texname = 'm_c',
                  lhablock = 'FRBlock',
                  lhacode = [ 8 ])

umass = Parameter(name = 'umass',
                  nature = 'external',
                  type = 'real',
                  value = 0.0025499999999999997,
                  texname = 'm_u',
                  lhablock = 'FRBlock',
                  lhacode = [ 9 ])

bmass = Parameter(name = 'bmass',
                  nature = 'external',
                  type = 'real',
                  value = 4.7,
                  texname = 'm_b',
                  lhablock = 'FRBlock',
                  lhacode = [ 10 ])

smass = Parameter(name = 'smass',
                  nature = 'external',
                  type = 'real',
                  value = 0.101,
                  texname = 'm_s',
                  lhablock = 'FRBlock',
                  lhacode = [ 11 ])

dmass = Parameter(name = 'dmass',
                  nature = 'external',
                  type = 'real',
                  value = 0.00504,
                  texname = 'm_d',
                  lhablock = 'FRBlock',
                  lhacode = [ 12 ])

taumass = Parameter(name = 'taumass',
                    nature = 'external',
                    type = 'real',
                    value = 1.77686,
                    texname = 'm_{\\tau }',
                    lhablock = 'FRBlock',
                    lhacode = [ 13 ])

mumass = Parameter(name = 'mumass',
                   nature = 'external',
                   type = 'real',
                   value = 0.1056583755,
                   texname = 'm_{\\mu }',
                   lhablock = 'FRBlock',
                   lhacode = [ 14 ])

emass = Parameter(name = 'emass',
                  nature = 'external',
                  type = 'real',
                  value = 0.00051099895,
                  texname = 'm_e',
                  lhablock = 'FRBlock',
                  lhacode = [ 15 ])

lamT = Parameter(name = 'lamT',
                 nature = 'external',
                 type = 'real',
                 value = 0.22537,
                 texname = '\\lambda _T',
                 lhablock = 'FRBlock',
                 lhacode = [ 16 ])

AT = Parameter(name = 'AT',
               nature = 'external',
               type = 'real',
               value = 0.828,
               texname = 'A_T',
               lhablock = 'FRBlock',
               lhacode = [ 17 ])

rhoT = Parameter(name = 'rhoT',
                 nature = 'external',
                 type = 'real',
                 value = 0.194,
                 texname = '\\rho _T',
                 lhablock = 'FRBlock',
                 lhacode = [ 18 ])

etaT = Parameter(name = 'etaT',
                 nature = 'external',
                 type = 'real',
                 value = 0.391,
                 texname = '\\eta _T',
                 lhablock = 'FRBlock',
                 lhacode = [ 19 ])

theta12 = Parameter(name = 'theta12',
                    nature = 'external',
                    type = 'real',
                    value = 0.5836381018669038,
                    texname = '\\theta _{12}',
                    lhablock = 'FRBlock',
                    lhacode = [ 20 ])

theta13 = Parameter(name = 'theta13',
                    nature = 'external',
                    type = 'real',
                    value = 0.14957471689591406,
                    texname = '\\theta _{13}',
                    lhablock = 'FRBlock',
                    lhacode = [ 21 ])

theta23 = Parameter(name = 'theta23',
                    nature = 'external',
                    type = 'real',
                    value = 0.8587019919812102,
                    texname = '\\theta _{23}',
                    lhablock = 'FRBlock',
                    lhacode = [ 22 ])

delta = Parameter(name = 'delta',
                  nature = 'external',
                  type = 'real',
                  value = 3.3859562021615193,
                  texname = '\\delta',
                  lhablock = 'FRBlock',
                  lhacode = [ 23 ])

taumu = Parameter(name = 'taumu',
                  nature = 'external',
                  type = 'real',
                  value = 3.337862504e18,
                  texname = '\\tau _{\\mu }',
                  lhablock = 'FRBlock',
                  lhacode = [ 24 ])

mB = Parameter(name = 'mB',
               nature = 'external',
               type = 'real',
               value = 5.27932,
               texname = 'm^{\\text{B+}}',
               lhablock = 'FRBlock',
               lhacode = [ 25 ])

mBs = Parameter(name = 'mBs',
                nature = 'external',
                type = 'real',
                value = 5.36689,
                texname = 'm_{\\text{Bs}}',
                lhablock = 'FRBlock',
                lhacode = [ 26 ])

mBd = Parameter(name = 'mBd',
                nature = 'external',
                type = 'real',
                value = 5.27963,
                texname = 'm_{\\text{Bd}}',
                lhablock = 'FRBlock',
                lhacode = [ 27 ])

mK = Parameter(name = 'mK',
               nature = 'external',
               type = 'real',
               value = 0.493677,
               texname = 'm^{\\text{K+}}',
               lhablock = 'FRBlock',
               lhacode = [ 28 ])

mPi = Parameter(name = 'mPi',
                nature = 'external',
                type = 'real',
                value = 0.13957061,
                texname = 'm^{\\text{$\\pi $+}}',
                lhablock = 'FRBlock',
                lhacode = [ 29 ])

S1 = Parameter(name = 'S1',
               nature = 'external',
               type = 'real',
               value = 2.3124,
               texname = 'S_1\\left(m_W\\right)',
               lhablock = 'FRBlock',
               lhacode = [ 30 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 0.00754852887435655,
                  texname = '\\alpha _{\\text{em}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 31 ])

G1 = Parameter(name = 'G1',
               nature = 'external',
               type = 'real',
               value = 0.34940513159160064,
               texname = 'G_1',
               lhablock = 'FRBlock',
               lhacode = [ 32 ])

GW = Parameter(name = 'GW',
               nature = 'external',
               type = 'real',
               value = 0.6521849654370863,
               texname = 'G_W',
               lhablock = 'FRBlock',
               lhacode = [ 33 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1176,
               texname = '\\alpha _s',
               lhablock = 'FRBlock',
               lhacode = [ 34 ])

vev = Parameter(name = 'vev',
                nature = 'external',
                type = 'real',
                value = 246.49142270898864,
                texname = 'v',
                lhablock = 'FRBlock',
                lhacode = [ 35 ])

hlambda = Parameter(name = 'hlambda',
                    nature = 'external',
                    type = 'real',
                    value = 0.2586098447591928,
                    texname = '\\lambda',
                    lhablock = 'FRBlock',
                    lhacode = [ 36 ])

mz = Parameter(name = 'mz',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = 'M_Z',
               lhablock = 'FRBlock',
               lhacode = [ 37 ])

mw = Parameter(name = 'mw',
               nature = 'external',
               type = 'real',
               value = 80.379,
               texname = 'M_W',
               lhablock = 'FRBlock',
               lhacode = [ 38 ])

mh = Parameter(name = 'mh',
               nature = 'external',
               type = 'real',
               value = 125.35,
               texname = 'M_H',
               lhablock = 'FRBlock',
               lhacode = [ 39 ])

mqt = Parameter(name = 'mqt',
                nature = 'external',
                type = 'real',
                value = 172.76,
                texname = 'm_t',
                lhablock = 'FRBlock',
                lhacode = [ 40 ])

mqc = Parameter(name = 'mqc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = 'm_c',
                lhablock = 'FRBlock',
                lhacode = [ 41 ])

mqu = Parameter(name = 'mqu',
                nature = 'external',
                type = 'real',
                value = 0.0025499999999999997,
                texname = 'm_u',
                lhablock = 'FRBlock',
                lhacode = [ 42 ])

mqb = Parameter(name = 'mqb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = 'm_b',
                lhablock = 'FRBlock',
                lhacode = [ 43 ])

mqs = Parameter(name = 'mqs',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = 'm_s',
                lhablock = 'FRBlock',
                lhacode = [ 44 ])

mqd = Parameter(name = 'mqd',
                nature = 'external',
                type = 'real',
                value = 0.00504,
                texname = 'm_d',
                lhablock = 'FRBlock',
                lhacode = [ 45 ])

mlt = Parameter(name = 'mlt',
                nature = 'external',
                type = 'real',
                value = 1.77686,
                texname = 'm_{\\tau }',
                lhablock = 'FRBlock',
                lhacode = [ 46 ])

mlm = Parameter(name = 'mlm',
                nature = 'external',
                type = 'real',
                value = 0.1056583755,
                texname = 'm_{\\mu }',
                lhablock = 'FRBlock',
                lhacode = [ 47 ])

mle = Parameter(name = 'mle',
                nature = 'external',
                type = 'real',
                value = 0.00051099895,
                texname = 'm_e',
                lhablock = 'FRBlock',
                lhacode = [ 48 ])

mve = Parameter(name = 'mve',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'm_{\\text{$\\nu $e}}',
                lhablock = 'FRBlock',
                lhacode = [ 49 ])

mvm = Parameter(name = 'mvm',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'm_{\\nu \\mu }',
                lhablock = 'FRBlock',
                lhacode = [ 50 ])

mvt = Parameter(name = 'mvt',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'm_{\\nu \\tau }',
                lhablock = 'FRBlock',
                lhacode = [ 51 ])

MG0 = Parameter(name = 'MG0',
                nature = 'external',
                type = 'real',
                value = 91.1876,
                texname = 'M_{\\text{G0}}',
                lhablock = 'FRBlock',
                lhacode = [ 52 ])

MGP = Parameter(name = 'MGP',
                nature = 'external',
                type = 'real',
                value = 80.379,
                texname = 'M_{\\text{GP}}',
                lhablock = 'FRBlock',
                lhacode = [ 53 ])

MgZ = Parameter(name = 'MgZ',
                nature = 'external',
                type = 'real',
                value = 91.1876,
                texname = 'M_{\\text{etaZ}}',
                lhablock = 'FRBlock',
                lhacode = [ 54 ])

MgW = Parameter(name = 'MgW',
                nature = 'external',
                type = 'real',
                value = 80.379,
                texname = 'M_{\\text{etaW}}',
                lhablock = 'FRBlock',
                lhacode = [ 55 ])

xiW = Parameter(name = 'xiW',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\xi _W',
                lhablock = 'FRBlock',
                lhacode = [ 56 ])

xiZ = Parameter(name = 'xiZ',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\xi _Z',
                lhablock = 'FRBlock',
                lhacode = [ 57 ])

xiA = Parameter(name = 'xiA',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\xi _A',
                lhablock = 'FRBlock',
                lhacode = [ 58 ])

xiG = Parameter(name = 'xiG',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\xi _G',
                lhablock = 'FRBlock',
                lhacode = [ 59 ])

g1norm = Parameter(name = 'g1norm',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = 'Z_{\\text{g\'}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 60 ])

gwnorm = Parameter(name = 'gwnorm',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = 'Z_g',
                   lhablock = 'FRBlock',
                   lhacode = [ 61 ])

gsnorm = Parameter(name = 'gsnorm',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = 'Z_{\\text{gs}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 62 ])

Hnorm = Parameter(name = 'Hnorm',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Z_h',
                  lhablock = 'FRBlock',
                  lhacode = [ 63 ])

G0norm = Parameter(name = 'G0norm',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = 'Z_{\\text{G0}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 64 ])

GPnorm = Parameter(name = 'GPnorm',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = 'Z_{\\text{G+}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 65 ])

Wnorm = Parameter(name = 'Wnorm',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Z_W',
                  lhablock = 'FRBlock',
                  lhacode = [ 66 ])

Gnorm = Parameter(name = 'Gnorm',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = 'Z_{\\text{gl}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 67 ])

AZnorm11 = Parameter(name = 'AZnorm11',
                     nature = 'external',
                     type = 'real',
                     value = 0.8814685330022942,
                     texname = 'Z_{\\text{$\\gamma $Z}}^{11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 68 ])

AZnorm12 = Parameter(name = 'AZnorm12',
                     nature = 'external',
                     type = 'real',
                     value = 0.4722427610104611,
                     texname = 'Z_{\\text{$\\gamma $Z}}^{12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 69 ])

AZnorm21 = Parameter(name = 'AZnorm21',
                     nature = 'external',
                     type = 'real',
                     value = -0.4722427610104611,
                     texname = 'Z_{\\text{$\\gamma $Z}}^{21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 70 ])

AZnorm22 = Parameter(name = 'AZnorm22',
                     nature = 'external',
                     type = 'real',
                     value = 0.8814685330022942,
                     texname = 'Z_{\\text{$\\gamma $Z}}^{22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 71 ])

UFOOrder = Parameter(name = 'UFOOrder',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '1',
                     lhablock = 'FRBlock',
                     lhacode = [ 72 ])

ReKq11 = Parameter(name = 'ReKq11',
                   nature = 'external',
                   type = 'real',
                   value = 0.974282,
                   texname = 'K_{11} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 73 ])

ReKq12 = Parameter(name = 'ReKq12',
                   nature = 'external',
                   type = 'real',
                   value = 0.22537,
                   texname = 'K_{12} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 74 ])

ReKq13 = Parameter(name = 'ReKq13',
                   nature = 'external',
                   type = 'real',
                   value = 0.00188544,
                   texname = 'K_{13} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 75 ])

ImKq13 = Parameter(name = 'ImKq13',
                   nature = 'external',
                   type = 'real',
                   value = -0.00380003,
                   texname = '\\text{Im} K_{13}',
                   lhablock = 'FRBlock',
                   lhacode = [ 76 ])

ReKq21 = Parameter(name = 'ReKq21',
                   nature = 'external',
                   type = 'real',
                   value = -0.225248,
                   texname = 'K_{21} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 77 ])

ImKq21 = Parameter(name = 'ImKq21',
                   nature = 'external',
                   type = 'real',
                   value = -0.000155854,
                   texname = '\\text{Im} K_{21}',
                   lhablock = 'FRBlock',
                   lhacode = [ 78 ])

ReKq22 = Parameter(name = 'ReKq22',
                   nature = 'external',
                   type = 'real',
                   value = 0.973397,
                   texname = 'K_{22} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 79 ])

ReKq23 = Parameter(name = 'ReKq23',
                   nature = 'external',
                   type = 'real',
                   value = 0.0420555,
                   texname = 'K_{23} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 80 ])

ReKq31 = Parameter(name = 'ReKq31',
                   nature = 'external',
                   type = 'real',
                   value = 0.0076393,
                   texname = 'K_{31} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 81 ])

ImKq31 = Parameter(name = 'ImKq31',
                   nature = 'external',
                   type = 'real',
                   value = -0.00370591,
                   texname = '\\text{Im} K_{31}',
                   lhablock = 'FRBlock',
                   lhacode = [ 82 ])

ReKq32 = Parameter(name = 'ReKq32',
                   nature = 'external',
                   type = 'real',
                   value = -0.0414018,
                   texname = 'K_{32} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 83 ])

ImKq32 = Parameter(name = 'ImKq32',
                   nature = 'external',
                   type = 'real',
                   value = -0.000835202,
                   texname = '\\text{Im} K_{32}',
                   lhablock = 'FRBlock',
                   lhacode = [ 84 ])

ReKq33 = Parameter(name = 'ReKq33',
                   nature = 'external',
                   type = 'real',
                   value = 0.999116,
                   texname = 'K_{33} \\text{Re}',
                   lhablock = 'FRBlock',
                   lhacode = [ 85 ])

ReCleWHD2n111 = Parameter(name = 'ReCleWHD2n111',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 86 ])

ReCleWHD2n112 = Parameter(name = 'ReCleWHD2n112',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 87 ])

ReCleWHD2n113 = Parameter(name = 'ReCleWHD2n113',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 88 ])

ReCleWHD2n121 = Parameter(name = 'ReCleWHD2n121',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 89 ])

ReCleWHD2n122 = Parameter(name = 'ReCleWHD2n122',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 90 ])

ReCleWHD2n123 = Parameter(name = 'ReCleWHD2n123',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 91 ])

ReCleWHD2n131 = Parameter(name = 'ReCleWHD2n131',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 92 ])

ReCleWHD2n132 = Parameter(name = 'ReCleWHD2n132',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 93 ])

ReCleWHD2n133 = Parameter(name = 'ReCleWHD2n133',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = 'C^{\\text{leWHD2n1}}',
                          lhablock = 'FRBlock',
                          lhacode = [ 94 ])

Lam = Parameter(name = 'Lam',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\frac{1}{\\Lambda ^2}',
                lhablock = 'FRBlock',
                lhacode = [ 95 ])

AZnorm1x1 = Parameter(name = 'AZnorm1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.8814685330022942,
                      texname = '\\text{AZnorm1x1}',
                      lhablock = 'FRBlock6',
                      lhacode = [ 1, 1 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.379,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MLE = Parameter(name = 'MLE',
                nature = 'external',
                type = 'real',
                value = 0.00051099895,
                texname = '\\text{MLE}',
                lhablock = 'MASS',
                lhacode = [ 11 ])

MLM = Parameter(name = 'MLM',
                nature = 'external',
                type = 'real',
                value = 0.1056583755,
                texname = '\\text{MLM}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MLT = Parameter(name = 'MLT',
                nature = 'external',
                type = 'real',
                value = 1.77686,
                texname = '\\text{MLT}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MQU = Parameter(name = 'MQU',
                nature = 'external',
                type = 'real',
                value = 0.0025499999999999997,
                texname = '\\text{MQU}',
                lhablock = 'MASS',
                lhacode = [ 2 ])

MQC = Parameter(name = 'MQC',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{MQC}',
                lhablock = 'MASS',
                lhacode = [ 4 ])

MQT = Parameter(name = 'MQT',
                nature = 'external',
                type = 'real',
                value = 172.76,
                texname = '\\text{MQT}',
                lhablock = 'MASS',
                lhacode = [ 6 ])

MQD = Parameter(name = 'MQD',
                nature = 'external',
                type = 'real',
                value = 0.00504,
                texname = '\\text{MQD}',
                lhablock = 'MASS',
                lhacode = [ 1 ])

MQS = Parameter(name = 'MQS',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{MQS}',
                lhablock = 'MASS',
                lhacode = [ 3 ])

MQB = Parameter(name = 'MQB',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{MQB}',
                lhablock = 'MASS',
                lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.35,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX = Parameter(name = 'MX',
               nature = 'external',
               type = 'real',
               value = 100000000,
               texname = '\\text{MX}',
               lhablock = 'MASS',
               lhacode = [ 9000010 ])

GAMZ = Parameter(name = 'GAMZ',
                 nature = 'external',
                 type = 'real',
                 value = 2.4952,
                 texname = '\\text{GAMZ}',
                 lhablock = 'DECAY',
                 lhacode = [ 23 ])

GAMW = Parameter(name = 'GAMW',
                 nature = 'external',
                 type = 'real',
                 value = 2.085,
                 texname = '\\text{GAMW}',
                 lhablock = 'DECAY',
                 lhacode = [ 24 ])

WLT = Parameter(name = 'WLT',
                nature = 'external',
                type = 'real',
                value = 2.25e-12,
                texname = '\\text{WLT}',
                lhablock = 'DECAY',
                lhacode = [ 15 ])

WQT = Parameter(name = 'WQT',
                nature = 'external',
                type = 'real',
                value = 1.35,
                texname = '\\text{WQT}',
                lhablock = 'DECAY',
                lhacode = [ 6 ])

GAMH = Parameter(name = 'GAMH',
                 nature = 'external',
                 type = 'real',
                 value = 0.00575,
                 texname = '\\text{GAMH}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

Wduq = Parameter(name = 'Wduq',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wduq}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

Wqqu = Parameter(name = 'Wqqu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wqqu}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000007 ])

Wqqq = Parameter(name = 'Wqqq',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wqqq}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000008 ])

Wduu = Parameter(name = 'Wduu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wduu}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000009 ])

Wll = Parameter(name = 'Wll',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wll}',
                lhablock = 'DECAY',
                lhacode = [ 9000010 ])

echarge = Parameter(name = 'echarge',
                    nature = 'internal',
                    type = 'real',
                    value = '2*cmath.sqrt(aEWM1)*cmath.sqrt(cmath.pi)',
                    texname = 'q_e')

GS = Parameter(name = 'GS',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
               texname = 'G_s')

