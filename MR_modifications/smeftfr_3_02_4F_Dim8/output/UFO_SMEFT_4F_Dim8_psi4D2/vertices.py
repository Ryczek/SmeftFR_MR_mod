# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Sun 18 Jan 2026 17:55:20


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
             couplings = {(0,0):C.GC_490})

V_4 = Vertex(name = 'V_4',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_491,(0,0):C.GC_491,(2,2):C.GC_491})

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
              couplings = {(0,0):C.GC_528})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_510})

V_34 = Vertex(name = 'V_34',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_511})

V_35 = Vertex(name = 'V_35',
              particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_513})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_515})

V_37 = Vertex(name = 'V_37',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_512})

V_38 = Vertex(name = 'V_38',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_525})

V_39 = Vertex(name = 'V_39',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_517})

V_40 = Vertex(name = 'V_40',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_518})

V_41 = Vertex(name = 'V_41',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_514})

V_42 = Vertex(name = 'V_42',
              particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_196,(0,4):C.GC_195,(0,7):C.GC_177,(0,1):C.GC_178,(0,0):C.GC_178,(0,5):C.GC_195,(0,2):C.GC_177,(0,6):C.GC_196})

V_43 = Vertex(name = 'V_43',
              particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,3):C.GC_199,(0,4):C.GC_197,(0,8):C.GC_206,(0,7):C.GC_47,(0,1):C.GC_207,(0,0):C.GC_207,(0,5):C.GC_198,(0,2):C.GC_206,(0,6):C.GC_199})

V_44 = Vertex(name = 'V_44',
              particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,4):C.GC_201,(0,5):C.GC_200,(0,8):C.GC_216,(0,2):C.GC_217,(0,0):C.GC_48,(0,1):C.GC_218,(0,3):C.GC_216,(0,6):C.GC_200,(0,7):C.GC_201})

V_45 = Vertex(name = 'V_45',
              particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_203,(0,4):C.GC_202,(0,7):C.GC_227,(0,1):C.GC_228,(0,0):C.GC_228,(0,5):C.GC_202,(0,2):C.GC_227,(0,6):C.GC_203})

V_46 = Vertex(name = 'V_46',
              particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_242,(0,4):C.GC_241,(0,7):C.GC_229,(0,1):C.GC_230,(0,0):C.GC_230,(0,5):C.GC_241,(0,2):C.GC_229,(0,6):C.GC_242})

V_47 = Vertex(name = 'V_47',
              particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_256,(0,4):C.GC_255,(0,7):C.GC_231,(0,1):C.GC_232,(0,0):C.GC_232,(0,5):C.GC_255,(0,2):C.GC_231,(0,6):C.GC_256})

V_48 = Vertex(name = 'V_48',
              particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_205,(0,4):C.GC_204,(0,7):C.GC_269,(0,1):C.GC_270,(0,0):C.GC_270,(0,5):C.GC_204,(0,2):C.GC_269,(0,6):C.GC_205})

V_49 = Vertex(name = 'V_49',
              particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8, L.FFFF9 ],
              couplings = {(0,3):C.GC_289,(0,8):C.GC_271,(0,4):C.GC_288,(0,1):C.GC_272,(0,0):C.GC_272,(0,5):C.GC_287,(0,2):C.GC_271,(0,7):C.GC_49,(0,6):C.GC_289})

V_50 = Vertex(name = 'V_50',
              particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_307,(0,4):C.GC_306,(0,7):C.GC_273,(0,1):C.GC_274,(0,0):C.GC_274,(0,5):C.GC_306,(0,2):C.GC_273,(0,6):C.GC_307})

V_51 = Vertex(name = 'V_51',
              particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_209,(0,4):C.GC_208,(0,7):C.GC_179,(0,1):C.GC_180,(0,0):C.GC_180,(0,5):C.GC_208,(0,2):C.GC_179,(0,6):C.GC_209})

V_52 = Vertex(name = 'V_52',
              particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_211,(0,4):C.GC_210,(0,7):C.GC_219,(0,1):C.GC_220,(0,0):C.GC_220,(0,5):C.GC_210,(0,2):C.GC_219,(0,6):C.GC_211})

V_53 = Vertex(name = 'V_53',
              particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_213,(0,4):C.GC_212,(0,7):C.GC_243,(0,1):C.GC_244,(0,0):C.GC_244,(0,5):C.GC_212,(0,2):C.GC_243,(0,6):C.GC_213})

V_54 = Vertex(name = 'V_54',
              particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_258,(0,4):C.GC_257,(0,7):C.GC_245,(0,1):C.GC_246,(0,0):C.GC_246,(0,5):C.GC_257,(0,2):C.GC_245,(0,6):C.GC_258})

V_55 = Vertex(name = 'V_55',
              particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_215,(0,4):C.GC_214,(0,7):C.GC_290,(0,1):C.GC_291,(0,0):C.GC_291,(0,5):C.GC_214,(0,2):C.GC_290,(0,6):C.GC_215})

V_56 = Vertex(name = 'V_56',
              particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_309,(0,4):C.GC_308,(0,7):C.GC_292,(0,1):C.GC_293,(0,0):C.GC_293,(0,5):C.GC_308,(0,2):C.GC_292,(0,6):C.GC_309})

V_57 = Vertex(name = 'V_57',
              particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_222,(0,4):C.GC_221,(0,7):C.GC_181,(0,1):C.GC_182,(0,0):C.GC_182,(0,5):C.GC_221,(0,2):C.GC_181,(0,6):C.GC_222})

V_58 = Vertex(name = 'V_58',
              particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_224,(0,4):C.GC_223,(0,7):C.GC_259,(0,1):C.GC_260,(0,0):C.GC_260,(0,5):C.GC_223,(0,2):C.GC_259,(0,6):C.GC_224})

V_59 = Vertex(name = 'V_59',
              particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_226,(0,4):C.GC_225,(0,7):C.GC_310,(0,1):C.GC_311,(0,0):C.GC_311,(0,5):C.GC_225,(0,2):C.GC_310,(0,6):C.GC_226})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ve__tilde__, P.vm, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_234,(0,4):C.GC_233,(0,7):C.GC_183,(0,1):C.GC_184,(0,0):C.GC_184,(0,5):C.GC_233,(0,2):C.GC_183,(0,6):C.GC_234})

V_61 = Vertex(name = 'V_61',
              particles = [ P.vm__tilde__, P.vm, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_236,(0,4):C.GC_235,(0,7):C.GC_247,(0,1):C.GC_248,(0,0):C.GC_248,(0,5):C.GC_235,(0,2):C.GC_247,(0,6):C.GC_236})

V_62 = Vertex(name = 'V_62',
              particles = [ P.vt__tilde__, P.vm, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_238,(0,4):C.GC_237,(0,7):C.GC_261,(0,1):C.GC_262,(0,0):C.GC_262,(0,5):C.GC_237,(0,2):C.GC_261,(0,6):C.GC_238})

V_63 = Vertex(name = 'V_63',
              particles = [ P.ve__tilde__, P.vm, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_240,(0,4):C.GC_239,(0,7):C.GC_275,(0,1):C.GC_276,(0,0):C.GC_276,(0,5):C.GC_239,(0,2):C.GC_275,(0,6):C.GC_240})

V_64 = Vertex(name = 'V_64',
              particles = [ P.vm__tilde__, P.vm, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_295,(0,4):C.GC_294,(0,7):C.GC_277,(0,1):C.GC_278,(0,0):C.GC_278,(0,5):C.GC_294,(0,2):C.GC_277,(0,6):C.GC_295})

V_65 = Vertex(name = 'V_65',
              particles = [ P.vt__tilde__, P.vm, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_313,(0,4):C.GC_312,(0,7):C.GC_279,(0,1):C.GC_280,(0,0):C.GC_280,(0,5):C.GC_312,(0,2):C.GC_279,(0,6):C.GC_313})

V_66 = Vertex(name = 'V_66',
              particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_250,(0,4):C.GC_249,(0,7):C.GC_185,(0,1):C.GC_186,(0,0):C.GC_186,(0,5):C.GC_249,(0,2):C.GC_185,(0,6):C.GC_250})

V_67 = Vertex(name = 'V_67',
              particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_252,(0,4):C.GC_251,(0,7):C.GC_263,(0,1):C.GC_264,(0,0):C.GC_264,(0,5):C.GC_251,(0,2):C.GC_263,(0,6):C.GC_252})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_254,(0,4):C.GC_253,(0,7):C.GC_296,(0,1):C.GC_297,(0,0):C.GC_297,(0,5):C.GC_253,(0,2):C.GC_296,(0,6):C.GC_254})

V_69 = Vertex(name = 'V_69',
              particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_315,(0,4):C.GC_314,(0,7):C.GC_298,(0,1):C.GC_299,(0,0):C.GC_299,(0,5):C.GC_314,(0,2):C.GC_298,(0,6):C.GC_315})

V_70 = Vertex(name = 'V_70',
              particles = [ P.vt__tilde__, P.vm, P.vt__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_266,(0,4):C.GC_265,(0,7):C.GC_187,(0,1):C.GC_188,(0,0):C.GC_188,(0,5):C.GC_265,(0,2):C.GC_187,(0,6):C.GC_266})

V_71 = Vertex(name = 'V_71',
              particles = [ P.vt__tilde__, P.vm, P.vt__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_268,(0,4):C.GC_267,(0,7):C.GC_316,(0,1):C.GC_317,(0,0):C.GC_317,(0,5):C.GC_267,(0,2):C.GC_316,(0,6):C.GC_268})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ve__tilde__, P.vt, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_282,(0,4):C.GC_281,(0,7):C.GC_189,(0,1):C.GC_190,(0,0):C.GC_190,(0,5):C.GC_281,(0,2):C.GC_189,(0,6):C.GC_282})

V_73 = Vertex(name = 'V_73',
              particles = [ P.vm__tilde__, P.vt, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_284,(0,4):C.GC_283,(0,7):C.GC_300,(0,1):C.GC_301,(0,0):C.GC_301,(0,5):C.GC_283,(0,2):C.GC_300,(0,6):C.GC_284})

V_74 = Vertex(name = 'V_74',
              particles = [ P.vt__tilde__, P.vt, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_286,(0,4):C.GC_285,(0,7):C.GC_318,(0,1):C.GC_319,(0,0):C.GC_319,(0,5):C.GC_285,(0,2):C.GC_318,(0,6):C.GC_286})

V_75 = Vertex(name = 'V_75',
              particles = [ P.vm__tilde__, P.vt, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_303,(0,4):C.GC_302,(0,7):C.GC_191,(0,1):C.GC_192,(0,0):C.GC_192,(0,5):C.GC_302,(0,2):C.GC_191,(0,6):C.GC_303})

V_76 = Vertex(name = 'V_76',
              particles = [ P.vt__tilde__, P.vt, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_305,(0,4):C.GC_304,(0,7):C.GC_320,(0,1):C.GC_321,(0,0):C.GC_321,(0,5):C.GC_304,(0,2):C.GC_320,(0,6):C.GC_305})

V_77 = Vertex(name = 'V_77',
              particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
              couplings = {(0,3):C.GC_323,(0,4):C.GC_322,(0,7):C.GC_193,(0,1):C.GC_194,(0,0):C.GC_194,(0,5):C.GC_322,(0,2):C.GC_193,(0,6):C.GC_323})

V_78 = Vertex(name = 'V_78',
              particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_324,(0,1):C.GC_325,(0,0):C.GC_325,(0,2):C.GC_324})

V_79 = Vertex(name = 'V_79',
              particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_326,(0,1):C.GC_327,(0,0):C.GC_327,(0,2):C.GC_326})

V_80 = Vertex(name = 'V_80',
              particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_328,(0,1):C.GC_329,(0,0):C.GC_329,(0,2):C.GC_328})

V_81 = Vertex(name = 'V_81',
              particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_330,(0,1):C.GC_331,(0,0):C.GC_331,(0,2):C.GC_330})

V_82 = Vertex(name = 'V_82',
              particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_332,(0,1):C.GC_333,(0,0):C.GC_333,(0,2):C.GC_332})

V_83 = Vertex(name = 'V_83',
              particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_334,(0,1):C.GC_335,(0,0):C.GC_335,(0,2):C.GC_334})

V_84 = Vertex(name = 'V_84',
              particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_336,(0,1):C.GC_337,(0,0):C.GC_337,(0,2):C.GC_336})

V_85 = Vertex(name = 'V_85',
              particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_338,(0,1):C.GC_339,(0,0):C.GC_339,(0,2):C.GC_338})

V_86 = Vertex(name = 'V_86',
              particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_340,(0,1):C.GC_341,(0,0):C.GC_341,(0,2):C.GC_340})

V_87 = Vertex(name = 'V_87',
              particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_342,(0,1):C.GC_343,(0,0):C.GC_343,(0,2):C.GC_342})

V_88 = Vertex(name = 'V_88',
              particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_344,(0,1):C.GC_345,(0,0):C.GC_345,(0,2):C.GC_344})

V_89 = Vertex(name = 'V_89',
              particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF9 ],
              couplings = {(0,4):C.GC_347,(0,1):C.GC_348,(0,0):C.GC_348,(0,2):C.GC_346,(0,3):C.GC_44})

V_90 = Vertex(name = 'V_90',
              particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_349,(0,1):C.GC_350,(0,0):C.GC_350,(0,2):C.GC_349})

V_91 = Vertex(name = 'V_91',
              particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_351,(0,1):C.GC_352,(0,0):C.GC_352,(0,2):C.GC_351})

V_92 = Vertex(name = 'V_92',
              particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_353,(0,1):C.GC_354,(0,0):C.GC_354,(0,2):C.GC_353})

V_93 = Vertex(name = 'V_93',
              particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_355,(0,1):C.GC_356,(0,0):C.GC_356,(0,2):C.GC_355})

V_94 = Vertex(name = 'V_94',
              particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_357,(0,1):C.GC_358,(0,0):C.GC_358,(0,2):C.GC_357})

V_95 = Vertex(name = 'V_95',
              particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_359,(0,1):C.GC_360,(0,0):C.GC_360,(0,2):C.GC_359})

V_96 = Vertex(name = 'V_96',
              particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_361,(0,1):C.GC_362,(0,0):C.GC_362,(0,2):C.GC_361})

V_97 = Vertex(name = 'V_97',
              particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_363,(0,1):C.GC_364,(0,0):C.GC_364,(0,2):C.GC_363})

V_98 = Vertex(name = 'V_98',
              particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_365,(0,1):C.GC_366,(0,0):C.GC_366,(0,2):C.GC_365})

V_99 = Vertex(name = 'V_99',
              particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
              couplings = {(0,3):C.GC_367,(0,1):C.GC_368,(0,0):C.GC_368,(0,2):C.GC_367})

V_100 = Vertex(name = 'V_100',
               particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_369,(0,1):C.GC_370,(0,0):C.GC_370,(0,2):C.GC_369})

V_101 = Vertex(name = 'V_101',
               particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_371,(0,1):C.GC_372,(0,0):C.GC_372,(0,2):C.GC_371})

V_102 = Vertex(name = 'V_102',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_373,(0,1):C.GC_374,(0,0):C.GC_374,(0,2):C.GC_373})

V_103 = Vertex(name = 'V_103',
               particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_375,(0,1):C.GC_376,(0,0):C.GC_376,(0,2):C.GC_375})

V_104 = Vertex(name = 'V_104',
               particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_377,(0,1):C.GC_378,(0,0):C.GC_378,(0,2):C.GC_377})

V_105 = Vertex(name = 'V_105',
               particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_379,(0,1):C.GC_380,(0,0):C.GC_380,(0,2):C.GC_379})

V_106 = Vertex(name = 'V_106',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_381,(0,1):C.GC_382,(0,0):C.GC_382,(0,2):C.GC_381})

V_107 = Vertex(name = 'V_107',
               particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_383,(0,1):C.GC_384,(0,0):C.GC_384,(0,2):C.GC_383})

V_108 = Vertex(name = 'V_108',
               particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_385,(0,1):C.GC_386,(0,0):C.GC_386,(0,2):C.GC_385})

V_109 = Vertex(name = 'V_109',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_387,(0,1):C.GC_388,(0,0):C.GC_388,(0,2):C.GC_387})

V_110 = Vertex(name = 'V_110',
               particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_389,(0,1):C.GC_390,(0,0):C.GC_390,(0,2):C.GC_389})

V_111 = Vertex(name = 'V_111',
               particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_391,(0,1):C.GC_392,(0,0):C.GC_392,(0,2):C.GC_391})

V_112 = Vertex(name = 'V_112',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_393,(0,1):C.GC_394,(0,0):C.GC_394,(0,2):C.GC_393})

V_113 = Vertex(name = 'V_113',
               particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_395,(0,1):C.GC_396,(0,0):C.GC_396,(0,2):C.GC_395})

V_114 = Vertex(name = 'V_114',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_397,(0,1):C.GC_398,(0,0):C.GC_398,(0,2):C.GC_397})

V_115 = Vertex(name = 'V_115',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_399,(0,1):C.GC_400,(0,0):C.GC_400,(0,2):C.GC_399})

V_116 = Vertex(name = 'V_116',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_401,(0,1):C.GC_402,(0,0):C.GC_402,(0,2):C.GC_401})

V_117 = Vertex(name = 'V_117',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF9 ],
               couplings = {(0,4):C.GC_404,(0,1):C.GC_405,(0,0):C.GC_405,(0,2):C.GC_403,(0,3):C.GC_46})

V_118 = Vertex(name = 'V_118',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_406,(0,1):C.GC_407,(0,0):C.GC_407,(0,2):C.GC_406})

V_119 = Vertex(name = 'V_119',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_408,(0,1):C.GC_409,(0,0):C.GC_409,(0,2):C.GC_408})

V_120 = Vertex(name = 'V_120',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_410,(0,1):C.GC_411,(0,0):C.GC_411,(0,2):C.GC_410})

V_121 = Vertex(name = 'V_121',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_412,(0,1):C.GC_413,(0,0):C.GC_413,(0,2):C.GC_412})

V_122 = Vertex(name = 'V_122',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_414,(0,1):C.GC_415,(0,0):C.GC_415,(0,2):C.GC_414})

V_123 = Vertex(name = 'V_123',
               particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_416,(0,1):C.GC_417,(0,0):C.GC_417,(0,2):C.GC_416})

V_124 = Vertex(name = 'V_124',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_418,(0,1):C.GC_419,(0,0):C.GC_419,(0,2):C.GC_418})

V_125 = Vertex(name = 'V_125',
               particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_420,(0,1):C.GC_421,(0,0):C.GC_421,(0,2):C.GC_420})

V_126 = Vertex(name = 'V_126',
               particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_422,(0,1):C.GC_423,(0,0):C.GC_423,(0,2):C.GC_422})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_424,(0,1):C.GC_425,(0,0):C.GC_425,(0,2):C.GC_424})

V_128 = Vertex(name = 'V_128',
               particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_426,(0,1):C.GC_427,(0,0):C.GC_427,(0,2):C.GC_426})

V_129 = Vertex(name = 'V_129',
               particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_428,(0,1):C.GC_429,(0,0):C.GC_429,(0,2):C.GC_428})

V_130 = Vertex(name = 'V_130',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_430,(0,1):C.GC_431,(0,0):C.GC_431,(0,2):C.GC_430})

V_131 = Vertex(name = 'V_131',
               particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_432,(0,1):C.GC_433,(0,0):C.GC_433,(0,2):C.GC_432})

V_132 = Vertex(name = 'V_132',
               particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF9 ],
               couplings = {(0,4):C.GC_435,(0,1):C.GC_436,(0,0):C.GC_436,(0,2):C.GC_434,(0,3):C.GC_45})

V_133 = Vertex(name = 'V_133',
               particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_437,(0,1):C.GC_438,(0,0):C.GC_438,(0,2):C.GC_437})

V_134 = Vertex(name = 'V_134',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_439,(0,1):C.GC_440,(0,0):C.GC_440,(0,2):C.GC_439})

V_135 = Vertex(name = 'V_135',
               particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_441,(0,1):C.GC_442,(0,0):C.GC_442,(0,2):C.GC_441})

V_136 = Vertex(name = 'V_136',
               particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_443,(0,1):C.GC_444,(0,0):C.GC_444,(0,2):C.GC_443})

V_137 = Vertex(name = 'V_137',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_445,(0,1):C.GC_446,(0,0):C.GC_446,(0,2):C.GC_445})

V_138 = Vertex(name = 'V_138',
               particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_447,(0,1):C.GC_448,(0,0):C.GC_448,(0,2):C.GC_447})

V_139 = Vertex(name = 'V_139',
               particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_449,(0,1):C.GC_450,(0,0):C.GC_450,(0,2):C.GC_449})

V_140 = Vertex(name = 'V_140',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_451,(0,1):C.GC_452,(0,0):C.GC_452,(0,2):C.GC_451})

V_141 = Vertex(name = 'V_141',
               particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_453,(0,1):C.GC_454,(0,0):C.GC_454,(0,2):C.GC_453})

V_142 = Vertex(name = 'V_142',
               particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_455,(0,1):C.GC_456,(0,0):C.GC_456,(0,2):C.GC_455})

V_143 = Vertex(name = 'V_143',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_457,(0,1):C.GC_458,(0,0):C.GC_458,(0,2):C.GC_457})

V_144 = Vertex(name = 'V_144',
               particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_459,(0,1):C.GC_460,(0,0):C.GC_460,(0,2):C.GC_459})

V_145 = Vertex(name = 'V_145',
               particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_461,(0,1):C.GC_462,(0,0):C.GC_462,(0,2):C.GC_461})

V_146 = Vertex(name = 'V_146',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_463,(0,1):C.GC_464,(0,0):C.GC_464,(0,2):C.GC_463})

V_147 = Vertex(name = 'V_147',
               particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_465,(0,1):C.GC_466,(0,0):C.GC_466,(0,2):C.GC_465})

V_148 = Vertex(name = 'V_148',
               particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_467,(0,1):C.GC_468,(0,0):C.GC_468,(0,2):C.GC_467})

V_149 = Vertex(name = 'V_149',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_469,(0,1):C.GC_470,(0,0):C.GC_470,(0,2):C.GC_469})

V_150 = Vertex(name = 'V_150',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_471,(0,1):C.GC_472,(0,0):C.GC_472,(0,2):C.GC_471})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_473,(0,1):C.GC_474,(0,0):C.GC_474,(0,2):C.GC_473})

V_152 = Vertex(name = 'V_152',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_475,(0,1):C.GC_476,(0,0):C.GC_476,(0,2):C.GC_475})

V_153 = Vertex(name = 'V_153',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_477,(0,1):C.GC_478,(0,0):C.GC_478,(0,2):C.GC_477})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_479,(0,1):C.GC_480,(0,0):C.GC_480,(0,2):C.GC_479})

V_155 = Vertex(name = 'V_155',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_481,(0,1):C.GC_482,(0,0):C.GC_482,(0,2):C.GC_481})

V_156 = Vertex(name = 'V_156',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_483,(0,1):C.GC_484,(0,0):C.GC_484,(0,2):C.GC_483})

V_157 = Vertex(name = 'V_157',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_485,(0,1):C.GC_486,(0,0):C.GC_486,(0,2):C.GC_485})

V_158 = Vertex(name = 'V_158',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF9 ],
               couplings = {(0,3):C.GC_487,(0,1):C.GC_488,(0,0):C.GC_488,(0,2):C.GC_487})

V_159 = Vertex(name = 'V_159',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_87,(0,3):C.GC_30,(0,12):C.GC_86,(0,15):C.GC_86,(0,4):C.GC_30,(0,7):C.GC_30,(0,1):C.GC_87,(0,9):C.GC_30,(0,0):C.GC_87,(0,8):C.GC_30,(0,13):C.GC_86,(0,2):C.GC_86,(0,5):C.GC_30,(0,10):C.GC_30,(0,14):C.GC_87,(0,6):C.GC_30})

V_160 = Vertex(name = 'V_160',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,11):C.GC_90,(0,3):C.GC_50,(0,12):C.GC_88,(0,16):C.GC_89,(0,15):C.GC_43,(0,4):C.GC_50,(0,7):C.GC_50,(0,1):C.GC_90,(0,9):C.GC_50,(0,0):C.GC_90,(0,8):C.GC_50,(0,13):C.GC_89,(0,2):C.GC_89,(0,5):C.GC_50,(0,10):C.GC_50,(0,14):C.GC_90,(0,6):C.GC_50})

V_161 = Vertex(name = 'V_161',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_94,(0,3):C.GC_51,(0,12):C.GC_93,(0,15):C.GC_93,(0,4):C.GC_51,(0,7):C.GC_51,(0,1):C.GC_94,(0,9):C.GC_51,(0,0):C.GC_94,(0,8):C.GC_51,(0,13):C.GC_93,(0,2):C.GC_93,(0,5):C.GC_51,(0,10):C.GC_51,(0,14):C.GC_94,(0,6):C.GC_51})

V_162 = Vertex(name = 'V_162',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_100,(0,3):C.GC_53,(0,12):C.GC_99,(0,15):C.GC_99,(0,4):C.GC_53,(0,7):C.GC_53,(0,1):C.GC_100,(0,9):C.GC_53,(0,0):C.GC_100,(0,8):C.GC_53,(0,13):C.GC_99,(0,2):C.GC_99,(0,5):C.GC_53,(0,10):C.GC_53,(0,14):C.GC_100,(0,6):C.GC_53})

V_163 = Vertex(name = 'V_163',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_108,(0,3):C.GC_56,(0,12):C.GC_107,(0,15):C.GC_101,(0,4):C.GC_56,(0,7):C.GC_54,(0,1):C.GC_102,(0,9):C.GC_54,(0,0):C.GC_102,(0,8):C.GC_54,(0,13):C.GC_107,(0,2):C.GC_101,(0,5):C.GC_56,(0,10):C.GC_54,(0,14):C.GC_108,(0,6):C.GC_56})

V_164 = Vertex(name = 'V_164',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_118,(0,3):C.GC_60,(0,12):C.GC_117,(0,15):C.GC_103,(0,4):C.GC_60,(0,7):C.GC_55,(0,1):C.GC_104,(0,9):C.GC_55,(0,0):C.GC_104,(0,8):C.GC_55,(0,13):C.GC_117,(0,2):C.GC_103,(0,5):C.GC_60,(0,10):C.GC_55,(0,14):C.GC_118,(0,6):C.GC_60})

V_165 = Vertex(name = 'V_165',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_130,(0,3):C.GC_65,(0,12):C.GC_129,(0,15):C.GC_129,(0,4):C.GC_65,(0,7):C.GC_65,(0,1):C.GC_130,(0,9):C.GC_65,(0,0):C.GC_130,(0,8):C.GC_65,(0,13):C.GC_129,(0,2):C.GC_129,(0,5):C.GC_65,(0,10):C.GC_65,(0,14):C.GC_130,(0,6):C.GC_65})

V_166 = Vertex(name = 'V_166',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_144,(0,3):C.GC_71,(0,12):C.GC_143,(0,15):C.GC_131,(0,4):C.GC_71,(0,7):C.GC_66,(0,1):C.GC_132,(0,9):C.GC_66,(0,0):C.GC_132,(0,8):C.GC_66,(0,13):C.GC_143,(0,2):C.GC_131,(0,5):C.GC_71,(0,10):C.GC_66,(0,14):C.GC_144,(0,6):C.GC_71})

V_167 = Vertex(name = 'V_167',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_160,(0,3):C.GC_78,(0,12):C.GC_159,(0,15):C.GC_133,(0,4):C.GC_78,(0,7):C.GC_67,(0,1):C.GC_134,(0,9):C.GC_67,(0,0):C.GC_134,(0,8):C.GC_67,(0,13):C.GC_159,(0,2):C.GC_133,(0,5):C.GC_78,(0,10):C.GC_67,(0,14):C.GC_160,(0,6):C.GC_78})

V_168 = Vertex(name = 'V_168',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_92,(0,3):C.GC_31,(0,12):C.GC_91,(0,15):C.GC_91,(0,4):C.GC_31,(0,7):C.GC_31,(0,1):C.GC_92,(0,9):C.GC_31,(0,0):C.GC_92,(0,8):C.GC_31,(0,13):C.GC_91,(0,2):C.GC_91,(0,5):C.GC_31,(0,10):C.GC_31,(0,14):C.GC_92,(0,6):C.GC_31})

V_169 = Vertex(name = 'V_169',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_96,(0,3):C.GC_52,(0,12):C.GC_95,(0,15):C.GC_95,(0,4):C.GC_52,(0,7):C.GC_52,(0,1):C.GC_96,(0,9):C.GC_52,(0,0):C.GC_96,(0,8):C.GC_52,(0,13):C.GC_95,(0,2):C.GC_95,(0,5):C.GC_52,(0,10):C.GC_52,(0,14):C.GC_96,(0,6):C.GC_52})

V_170 = Vertex(name = 'V_170',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_110,(0,3):C.GC_57,(0,12):C.GC_109,(0,15):C.GC_109,(0,4):C.GC_57,(0,7):C.GC_57,(0,1):C.GC_110,(0,9):C.GC_57,(0,0):C.GC_110,(0,8):C.GC_57,(0,13):C.GC_109,(0,2):C.GC_109,(0,5):C.GC_57,(0,10):C.GC_57,(0,14):C.GC_110,(0,6):C.GC_57})

V_171 = Vertex(name = 'V_171',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_120,(0,3):C.GC_61,(0,12):C.GC_119,(0,15):C.GC_111,(0,4):C.GC_61,(0,7):C.GC_58,(0,1):C.GC_112,(0,9):C.GC_58,(0,0):C.GC_112,(0,8):C.GC_58,(0,13):C.GC_119,(0,2):C.GC_111,(0,5):C.GC_61,(0,10):C.GC_58,(0,14):C.GC_120,(0,6):C.GC_61})

V_172 = Vertex(name = 'V_172',
               particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_146,(0,3):C.GC_72,(0,12):C.GC_145,(0,15):C.GC_145,(0,4):C.GC_72,(0,7):C.GC_72,(0,1):C.GC_146,(0,9):C.GC_72,(0,0):C.GC_146,(0,8):C.GC_72,(0,13):C.GC_145,(0,2):C.GC_145,(0,5):C.GC_72,(0,10):C.GC_72,(0,14):C.GC_146,(0,6):C.GC_72})

V_173 = Vertex(name = 'V_173',
               particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,12):C.GC_162,(0,4):C.GC_79,(0,13):C.GC_161,(0,16):C.GC_147,(0,5):C.GC_79,(0,8):C.GC_73,(0,1):C.GC_148,(0,10):C.GC_73,(0,0):C.GC_148,(0,9):C.GC_40,(0,3):C.GC_33,(0,14):C.GC_161,(0,2):C.GC_147,(0,11):C.GC_73,(0,6):C.GC_79,(0,15):C.GC_162,(0,7):C.GC_79})

V_174 = Vertex(name = 'V_174',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_98,(0,3):C.GC_32,(0,12):C.GC_97,(0,15):C.GC_97,(0,4):C.GC_32,(0,7):C.GC_32,(0,1):C.GC_98,(0,9):C.GC_32,(0,0):C.GC_98,(0,8):C.GC_32,(0,13):C.GC_97,(0,2):C.GC_97,(0,5):C.GC_32,(0,10):C.GC_32,(0,14):C.GC_98,(0,6):C.GC_32})

V_175 = Vertex(name = 'V_175',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_122,(0,3):C.GC_62,(0,12):C.GC_121,(0,15):C.GC_121,(0,4):C.GC_62,(0,7):C.GC_62,(0,1):C.GC_122,(0,9):C.GC_62,(0,0):C.GC_122,(0,8):C.GC_62,(0,13):C.GC_121,(0,2):C.GC_121,(0,5):C.GC_62,(0,10):C.GC_62,(0,14):C.GC_122,(0,6):C.GC_62})

V_176 = Vertex(name = 'V_176',
               particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_164,(0,3):C.GC_80,(0,12):C.GC_163,(0,15):C.GC_163,(0,4):C.GC_80,(0,7):C.GC_80,(0,1):C.GC_164,(0,9):C.GC_80,(0,0):C.GC_164,(0,8):C.GC_80,(0,13):C.GC_163,(0,2):C.GC_163,(0,5):C.GC_80,(0,10):C.GC_80,(0,14):C.GC_164,(0,6):C.GC_80})

V_177 = Vertex(name = 'V_177',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_106,(0,3):C.GC_34,(0,12):C.GC_105,(0,15):C.GC_105,(0,4):C.GC_34,(0,7):C.GC_34,(0,1):C.GC_106,(0,9):C.GC_34,(0,0):C.GC_106,(0,8):C.GC_34,(0,13):C.GC_105,(0,2):C.GC_105,(0,5):C.GC_34,(0,10):C.GC_34,(0,14):C.GC_106,(0,6):C.GC_34})

V_178 = Vertex(name = 'V_178',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_114,(0,3):C.GC_59,(0,12):C.GC_113,(0,15):C.GC_113,(0,4):C.GC_59,(0,7):C.GC_59,(0,1):C.GC_114,(0,9):C.GC_59,(0,0):C.GC_114,(0,8):C.GC_59,(0,13):C.GC_113,(0,2):C.GC_113,(0,5):C.GC_59,(0,10):C.GC_59,(0,14):C.GC_114,(0,6):C.GC_59})

V_179 = Vertex(name = 'V_179',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_124,(0,3):C.GC_63,(0,12):C.GC_123,(0,15):C.GC_123,(0,4):C.GC_63,(0,7):C.GC_63,(0,1):C.GC_124,(0,9):C.GC_63,(0,0):C.GC_124,(0,8):C.GC_63,(0,13):C.GC_123,(0,2):C.GC_123,(0,5):C.GC_63,(0,10):C.GC_63,(0,14):C.GC_124,(0,6):C.GC_63})

V_180 = Vertex(name = 'V_180',
               particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_136,(0,3):C.GC_68,(0,12):C.GC_135,(0,15):C.GC_135,(0,4):C.GC_68,(0,7):C.GC_68,(0,1):C.GC_136,(0,9):C.GC_68,(0,0):C.GC_136,(0,8):C.GC_68,(0,13):C.GC_135,(0,2):C.GC_135,(0,5):C.GC_68,(0,10):C.GC_68,(0,14):C.GC_136,(0,6):C.GC_68})

V_181 = Vertex(name = 'V_181',
               particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_150,(0,3):C.GC_74,(0,12):C.GC_149,(0,15):C.GC_137,(0,4):C.GC_74,(0,7):C.GC_69,(0,1):C.GC_138,(0,9):C.GC_69,(0,0):C.GC_138,(0,8):C.GC_69,(0,13):C.GC_149,(0,2):C.GC_137,(0,5):C.GC_74,(0,10):C.GC_69,(0,14):C.GC_150,(0,6):C.GC_74})

V_182 = Vertex(name = 'V_182',
               particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_166,(0,3):C.GC_81,(0,12):C.GC_165,(0,15):C.GC_139,(0,4):C.GC_81,(0,7):C.GC_70,(0,1):C.GC_140,(0,9):C.GC_70,(0,0):C.GC_140,(0,8):C.GC_70,(0,13):C.GC_165,(0,2):C.GC_139,(0,5):C.GC_81,(0,10):C.GC_70,(0,14):C.GC_166,(0,6):C.GC_81})

V_183 = Vertex(name = 'V_183',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_116,(0,3):C.GC_35,(0,12):C.GC_115,(0,15):C.GC_115,(0,4):C.GC_35,(0,7):C.GC_35,(0,1):C.GC_116,(0,9):C.GC_35,(0,0):C.GC_116,(0,8):C.GC_35,(0,13):C.GC_115,(0,2):C.GC_115,(0,5):C.GC_35,(0,10):C.GC_35,(0,14):C.GC_116,(0,6):C.GC_35})

V_184 = Vertex(name = 'V_184',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,12):C.GC_126,(0,3):C.GC_64,(0,13):C.GC_125,(0,16):C.GC_125,(0,8):C.GC_64,(0,4):C.GC_64,(0,1):C.GC_126,(0,10):C.GC_64,(0,0):C.GC_126,(0,9):C.GC_64,(0,14):C.GC_125,(0,2):C.GC_125,(0,11):C.GC_64,(0,5):C.GC_64,(0,15):C.GC_126,(0,6):C.GC_37,(0,7):C.GC_36})

V_185 = Vertex(name = 'V_185',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_152,(0,3):C.GC_75,(0,12):C.GC_151,(0,15):C.GC_151,(0,4):C.GC_75,(0,7):C.GC_75,(0,1):C.GC_152,(0,9):C.GC_75,(0,0):C.GC_152,(0,8):C.GC_75,(0,13):C.GC_151,(0,2):C.GC_151,(0,5):C.GC_75,(0,10):C.GC_75,(0,14):C.GC_152,(0,6):C.GC_75})

V_186 = Vertex(name = 'V_186',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_168,(0,3):C.GC_82,(0,12):C.GC_167,(0,15):C.GC_153,(0,4):C.GC_82,(0,7):C.GC_76,(0,1):C.GC_154,(0,9):C.GC_76,(0,0):C.GC_154,(0,8):C.GC_76,(0,13):C.GC_167,(0,2):C.GC_153,(0,5):C.GC_82,(0,10):C.GC_76,(0,14):C.GC_168,(0,6):C.GC_82})

V_187 = Vertex(name = 'V_187',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_128,(0,3):C.GC_38,(0,12):C.GC_127,(0,15):C.GC_127,(0,4):C.GC_38,(0,7):C.GC_38,(0,1):C.GC_128,(0,9):C.GC_38,(0,0):C.GC_128,(0,8):C.GC_38,(0,13):C.GC_127,(0,2):C.GC_127,(0,5):C.GC_38,(0,10):C.GC_38,(0,14):C.GC_128,(0,6):C.GC_38})

V_188 = Vertex(name = 'V_188',
               particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_170,(0,3):C.GC_83,(0,12):C.GC_169,(0,15):C.GC_169,(0,4):C.GC_83,(0,7):C.GC_83,(0,1):C.GC_170,(0,9):C.GC_83,(0,0):C.GC_170,(0,8):C.GC_83,(0,13):C.GC_169,(0,2):C.GC_169,(0,5):C.GC_83,(0,10):C.GC_83,(0,14):C.GC_170,(0,6):C.GC_83})

V_189 = Vertex(name = 'V_189',
               particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_142,(0,3):C.GC_39,(0,12):C.GC_141,(0,15):C.GC_141,(0,4):C.GC_39,(0,7):C.GC_39,(0,1):C.GC_142,(0,9):C.GC_39,(0,0):C.GC_142,(0,8):C.GC_39,(0,13):C.GC_141,(0,2):C.GC_141,(0,5):C.GC_39,(0,10):C.GC_39,(0,14):C.GC_142,(0,6):C.GC_39})

V_190 = Vertex(name = 'V_190',
               particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_156,(0,3):C.GC_77,(0,12):C.GC_155,(0,15):C.GC_155,(0,4):C.GC_77,(0,7):C.GC_77,(0,1):C.GC_156,(0,9):C.GC_77,(0,0):C.GC_156,(0,8):C.GC_77,(0,13):C.GC_155,(0,2):C.GC_155,(0,5):C.GC_77,(0,10):C.GC_77,(0,14):C.GC_156,(0,6):C.GC_77})

V_191 = Vertex(name = 'V_191',
               particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_172,(0,3):C.GC_84,(0,12):C.GC_171,(0,15):C.GC_171,(0,4):C.GC_84,(0,7):C.GC_84,(0,1):C.GC_172,(0,9):C.GC_84,(0,0):C.GC_172,(0,8):C.GC_84,(0,13):C.GC_171,(0,2):C.GC_171,(0,5):C.GC_84,(0,10):C.GC_84,(0,14):C.GC_172,(0,6):C.GC_84})

V_192 = Vertex(name = 'V_192',
               particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_158,(0,3):C.GC_41,(0,12):C.GC_157,(0,15):C.GC_157,(0,4):C.GC_41,(0,7):C.GC_41,(0,1):C.GC_158,(0,9):C.GC_41,(0,0):C.GC_158,(0,8):C.GC_41,(0,13):C.GC_157,(0,2):C.GC_157,(0,5):C.GC_41,(0,10):C.GC_41,(0,14):C.GC_158,(0,6):C.GC_41})

V_193 = Vertex(name = 'V_193',
               particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_174,(0,3):C.GC_85,(0,12):C.GC_173,(0,15):C.GC_173,(0,4):C.GC_85,(0,7):C.GC_85,(0,1):C.GC_174,(0,9):C.GC_85,(0,0):C.GC_174,(0,8):C.GC_85,(0,13):C.GC_173,(0,2):C.GC_173,(0,5):C.GC_85,(0,10):C.GC_85,(0,14):C.GC_174,(0,6):C.GC_85})

V_194 = Vertex(name = 'V_194',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF9 ],
               couplings = {(0,11):C.GC_176,(0,3):C.GC_42,(0,12):C.GC_175,(0,15):C.GC_175,(0,4):C.GC_42,(0,7):C.GC_42,(0,1):C.GC_176,(0,9):C.GC_42,(0,0):C.GC_176,(0,8):C.GC_42,(0,13):C.GC_175,(0,2):C.GC_175,(0,5):C.GC_42,(0,10):C.GC_42,(0,14):C.GC_176,(0,6):C.GC_42})

V_195 = Vertex(name = 'V_195',
               particles = [ P.d__tilde__, P.d, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_526})

V_196 = Vertex(name = 'V_196',
               particles = [ P.s__tilde__, P.s, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_526})

V_197 = Vertex(name = 'V_197',
               particles = [ P.b__tilde__, P.b, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_526})

V_198 = Vertex(name = 'V_198',
               particles = [ P.e__plus__, P.e__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_529})

V_199 = Vertex(name = 'V_199',
               particles = [ P.mu__plus__, P.mu__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_529})

V_200 = Vertex(name = 'V_200',
               particles = [ P.ta__plus__, P.ta__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_529})

V_201 = Vertex(name = 'V_201',
               particles = [ P.u__tilde__, P.u, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_527})

V_202 = Vertex(name = 'V_202',
               particles = [ P.c__tilde__, P.c, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_527})

V_203 = Vertex(name = 'V_203',
               particles = [ P.t__tilde__, P.t, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_527})

V_204 = Vertex(name = 'V_204',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_489})

V_205 = Vertex(name = 'V_205',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_489})

V_206 = Vertex(name = 'V_206',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_489})

V_207 = Vertex(name = 'V_207',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_489})

V_208 = Vertex(name = 'V_208',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_489})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_489})

V_210 = Vertex(name = 'V_210',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_539})

V_211 = Vertex(name = 'V_211',
               particles = [ P.mu__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_542})

V_212 = Vertex(name = 'V_212',
               particles = [ P.ta__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_545})

V_213 = Vertex(name = 'V_213',
               particles = [ P.e__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_540})

V_214 = Vertex(name = 'V_214',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_543})

V_215 = Vertex(name = 'V_215',
               particles = [ P.ta__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_546})

V_216 = Vertex(name = 'V_216',
               particles = [ P.e__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_541})

V_217 = Vertex(name = 'V_217',
               particles = [ P.mu__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_544})

V_218 = Vertex(name = 'V_218',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_547})

V_219 = Vertex(name = 'V_219',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_492})

V_220 = Vertex(name = 'V_220',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_493})

V_221 = Vertex(name = 'V_221',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_494})

V_222 = Vertex(name = 'V_222',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_495})

V_223 = Vertex(name = 'V_223',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_496})

V_224 = Vertex(name = 'V_224',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_497})

V_225 = Vertex(name = 'V_225',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_498})

V_226 = Vertex(name = 'V_226',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_499})

V_227 = Vertex(name = 'V_227',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_500})

V_228 = Vertex(name = 'V_228',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_530})

V_229 = Vertex(name = 'V_229',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_533})

V_230 = Vertex(name = 'V_230',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_536})

V_231 = Vertex(name = 'V_231',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_531})

V_232 = Vertex(name = 'V_232',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_534})

V_233 = Vertex(name = 'V_233',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_537})

V_234 = Vertex(name = 'V_234',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_532})

V_235 = Vertex(name = 'V_235',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_535})

V_236 = Vertex(name = 'V_236',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_538})

V_237 = Vertex(name = 'V_237',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_501})

V_238 = Vertex(name = 'V_238',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_502})

V_239 = Vertex(name = 'V_239',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_503})

V_240 = Vertex(name = 'V_240',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_504})

V_241 = Vertex(name = 'V_241',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_505})

V_242 = Vertex(name = 'V_242',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_506})

V_243 = Vertex(name = 'V_243',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_507})

V_244 = Vertex(name = 'V_244',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_508})

V_245 = Vertex(name = 'V_245',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_509})

V_246 = Vertex(name = 'V_246',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_521})

V_247 = Vertex(name = 'V_247',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_521})

V_248 = Vertex(name = 'V_248',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_521})

V_249 = Vertex(name = 'V_249',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_524})

V_250 = Vertex(name = 'V_250',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_524})

V_251 = Vertex(name = 'V_251',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_524})

V_252 = Vertex(name = 'V_252',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_520,(0,1):C.GC_523})

V_253 = Vertex(name = 'V_253',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_520,(0,1):C.GC_523})

V_254 = Vertex(name = 'V_254',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_520,(0,1):C.GC_523})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_516})

V_256 = Vertex(name = 'V_256',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_516})

V_257 = Vertex(name = 'V_257',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_516})

