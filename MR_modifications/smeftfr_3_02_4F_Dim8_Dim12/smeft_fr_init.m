(* ::Package:: *)

Quit[]


(* SmeftFR v3.0 package *)
(* main initialization sequence, generation of mass basis Lagrangian
and Feynman rules in Mathematica format *)

Quiet[Remove["Global`*"]];
(*Off[General::stop];*)

(* FeynRules and SmeftFR package installation paths - edit if necessary *)
$FeynRulesPath = FileNameJoin[{"/Users/michalryczkowski/Library/Mathematica/Applications/feynrules-current"}];
SMEFT$MajorVersion      = "3";
SMEFT$MinorVersion      = "02";
SMEFT$Path = FileNameJoin[{$FeynRulesPath, "Models", "smeftfr_3_02_4F_Dim8_Dim12"}];
If[ ! DirectoryQ[SMEFT$Path], 
  Print["Directory " <> SMEFT$Path <> "does not exist, please check package setup"];
  Abort[];
];
  
(* Load FeynRules and SMEFT packages *)
Get[ FileNameJoin[{$FeynRulesPath,"FeynRules.m"}] ];
Get[ FileNameJoin[{ SMEFT$Path, "code", "smeft_package.m"}] ];

(* Choose operators to include, full list at dimension 6 and allowed list at dim8 is:

OpList6 = { "G", "Gtilde", "W", "Wtilde", "phi", "phiBox", "phiD",
 "phiW", "phiB", "phiWB", "phiWtilde", "phiBtilde", "phiWtildeB",
 "phiGtilde", "phiG", "ephi", "dphi", "uphi", "eW", "eB", "uG", "uW",
 "uB", "dG", "dW", "dB", "phil1", "phil3", "phie", "phiq1", "phiq3",
 "phiu", "phid", "phiud", "ll", "qq1", "qq3", "lq1", "lq3", "ee",
 "uu", "dd", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1",
 "qu8", "qd1", "qd8", "ledq", "quqd1", "quqd8", "lequ1", "lequ3",
 "vv", "duq", "qqu", "qqq", "duu" };

OpList8 = {"phi8", "phi6Box", "phi6D2", "G2phi4n1", "G2phi4n2",
"W2phi4n1", "W2phi4n2", "W2phi4n3", "W2phi4n4", "WBphi4n1",
"WBphi4n2", "B2phi4n1", "B2phi4n2", "G4n1", "G4n2", "G4n3", "G4n4",
"G4n5", "G4n6", "G4n7", "G4n8", "G4n9", "W4n1", "W4n2", "W4n3",
"W4n4", "W4n5", "W4n6", "B4n1", "B4n2", "B4n3", "G3Bn1", "G3Bn2",
"G3Bn3", "G3Bn4", "G2W2n1", "G2W2n2", "G2W2n3", "G2W2n4", "G2W2n5",
"G2W2n6", "G2W2n7", "G2B2n1", "G2B2n2", "G2B2n3", "G2B2n4", "G2B2n5",
"G2B2n6", "G2B2n7", "W2B2n1", "W2B2n2", "W2B2n3", "W2B2n4", "W2B2n5",
"W2B2n6", "W2B2n7", "phi4D4n1", "phi4D4n2", "phi4D4n3", "G3phi2n1",
"G3phi2n2", "W3phi2n1", "W3phi2n2", "W2Bphi2n1", "W2Bphi2n2",
"G2phi2D2n1", "G2phi2D2n2", "G2phi2D2n3", "W2phi2D2n1", "W2phi2D2n2",
"W2phi2D2n3", "W2phi2D2n4", "W2phi2D2n5", "W2phi2D2n6", "WBphi2D2n1",
"WBphi2D2n2", "WBphi2D2n3", "WBphi2D2n4", "WBphi2D2n5", "WBphi2D2n6",
"B2phi2D2n1", "B2phi2D2n2", "B2phi2D2n3", "Wphi4D2n1", "Wphi4D2n2",
"Wphi4D2n3", "Wphi4D2n4", "Bphi4D2n1", "Bphi4D2n2" ,"G2phi4D2n1", 
"G2phi4D4n1", "G2phi4D4n2", (*"l3ephiDn3","le3phiDn1"*)};!};
   
*)
(* Example of subset of operators (using full list leads to lengthy
calculations (may never end for full dim-8 set)!) *)

OpList6 = {"phi", "phiBox", "phiD", "phiW", "phiB", "phiWB", "phiWtilde", "phiBtilde", "phiWtildeB"};

OpList8 = {};

OpList = DeleteDuplicates[ Join[OpList6, OpList8] ];

(* file with numerical values of SMEFT parameters in WCxf JSON format,
If equal to "wcxf_default.json" or does not exist, all WCs are by
initialized to 0 *)

WCXFInput = FileNameJoin[{SMEFT$Path, "definitions", "wcxf_default.json"}];

(* initialize time counter and calculate Feynman rules, consult manual for full list of options *)
CPUTime = TimeUsed[];
SMEFTInitializeModel[Operators -> OpList,
                     Gauge -> Unitary,
                     ExpansionOrder -> 2,
                     WCXFInitFile -> WCXFInput,
                     InputScheme -> "GF",
                     CKMInput -> "no",
                     RealParameters -> True,
                     MaxParticles -> 5];

SMEFTLoadModel[];
Print[Style["Lagrangian generation completed, time = ", Bold ], TimeUsed[] - CPUTime];

SMEFTFindMassBasis[];
Print[Style["Transformations to physical basis calculated, time = ", Bold ], TimeUsed[] - CPUTime]; 

SMEFTFeynmanRules[];
Print[Style["Feynman rules evaluated, time = ", Bold], TimeUsed[] - CPUTime];

SMEFTOutput[];
Print[Style["Output file generated, time = ", Bold], TimeUsed[] - CPUTime];

(* Mass basis vertices in different parametrizations *)

(* By default, vertices in FeynRules format are given in "none"
scheme, e.g. for Higgs-photon-photon vertex one has: *)
Print["Higgs-photon-photon vertex in \"none\" scheme: ",
      SelectVertices[GaugeHiggsVertices, SelectParticles -> {H, A, A}]];

(* For expanded vertices, one needs to choose "input scheme"; note
"Exp" extension added at the end of the name of variable storing
vertices *)

(* "smeft" input scheme *)
SMEFTExpandVertices[Input -> "smeft", ExpOrder -> 2];
Print["Higgs-photon-photon vertex in \"smeft\" scheme: ",
      SelectVertices[GaugeHiggsVerticesExp, SelectParticles -> {H, A, A}]];

(* "user" input scheme, previously chosen to be "GF" scheme *)
SMEFTExpandVertices[Input -> "user", ExpOrder -> 2];
Print["Higgs-photon-photon vertex in \"user\" scheme: ",
      SelectVertices[GaugeHiggsVerticesExp, SelectParticles -> {H, A, A}]];

(* To produce other output formats (Latex, WCxf, FeynArts, UFO) it is
now necessary to quit this session and run SmeftFR-interfaces.nb in
new kernel *)


(* "smeft" input scheme *)
SMEFTExpandVertices[Input -> "smeft", ExpOrder -> 1];
Print["Higgs-photon-photon vertex in \"smeft\" scheme: ",
      SelectVertices[GaugeHiggsVerticesExp, SelectParticles -> {H, Z, Z}]];


GaugeHig


FourLeptonVerticesExp[[4]]


SelectVertices[QuarkHiggsGaugeVertices, SelectParticles -> {H, uq, uqbar}]


FourLeptonVerticesExp[[8]]


FourLeptonVerticesExp[[8]]


FourLeptonVerticesExp[[3]]


FourLeptonVertices


FourLeptonVerticesExp[[5]]


FourLeptonVerticesExp = FourLeptonVertices // OutputParametersExpansio


FourLeptonVertices[[2]]/.OutputParametersExpansion


oplist


For [i=1, i<Length[oplist8]+1, i++,
   FourLeptonLagrangian = FourLeptonLagrangian + Lam^2 ToExpression[ "LQ"<>oplist8[[i]] ];
];


OutputParametersExpansion


FourLeptonLagrangian


SMEFT$OperatorList


SelectVertices[GluonHiggsVerticesExp, SelectParticles -> {l, lbar , l ,lbar}]





FourLeptonVertices[[2]]


LQle3phiDn1 := Module[{sp1,sp2,sp3,sp4,ff1,ff2,ff3,ff4,ii,jj,nu},

aux = I (lRbar[sp1,ff1] . Ga[nu,sp1,sp2] . lR[sp2,ff2]) . (LLbar[sp3,jj,ff3] . DC[lR[sp3,ff4],nu]) Phi[jj];

aux = ExpandIndices[ ToExpression[SMEFT$WB <> "le3phiDn1"][ff1,ff2,ff3,ff4] aux, FlavorExpand->{SU2W, SU2D} ];

aux + HC[aux] 
];



LQle3phiDn1


FeynmanRules[LQle3phiDn1]


SMEFT$OperatorList


aux + HC[aux]


 ToExpression[SMEFT$WB <> "l3ephiDn3"][ff1,ff2,ff3,ff4] aux //ExpandIndices


Intersection[ SMEFT$OperatorList, {"ll","ee","le","l3ephiDn3"}]


aux =(LLbar[sp1,ii,ff1] . LL[sp2,ii,ff2]) . (DC[LLbar[sp3,jj,ff3],mu] . lR[sp4,ff4]) Phi[jj] Ga[nu,sp1,sp2] Ga[nu,sp3,sp4]


LQl3ephiDn3 := Module[{sp1,sp2,sp3,sp4,ff1,ff2,ff3,ff4,ii,jj,nu},

aux = I (LLbar[sp1,ii,ff1] . Ga[nu,sp1,sp2] . LL[sp2,ii,ff2]) . (DC[LLbar[sp3,jj,ff3],nu] . lR[sp4,ff4]) Phi[jj];

aux = ExpandIndices[ ToExpression[SMEFT$WB <> "l3ephiDn3"][ff1,ff2,ff3,ff4] aux, FlavorExpand->{SU2W, SU2D} ];

aux + HC[aux] 
];



LQl3ephiDn3


aux = I (LLbar[sp1,ii,ff1] . LL[sp2,ii,ff2]) . (DC[LLbar[sp3,jj,ff3],mu] . lR[sp4,ff4]) Phi[jj] Ga[nu,sp1,sp2] Ga[nu,sp3,sp4]
ExpandIndices[ ToExpression[SMEFT$WB <> "l3ephiDn3"][ff1,ff2,ff3,ff4] aux ]


aux


aux =(LLbar[sp1,ii,ff1] . LL[sp2,ii,ff2]) . (DC[LLbar[sp3,jj,ff3],mu] . lR[sp4,ff4] . Phi[jj]) Ga[nu,sp1,sp2] Ga[nu,sp3,sp4];
aux = ExpandIndices[ ToExpression[SMEFT$WB <> "l3ephiDn3"][ff1,ff2,ff3,ff4] aux, FlavorExpand->{SU2W, SU2D} ]


aux = ExpandIndices[ ToExpression[SMEFT$WB <> "l3ephiDn3"][ff1,ff2,ff3,ff4] aux, FlavorExpand->{SU2W, SU2D} ]


aux = (QLbar[sp1,ii,ff1,dd] . uR[sp1,ff2,dd]) . (QLbar[sp2,jj,ff3,cc] . dR[sp2,ff4,cc]) Eps[ii,jj];
aux = ExpandIndices[ ToExpression[SMEFT$WB <> "quqd1"][ff1,ff2,ff3,ff4] aux, FlavorExpand->{SU2D} ]


LLbar[sp1,ii,ff1] . LL[sp2,ii,ff2] . (DC[LLbar[sp3,jj,ff3],mu] . lR[sp4,ff4]) Phi[jj] Ga[nu,sp1,sp2] Ga[nu,sp3,sp4]


Get[ FileNameJoin[{SMEFT$Path, "lagrangian", "30_Dim8AR.fr"}] ]


oplist = Intersection[ SMEFT$OperatorList, {"ll","ee","le","l3ephiDn3"}];
FourLeptonLagrangian = 0;
For [i=1, i<Length[oplist]+1, i++,
   FourLeptonLagrangian = FourLeptonLagrangian + Lam ToExpression[ "LQ"<>oplist[[i]] ];
];
FourLeptonLagrangian = ReplaceFlavorRotations[FourLeptonLagrangian] // Expand;
FourLeptonLagrangian = FourLeptonLagrangian /. Lam^k_->If[k>1,0,Lam^k];
FourLeptonVertices = FeynmanRules[FourLeptonLagrangian];
If [ SMEFT$MajoranaNeutrino,
   FourLeptonVertices = SymmetrizeNeutrino4Current[FourLeptonVertices];
   i = Position[ FourLeptonVertices[[All, 1]], {{vlbar, 1}, {vl, 2}, {vlbar, 3}, {vl,4}} ];
   If[ Length[i]>0, FourLeptonVertices[[i[[1,1]], 2]] = Neutrino4Vertex[] ];
 ];



For [i=1, i<Length[oplist]+1, i++,
   FourLeptonLagrangian = FourLeptonLagrangian + Lam ToExpression[ "LQ"<>oplist[[i]] ];
]


ToExpression[ "LQ" <> oplist[[1]]]


oplist[[1]]


oplist[[i]]


Length[oplist]+1


Lam ToExpression[ "LQ"<>oplist[[1]] ]


FourLeptonLagrangian


FourFermionInteractions


FourLeptonLagrangian


GluonHiggsVerticesExp


BLViolatingVertices


FourLeptonLagrangian


GaugeHiggsLagrangian


SMEFT$Dim8FermionOperators


SMEFTExpandVertices[Input -> "user", ExpOrder -> 2];
Print["gghhh vertex with CG2phi4D4n2 ",
      SelectVertices[GluonHiggsVerticesExp, SelectParticles -> {H, H, H, G, G}]/.CG2phi4D4n1->0];
Print["gghhh vertex with CG2phi4D4n1 ",
      SelectVertices[GluonHiggsVerticesExp, SelectParticles -> {H, H, H, G, G}]/.CG2phi4D4n2->0];



dd//FullForm


FeynmanRules[LQG2phi4D4n3]


LQG2phi4D4n3


LQG2phi4D4n4 := Module[{mu,nu,al,be,ga,del,rho,sig,a,aux,jj,ii},

aux = Phi8bar[ii] Phi8[ii] del[del[Phi8bar[jj],nu],mu] del[del[Phi8[jj],be],al] Eps[mu,al,rho,sig]/2 HC[FS[Gl,rho,sig,a]] FS[Gl,nu,be,a];

aux = ExpandIndices[aux,FlavorExpand->{SU2W,SU2D}];

ExpandIndices[ ToExpression[SMEFT$WB <> "G2phi4D4n4"] ] aux /. SMEFTGaugeRules
];


FourLeptonLagrangian


LQG2phi4D4n3//Expand


FeynmanRules[LQG2phi4D4n3]


SMEFT$OperatorList


LQG2phi4D4n3 := Module[{mu,nu,al,be,ga,om,rho,sig,a,aux,jj,ii},

aux = Phi8bar[ii] Phi8[ii] del[del[Phi8bar[jj],nu],mu]del[del[Phi8[jj],be],al] Eps[mu,al,rho,sig]/2 HC[FS[Gl,rho,sig,a]] Eps[nu,be,ga,om]/2 HC[FS[Gl,ga,om,a]];

aux = ExpandIndices[aux,FlavorExpand->{SU2W,SU2D}];

ExpandIndices[ ToExpression[SMEFT$WB <> "G2phi4D4n3"] ] aux /. SMEFTGaugeRules
];
LQG2phi4D4n3


FourFermionOperators8


SMEFT$Dim6FermionOperators


SMEFT$Dim8NullList


SMEFT$Dim6NullList


SMEFT$Dim8BosonOperators


SMEFT$Dim8FermionOperators


SMEFT$Dim8NullList


SMEFT$Dim8NullList = Join[ (# -> 0 & /@ SMEFT$Dim8BosonOperators),
						(#[__] -> 0 & /@ SMEFT$Dim8FermionOperators) ]

SMEFT$Dim6NullList


SMEFT$Dim8NullList


SMEFT$Dim6NullList


FourFermionOperators8


SMEFT$OperatorList


ToExpression["LQ"<>#] ] & /@ FourFermionOperators8


If[ MemberQ[ SMEFT$OperatorList, # ], SMEFT$LGferm6 = SMEFT$LGferm6
+ Lam^2 ToExpression["LQ"<>#] ] & /@ FourFermionOperators8;


SMEFT$OperatorList


SMEFT$LGferm6


SMEFT$LGferm6


SMEFT$LGferm6


SMEFT$LGferm


SMEFT$OperatorList={"l3ephiDn3"}


oplist = Intersection[ SMEFT$OperatorList, {"ll","ee","le","l3ephiDn3"}]


FourLeptonLagrangian = 0;
For [i=1, i<Length[oplist]+1, i++,
   FourLeptonLagrangian = FourLeptonLagrangian + Lam ToExpression[ "LQ"<>oplist[[i]] ];
]


oplist[[1]]


ToExpression[ "LQ"<>oplist[[1]] ]


FourLeptonLagrangian


Length[oplist]


Lam ToExpression[ "LQ"<>oplist[[i]] ]



oplist = Intersection[ SMEFT$OperatorList, {"ll","ee","le"}];
oplist8 = Intersection[ SMEFT$OperatorList, {"l3ephiDn3","le3phiDn1"}];
FourLeptonLagrangian = 0;
For [i=1, i<Length[oplist]+1, i++,
   FourLeptonLagrangian = FourLeptonLagrangian + Lam ToExpression[ "LQ"<>oplist[[i]] ];
];
For [i=1, i<Length[oplist8]+1, i++,
   FourLeptonLagrangian = FourLeptonLagrangian + Lam^2 ToExpression[ "LQ"<>oplist8[[i]] ];
];


FourLeptonLagrangian
