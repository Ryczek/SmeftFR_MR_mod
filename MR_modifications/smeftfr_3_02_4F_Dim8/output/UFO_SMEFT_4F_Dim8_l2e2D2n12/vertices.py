# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Thu 18 Dec 2025 13:46:15


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_28})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_29})

V_3 = Vertex(name = 'V_3',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_947})

V_4 = Vertex(name = 'V_4',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_948,(0,0):C.GC_948,(2,2):C.GC_948})

V_5 = Vertex(name = 'V_5',
             particles = [ P.d__tilde__, P.d, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_6 = Vertex(name = 'V_6',
             particles = [ P.s__tilde__, P.d, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.d, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_3})

V_8 = Vertex(name = 'V_8',
             particles = [ P.d__tilde__, P.s, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_4})

V_9 = Vertex(name = 'V_9',
             particles = [ P.s__tilde__, P.s, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_5})

V_10 = Vertex(name = 'V_10',
              particles = [ P.b__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_6})

V_11 = Vertex(name = 'V_11',
              particles = [ P.d__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_7})

V_12 = Vertex(name = 'V_12',
              particles = [ P.s__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_8})

V_13 = Vertex(name = 'V_13',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_9})

V_14 = Vertex(name = 'V_14',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_10})

V_15 = Vertex(name = 'V_15',
              particles = [ P.mu__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_11})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ta__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_12})

V_17 = Vertex(name = 'V_17',
              particles = [ P.e__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_13})

V_18 = Vertex(name = 'V_18',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_14})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ta__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_15})

V_20 = Vertex(name = 'V_20',
              particles = [ P.e__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_16})

V_21 = Vertex(name = 'V_21',
              particles = [ P.mu__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_17})

V_22 = Vertex(name = 'V_22',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_18})

V_23 = Vertex(name = 'V_23',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_24 = Vertex(name = 'V_24',
              particles = [ P.c__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_20})

V_25 = Vertex(name = 'V_25',
              particles = [ P.t__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_21})

V_26 = Vertex(name = 'V_26',
              particles = [ P.u__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_22})

V_27 = Vertex(name = 'V_27',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_23})

V_28 = Vertex(name = 'V_28',
              particles = [ P.t__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_24})

V_29 = Vertex(name = 'V_29',
              particles = [ P.u__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_25})

V_30 = Vertex(name = 'V_30',
              particles = [ P.c__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_26})

V_31 = Vertex(name = 'V_31',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_27})

V_32 = Vertex(name = 'V_32',
              particles = [ P.A, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_985})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_967})

V_34 = Vertex(name = 'V_34',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_968})

V_35 = Vertex(name = 'V_35',
              particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_970})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_972})

V_37 = Vertex(name = 'V_37',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_969})

V_38 = Vertex(name = 'V_38',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_982})

V_39 = Vertex(name = 'V_39',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_974})

V_40 = Vertex(name = 'V_40',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_975})

V_41 = Vertex(name = 'V_41',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_971})

V_42 = Vertex(name = 'V_42',
              particles = [ P.ve__tilde__, P.ve, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_241,(0,2):C.GC_242,(0,1):C.GC_242,(0,3):C.GC_241})

V_43 = Vertex(name = 'V_43',
              particles = [ P.ve__tilde__, P.ve, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_403,(0,2):C.GC_404,(0,1):C.GC_404,(0,3):C.GC_403})

V_44 = Vertex(name = 'V_44',
              particles = [ P.vm__tilde__, P.ve, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_243,(0,2):C.GC_244,(0,1):C.GC_244,(0,3):C.GC_243})

V_45 = Vertex(name = 'V_45',
              particles = [ P.vm__tilde__, P.ve, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_405,(0,2):C.GC_406,(0,1):C.GC_406,(0,3):C.GC_405})

V_46 = Vertex(name = 'V_46',
              particles = [ P.vt__tilde__, P.ve, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,1):C.GC_245,(0,3):C.GC_246,(0,2):C.GC_246,(0,0):C.GC_30,(0,4):C.GC_33})

V_47 = Vertex(name = 'V_47',
              particles = [ P.vt__tilde__, P.ve, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_407,(0,2):C.GC_408,(0,1):C.GC_408,(0,3):C.GC_407})

V_48 = Vertex(name = 'V_48',
              particles = [ P.ve__tilde__, P.vm, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_247,(0,2):C.GC_248,(0,1):C.GC_248,(0,3):C.GC_247})

V_49 = Vertex(name = 'V_49',
              particles = [ P.ve__tilde__, P.vm, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_409,(0,2):C.GC_410,(0,1):C.GC_410,(0,3):C.GC_409})

V_50 = Vertex(name = 'V_50',
              particles = [ P.vm__tilde__, P.vm, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_249,(0,2):C.GC_250,(0,1):C.GC_250,(0,3):C.GC_249})

V_51 = Vertex(name = 'V_51',
              particles = [ P.vm__tilde__, P.vm, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_411,(0,2):C.GC_412,(0,1):C.GC_412,(0,3):C.GC_411})

V_52 = Vertex(name = 'V_52',
              particles = [ P.vt__tilde__, P.vm, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_251,(0,2):C.GC_252,(0,1):C.GC_252,(0,3):C.GC_251})

V_53 = Vertex(name = 'V_53',
              particles = [ P.vt__tilde__, P.vm, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_413,(0,2):C.GC_414,(0,1):C.GC_414,(0,3):C.GC_413})

V_54 = Vertex(name = 'V_54',
              particles = [ P.ve__tilde__, P.vt, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_253,(0,2):C.GC_254,(0,1):C.GC_254,(0,3):C.GC_253})

V_55 = Vertex(name = 'V_55',
              particles = [ P.ve__tilde__, P.vt, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_415,(0,2):C.GC_416,(0,1):C.GC_416,(0,3):C.GC_415})

V_56 = Vertex(name = 'V_56',
              particles = [ P.vm__tilde__, P.vt, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_255,(0,2):C.GC_256,(0,1):C.GC_256,(0,3):C.GC_255})

V_57 = Vertex(name = 'V_57',
              particles = [ P.vm__tilde__, P.vt, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_417,(0,2):C.GC_418,(0,1):C.GC_418,(0,3):C.GC_417})

V_58 = Vertex(name = 'V_58',
              particles = [ P.vt__tilde__, P.vt, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_257,(0,2):C.GC_258,(0,1):C.GC_258,(0,3):C.GC_257})

V_59 = Vertex(name = 'V_59',
              particles = [ P.vt__tilde__, P.vt, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_419,(0,2):C.GC_420,(0,1):C.GC_420,(0,3):C.GC_419})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ve__tilde__, P.ve, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_259,(0,2):C.GC_260,(0,1):C.GC_260,(0,3):C.GC_259})

V_61 = Vertex(name = 'V_61',
              particles = [ P.ve__tilde__, P.ve, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_421,(0,2):C.GC_422,(0,1):C.GC_422,(0,3):C.GC_421})

V_62 = Vertex(name = 'V_62',
              particles = [ P.vm__tilde__, P.ve, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_261,(0,2):C.GC_262,(0,1):C.GC_262,(0,3):C.GC_261})

V_63 = Vertex(name = 'V_63',
              particles = [ P.vm__tilde__, P.ve, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_423,(0,2):C.GC_424,(0,1):C.GC_424,(0,3):C.GC_423})

V_64 = Vertex(name = 'V_64',
              particles = [ P.vt__tilde__, P.ve, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_263,(0,2):C.GC_264,(0,1):C.GC_264,(0,3):C.GC_263})

V_65 = Vertex(name = 'V_65',
              particles = [ P.vt__tilde__, P.ve, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_425,(0,2):C.GC_426,(0,1):C.GC_426,(0,3):C.GC_425})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ve__tilde__, P.vm, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_265,(0,2):C.GC_266,(0,1):C.GC_266,(0,3):C.GC_265})

V_67 = Vertex(name = 'V_67',
              particles = [ P.ve__tilde__, P.vm, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_427,(0,2):C.GC_428,(0,1):C.GC_428,(0,3):C.GC_427})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vm__tilde__, P.vm, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_267,(0,2):C.GC_268,(0,1):C.GC_268,(0,3):C.GC_267})

V_69 = Vertex(name = 'V_69',
              particles = [ P.vm__tilde__, P.vm, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_429,(0,2):C.GC_430,(0,1):C.GC_430,(0,3):C.GC_429})

V_70 = Vertex(name = 'V_70',
              particles = [ P.vt__tilde__, P.vm, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_269,(0,2):C.GC_270,(0,1):C.GC_270,(0,3):C.GC_269})

V_71 = Vertex(name = 'V_71',
              particles = [ P.vt__tilde__, P.vm, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_431,(0,2):C.GC_432,(0,1):C.GC_432,(0,3):C.GC_431})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ve__tilde__, P.vt, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_271,(0,2):C.GC_272,(0,1):C.GC_272,(0,3):C.GC_271})

V_73 = Vertex(name = 'V_73',
              particles = [ P.ve__tilde__, P.vt, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_433,(0,2):C.GC_434,(0,1):C.GC_434,(0,3):C.GC_433})

V_74 = Vertex(name = 'V_74',
              particles = [ P.vm__tilde__, P.vt, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_273,(0,2):C.GC_274,(0,1):C.GC_274,(0,3):C.GC_273})

V_75 = Vertex(name = 'V_75',
              particles = [ P.vm__tilde__, P.vt, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_435,(0,2):C.GC_436,(0,1):C.GC_436,(0,3):C.GC_435})

V_76 = Vertex(name = 'V_76',
              particles = [ P.vt__tilde__, P.vt, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_275,(0,2):C.GC_276,(0,1):C.GC_276,(0,3):C.GC_275})

V_77 = Vertex(name = 'V_77',
              particles = [ P.vt__tilde__, P.vt, P.mu__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_437,(0,2):C.GC_438,(0,1):C.GC_438,(0,3):C.GC_437})

V_78 = Vertex(name = 'V_78',
              particles = [ P.ve__tilde__, P.ve, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_277,(0,2):C.GC_278,(0,1):C.GC_278,(0,3):C.GC_277})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ve__tilde__, P.ve, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_439,(0,2):C.GC_440,(0,1):C.GC_440,(0,3):C.GC_439})

V_80 = Vertex(name = 'V_80',
              particles = [ P.vm__tilde__, P.ve, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_279,(0,2):C.GC_280,(0,1):C.GC_280,(0,3):C.GC_279})

V_81 = Vertex(name = 'V_81',
              particles = [ P.vm__tilde__, P.ve, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_441,(0,2):C.GC_442,(0,1):C.GC_442,(0,3):C.GC_441})

V_82 = Vertex(name = 'V_82',
              particles = [ P.vt__tilde__, P.ve, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_281,(0,2):C.GC_282,(0,1):C.GC_282,(0,3):C.GC_281})

V_83 = Vertex(name = 'V_83',
              particles = [ P.vt__tilde__, P.ve, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_443,(0,2):C.GC_444,(0,1):C.GC_444,(0,3):C.GC_443})

V_84 = Vertex(name = 'V_84',
              particles = [ P.ve__tilde__, P.vm, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_283,(0,2):C.GC_284,(0,1):C.GC_284,(0,3):C.GC_283})

V_85 = Vertex(name = 'V_85',
              particles = [ P.ve__tilde__, P.vm, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_445,(0,2):C.GC_446,(0,1):C.GC_446,(0,3):C.GC_445})

V_86 = Vertex(name = 'V_86',
              particles = [ P.vm__tilde__, P.vm, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_285,(0,2):C.GC_286,(0,1):C.GC_286,(0,3):C.GC_285})

V_87 = Vertex(name = 'V_87',
              particles = [ P.vm__tilde__, P.vm, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_447,(0,2):C.GC_448,(0,1):C.GC_448,(0,3):C.GC_447})

V_88 = Vertex(name = 'V_88',
              particles = [ P.vt__tilde__, P.vm, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_287,(0,2):C.GC_288,(0,1):C.GC_288,(0,3):C.GC_287})

V_89 = Vertex(name = 'V_89',
              particles = [ P.vt__tilde__, P.vm, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_449,(0,2):C.GC_450,(0,1):C.GC_450,(0,3):C.GC_449})

V_90 = Vertex(name = 'V_90',
              particles = [ P.ve__tilde__, P.vt, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_289,(0,2):C.GC_290,(0,1):C.GC_290,(0,3):C.GC_289})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ve__tilde__, P.vt, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_451,(0,2):C.GC_452,(0,1):C.GC_452,(0,3):C.GC_451})

V_92 = Vertex(name = 'V_92',
              particles = [ P.vm__tilde__, P.vt, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_291,(0,2):C.GC_292,(0,1):C.GC_292,(0,3):C.GC_291})

V_93 = Vertex(name = 'V_93',
              particles = [ P.vm__tilde__, P.vt, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_453,(0,2):C.GC_454,(0,1):C.GC_454,(0,3):C.GC_453})

V_94 = Vertex(name = 'V_94',
              particles = [ P.vt__tilde__, P.vt, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_293,(0,2):C.GC_294,(0,1):C.GC_294,(0,3):C.GC_293})

V_95 = Vertex(name = 'V_95',
              particles = [ P.vt__tilde__, P.vt, P.ta__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_455,(0,2):C.GC_456,(0,1):C.GC_456,(0,3):C.GC_455})

V_96 = Vertex(name = 'V_96',
              particles = [ P.ve__tilde__, P.ve, P.e__plus__, P.mu__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_295,(0,2):C.GC_296,(0,1):C.GC_296,(0,3):C.GC_295})

V_97 = Vertex(name = 'V_97',
              particles = [ P.ve__tilde__, P.ve, P.e__plus__, P.mu__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_457,(0,2):C.GC_458,(0,1):C.GC_458,(0,3):C.GC_457})

V_98 = Vertex(name = 'V_98',
              particles = [ P.vm__tilde__, P.ve, P.e__plus__, P.mu__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_297,(0,2):C.GC_298,(0,1):C.GC_298,(0,3):C.GC_297})

V_99 = Vertex(name = 'V_99',
              particles = [ P.vm__tilde__, P.ve, P.e__plus__, P.mu__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
              couplings = {(0,0):C.GC_459,(0,2):C.GC_460,(0,1):C.GC_460,(0,3):C.GC_459})

V_100 = Vertex(name = 'V_100',
               particles = [ P.vt__tilde__, P.ve, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_299,(0,2):C.GC_300,(0,1):C.GC_300,(0,3):C.GC_299})

V_101 = Vertex(name = 'V_101',
               particles = [ P.vt__tilde__, P.ve, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_461,(0,2):C.GC_462,(0,1):C.GC_462,(0,3):C.GC_461})

V_102 = Vertex(name = 'V_102',
               particles = [ P.ve__tilde__, P.vm, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,1):C.GC_301,(0,3):C.GC_302,(0,2):C.GC_302,(0,0):C.GC_36,(0,4):C.GC_301})

V_103 = Vertex(name = 'V_103',
               particles = [ P.ve__tilde__, P.vm, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_463,(0,2):C.GC_464,(0,1):C.GC_464,(0,3):C.GC_38})

V_104 = Vertex(name = 'V_104',
               particles = [ P.vm__tilde__, P.vm, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_303,(0,2):C.GC_304,(0,1):C.GC_304,(0,3):C.GC_303})

V_105 = Vertex(name = 'V_105',
               particles = [ P.vm__tilde__, P.vm, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_465,(0,2):C.GC_466,(0,1):C.GC_466,(0,3):C.GC_465})

V_106 = Vertex(name = 'V_106',
               particles = [ P.vt__tilde__, P.vm, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_305,(0,2):C.GC_306,(0,1):C.GC_306,(0,3):C.GC_305})

V_107 = Vertex(name = 'V_107',
               particles = [ P.vt__tilde__, P.vm, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_467,(0,2):C.GC_468,(0,1):C.GC_468,(0,3):C.GC_467})

V_108 = Vertex(name = 'V_108',
               particles = [ P.ve__tilde__, P.vt, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_307,(0,2):C.GC_308,(0,1):C.GC_308,(0,3):C.GC_307})

V_109 = Vertex(name = 'V_109',
               particles = [ P.ve__tilde__, P.vt, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_469,(0,2):C.GC_470,(0,1):C.GC_470,(0,3):C.GC_469})

V_110 = Vertex(name = 'V_110',
               particles = [ P.vm__tilde__, P.vt, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_309,(0,2):C.GC_310,(0,1):C.GC_310,(0,3):C.GC_309})

V_111 = Vertex(name = 'V_111',
               particles = [ P.vm__tilde__, P.vt, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_471,(0,2):C.GC_472,(0,1):C.GC_472,(0,3):C.GC_471})

V_112 = Vertex(name = 'V_112',
               particles = [ P.vt__tilde__, P.vt, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,1):C.GC_311,(0,3):C.GC_312,(0,2):C.GC_312,(0,0):C.GC_31,(0,4):C.GC_34})

V_113 = Vertex(name = 'V_113',
               particles = [ P.vt__tilde__, P.vt, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_473,(0,2):C.GC_474,(0,1):C.GC_474,(0,3):C.GC_473})

V_114 = Vertex(name = 'V_114',
               particles = [ P.ve__tilde__, P.ve, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_313,(0,2):C.GC_314,(0,1):C.GC_314,(0,3):C.GC_313})

V_115 = Vertex(name = 'V_115',
               particles = [ P.ve__tilde__, P.ve, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_475,(0,2):C.GC_476,(0,1):C.GC_476,(0,3):C.GC_475})

V_116 = Vertex(name = 'V_116',
               particles = [ P.vm__tilde__, P.ve, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_315,(0,2):C.GC_316,(0,1):C.GC_316,(0,3):C.GC_315})

V_117 = Vertex(name = 'V_117',
               particles = [ P.vm__tilde__, P.ve, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_477,(0,2):C.GC_478,(0,1):C.GC_478,(0,3):C.GC_477})

V_118 = Vertex(name = 'V_118',
               particles = [ P.vt__tilde__, P.ve, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_317,(0,2):C.GC_318,(0,1):C.GC_318,(0,3):C.GC_317})

V_119 = Vertex(name = 'V_119',
               particles = [ P.vt__tilde__, P.ve, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_479,(0,2):C.GC_480,(0,1):C.GC_480,(0,3):C.GC_479})

V_120 = Vertex(name = 'V_120',
               particles = [ P.ve__tilde__, P.vm, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_319,(0,2):C.GC_320,(0,1):C.GC_320,(0,3):C.GC_319})

V_121 = Vertex(name = 'V_121',
               particles = [ P.ve__tilde__, P.vm, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_481,(0,2):C.GC_482,(0,1):C.GC_482,(0,3):C.GC_481})

V_122 = Vertex(name = 'V_122',
               particles = [ P.vm__tilde__, P.vm, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_321,(0,2):C.GC_322,(0,1):C.GC_322,(0,3):C.GC_321})

V_123 = Vertex(name = 'V_123',
               particles = [ P.vm__tilde__, P.vm, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_483,(0,2):C.GC_484,(0,1):C.GC_484,(0,3):C.GC_483})

V_124 = Vertex(name = 'V_124',
               particles = [ P.vt__tilde__, P.vm, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_323,(0,2):C.GC_324,(0,1):C.GC_324,(0,3):C.GC_323})

V_125 = Vertex(name = 'V_125',
               particles = [ P.vt__tilde__, P.vm, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_485,(0,2):C.GC_486,(0,1):C.GC_486,(0,3):C.GC_485})

V_126 = Vertex(name = 'V_126',
               particles = [ P.ve__tilde__, P.vt, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_325,(0,2):C.GC_326,(0,1):C.GC_326,(0,3):C.GC_325})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ve__tilde__, P.vt, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_487,(0,2):C.GC_488,(0,1):C.GC_488,(0,3):C.GC_487})

V_128 = Vertex(name = 'V_128',
               particles = [ P.vm__tilde__, P.vt, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_327,(0,2):C.GC_328,(0,1):C.GC_328,(0,3):C.GC_327})

V_129 = Vertex(name = 'V_129',
               particles = [ P.vm__tilde__, P.vt, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_489,(0,2):C.GC_490,(0,1):C.GC_490,(0,3):C.GC_489})

V_130 = Vertex(name = 'V_130',
               particles = [ P.vt__tilde__, P.vt, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_329,(0,2):C.GC_330,(0,1):C.GC_330,(0,3):C.GC_329})

V_131 = Vertex(name = 'V_131',
               particles = [ P.vt__tilde__, P.vt, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_491,(0,2):C.GC_492,(0,1):C.GC_492,(0,3):C.GC_491})

V_132 = Vertex(name = 'V_132',
               particles = [ P.ve__tilde__, P.ve, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_331,(0,2):C.GC_332,(0,1):C.GC_332,(0,3):C.GC_331})

V_133 = Vertex(name = 'V_133',
               particles = [ P.ve__tilde__, P.ve, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_493,(0,2):C.GC_494,(0,1):C.GC_494,(0,3):C.GC_493})

V_134 = Vertex(name = 'V_134',
               particles = [ P.vm__tilde__, P.ve, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_333,(0,2):C.GC_334,(0,1):C.GC_334,(0,3):C.GC_333})

V_135 = Vertex(name = 'V_135',
               particles = [ P.vm__tilde__, P.ve, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_495,(0,2):C.GC_496,(0,1):C.GC_496,(0,3):C.GC_495})

V_136 = Vertex(name = 'V_136',
               particles = [ P.vt__tilde__, P.ve, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_335,(0,2):C.GC_336,(0,1):C.GC_336,(0,3):C.GC_335})

V_137 = Vertex(name = 'V_137',
               particles = [ P.vt__tilde__, P.ve, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_497,(0,2):C.GC_498,(0,1):C.GC_498,(0,3):C.GC_497})

V_138 = Vertex(name = 'V_138',
               particles = [ P.ve__tilde__, P.vm, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_337,(0,2):C.GC_338,(0,1):C.GC_338,(0,3):C.GC_337})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ve__tilde__, P.vm, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_499,(0,2):C.GC_500,(0,1):C.GC_500,(0,3):C.GC_499})

V_140 = Vertex(name = 'V_140',
               particles = [ P.vm__tilde__, P.vm, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_339,(0,2):C.GC_340,(0,1):C.GC_340,(0,3):C.GC_339})

V_141 = Vertex(name = 'V_141',
               particles = [ P.vm__tilde__, P.vm, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_501,(0,2):C.GC_502,(0,1):C.GC_502,(0,3):C.GC_501})

V_142 = Vertex(name = 'V_142',
               particles = [ P.vt__tilde__, P.vm, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_341,(0,2):C.GC_342,(0,1):C.GC_342,(0,3):C.GC_341})

V_143 = Vertex(name = 'V_143',
               particles = [ P.vt__tilde__, P.vm, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_503,(0,2):C.GC_504,(0,1):C.GC_504,(0,3):C.GC_503})

V_144 = Vertex(name = 'V_144',
               particles = [ P.ve__tilde__, P.vt, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_343,(0,2):C.GC_344,(0,1):C.GC_344,(0,3):C.GC_343})

V_145 = Vertex(name = 'V_145',
               particles = [ P.ve__tilde__, P.vt, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_505,(0,2):C.GC_506,(0,1):C.GC_506,(0,3):C.GC_505})

V_146 = Vertex(name = 'V_146',
               particles = [ P.vm__tilde__, P.vt, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_345,(0,2):C.GC_346,(0,1):C.GC_346,(0,3):C.GC_345})

V_147 = Vertex(name = 'V_147',
               particles = [ P.vm__tilde__, P.vt, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_507,(0,2):C.GC_508,(0,1):C.GC_508,(0,3):C.GC_507})

V_148 = Vertex(name = 'V_148',
               particles = [ P.vt__tilde__, P.vt, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_347,(0,2):C.GC_348,(0,1):C.GC_348,(0,3):C.GC_347})

V_149 = Vertex(name = 'V_149',
               particles = [ P.vt__tilde__, P.vt, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_509,(0,2):C.GC_510,(0,1):C.GC_510,(0,3):C.GC_509})

V_150 = Vertex(name = 'V_150',
               particles = [ P.ve__tilde__, P.ve, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_349,(0,2):C.GC_350,(0,1):C.GC_350,(0,3):C.GC_349})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ve__tilde__, P.ve, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_511,(0,2):C.GC_512,(0,1):C.GC_512,(0,3):C.GC_511})

V_152 = Vertex(name = 'V_152',
               particles = [ P.vm__tilde__, P.ve, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_351,(0,2):C.GC_352,(0,1):C.GC_352,(0,3):C.GC_351})

V_153 = Vertex(name = 'V_153',
               particles = [ P.vm__tilde__, P.ve, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_513,(0,2):C.GC_514,(0,1):C.GC_514,(0,3):C.GC_513})

V_154 = Vertex(name = 'V_154',
               particles = [ P.vt__tilde__, P.ve, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_353,(0,2):C.GC_354,(0,1):C.GC_354,(0,3):C.GC_353})

V_155 = Vertex(name = 'V_155',
               particles = [ P.vt__tilde__, P.ve, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_515,(0,2):C.GC_516,(0,1):C.GC_516,(0,3):C.GC_515})

V_156 = Vertex(name = 'V_156',
               particles = [ P.ve__tilde__, P.vm, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_355,(0,2):C.GC_356,(0,1):C.GC_356,(0,3):C.GC_355})

V_157 = Vertex(name = 'V_157',
               particles = [ P.ve__tilde__, P.vm, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_517,(0,2):C.GC_518,(0,1):C.GC_518,(0,3):C.GC_517})

V_158 = Vertex(name = 'V_158',
               particles = [ P.vm__tilde__, P.vm, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_357,(0,2):C.GC_358,(0,1):C.GC_358,(0,3):C.GC_357})

V_159 = Vertex(name = 'V_159',
               particles = [ P.vm__tilde__, P.vm, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_519,(0,2):C.GC_520,(0,1):C.GC_520,(0,3):C.GC_519})

V_160 = Vertex(name = 'V_160',
               particles = [ P.vt__tilde__, P.vm, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_359,(0,2):C.GC_360,(0,1):C.GC_360,(0,3):C.GC_359})

V_161 = Vertex(name = 'V_161',
               particles = [ P.vt__tilde__, P.vm, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_521,(0,2):C.GC_522,(0,1):C.GC_522,(0,3):C.GC_521})

V_162 = Vertex(name = 'V_162',
               particles = [ P.ve__tilde__, P.vt, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_361,(0,2):C.GC_362,(0,1):C.GC_362,(0,3):C.GC_361})

V_163 = Vertex(name = 'V_163',
               particles = [ P.ve__tilde__, P.vt, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_523,(0,2):C.GC_524,(0,1):C.GC_524,(0,3):C.GC_523})

V_164 = Vertex(name = 'V_164',
               particles = [ P.vm__tilde__, P.vt, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_363,(0,2):C.GC_364,(0,1):C.GC_364,(0,3):C.GC_363})

V_165 = Vertex(name = 'V_165',
               particles = [ P.vm__tilde__, P.vt, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_525,(0,2):C.GC_526,(0,1):C.GC_526,(0,3):C.GC_525})

V_166 = Vertex(name = 'V_166',
               particles = [ P.vt__tilde__, P.vt, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_365,(0,2):C.GC_366,(0,1):C.GC_366,(0,3):C.GC_365})

V_167 = Vertex(name = 'V_167',
               particles = [ P.vt__tilde__, P.vt, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_527,(0,2):C.GC_528,(0,1):C.GC_528,(0,3):C.GC_527})

V_168 = Vertex(name = 'V_168',
               particles = [ P.ve__tilde__, P.ve, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,1):C.GC_367,(0,3):C.GC_368,(0,2):C.GC_368,(0,0):C.GC_37,(0,4):C.GC_367})

V_169 = Vertex(name = 'V_169',
               particles = [ P.ve__tilde__, P.ve, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_529,(0,2):C.GC_530,(0,1):C.GC_530,(0,3):C.GC_39})

V_170 = Vertex(name = 'V_170',
               particles = [ P.vm__tilde__, P.ve, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_369,(0,2):C.GC_370,(0,1):C.GC_370,(0,3):C.GC_369})

V_171 = Vertex(name = 'V_171',
               particles = [ P.vm__tilde__, P.ve, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_531,(0,2):C.GC_532,(0,1):C.GC_532,(0,3):C.GC_531})

V_172 = Vertex(name = 'V_172',
               particles = [ P.vt__tilde__, P.ve, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_371,(0,2):C.GC_372,(0,1):C.GC_372,(0,3):C.GC_371})

V_173 = Vertex(name = 'V_173',
               particles = [ P.vt__tilde__, P.ve, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_533,(0,2):C.GC_534,(0,1):C.GC_534,(0,3):C.GC_533})

V_174 = Vertex(name = 'V_174',
               particles = [ P.ve__tilde__, P.vm, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_373,(0,2):C.GC_374,(0,1):C.GC_374,(0,3):C.GC_373})

V_175 = Vertex(name = 'V_175',
               particles = [ P.ve__tilde__, P.vm, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_535,(0,2):C.GC_536,(0,1):C.GC_536,(0,3):C.GC_535})

V_176 = Vertex(name = 'V_176',
               particles = [ P.vm__tilde__, P.vm, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_375,(0,2):C.GC_376,(0,1):C.GC_376,(0,3):C.GC_375})

V_177 = Vertex(name = 'V_177',
               particles = [ P.vm__tilde__, P.vm, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_537,(0,2):C.GC_538,(0,1):C.GC_538,(0,3):C.GC_537})

V_178 = Vertex(name = 'V_178',
               particles = [ P.vt__tilde__, P.vm, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_377,(0,2):C.GC_378,(0,1):C.GC_378,(0,3):C.GC_377})

V_179 = Vertex(name = 'V_179',
               particles = [ P.vt__tilde__, P.vm, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_539,(0,2):C.GC_540,(0,1):C.GC_540,(0,3):C.GC_539})

V_180 = Vertex(name = 'V_180',
               particles = [ P.ve__tilde__, P.vt, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_379,(0,2):C.GC_380,(0,1):C.GC_380,(0,3):C.GC_379})

V_181 = Vertex(name = 'V_181',
               particles = [ P.ve__tilde__, P.vt, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_541,(0,2):C.GC_542,(0,1):C.GC_542,(0,3):C.GC_541})

V_182 = Vertex(name = 'V_182',
               particles = [ P.vm__tilde__, P.vt, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_381,(0,2):C.GC_382,(0,1):C.GC_382,(0,3):C.GC_381})

V_183 = Vertex(name = 'V_183',
               particles = [ P.vm__tilde__, P.vt, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_543,(0,2):C.GC_544,(0,1):C.GC_544,(0,3):C.GC_543})

V_184 = Vertex(name = 'V_184',
               particles = [ P.vt__tilde__, P.vt, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_383,(0,2):C.GC_384,(0,1):C.GC_384,(0,3):C.GC_383})

V_185 = Vertex(name = 'V_185',
               particles = [ P.vt__tilde__, P.vt, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_545,(0,2):C.GC_546,(0,1):C.GC_546,(0,3):C.GC_545})

V_186 = Vertex(name = 'V_186',
               particles = [ P.ve__tilde__, P.ve, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,1):C.GC_385,(0,3):C.GC_386,(0,2):C.GC_386,(0,0):C.GC_32,(0,4):C.GC_35})

V_187 = Vertex(name = 'V_187',
               particles = [ P.ve__tilde__, P.ve, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_547,(0,2):C.GC_548,(0,1):C.GC_548,(0,3):C.GC_547})

V_188 = Vertex(name = 'V_188',
               particles = [ P.vm__tilde__, P.ve, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_387,(0,2):C.GC_388,(0,1):C.GC_388,(0,3):C.GC_387})

V_189 = Vertex(name = 'V_189',
               particles = [ P.vm__tilde__, P.ve, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_549,(0,2):C.GC_550,(0,1):C.GC_550,(0,3):C.GC_549})

V_190 = Vertex(name = 'V_190',
               particles = [ P.vt__tilde__, P.ve, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_389,(0,2):C.GC_390,(0,1):C.GC_390,(0,3):C.GC_389})

V_191 = Vertex(name = 'V_191',
               particles = [ P.vt__tilde__, P.ve, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_551,(0,2):C.GC_552,(0,1):C.GC_552,(0,3):C.GC_551})

V_192 = Vertex(name = 'V_192',
               particles = [ P.ve__tilde__, P.vm, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_391,(0,2):C.GC_392,(0,1):C.GC_392,(0,3):C.GC_391})

V_193 = Vertex(name = 'V_193',
               particles = [ P.ve__tilde__, P.vm, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_553,(0,2):C.GC_554,(0,1):C.GC_554,(0,3):C.GC_553})

V_194 = Vertex(name = 'V_194',
               particles = [ P.vm__tilde__, P.vm, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_393,(0,2):C.GC_394,(0,1):C.GC_394,(0,3):C.GC_393})

V_195 = Vertex(name = 'V_195',
               particles = [ P.vm__tilde__, P.vm, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_555,(0,2):C.GC_556,(0,1):C.GC_556,(0,3):C.GC_555})

V_196 = Vertex(name = 'V_196',
               particles = [ P.vt__tilde__, P.vm, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_395,(0,2):C.GC_396,(0,1):C.GC_396,(0,3):C.GC_395})

V_197 = Vertex(name = 'V_197',
               particles = [ P.vt__tilde__, P.vm, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_557,(0,2):C.GC_558,(0,1):C.GC_558,(0,3):C.GC_557})

V_198 = Vertex(name = 'V_198',
               particles = [ P.ve__tilde__, P.vt, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_397,(0,2):C.GC_398,(0,1):C.GC_398,(0,3):C.GC_397})

V_199 = Vertex(name = 'V_199',
               particles = [ P.ve__tilde__, P.vt, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_559,(0,2):C.GC_560,(0,1):C.GC_560,(0,3):C.GC_559})

V_200 = Vertex(name = 'V_200',
               particles = [ P.vm__tilde__, P.vt, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_399,(0,2):C.GC_400,(0,1):C.GC_400,(0,3):C.GC_399})

V_201 = Vertex(name = 'V_201',
               particles = [ P.vm__tilde__, P.vt, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_561,(0,2):C.GC_562,(0,1):C.GC_562,(0,3):C.GC_561})

V_202 = Vertex(name = 'V_202',
               particles = [ P.vt__tilde__, P.vt, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_401,(0,2):C.GC_402,(0,1):C.GC_402,(0,3):C.GC_401})

V_203 = Vertex(name = 'V_203',
               particles = [ P.vt__tilde__, P.vt, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18 ],
               couplings = {(0,0):C.GC_563,(0,2):C.GC_564,(0,1):C.GC_564,(0,3):C.GC_563})

V_204 = Vertex(name = 'V_204',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_62,(0,13):C.GC_785,(0,9):C.GC_97,(0,2):C.GC_61,(0,14):C.GC_784,(0,5):C.GC_565,(0,11):C.GC_98,(0,7):C.GC_566,(0,10):C.GC_98,(0,6):C.GC_566,(0,12):C.GC_97,(0,3):C.GC_61,(0,15):C.GC_784,(0,8):C.GC_565,(0,4):C.GC_62,(0,0):C.GC_785})

V_205 = Vertex(name = 'V_205',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_80,(0,13):C.GC_44,(0,9):C.GC_151,(0,2):C.GC_79,(0,14):C.GC_43,(0,5):C.GC_621,(0,11):C.GC_152,(0,7):C.GC_622,(0,10):C.GC_152,(0,6):C.GC_622,(0,12):C.GC_151,(0,3):C.GC_79,(0,15):C.GC_43,(0,8):C.GC_621,(0,4):C.GC_80,(0,0):C.GC_44})

V_206 = Vertex(name = 'V_206',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_104,(0,13):C.GC_787,(0,9):C.GC_99,(0,2):C.GC_103,(0,14):C.GC_786,(0,5):C.GC_802,(0,11):C.GC_100,(0,7):C.GC_803,(0,10):C.GC_100,(0,6):C.GC_803,(0,12):C.GC_99,(0,3):C.GC_103,(0,15):C.GC_786,(0,8):C.GC_802,(0,4):C.GC_104,(0,0):C.GC_787})

V_207 = Vertex(name = 'V_207',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_162,(0,13):C.GC_640,(0,9):C.GC_153,(0,2):C.GC_161,(0,14):C.GC_639,(0,5):C.GC_623,(0,11):C.GC_154,(0,7):C.GC_624,(0,10):C.GC_154,(0,6):C.GC_624,(0,12):C.GC_153,(0,3):C.GC_161,(0,15):C.GC_639,(0,8):C.GC_623,(0,4):C.GC_162,(0,0):C.GC_640})

V_208 = Vertex(name = 'V_208',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,2):C.GC_110,(0,14):C.GC_789,(0,10):C.GC_101,(0,3):C.GC_109,(0,15):C.GC_788,(0,6):C.GC_820,(0,12):C.GC_102,(0,8):C.GC_821,(0,11):C.GC_102,(0,7):C.GC_821,(0,0):C.GC_42,(0,9):C.GC_820,(0,13):C.GC_101,(0,4):C.GC_109,(0,16):C.GC_788,(0,5):C.GC_110,(0,1):C.GC_789})

V_209 = Vertex(name = 'V_209',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_172,(0,13):C.GC_658,(0,9):C.GC_155,(0,2):C.GC_171,(0,14):C.GC_657,(0,5):C.GC_625,(0,11):C.GC_156,(0,7):C.GC_626,(0,10):C.GC_156,(0,6):C.GC_626,(0,8):C.GC_620,(0,12):C.GC_155,(0,3):C.GC_171,(0,15):C.GC_657,(0,4):C.GC_172,(0,0):C.GC_658})

V_210 = Vertex(name = 'V_210',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_584,(0,13):C.GC_791,(0,9):C.GC_838,(0,2):C.GC_583,(0,14):C.GC_790,(0,5):C.GC_567,(0,11):C.GC_839,(0,7):C.GC_568,(0,10):C.GC_839,(0,6):C.GC_568,(0,12):C.GC_838,(0,3):C.GC_583,(0,15):C.GC_790,(0,8):C.GC_567,(0,4):C.GC_584,(0,0):C.GC_791})

V_211 = Vertex(name = 'V_211',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_676,(0,13):C.GC_182,(0,9):C.GC_157,(0,2):C.GC_675,(0,14):C.GC_181,(0,5):C.GC_627,(0,11):C.GC_158,(0,7):C.GC_628,(0,10):C.GC_158,(0,6):C.GC_628,(0,12):C.GC_157,(0,3):C.GC_675,(0,15):C.GC_181,(0,8):C.GC_627,(0,4):C.GC_676,(0,0):C.GC_182})

V_212 = Vertex(name = 'V_212',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_857,(0,13):C.GC_793,(0,9):C.GC_840,(0,2):C.GC_856,(0,14):C.GC_792,(0,5):C.GC_808,(0,11):C.GC_841,(0,7):C.GC_809,(0,10):C.GC_841,(0,6):C.GC_809,(0,12):C.GC_840,(0,3):C.GC_856,(0,15):C.GC_792,(0,8):C.GC_808,(0,4):C.GC_857,(0,0):C.GC_793})

V_213 = Vertex(name = 'V_213',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_678,(0,13):C.GC_646,(0,9):C.GC_693,(0,2):C.GC_677,(0,14):C.GC_645,(0,5):C.GC_629,(0,11):C.GC_694,(0,7):C.GC_630,(0,10):C.GC_694,(0,6):C.GC_630,(0,12):C.GC_693,(0,3):C.GC_677,(0,15):C.GC_645,(0,8):C.GC_629,(0,4):C.GC_678,(0,0):C.GC_646})

V_214 = Vertex(name = 'V_214',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_875,(0,13):C.GC_795,(0,9):C.GC_842,(0,2):C.GC_874,(0,14):C.GC_794,(0,5):C.GC_826,(0,11):C.GC_843,(0,7):C.GC_827,(0,10):C.GC_843,(0,6):C.GC_827,(0,12):C.GC_842,(0,3):C.GC_874,(0,15):C.GC_794,(0,8):C.GC_826,(0,4):C.GC_875,(0,0):C.GC_795})

V_215 = Vertex(name = 'V_215',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_680,(0,13):C.GC_664,(0,9):C.GC_711,(0,2):C.GC_679,(0,14):C.GC_663,(0,5):C.GC_631,(0,11):C.GC_712,(0,7):C.GC_632,(0,10):C.GC_712,(0,6):C.GC_632,(0,12):C.GC_711,(0,3):C.GC_679,(0,15):C.GC_663,(0,8):C.GC_631,(0,4):C.GC_680,(0,0):C.GC_664})

V_216 = Vertex(name = 'V_216',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_602,(0,13):C.GC_797,(0,9):C.GC_892,(0,2):C.GC_601,(0,14):C.GC_796,(0,5):C.GC_569,(0,11):C.GC_893,(0,7):C.GC_570,(0,10):C.GC_893,(0,6):C.GC_570,(0,12):C.GC_892,(0,3):C.GC_601,(0,15):C.GC_796,(0,8):C.GC_569,(0,4):C.GC_602,(0,0):C.GC_797})

V_217 = Vertex(name = 'V_217',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_730,(0,13):C.GC_212,(0,9):C.GC_159,(0,2):C.GC_729,(0,14):C.GC_211,(0,5):C.GC_633,(0,11):C.GC_160,(0,7):C.GC_634,(0,10):C.GC_160,(0,6):C.GC_634,(0,12):C.GC_159,(0,3):C.GC_729,(0,15):C.GC_211,(0,8):C.GC_633,(0,4):C.GC_730,(0,0):C.GC_212})

V_218 = Vertex(name = 'V_218',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_911,(0,13):C.GC_799,(0,9):C.GC_894,(0,2):C.GC_910,(0,14):C.GC_798,(0,5):C.GC_814,(0,11):C.GC_895,(0,7):C.GC_815,(0,10):C.GC_895,(0,6):C.GC_815,(0,12):C.GC_894,(0,3):C.GC_910,(0,15):C.GC_798,(0,8):C.GC_814,(0,4):C.GC_911,(0,0):C.GC_799})

V_219 = Vertex(name = 'V_219',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_732,(0,13):C.GC_652,(0,9):C.GC_747,(0,2):C.GC_731,(0,14):C.GC_651,(0,5):C.GC_635,(0,11):C.GC_748,(0,7):C.GC_636,(0,10):C.GC_748,(0,6):C.GC_636,(0,12):C.GC_747,(0,3):C.GC_731,(0,15):C.GC_651,(0,8):C.GC_635,(0,4):C.GC_732,(0,0):C.GC_652})

V_220 = Vertex(name = 'V_220',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_929,(0,13):C.GC_801,(0,9):C.GC_896,(0,2):C.GC_928,(0,14):C.GC_800,(0,5):C.GC_832,(0,11):C.GC_897,(0,7):C.GC_833,(0,10):C.GC_897,(0,6):C.GC_833,(0,12):C.GC_896,(0,3):C.GC_928,(0,15):C.GC_800,(0,8):C.GC_832,(0,4):C.GC_929,(0,0):C.GC_801})

V_221 = Vertex(name = 'V_221',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_734,(0,13):C.GC_670,(0,9):C.GC_765,(0,2):C.GC_733,(0,14):C.GC_669,(0,5):C.GC_637,(0,11):C.GC_766,(0,7):C.GC_638,(0,10):C.GC_766,(0,6):C.GC_638,(0,12):C.GC_765,(0,3):C.GC_733,(0,15):C.GC_669,(0,8):C.GC_637,(0,4):C.GC_734,(0,0):C.GC_670})

V_222 = Vertex(name = 'V_222',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_64,(0,13):C.GC_805,(0,9):C.GC_105,(0,2):C.GC_63,(0,14):C.GC_804,(0,5):C.GC_571,(0,11):C.GC_106,(0,7):C.GC_572,(0,10):C.GC_106,(0,6):C.GC_572,(0,12):C.GC_105,(0,3):C.GC_63,(0,15):C.GC_804,(0,8):C.GC_571,(0,4):C.GC_64,(0,0):C.GC_805})

V_223 = Vertex(name = 'V_223',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_82,(0,13):C.GC_46,(0,9):C.GC_163,(0,2):C.GC_81,(0,14):C.GC_45,(0,5):C.GC_641,(0,11):C.GC_164,(0,7):C.GC_642,(0,10):C.GC_164,(0,6):C.GC_642,(0,12):C.GC_163,(0,3):C.GC_81,(0,15):C.GC_45,(0,8):C.GC_641,(0,4):C.GC_82,(0,0):C.GC_46})

V_224 = Vertex(name = 'V_224',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_112,(0,13):C.GC_807,(0,9):C.GC_107,(0,2):C.GC_111,(0,14):C.GC_806,(0,5):C.GC_822,(0,11):C.GC_108,(0,7):C.GC_823,(0,10):C.GC_108,(0,6):C.GC_823,(0,12):C.GC_107,(0,3):C.GC_111,(0,15):C.GC_806,(0,8):C.GC_822,(0,4):C.GC_112,(0,0):C.GC_807})

V_225 = Vertex(name = 'V_225',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_174,(0,13):C.GC_660,(0,9):C.GC_165,(0,2):C.GC_173,(0,14):C.GC_659,(0,5):C.GC_643,(0,11):C.GC_166,(0,7):C.GC_644,(0,10):C.GC_166,(0,6):C.GC_644,(0,12):C.GC_165,(0,3):C.GC_173,(0,15):C.GC_659,(0,8):C.GC_643,(0,4):C.GC_174,(0,0):C.GC_660})

V_226 = Vertex(name = 'V_226',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_590,(0,13):C.GC_811,(0,9):C.GC_858,(0,2):C.GC_589,(0,14):C.GC_810,(0,5):C.GC_573,(0,11):C.GC_859,(0,7):C.GC_574,(0,10):C.GC_859,(0,6):C.GC_574,(0,12):C.GC_858,(0,3):C.GC_589,(0,15):C.GC_810,(0,8):C.GC_573,(0,4):C.GC_590,(0,0):C.GC_811})

V_227 = Vertex(name = 'V_227',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_696,(0,13):C.GC_192,(0,9):C.GC_167,(0,2):C.GC_695,(0,14):C.GC_191,(0,5):C.GC_647,(0,11):C.GC_168,(0,7):C.GC_648,(0,10):C.GC_168,(0,6):C.GC_648,(0,12):C.GC_167,(0,3):C.GC_695,(0,15):C.GC_191,(0,8):C.GC_647,(0,4):C.GC_696,(0,0):C.GC_192})

V_228 = Vertex(name = 'V_228',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_877,(0,13):C.GC_813,(0,9):C.GC_860,(0,2):C.GC_876,(0,14):C.GC_812,(0,5):C.GC_828,(0,11):C.GC_861,(0,7):C.GC_829,(0,10):C.GC_861,(0,6):C.GC_829,(0,12):C.GC_860,(0,3):C.GC_876,(0,15):C.GC_812,(0,8):C.GC_828,(0,4):C.GC_877,(0,0):C.GC_813})

V_229 = Vertex(name = 'V_229',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_698,(0,13):C.GC_666,(0,9):C.GC_713,(0,2):C.GC_697,(0,14):C.GC_665,(0,5):C.GC_649,(0,11):C.GC_714,(0,7):C.GC_650,(0,10):C.GC_714,(0,6):C.GC_650,(0,12):C.GC_713,(0,3):C.GC_697,(0,15):C.GC_665,(0,8):C.GC_649,(0,4):C.GC_698,(0,0):C.GC_666})

V_230 = Vertex(name = 'V_230',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_608,(0,13):C.GC_817,(0,9):C.GC_912,(0,2):C.GC_607,(0,14):C.GC_816,(0,5):C.GC_575,(0,11):C.GC_913,(0,7):C.GC_576,(0,10):C.GC_913,(0,6):C.GC_576,(0,12):C.GC_912,(0,3):C.GC_607,(0,15):C.GC_816,(0,8):C.GC_575,(0,4):C.GC_608,(0,0):C.GC_817})

V_231 = Vertex(name = 'V_231',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_750,(0,13):C.GC_222,(0,9):C.GC_169,(0,2):C.GC_749,(0,14):C.GC_221,(0,5):C.GC_653,(0,11):C.GC_170,(0,7):C.GC_654,(0,10):C.GC_170,(0,6):C.GC_654,(0,12):C.GC_169,(0,3):C.GC_749,(0,15):C.GC_221,(0,8):C.GC_653,(0,4):C.GC_750,(0,0):C.GC_222})

V_232 = Vertex(name = 'V_232',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_931,(0,13):C.GC_819,(0,9):C.GC_914,(0,2):C.GC_930,(0,14):C.GC_818,(0,5):C.GC_834,(0,11):C.GC_915,(0,7):C.GC_835,(0,10):C.GC_915,(0,6):C.GC_835,(0,12):C.GC_914,(0,3):C.GC_930,(0,15):C.GC_818,(0,8):C.GC_834,(0,4):C.GC_931,(0,0):C.GC_819})

V_233 = Vertex(name = 'V_233',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_752,(0,13):C.GC_672,(0,9):C.GC_767,(0,2):C.GC_751,(0,14):C.GC_671,(0,5):C.GC_655,(0,11):C.GC_768,(0,7):C.GC_656,(0,10):C.GC_768,(0,6):C.GC_656,(0,12):C.GC_767,(0,3):C.GC_751,(0,15):C.GC_671,(0,8):C.GC_655,(0,4):C.GC_752,(0,0):C.GC_672})

V_234 = Vertex(name = 'V_234',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_66,(0,13):C.GC_825,(0,9):C.GC_113,(0,2):C.GC_65,(0,14):C.GC_824,(0,5):C.GC_577,(0,11):C.GC_114,(0,7):C.GC_578,(0,10):C.GC_114,(0,6):C.GC_578,(0,12):C.GC_113,(0,3):C.GC_65,(0,15):C.GC_824,(0,8):C.GC_577,(0,4):C.GC_66,(0,0):C.GC_825})

V_235 = Vertex(name = 'V_235',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_84,(0,13):C.GC_48,(0,9):C.GC_175,(0,2):C.GC_83,(0,14):C.GC_47,(0,5):C.GC_661,(0,11):C.GC_176,(0,7):C.GC_662,(0,10):C.GC_176,(0,6):C.GC_662,(0,12):C.GC_175,(0,3):C.GC_83,(0,15):C.GC_47,(0,8):C.GC_661,(0,4):C.GC_84,(0,0):C.GC_48})

V_236 = Vertex(name = 'V_236',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_596,(0,13):C.GC_831,(0,9):C.GC_878,(0,2):C.GC_595,(0,14):C.GC_830,(0,5):C.GC_579,(0,11):C.GC_879,(0,7):C.GC_580,(0,10):C.GC_879,(0,6):C.GC_580,(0,12):C.GC_878,(0,3):C.GC_595,(0,15):C.GC_830,(0,8):C.GC_579,(0,4):C.GC_596,(0,0):C.GC_831})

V_237 = Vertex(name = 'V_237',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_716,(0,13):C.GC_202,(0,9):C.GC_177,(0,2):C.GC_715,(0,14):C.GC_201,(0,5):C.GC_667,(0,11):C.GC_178,(0,7):C.GC_668,(0,10):C.GC_178,(0,6):C.GC_668,(0,12):C.GC_177,(0,3):C.GC_715,(0,15):C.GC_201,(0,8):C.GC_667,(0,4):C.GC_716,(0,0):C.GC_202})

V_238 = Vertex(name = 'V_238',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_615,(0,13):C.GC_837,(0,9):C.GC_932,(0,2):C.GC_614,(0,14):C.GC_836,(0,5):C.GC_581,(0,11):C.GC_933,(0,7):C.GC_582,(0,10):C.GC_933,(0,6):C.GC_582,(0,12):C.GC_932,(0,3):C.GC_614,(0,15):C.GC_836,(0,8):C.GC_581,(0,4):C.GC_615,(0,0):C.GC_837})

V_239 = Vertex(name = 'V_239',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_770,(0,13):C.GC_232,(0,9):C.GC_179,(0,2):C.GC_769,(0,14):C.GC_231,(0,5):C.GC_673,(0,11):C.GC_180,(0,7):C.GC_674,(0,10):C.GC_180,(0,6):C.GC_674,(0,12):C.GC_179,(0,3):C.GC_769,(0,15):C.GC_231,(0,8):C.GC_673,(0,4):C.GC_770,(0,0):C.GC_232})

V_240 = Vertex(name = 'V_240',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_68,(0,13):C.GC_845,(0,9):C.GC_115,(0,2):C.GC_67,(0,14):C.GC_844,(0,5):C.GC_585,(0,11):C.GC_116,(0,7):C.GC_586,(0,10):C.GC_116,(0,6):C.GC_586,(0,12):C.GC_115,(0,3):C.GC_67,(0,15):C.GC_844,(0,8):C.GC_585,(0,4):C.GC_68,(0,0):C.GC_845})

V_241 = Vertex(name = 'V_241',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_86,(0,13):C.GC_50,(0,9):C.GC_183,(0,2):C.GC_85,(0,14):C.GC_49,(0,5):C.GC_681,(0,11):C.GC_184,(0,7):C.GC_682,(0,10):C.GC_184,(0,6):C.GC_682,(0,12):C.GC_183,(0,3):C.GC_85,(0,15):C.GC_49,(0,8):C.GC_681,(0,4):C.GC_86,(0,0):C.GC_50})

V_242 = Vertex(name = 'V_242',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_122,(0,13):C.GC_847,(0,9):C.GC_117,(0,2):C.GC_121,(0,14):C.GC_846,(0,5):C.GC_862,(0,11):C.GC_118,(0,7):C.GC_863,(0,10):C.GC_118,(0,6):C.GC_863,(0,12):C.GC_117,(0,3):C.GC_121,(0,15):C.GC_846,(0,8):C.GC_862,(0,4):C.GC_122,(0,0):C.GC_847})

V_243 = Vertex(name = 'V_243',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_194,(0,13):C.GC_700,(0,9):C.GC_185,(0,2):C.GC_193,(0,14):C.GC_699,(0,5):C.GC_683,(0,11):C.GC_186,(0,7):C.GC_684,(0,10):C.GC_186,(0,6):C.GC_684,(0,12):C.GC_185,(0,3):C.GC_193,(0,15):C.GC_699,(0,8):C.GC_683,(0,4):C.GC_194,(0,0):C.GC_700})

V_244 = Vertex(name = 'V_244',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_128,(0,13):C.GC_849,(0,9):C.GC_119,(0,2):C.GC_127,(0,14):C.GC_848,(0,5):C.GC_880,(0,11):C.GC_120,(0,7):C.GC_881,(0,10):C.GC_120,(0,6):C.GC_881,(0,12):C.GC_119,(0,3):C.GC_127,(0,15):C.GC_848,(0,8):C.GC_880,(0,4):C.GC_128,(0,0):C.GC_849})

V_245 = Vertex(name = 'V_245',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_204,(0,13):C.GC_718,(0,9):C.GC_187,(0,2):C.GC_203,(0,14):C.GC_717,(0,5):C.GC_685,(0,11):C.GC_188,(0,7):C.GC_686,(0,10):C.GC_188,(0,6):C.GC_686,(0,12):C.GC_187,(0,3):C.GC_203,(0,15):C.GC_717,(0,8):C.GC_685,(0,4):C.GC_204,(0,0):C.GC_718})

V_246 = Vertex(name = 'V_246',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_604,(0,13):C.GC_851,(0,9):C.GC_898,(0,2):C.GC_603,(0,14):C.GC_850,(0,5):C.GC_587,(0,11):C.GC_899,(0,7):C.GC_588,(0,10):C.GC_899,(0,6):C.GC_588,(0,12):C.GC_898,(0,3):C.GC_603,(0,15):C.GC_850,(0,8):C.GC_587,(0,4):C.GC_604,(0,0):C.GC_851})

V_247 = Vertex(name = 'V_247',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_736,(0,13):C.GC_214,(0,9):C.GC_189,(0,2):C.GC_735,(0,14):C.GC_213,(0,5):C.GC_687,(0,11):C.GC_190,(0,7):C.GC_688,(0,10):C.GC_190,(0,6):C.GC_688,(0,12):C.GC_189,(0,3):C.GC_735,(0,15):C.GC_213,(0,8):C.GC_687,(0,4):C.GC_736,(0,0):C.GC_214})

V_248 = Vertex(name = 'V_248',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_917,(0,13):C.GC_853,(0,9):C.GC_900,(0,2):C.GC_916,(0,14):C.GC_852,(0,5):C.GC_868,(0,11):C.GC_901,(0,7):C.GC_869,(0,10):C.GC_901,(0,6):C.GC_869,(0,12):C.GC_900,(0,3):C.GC_916,(0,15):C.GC_852,(0,8):C.GC_868,(0,4):C.GC_917,(0,0):C.GC_853})

V_249 = Vertex(name = 'V_249',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_738,(0,13):C.GC_706,(0,9):C.GC_753,(0,2):C.GC_737,(0,14):C.GC_705,(0,5):C.GC_689,(0,11):C.GC_754,(0,7):C.GC_690,(0,10):C.GC_754,(0,6):C.GC_690,(0,12):C.GC_753,(0,3):C.GC_737,(0,15):C.GC_705,(0,8):C.GC_689,(0,4):C.GC_738,(0,0):C.GC_706})

V_250 = Vertex(name = 'V_250',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_935,(0,13):C.GC_855,(0,9):C.GC_902,(0,2):C.GC_934,(0,14):C.GC_854,(0,5):C.GC_886,(0,11):C.GC_903,(0,7):C.GC_887,(0,10):C.GC_903,(0,6):C.GC_887,(0,12):C.GC_902,(0,3):C.GC_934,(0,15):C.GC_854,(0,8):C.GC_886,(0,4):C.GC_935,(0,0):C.GC_855})

V_251 = Vertex(name = 'V_251',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_740,(0,13):C.GC_724,(0,9):C.GC_771,(0,2):C.GC_739,(0,14):C.GC_723,(0,5):C.GC_691,(0,11):C.GC_772,(0,7):C.GC_692,(0,10):C.GC_772,(0,6):C.GC_692,(0,12):C.GC_771,(0,3):C.GC_739,(0,15):C.GC_723,(0,8):C.GC_691,(0,4):C.GC_740,(0,0):C.GC_724})

V_252 = Vertex(name = 'V_252',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_70,(0,13):C.GC_865,(0,9):C.GC_123,(0,2):C.GC_69,(0,14):C.GC_864,(0,5):C.GC_591,(0,11):C.GC_124,(0,7):C.GC_592,(0,10):C.GC_124,(0,6):C.GC_592,(0,12):C.GC_123,(0,3):C.GC_69,(0,15):C.GC_864,(0,8):C.GC_591,(0,4):C.GC_70,(0,0):C.GC_865})

V_253 = Vertex(name = 'V_253',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_88,(0,13):C.GC_52,(0,9):C.GC_195,(0,2):C.GC_87,(0,14):C.GC_51,(0,5):C.GC_701,(0,11):C.GC_196,(0,7):C.GC_702,(0,10):C.GC_196,(0,6):C.GC_702,(0,12):C.GC_195,(0,3):C.GC_87,(0,15):C.GC_51,(0,8):C.GC_701,(0,4):C.GC_88,(0,0):C.GC_52})

V_254 = Vertex(name = 'V_254',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_130,(0,13):C.GC_867,(0,9):C.GC_125,(0,2):C.GC_129,(0,14):C.GC_866,(0,5):C.GC_882,(0,11):C.GC_126,(0,7):C.GC_883,(0,10):C.GC_126,(0,6):C.GC_883,(0,12):C.GC_125,(0,3):C.GC_129,(0,15):C.GC_866,(0,8):C.GC_882,(0,4):C.GC_130,(0,0):C.GC_867})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_206,(0,13):C.GC_720,(0,9):C.GC_197,(0,2):C.GC_205,(0,14):C.GC_719,(0,5):C.GC_703,(0,11):C.GC_198,(0,7):C.GC_704,(0,10):C.GC_198,(0,6):C.GC_704,(0,12):C.GC_197,(0,3):C.GC_205,(0,15):C.GC_719,(0,8):C.GC_703,(0,4):C.GC_206,(0,0):C.GC_720})

V_256 = Vertex(name = 'V_256',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,14):C.GC_871,(0,1):C.GC_611,(0,9):C.GC_40,(0,2):C.GC_609,(0,10):C.GC_918,(0,15):C.GC_870,(0,5):C.GC_593,(0,7):C.GC_594,(0,12):C.GC_919,(0,6):C.GC_594,(0,11):C.GC_919,(0,3):C.GC_610,(0,16):C.GC_870,(0,8):C.GC_593,(0,13):C.GC_918,(0,4):C.GC_611,(0,0):C.GC_871})

V_257 = Vertex(name = 'V_257',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,13):C.GC_224,(0,1):C.GC_756,(0,2):C.GC_755,(0,9):C.GC_199,(0,14):C.GC_223,(0,5):C.GC_707,(0,7):C.GC_708,(0,11):C.GC_200,(0,6):C.GC_708,(0,10):C.GC_200,(0,3):C.GC_755,(0,15):C.GC_223,(0,8):C.GC_707,(0,12):C.GC_199,(0,4):C.GC_756,(0,0):C.GC_224})

V_258 = Vertex(name = 'V_258',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_937,(0,13):C.GC_873,(0,9):C.GC_920,(0,2):C.GC_936,(0,14):C.GC_872,(0,5):C.GC_888,(0,11):C.GC_921,(0,7):C.GC_889,(0,10):C.GC_921,(0,6):C.GC_889,(0,12):C.GC_920,(0,3):C.GC_936,(0,15):C.GC_872,(0,8):C.GC_888,(0,4):C.GC_937,(0,0):C.GC_873})

V_259 = Vertex(name = 'V_259',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_758,(0,13):C.GC_726,(0,9):C.GC_773,(0,2):C.GC_757,(0,14):C.GC_725,(0,5):C.GC_709,(0,11):C.GC_774,(0,7):C.GC_710,(0,10):C.GC_774,(0,6):C.GC_710,(0,12):C.GC_773,(0,3):C.GC_757,(0,15):C.GC_725,(0,8):C.GC_709,(0,4):C.GC_758,(0,0):C.GC_726})

V_260 = Vertex(name = 'V_260',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_72,(0,13):C.GC_885,(0,9):C.GC_131,(0,2):C.GC_71,(0,14):C.GC_884,(0,5):C.GC_597,(0,11):C.GC_132,(0,7):C.GC_598,(0,10):C.GC_132,(0,6):C.GC_598,(0,12):C.GC_131,(0,3):C.GC_71,(0,15):C.GC_884,(0,8):C.GC_597,(0,4):C.GC_72,(0,0):C.GC_885})

V_261 = Vertex(name = 'V_261',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_90,(0,13):C.GC_54,(0,9):C.GC_207,(0,2):C.GC_89,(0,14):C.GC_53,(0,5):C.GC_721,(0,11):C.GC_208,(0,7):C.GC_722,(0,10):C.GC_208,(0,6):C.GC_722,(0,12):C.GC_207,(0,3):C.GC_89,(0,15):C.GC_53,(0,8):C.GC_721,(0,4):C.GC_90,(0,0):C.GC_54})

V_262 = Vertex(name = 'V_262',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,14):C.GC_891,(0,1):C.GC_617,(0,9):C.GC_41,(0,2):C.GC_616,(0,15):C.GC_890,(0,5):C.GC_599,(0,10):C.GC_938,(0,7):C.GC_600,(0,12):C.GC_939,(0,6):C.GC_600,(0,11):C.GC_939,(0,3):C.GC_616,(0,16):C.GC_890,(0,8):C.GC_599,(0,13):C.GC_938,(0,4):C.GC_617,(0,0):C.GC_891})

V_263 = Vertex(name = 'V_263',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,13):C.GC_234,(0,1):C.GC_777,(0,2):C.GC_775,(0,14):C.GC_233,(0,5):C.GC_727,(0,9):C.GC_209,(0,7):C.GC_728,(0,11):C.GC_210,(0,6):C.GC_728,(0,10):C.GC_210,(0,3):C.GC_776,(0,15):C.GC_233,(0,8):C.GC_727,(0,12):C.GC_209,(0,4):C.GC_777,(0,0):C.GC_234})

V_264 = Vertex(name = 'V_264',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_74,(0,13):C.GC_905,(0,9):C.GC_133,(0,2):C.GC_73,(0,14):C.GC_904,(0,5):C.GC_605,(0,11):C.GC_134,(0,7):C.GC_606,(0,10):C.GC_134,(0,6):C.GC_606,(0,12):C.GC_133,(0,3):C.GC_73,(0,15):C.GC_904,(0,8):C.GC_605,(0,4):C.GC_74,(0,0):C.GC_905})

V_265 = Vertex(name = 'V_265',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_92,(0,13):C.GC_56,(0,9):C.GC_215,(0,2):C.GC_91,(0,14):C.GC_55,(0,5):C.GC_741,(0,11):C.GC_216,(0,7):C.GC_742,(0,10):C.GC_216,(0,6):C.GC_742,(0,12):C.GC_215,(0,3):C.GC_91,(0,15):C.GC_55,(0,8):C.GC_741,(0,4):C.GC_92,(0,0):C.GC_56})

V_266 = Vertex(name = 'V_266',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_140,(0,13):C.GC_907,(0,9):C.GC_135,(0,2):C.GC_139,(0,14):C.GC_906,(0,5):C.GC_922,(0,11):C.GC_136,(0,7):C.GC_923,(0,10):C.GC_136,(0,6):C.GC_923,(0,12):C.GC_135,(0,3):C.GC_139,(0,15):C.GC_906,(0,8):C.GC_922,(0,4):C.GC_140,(0,0):C.GC_907})

V_267 = Vertex(name = 'V_267',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_226,(0,13):C.GC_760,(0,9):C.GC_217,(0,2):C.GC_225,(0,14):C.GC_759,(0,5):C.GC_743,(0,11):C.GC_218,(0,7):C.GC_744,(0,10):C.GC_218,(0,6):C.GC_744,(0,12):C.GC_217,(0,3):C.GC_225,(0,15):C.GC_759,(0,8):C.GC_743,(0,4):C.GC_226,(0,0):C.GC_760})

V_268 = Vertex(name = 'V_268',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_146,(0,13):C.GC_909,(0,9):C.GC_137,(0,2):C.GC_145,(0,14):C.GC_908,(0,5):C.GC_940,(0,11):C.GC_138,(0,7):C.GC_941,(0,10):C.GC_138,(0,6):C.GC_941,(0,12):C.GC_137,(0,3):C.GC_145,(0,15):C.GC_908,(0,8):C.GC_940,(0,4):C.GC_146,(0,0):C.GC_909})

V_269 = Vertex(name = 'V_269',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_236,(0,13):C.GC_779,(0,9):C.GC_219,(0,2):C.GC_235,(0,14):C.GC_778,(0,5):C.GC_745,(0,11):C.GC_220,(0,7):C.GC_746,(0,10):C.GC_220,(0,6):C.GC_746,(0,12):C.GC_219,(0,3):C.GC_235,(0,15):C.GC_778,(0,8):C.GC_745,(0,4):C.GC_236,(0,0):C.GC_779})

V_270 = Vertex(name = 'V_270',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_76,(0,13):C.GC_925,(0,9):C.GC_141,(0,2):C.GC_75,(0,14):C.GC_924,(0,5):C.GC_612,(0,11):C.GC_142,(0,7):C.GC_613,(0,10):C.GC_142,(0,6):C.GC_613,(0,12):C.GC_141,(0,3):C.GC_75,(0,15):C.GC_924,(0,8):C.GC_612,(0,4):C.GC_76,(0,0):C.GC_925})

V_271 = Vertex(name = 'V_271',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_94,(0,13):C.GC_58,(0,9):C.GC_227,(0,2):C.GC_93,(0,14):C.GC_57,(0,5):C.GC_761,(0,11):C.GC_228,(0,7):C.GC_762,(0,10):C.GC_228,(0,6):C.GC_762,(0,12):C.GC_227,(0,3):C.GC_93,(0,15):C.GC_57,(0,8):C.GC_761,(0,4):C.GC_94,(0,0):C.GC_58})

V_272 = Vertex(name = 'V_272',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_148,(0,13):C.GC_927,(0,9):C.GC_143,(0,2):C.GC_147,(0,14):C.GC_926,(0,5):C.GC_942,(0,11):C.GC_144,(0,7):C.GC_943,(0,10):C.GC_144,(0,6):C.GC_943,(0,12):C.GC_143,(0,3):C.GC_147,(0,15):C.GC_926,(0,8):C.GC_942,(0,4):C.GC_148,(0,0):C.GC_927})

V_273 = Vertex(name = 'V_273',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_238,(0,13):C.GC_781,(0,9):C.GC_229,(0,2):C.GC_237,(0,14):C.GC_780,(0,5):C.GC_763,(0,11):C.GC_230,(0,7):C.GC_764,(0,10):C.GC_230,(0,6):C.GC_764,(0,12):C.GC_229,(0,3):C.GC_237,(0,15):C.GC_780,(0,8):C.GC_763,(0,4):C.GC_238,(0,0):C.GC_781})

V_274 = Vertex(name = 'V_274',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_78,(0,13):C.GC_945,(0,9):C.GC_149,(0,2):C.GC_77,(0,14):C.GC_944,(0,5):C.GC_618,(0,11):C.GC_150,(0,7):C.GC_619,(0,10):C.GC_150,(0,6):C.GC_619,(0,12):C.GC_149,(0,3):C.GC_77,(0,15):C.GC_944,(0,8):C.GC_618,(0,4):C.GC_78,(0,0):C.GC_945})

V_275 = Vertex(name = 'V_275',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,1):C.GC_96,(0,13):C.GC_60,(0,9):C.GC_239,(0,2):C.GC_95,(0,14):C.GC_59,(0,5):C.GC_782,(0,11):C.GC_240,(0,7):C.GC_783,(0,10):C.GC_240,(0,6):C.GC_783,(0,12):C.GC_239,(0,3):C.GC_95,(0,15):C.GC_59,(0,8):C.GC_782,(0,4):C.GC_96,(0,0):C.GC_60})

V_276 = Vertex(name = 'V_276',
               particles = [ P.d__tilde__, P.d, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_983})

V_277 = Vertex(name = 'V_277',
               particles = [ P.s__tilde__, P.s, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_983})

V_278 = Vertex(name = 'V_278',
               particles = [ P.b__tilde__, P.b, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_983})

V_279 = Vertex(name = 'V_279',
               particles = [ P.e__plus__, P.e__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_986})

V_280 = Vertex(name = 'V_280',
               particles = [ P.mu__plus__, P.mu__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_986})

V_281 = Vertex(name = 'V_281',
               particles = [ P.ta__plus__, P.ta__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_986})

V_282 = Vertex(name = 'V_282',
               particles = [ P.u__tilde__, P.u, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_984})

V_283 = Vertex(name = 'V_283',
               particles = [ P.c__tilde__, P.c, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_984})

V_284 = Vertex(name = 'V_284',
               particles = [ P.t__tilde__, P.t, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_984})

V_285 = Vertex(name = 'V_285',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_946})

V_286 = Vertex(name = 'V_286',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_946})

V_287 = Vertex(name = 'V_287',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_946})

V_288 = Vertex(name = 'V_288',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_946})

V_289 = Vertex(name = 'V_289',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_946})

V_290 = Vertex(name = 'V_290',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_946})

V_291 = Vertex(name = 'V_291',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_996})

V_292 = Vertex(name = 'V_292',
               particles = [ P.mu__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_999})

V_293 = Vertex(name = 'V_293',
               particles = [ P.ta__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1002})

V_294 = Vertex(name = 'V_294',
               particles = [ P.e__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_997})

V_295 = Vertex(name = 'V_295',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1000})

V_296 = Vertex(name = 'V_296',
               particles = [ P.ta__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1003})

V_297 = Vertex(name = 'V_297',
               particles = [ P.e__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_998})

V_298 = Vertex(name = 'V_298',
               particles = [ P.mu__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1001})

V_299 = Vertex(name = 'V_299',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1004})

V_300 = Vertex(name = 'V_300',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_949})

V_301 = Vertex(name = 'V_301',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_950})

V_302 = Vertex(name = 'V_302',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_951})

V_303 = Vertex(name = 'V_303',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_952})

V_304 = Vertex(name = 'V_304',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_953})

V_305 = Vertex(name = 'V_305',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_954})

V_306 = Vertex(name = 'V_306',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_955})

V_307 = Vertex(name = 'V_307',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_956})

V_308 = Vertex(name = 'V_308',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_957})

V_309 = Vertex(name = 'V_309',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_987})

V_310 = Vertex(name = 'V_310',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_990})

V_311 = Vertex(name = 'V_311',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_993})

V_312 = Vertex(name = 'V_312',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_988})

V_313 = Vertex(name = 'V_313',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_991})

V_314 = Vertex(name = 'V_314',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_994})

V_315 = Vertex(name = 'V_315',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_989})

V_316 = Vertex(name = 'V_316',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_992})

V_317 = Vertex(name = 'V_317',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_995})

V_318 = Vertex(name = 'V_318',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_958})

V_319 = Vertex(name = 'V_319',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_959})

V_320 = Vertex(name = 'V_320',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_960})

V_321 = Vertex(name = 'V_321',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_961})

V_322 = Vertex(name = 'V_322',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_962})

V_323 = Vertex(name = 'V_323',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_963})

V_324 = Vertex(name = 'V_324',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_964})

V_325 = Vertex(name = 'V_325',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_965})

V_326 = Vertex(name = 'V_326',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_966})

V_327 = Vertex(name = 'V_327',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_976,(0,1):C.GC_978})

V_328 = Vertex(name = 'V_328',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_976,(0,1):C.GC_978})

V_329 = Vertex(name = 'V_329',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_976,(0,1):C.GC_978})

V_330 = Vertex(name = 'V_330',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_979,(0,1):C.GC_981})

V_331 = Vertex(name = 'V_331',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_979,(0,1):C.GC_981})

V_332 = Vertex(name = 'V_332',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_979,(0,1):C.GC_981})

V_333 = Vertex(name = 'V_333',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_977,(0,1):C.GC_980})

V_334 = Vertex(name = 'V_334',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_977,(0,1):C.GC_980})

V_335 = Vertex(name = 'V_335',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_977,(0,1):C.GC_980})

V_336 = Vertex(name = 'V_336',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_973})

V_337 = Vertex(name = 'V_337',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_973})

V_338 = Vertex(name = 'V_338',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_973})

