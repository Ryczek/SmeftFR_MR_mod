# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Sun 28 Jun 2026 15:23:09


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-3*2**0.25*complex(0,1)*Hmass**2*cmath.sqrt(Gf)',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '-3*complex(0,1)*Gf*Hmass**2*cmath.sqrt(2)',
                order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = 'complex(0,1)*I1a11*Lam',
                order = {'NP':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'complex(0,1)*I1a12*Lam',
                order = {'NP':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'complex(0,1)*I1a13*Lam',
                order = {'NP':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'complex(0,1)*I1a21*Lam',
                order = {'NP':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*I1a22*Lam',
                order = {'NP':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*I1a23*Lam',
                order = {'NP':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*I1a31*Lam',
                order = {'NP':1})

GC_10 = Coupling(name = 'GC_10',
                 value = 'complex(0,1)*I1a32*Lam',
                 order = {'NP':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*I1a33*Lam',
                 order = {'NP':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(complex(0,1)*I4a11*Lam)',
                 order = {'NP':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*I4a22*Lam)',
                 order = {'NP':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*I4a33*Lam)',
                 order = {'NP':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*I5a11*Lam',
                 order = {'NP':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*I5a12*Lam',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*I5a13*Lam',
                 order = {'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*I5a21*Lam',
                 order = {'NP':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*I5a22*Lam',
                 order = {'NP':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*I5a23*Lam',
                 order = {'NP':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'complex(0,1)*I5a31*Lam',
                 order = {'NP':1})

GC_22 = Coupling(name = 'GC_22',
                 value = 'complex(0,1)*I5a32*Lam',
                 order = {'NP':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*I5a33*Lam',
                 order = {'NP':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(complex(0,1)*I6a11*Lam)',
                 order = {'NP':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*I6a22*Lam)',
                 order = {'NP':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(complex(0,1)*I6a33*Lam)',
                 order = {'NP':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-0.5*(complex(0,1)*I1a21*Lam) - (complex(0,1)*I4a12*Lam)/2.',
                 order = {'NP':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-0.5*(complex(0,1)*I1a31*Lam) - (complex(0,1)*I4a13*Lam)/2.',
                 order = {'NP':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(complex(0,1)*I1a12*Lam)/2. + (complex(0,1)*I4a21*Lam)/2.',
                 order = {'NP':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-0.5*(complex(0,1)*I1a32*Lam) - (complex(0,1)*I4a23*Lam)/2.',
                 order = {'NP':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(complex(0,1)*I1a13*Lam)/2. + (complex(0,1)*I4a31*Lam)/2.',
                 order = {'NP':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(complex(0,1)*I1a23*Lam)/2. + (complex(0,1)*I4a32*Lam)/2.',
                 order = {'NP':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-0.5*(complex(0,1)*I5a21*Lam) - (complex(0,1)*I6a12*Lam)/2.',
                 order = {'NP':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-0.5*(complex(0,1)*I5a31*Lam) - (complex(0,1)*I6a13*Lam)/2.',
                 order = {'NP':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(complex(0,1)*I5a12*Lam)/2. + (complex(0,1)*I6a21*Lam)/2.',
                 order = {'NP':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.5*(complex(0,1)*I5a32*Lam) - (complex(0,1)*I6a23*Lam)/2.',
                 order = {'NP':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(complex(0,1)*I5a13*Lam)/2. + (complex(0,1)*I6a31*Lam)/2.',
                 order = {'NP':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(complex(0,1)*I5a23*Lam)/2. + (complex(0,1)*I6a32*Lam)/2.',
                 order = {'NP':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(2**0.25*complex(0,1)*mle*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(2**0.25*complex(0,1)*mlm*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(2**0.25*complex(0,1)*mlt*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(2**0.25*complex(0,1)*mqb*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(2**0.25*complex(0,1)*mqc*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(2**0.25*complex(0,1)*mqd*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(2**0.25*complex(0,1)*mqs*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(2**0.25*complex(0,1)*mqt*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(2**0.25*complex(0,1)*mqu*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-2*2**0.25*complex(0,1)*mve*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-2*complex(0,1)*Gf*mve*cmath.sqrt(2)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-2*2**0.25*complex(0,1)*mvm*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-2*complex(0,1)*Gf*mvm*cmath.sqrt(2)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-2*2**0.25*complex(0,1)*mvt*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-2*complex(0,1)*Gf*mvt*cmath.sqrt(2)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-2*complex(0,1)*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
                 order = {'QCD':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
                 order = {'QCD':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '4*aS*cmath.pi*complex(0,1)',
                 order = {'QCD':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(complex(0,1)*I2a1*I3a1*Lam*MX**2*UFOOrder)',
                 order = {'UFO':1})

GC_58 = Coupling(name = 'GC_58',
                 value = 'complex(0,1)*I2a1*I3a1*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'complex(0,1)*I2a2*I3a1*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'complex(0,1)*I2a3*I3a1*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_61 = Coupling(name = 'GC_61',
                 value = 'complex(0,1)*I2a1*I3a2*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(complex(0,1)*I2a2*I3a2*Lam*MX**2*UFOOrder)',
                 order = {'UFO':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'complex(0,1)*I2a2*I3a2*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_64 = Coupling(name = 'GC_64',
                 value = 'complex(0,1)*I2a3*I3a2*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'complex(0,1)*I2a1*I3a3*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_66 = Coupling(name = 'GC_66',
                 value = 'complex(0,1)*I2a2*I3a3*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(complex(0,1)*I2a3*I3a3*Lam*MX**2*UFOOrder)',
                 order = {'UFO':1})

GC_68 = Coupling(name = 'GC_68',
                 value = 'complex(0,1)*I2a3*I3a3*Lam*MX**2*UFOOrder',
                 order = {'UFO':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-0.5*(complex(0,1)*I2a2*I3a1*Lam*MX**2*UFOOrder) - (complex(0,1)*I2a1*I3a2*Lam*MX**2*UFOOrder)/2.',
                 order = {'UFO':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(complex(0,1)*I2a2*I3a1*Lam*MX**2*UFOOrder)/2. + (complex(0,1)*I2a1*I3a2*Lam*MX**2*UFOOrder)/2.',
                 order = {'UFO':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-0.5*(complex(0,1)*I2a3*I3a1*Lam*MX**2*UFOOrder) - (complex(0,1)*I2a1*I3a3*Lam*MX**2*UFOOrder)/2.',
                 order = {'UFO':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(complex(0,1)*I2a3*I3a1*Lam*MX**2*UFOOrder)/2. + (complex(0,1)*I2a1*I3a3*Lam*MX**2*UFOOrder)/2.',
                 order = {'UFO':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-0.5*(complex(0,1)*I2a3*I3a2*Lam*MX**2*UFOOrder) - (complex(0,1)*I2a2*I3a3*Lam*MX**2*UFOOrder)/2.',
                 order = {'UFO':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(complex(0,1)*I2a3*I3a2*Lam*MX**2*UFOOrder)/2. + (complex(0,1)*I2a2*I3a3*Lam*MX**2*UFOOrder)/2.',
                 order = {'UFO':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-(2**0.75*complex(0,1)*Wmass*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(2**0.75*complex(0,1)*ReKq11*Wmass*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-(2**0.75*complex(0,1)*ReKq12*Wmass*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(2**0.75*complex(0,1)*ReKq22*Wmass*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(2**0.75*complex(0,1)*ReKq23*Wmass*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(2**0.75*complex(0,1)*ReKq33*Wmass*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '2*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '2*complex(0,1)*Gf*Wmass**2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-4*complex(0,1)*Gf*Wmass**2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(2**0.75*ImKq13*Wmass*cmath.sqrt(Gf)) - 2**0.75*complex(0,1)*ReKq13*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '2**0.75*ImKq13*Wmass*cmath.sqrt(Gf) - 2**0.75*complex(0,1)*ReKq13*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(2**0.75*ImKq21*Wmass*cmath.sqrt(Gf)) - 2**0.75*complex(0,1)*ReKq21*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '2**0.75*ImKq21*Wmass*cmath.sqrt(Gf) - 2**0.75*complex(0,1)*ReKq21*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(2**0.75*ImKq31*Wmass*cmath.sqrt(Gf)) - 2**0.75*complex(0,1)*ReKq31*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '2**0.75*ImKq31*Wmass*cmath.sqrt(Gf) - 2**0.75*complex(0,1)*ReKq31*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-(2**0.75*ImKq32*Wmass*cmath.sqrt(Gf)) - 2**0.75*complex(0,1)*ReKq32*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '2**0.75*ImKq32*Wmass*cmath.sqrt(Gf) - 2**0.75*complex(0,1)*ReKq32*Wmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '4*complex(0,1)*Gf*Wmass**2*cmath.sqrt(2) - (4*complex(0,1)*Gf*Wmass**4*cmath.sqrt(2))/Zmass**2',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(4*complex(0,1)*Gf*Wmass**4*cmath.sqrt(2))/Zmass**2',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(-2*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/Zmass',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '2*2**0.25*complex(0,1)*Zmass**2*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '2*complex(0,1)*Gf*Zmass**2*cmath.sqrt(2)',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '(2*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/(3.*Zmass) + (2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf))/3.',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(-4*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/(3.*Zmass) + (2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf))/3.',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(2*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/(3.*Zmass) - (2*2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf))/3.',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(2*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/Zmass - 2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(-4*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/(3.*Zmass) + (4*2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf))/3.',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(2*2**0.25*complex(0,1)*Wmass**2*cmath.sqrt(Gf))/Zmass - 2*2**0.25*complex(0,1)*Zmass*cmath.sqrt(Gf)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(-8*complex(0,1)*Gf*Wmass**3*cmath.sqrt(2)*cmath.sqrt(-Wmass**2 + Zmass**2))/Zmass**2',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(2*2**0.25*complex(0,1)*Wmass*cmath.sqrt(Gf)*cmath.sqrt(-Wmass**2 + Zmass**2))/(3.*Zmass)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(-4*2**0.25*complex(0,1)*Wmass*cmath.sqrt(Gf)*cmath.sqrt(-Wmass**2 + Zmass**2))/(3.*Zmass)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(-2*2**0.25*complex(0,1)*Wmass*cmath.sqrt(Gf)*cmath.sqrt(-Wmass**2 + Zmass**2))/Zmass',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(2*2**0.25*complex(0,1)*Wmass*cmath.sqrt(Gf)*cmath.sqrt(-Wmass**2 + Zmass**2))/Zmass',
                  order = {'QED':1})

