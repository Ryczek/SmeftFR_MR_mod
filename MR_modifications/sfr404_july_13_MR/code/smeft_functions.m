(* SmeftFR v4.0 package *)
(* Auxiliary functions to simplify and transform SMEFT Lagrangian *)

AntisymmetricArgSort = Function[{name, i1, i2, x},
(* sorting of antisymmetric arguments in function "fun" *)
  Order[i1, i2] name @@ Flatten[{Sort[{i1, i2}], x}]
];


(* sigma_munu Dirac matrix *)
Sigma[mu_,nu_,sp1_,sp2_] = I/2 Module[{spx},(Ga[mu,sp1,spx] Ga[nu,spx,sp2] -
                                             Ga[nu,sp1,spx] Ga[mu,spx,sp2])];

SigmaX = Function[{mu,nu,X,s1,s2},
(* Dirac matrix (sigma_{mu,nu} X)_{s1,s2} *)
If [ MemberQ[{ProjP, ProjM, IndexDelta}, X] || MemberQ[{Ga, SlashedP}, Head[X]],
  I/2 (TensDot[Ga[Index[Lorentz, mu]], Ga[Index[Lorentz, nu]],
               X][Index[Spin, s1], Index[Spin, s2]] -
       TensDot[Ga[Index[Lorentz, nu]],Ga[Index[Lorentz, mu]],
               X][Index[Spin, s1], Index[Spin, s2]])
,
  Print["Wrong Dirac operator called as SigmaX argument: X can be only
   P_L,R (ProjM, ProjP), Gamma_al (Ga[al]), Gamma_5 (Ga[5]), p-slash
   (SlashedP[p]), 1 (IndexDelta)" ];
  Abort[]
]

(* end of SigmaX *)
]

NumberToString = Function[{x},
(* string display format for floating point numbers *)
Module[{tmp,tmp1,tmp2,nmax},

(* number of significant digits in real numbers *)
nmax = 8;

If[ NumberQ[x],
  If[ Head[x] === Real || Head[x] === Rational,
    tmp1 = MantissaExponent[N[x]];
    tmp  = ToString[ N[tmp1[[1]], nmax] ] <> "*^" <> ToString[tmp1[[2]]];
  ];
  If[ Head[x] === Integer,
    tmp1 = MantissaExponent[x];
    tmp  = ToString[tmp1[[1]]] <> "*^" <> ToString[tmp1[[2]]];
  ];
  If[ Head[x] === Complex,
    tmp1 = MantissaExponent[N[Re[x]]];
    tmp1 = ToString[ N[tmp1[[1]], nmax] ] <> "*^" <> ToString[tmp1[[2]]];
    tmp = If[ Im[x] < 0, " - ", " + "];
    tmp2 = MantissaExponent[N[Abs[Im[x]]]];
    tmp2 = ToString[ N[tmp2[[1]], nmax] ] <> "*^" <> ToString[tmp2[[2]]];
    tmp  = tmp1 <> tmp <> tmp2 <> "*I";
  ];
,
  Print[ "NumberToString function called with argument ",x];
  Print[ "Argument is not a number, please correct!"];
  Abort[];
];

tmp

]
(* end of NumberToString *)
]



ComplexListElementTest = Function[{x},
(* check some if list element is complex number *)		
  MemberQ[ Head[#] & /@ Flatten[x], Complex ]	

(* end of ComplexListElementTest *)
]



ScalarParStructureTest = Function[{parlist},
(* check if input SM parameters are all real numbers and have no indices *)
Module[{test},

test = False;
If [ ComplexListElementTest[#],
  test = True;
  Print[ "Parameter ", Style[#[[1]], Bold],
	 " defined as Complex, correct or split into separate Real and Imaginary parts."]
] & /@ (parlist /. Rule -> List);

If [ test,
  Print[ Style[ "Complex SM input parameters defined, inspect list at the header of smeft_input_scheme.m.  Aborting...", Red ] ];
  Abort[]
];

If[ Head[ Value /. #[[2]] ] === List,
  test = True;
  Print[ "Parameter ", Style[#[[1]], Bold],
	 " defined as List, correct or split into separate elements."]
] & /@ parlist;

If [ test,
  Print[ Style[ "Non-scalar SM input parameters defined, inspect list at the header of smeft_input_scheme.m.  Aborting...",Red ] ];
  Abort[]
];

]
(* end of ScalarParStructureTest *)
];



SMEFTExpReduce = Function[{x},
(* cuts higher order terms in 1/Lambda *)
Module[{k}, x /. Lam^k_ -> If[ k>SMEFT$ExpansionOrder, 0, Lam^k ] ]
]



SMEFTExpOrder = Function[{x},
(* expands expression to given order in 1/Lambda *)
Module[{tmp,k},

tmp = x /. Lam^k_ -> If[ k>SMEFT$ExpansionOrder, 0, Lam^k ];
Normal[ Series[ tmp, {Lam, 0, SMEFT$ExpansionOrder}] ]

]
(* end of SMEFTExpOrder *)
]



MBScalarList = Function[{op},
(* returns scalar operator in mass basis if present in SMEFT$OperatorList or 0 otherwise *)
If[MemberQ[ SMEFT$OperatorList, ToString[op] ], ToExpression[SMEFT$MB<>ToString[op]], 0]
(*end of MBScalarList *)			
]


WBScalarList = Function[{op},
(* returns scalar operator in Warsaw basis if present in SMEFT$OperatorList or 0 otherwise *)
If[MemberQ[ SMEFT$OperatorList, ToString[op] ], ToExpression[SMEFT$WB<>ToString[op]], 0]
(*end of WBScalarList *)			
]


MBTensor2List = Function[{op,i,j},
(* returns flavor operator with 2 indices in mass basis if present in SMEFT$OperatorList or 0 otherwise *)
If[MemberQ[ SMEFT$OperatorList, ToString[op] ],
            ToExpression[SMEFT$MB<>ToString[op]<>"["<>ToString[i]<>","<>ToString[j]<>"]"], 0]
(*end of MBTensor2List *)			
]


WBTensor2List = Function[{op,i,j},
(* returns flavor operator with 2 indices in Warsaw basis if present in SMEFT$OperatorList or 0 otherwise *)
If[MemberQ[ SMEFT$OperatorList, ToString[op] ],
            ToExpression[SMEFT$WB<>ToString[op]<>"["<>ToString[i]<>","<>ToString[j]<>"]"], 0]
(*end of WBTensor2List *)			
]


MBTensor4List = Function[{op,i,j,k,l},
(* returns flavor operator with 4 indices in mass basis if present in
SMEFT$OperatorList or 0 otherwise *)

If[MemberQ[ SMEFT$OperatorList, ToString[op] ],
            ToExpression[SMEFT$MB<>ToString[op]<>"["<>ToString[i]<>","<>ToString[j]<>","<>ToString[k]<>","<>ToString[l]<>"]"], 0]
(*end of MBTensor4List *)			
]


WBTensor4List = Function[{op,i,j,k,l},
(* returns flavor operator with 4 indices in Warsaw basis if present
   in SMEFT$OperatorList or 0 otherwise *)

If[MemberQ[ SMEFT$OperatorList, ToString[op] ],
            ToExpression[SMEFT$WB<>ToString[op]<>"["<>ToString[i]<>","<>ToString[j]<>","<>ToString[k]<>","<>ToString[l]<>"]"], 0]

(*end of WBTensor4List *)			
]



GenerateOperatorLists[ OptionsPattern[ { Letter -> SMEFT$MB } ] ] :=
(* sublists of active operators *)
Module[{l,i},

l = OptionValue[Letter];

SMEFT$Dim6BosonOperators = ToExpression[l <> #] & /@ Intersection[
    SMEFT$Dim6BosonicOperators, SMEFT$OperatorList ];

SMEFT$Dim6FermionOperators = ToExpression[l <> #] & /@ Intersection[
    SMEFT$Dim6FermionicOperators, SMEFT$OperatorList ];

SMEFT$Dim8BosonOperators = ToExpression[l <> #] & /@ Intersection[
    SMEFT$Dim8BosonicOperators, SMEFT$OperatorList ];

SMEFT$Dim8FermionOperators = ToExpression[l <> #] & /@ Intersection[
    SMEFT$Dim8FermionicOperators, SMEFT$OperatorList ];

SMEFT$FourFermionOperators = ToExpression[l <> #] & /@ Intersection[
    Join[ SMEFT$Dim6FourFermionOperators, SMEFT$Dim8FourFermionOperators ], SMEFT$OperatorList ];

(* special sub-class, 4 identical fermions, WC with C_ijkl = C_klij symmetry *)
SMEFT$FFFFOperators = {};
If [ MemberQ[ {4,6}, #[[4]] ], AppendTo[ SMEFT$FFFFOperators, #[[1]] ] ] & /@ SMEFT$TensorWC;
SMEFT$FFFFOperators = Intersection[ SMEFT$FFFFOperators, SMEFT$OperatorList ];

SMEFT$Dim6NullList = Join[ (# -> 0 & /@ SMEFT$Dim6BosonOperators),
                           (#[__] -> 0 & /@ SMEFT$Dim6FermionOperators) ];

SMEFT$Dim8NullList = Join[ (# -> 0 & /@ SMEFT$Dim8BosonOperators),
                           (#[__] -> 0 & /@ SMEFT$Dim8FermionOperators) ];

]



CombineCommonPowers = Function[{expr,par,n},
(* rearranges power expansion into a_0 + a_1 par^1 + ... a_n par^n *)
Module[{tmp,fact,aa},
tmp =  expr /. par -> 0 // Simplify;
If[ n > 0,
  For[aa=1, aa < n+1, aa++,
    fact = Coefficient[expr, par^aa];
    tmp = tmp + par^aa If[ aa==1, Dim6CoefficientsSimplify[fact], Simplify[fact, TimeConstraint->5] ];
  ];
];

tmp

]
(* end of CombineCommonPowers *)
]



Dim6CoefficientsSimplify = Function[{expr},
(* simplifies coefficients of dim 6 operators *)
Module[{tmp,fact,aa},

tmp = 0;
For[aa=1, aa < Length[SMEFT$Dim6NullList]+1, aa++,
    tmp = tmp + Simplify[expr /. Drop[SMEFT$Dim6NullList,{aa} ], TimeConstraint->10 ];
  ];

tmp

]
(* end of Dim6CoefficientsSimplify *)
]



CouplingsFormSimplify = Function[{vlist},
(* Simplify couplings in front of interaction vertices *)
Module[{tmp},				

tmp = Map[ CombineCommonPowers[#, Lam, SMEFT$ExpansionOrder] &, vlist[[All, 2]]];
Partition[Riffle[vlist[[All,1]], tmp],2]

]
(* end of CouplingsFormSimplify *)
]				



SU2Simplify = Function[{expr},
(*** SU(2) generators simplification ***)
Module[{tmp,aa,bb,cc,y,z,y1,z1},

(* remove Ta8, it is the same as Ta *)       
tmp = expr //. Ta8->Ta;       
(* remove Ta8, it is the same as Ta *)       
tmp = expr //. Ta8->Ta;       
(* T^a_bc T^a_de reduction *)
tmp = tmp //. Ta[aa_,y_,z_] Ta[aa_,y1_,z1_] ->
          ( IndexDelta[y,z1] IndexDelta[z,y1] -
        1/2 IndexDelta[y,z]  IndexDelta[y1,z1] )/2 // Expand;
(* T antisymmetry in matrix product *)
tmp = tmp //. Ta[aa_,y_,z_] Ta[bb_,y1_,z_] -> - Ta[aa,y,z] Ta[bb,z,y1];
(* eps_abc T^a T^b reduction *)
tmp = tmp //. Eps[aa_,bb_,cc_] Ta[aa_,y_,z_] Ta[bb_,z_,y1_] ->   I Ta[cc,y,y1];
tmp = tmp //. Eps[aa_,cc_,bb_] Ta[aa_,y_,z_] Ta[bb_,z_,y1_] -> - I Ta[cc,y,y1];
tmp = tmp //. Eps[cc_,aa_,bb_] Ta[aa_,y_,z_] Ta[bb_,z_,y1_] ->   I Ta[cc,y,y1];

tmp
]
(* end of SU2Simplify *)
];


SU3Simplify = Function[{expr},
(*** SU(3) generators simplification ***)
Module[{tmp,aa,bb,cc,y,z,y1,z1},

(* remove T8, it is the same as T *)       
tmp = expr //. T8->T;       
(* T^a_bc T^a_de reduction *)
tmp = tmp //. T[aa_,y_,z_] T[aa_,y1_,z1_] ->
          ( IndexDelta[y,z1] IndexDelta[z,y1] -
        1/3 IndexDelta[y,z]  IndexDelta[y1,z1] )/2 // Expand;
(* T antisymmetry in matrix product *)
tmp = tmp //. T[aa_,y_,z_] T[bb_,y1_,z_] -> - T[aa,y,z] T[bb,z,y1];
(* f_abc T^a T^b reduction *)
tmp = tmp //. f[aa_,bb_,cc_] T[aa_,y_,z_] T[bb_,z_,y1_] ->   3 I/2 T[cc,y,y1];
tmp = tmp //. f[aa_,cc_,bb_] T[aa_,y_,z_] T[bb_,z_,y1_] -> - 3 I/2 T[cc,y,y1];
tmp = tmp //. f[cc_,aa_,bb_] T[aa_,y_,z_] T[bb_,z_,y1_] ->   3 I/2 T[cc,y,y1];

tmp
]
(* end of SU3Simplify *)
];





SMEFTExpandVertices[ OptionsPattern[{ Input -> "smeft",
				      ExpOrder-> SMEFT$ExpansionOrder,
				      ExpName -> "Exp",
				      Silent -> True}] ] :=
Module[{input, order, CPUTime, a, b},
(* expand normalization constant in terms of chosen set of input parameters *)

input = OptionValue[Input];
If [ ! MemberQ[{"smeft","user","none"}, input],
     Print["Currently only \"none\", \"smeft\" or  \"user\" allowed as options of SMEFTExpandVertices"];
     Abort[];
   ];

If [ ! MemberQ[ {0,1,2}, OptionValue[ExpOrder] ],
     Print["Currently only option ExpOrder = 0 (SM), ExpOrder = 1 (dim6) or = 2 (dim8) in SMEFTExpandVertices allowed"];
     Abort[];
   ];

(* store general expansion order *)
order = SMEFT$ExpansionOrder;

(* initialize time counter *)
CPUTime = TimeUsed[];

NormalizationConstantsExpansion[input];

If [ OptionValue[ExpName] == "Latex",
  SMEFT$ExpansionOrder = Min[ 1, OptionValue[ExpOrder] ];

  If[ ! OptionValue[Silent], Print["Expanding lepton vertices..."] ];
  LeptonGaugeVerticesLatex = LeptonGaugeVertices // OutputParametersExpansion;
  LeptonHiggsGaugeVerticesLatex = LeptonHiggsGaugeVertices // OutputParametersExpansion;

  If[ ! OptionValue[Silent], Print["Expanding quark vertices..."] ];
  QuarkGaugeVerticesLatex = QuarkGaugeVertices // OutputParametersExpansion;
  QuarkHiggsGaugeVerticesLatex = QuarkHiggsGaugeVertices // OutputParametersExpansion;
  QuarkGluonVerticesLatex = QuarkGluonVertices // OutputParametersExpansion;

  If[ ! OptionValue[Silent], Print["Expanding gauge and Higgs vertices..."] ];
  GaugeSelfVerticesLatex = GaugeSelfVertices // OutputParametersExpansion;
  GaugeHiggsVerticesLatex = GaugeHiggsVertices // OutputParametersExpansion;
  GluonSelfVerticesLatex = GluonSelfVertices // OutputParametersExpansion;
  GluonHiggsVerticesLatex = GluonHiggsVertices // OutputParametersExpansion;

  If [ SMEFT$RxiGaugeStatus,
       If[ ! OptionValue[Silent], Print["Expanding ghost vertices..."] ];
       GhostVerticesLatex = GhostVertices // OutputParametersExpansion
     ];

  If[ ! OptionValue[Silent], Print["Expanding 4-fermion vertices..."] ];
  FourLeptonVerticesLatex = FourLeptonVertices // OutputParametersExpansion;
  TwoQuarkTwoLeptonVerticesLatex = TwoQuarkTwoLeptonVertices // OutputParametersExpansion;
  FourQuarkVerticesLatex = FourQuarkVertices // OutputParametersExpansion;

  If[ ! OptionValue[Silent], Print["Expanding BL-violating vertices..."] ];
  BLViolatingVerticesLatex = BLViolatingVertices // OutputParametersExpansion;
,
  SMEFT$ExpansionOrder = OptionValue[ExpOrder];

  If[ ! OptionValue[Silent], Print["Expanding lepton vertices..."] ];
  LeptonGaugeVerticesExp = LeptonGaugeVertices // OutputParametersExpansion;
  LeptonHiggsGaugeVerticesExp = LeptonHiggsGaugeVertices // OutputParametersExpansion;

  If[ ! OptionValue[Silent], Print["Expanding quark vertices..."] ];
  QuarkGaugeVerticesExp = QuarkGaugeVertices // OutputParametersExpansion;
  QuarkHiggsGaugeVerticesExp = QuarkHiggsGaugeVertices // OutputParametersExpansion;
  QuarkGluonVerticesExp = QuarkGluonVertices // OutputParametersExpansion;

  If[ ! OptionValue[Silent], Print["Expanding gauge and Higgs vertices..."] ];
  GaugeSelfVerticesExp = GaugeSelfVertices // OutputParametersExpansion;
  GaugeHiggsVerticesExp = GaugeHiggsVertices // OutputParametersExpansion;
  GluonSelfVerticesExp = GluonSelfVertices // OutputParametersExpansion;
  GluonHiggsVerticesExp = GluonHiggsVertices // OutputParametersExpansion;

  If [ SMEFT$RxiGaugeStatus,
       If[ ! OptionValue[Silent], Print["Expanding ghost vertices..."] ];
       GhostVerticesExp = GhostVertices // OutputParametersExpansion
     ];

  If[ ! OptionValue[Silent], Print["Expanding 4-fermion vertices..."] ];
  FourLeptonVerticesExp = FourLeptonVertices // OutputParametersExpansion;
  TwoQuarkTwoLeptonVerticesExp = TwoQuarkTwoLeptonVertices // OutputParametersExpansion;
  FourQuarkVerticesExp = FourQuarkVertices // OutputParametersExpansion;

  If[ ! OptionValue[Silent], Print["Expanding BL-violating vertices..."] ];
  BLViolatingVerticesExp = BLViolatingVertices // OutputParametersExpansion;
];

If[ ! OptionValue[Silent], Print[Style["All vertices expanded, time = ", Bold], TimeUsed[] - CPUTime] ];

(* restore general expansion order *)
SMEFT$ExpansionOrder = order;

(* end of SMEFTExpandVertices *)
]




ReplaceFlavorRotations = Function[x,
(* replace flavor rotation matrices with CKM and PMNS *)
Module[{tmp,aa,b,c},

tmp = x;
	
(* apply unitarity of fermion rotations *)
tmp = tmp //. VVL[aa_,b_] Conjugate[VVL[aa_,c_]] -> IndexDelta[b,c];
tmp = tmp //. VLL[aa_,b_] Conjugate[VLL[aa_,c_]] -> IndexDelta[b,c];
tmp = tmp //. VLR[aa_,b_] Conjugate[VLR[aa_,c_]] -> IndexDelta[b,c];
tmp = tmp //. VUL[aa_,b_] Conjugate[VUL[aa_,c_]] -> IndexDelta[b,c];
tmp = tmp //. VUR[aa_,b_] Conjugate[VUR[aa_,c_]] -> IndexDelta[b,c];
tmp = tmp //. VDL[aa_,b_] Conjugate[VDL[aa_,c_]] -> IndexDelta[b,c];
tmp = tmp //. VDR[aa_,b_] Conjugate[VDR[aa_,c_]] -> IndexDelta[b,c];

tmp = tmp //. VVL[b_,aa_] Conjugate[VVL[c_,aa_]] -> IndexDelta[b,c];
tmp = tmp //. VLL[b_,aa_] Conjugate[VLL[c_,aa_]] -> IndexDelta[b,c];
tmp = tmp //. VLR[b_,aa_] Conjugate[VLR[c_,aa_]] -> IndexDelta[b,c];
tmp = tmp //. VUL[b_,aa_] Conjugate[VUL[c_,aa_]] -> IndexDelta[b,c];
tmp = tmp //. VUR[b_,aa_] Conjugate[VUR[c_,aa_]] -> IndexDelta[b,c];
tmp = tmp //. VDL[b_,aa_] Conjugate[VDL[c_,aa_]] -> IndexDelta[b,c];
tmp = tmp //. VDR[b_,aa_] Conjugate[VDR[c_,aa_]] -> IndexDelta[b,c];

(* K=VUL^+ VDL, U = VLL^+ VVL - NO dim-6 corrections, both matrices unitary! *)
tmp = tmp //. Conjugate[VLL[aa_,b_]] VVL[aa_,c_] -> Ul[b,c];
tmp = tmp //. Conjugate[VVL[aa_,b_]] VLL[aa_,c_] -> Conjugate[Ul[c,b]];
tmp = tmp //. Conjugate[VUL[aa_,b_]] VDL[aa_,c_] -> Kq[b,c];
tmp = tmp //. Conjugate[VDL[aa_,b_]] VUL[aa_,c_] -> Conjugate[Kq[c,b]];

tmp

]
(* End of ReplaceFlavorRotations *)
];




TensorWCSymmetrize = Function[{WC,cat},
(* symmetrization of flavor WC matrices according to their classes,
see smeft_variables.m; val contains full numerical matrix, sub
substitutions for dependent entries *)
Module[{val,sub,wc,ind,cpl,spec},

(* ind contains pairs of indices of identical WCs, cpl pairs of
indices of cc'ed WCs *)
ind = Table[{},{i,1,9}];
cpl = Table[{},{i,1,9}];

(* hermitian 3x3 matrix *)
cpl[[2]] = {{{2,1},{1,2}},
            {{3,1},{1,3}},
            {{3,2},{2,3}}};

(* symmetric 3x3 matrix *)
ind[[3]] = cpl[[2]];

(* two identical fermion currents *)
ind[[4]] = {{{1,2,1,1},{1,1,1,2}},
            {{1,3,1,1},{1,1,1,3}},
            {{1,3,1,2},{1,2,1,3}},
            {{2,1,1,2},{1,2,2,1}},
            {{2,2,1,1},{1,1,2,2}},
            {{2,2,1,2},{1,2,2,2}},
            {{2,2,1,3},{1,3,2,2}},
            {{2,3,1,1},{1,1,2,3}},
            {{2,3,1,2},{1,2,2,3}},
            {{2,3,1,3},{1,3,2,3}},
            {{2,3,2,2},{2,2,2,3}},
            {{3,1,1,2},{1,2,3,1}},
            {{3,1,1,3},{1,3,3,1}},
            {{3,2,1,2},{1,2,3,2}},
            {{3,2,1,3},{1,3,3,2}},
            {{3,2,2,3},{2,3,3,2}},
            {{3,3,1,1},{1,1,3,3}},
            {{3,3,1,2},{1,2,3,3}},
            {{3,3,1,3},{1,3,3,3}},
            {{3,3,2,2},{2,2,3,3}},
            {{3,3,2,3},{2,3,3,3}}};

cpl[[4]] = {{{1,1,2,1},{1,1,1,2}},
            {{1,1,3,1},{1,1,1,3}},
            {{1,1,3,2},{1,1,2,3}},
            {{1,3,2,1},{1,2,3,1}},
            {{2,1,1,1},{1,1,1,2}},
            {{2,1,1,3},{1,2,3,1}},
            {{2,1,2,1},{1,2,1,2}},
            {{2,1,2,2},{1,2,2,2}},
            {{2,1,2,3},{1,2,3,2}},
            {{2,1,3,1},{1,2,1,3}},
            {{2,1,3,2},{1,2,2,3}},
            {{2,1,3,3},{1,2,3,3}},
            {{2,2,2,1},{1,2,2,2}},
            {{2,2,3,1},{1,3,2,2}},
            {{2,2,3,2},{2,2,2,3}},
            {{2,3,2,1},{1,2,3,2}},
            {{2,3,3,1},{1,3,3,2}},
            {{3,1,1,1},{1,1,1,3}},
            {{3,1,2,1},{1,2,1,3}},
            {{3,1,2,2},{1,3,2,2}},
            {{3,1,2,3},{1,3,3,2}},
            {{3,1,3,1},{1,3,1,3}},
            {{3,1,3,2},{1,3,2,3}},
            {{3,1,3,3},{1,3,3,3}},
            {{3,2,1,1},{1,1,2,3}},
            {{3,2,2,1},{1,2,2,3}},
            {{3,2,2,2},{2,2,2,3}},
            {{3,2,3,1},{1,3,2,3}},
            {{3,2,3,2},{2,3,2,3}},
            {{3,2,3,3},{2,3,3,3}},
            {{3,3,2,1},{1,2,3,3}},
            {{3,3,3,1},{1,3,3,3}},
            {{3,3,3,2},{2,3,3,3}}};

(* two independent fermion currents *)
cpl[[5]]= {{{1,1,2,1},{1,1,1,2}},
           {{1,1,3,1},{1,1,1,3}},
           {{1,1,3,2},{1,1,2,3}},
           {{2,1,1,1},{1,2,1,1}},
           {{2,1,1,2},{1,2,2,1}},
           {{2,1,1,3},{1,2,3,1}},
           {{2,1,2,1},{1,2,1,2}},
           {{2,1,2,2},{1,2,2,2}},
           {{2,1,2,3},{1,2,3,2}},
           {{2,1,3,1},{1,2,1,3}},
           {{2,1,3,2},{1,2,2,3}},
           {{2,1,3,3},{1,2,3,3}},
           {{2,2,2,1},{2,2,1,2}},
           {{2,2,3,1},{2,2,1,3}},
           {{2,2,3,2},{2,2,2,3}},
           {{3,1,1,1},{1,3,1,1}},
           {{3,1,1,2},{1,3,2,1}},
           {{3,1,1,3},{1,3,3,1}},
           {{3,1,2,1},{1,3,1,2}},
           {{3,1,2,2},{1,3,2,2}},
           {{3,1,2,3},{1,3,3,2}},
           {{3,1,3,1},{1,3,1,3}},
           {{3,1,3,2},{1,3,2,3}},
           {{3,1,3,3},{1,3,3,3}},
           {{3,2,1,1},{2,3,1,1}},
           {{3,2,1,2},{2,3,2,1}},
           {{3,2,1,3},{2,3,3,1}},
           {{3,2,2,1},{2,3,1,2}},
           {{3,2,2,2},{2,3,2,2}},
           {{3,2,2,3},{2,3,3,2}},
           {{3,2,3,1},{2,3,1,3}},
           {{3,2,3,2},{2,3,2,3}},
           {{3,2,3,3},{2,3,3,3}},
           {{3,3,2,1},{3,3,1,2}},
           {{3,3,3,1},{3,3,1,3}},
           {{3,3,3,2},{3,3,2,3}}};

(* two identical fermion currents special case Cee *)
ind[[6]] = {{{1,2,1,1},{1,1,1,2}},
            {{1,2,2,1},{1,1,2,2}},
            {{1,3,1,1},{1,1,1,3}},
            {{1,3,1,2},{1,2,1,3}},
            {{1,3,2,1},{1,1,2,3}},
            {{1,3,2,2},{1,2,2,3}},
            {{1,3,3,1},{1,1,3,3}},
            {{1,3,3,2},{1,2,3,3}},
            {{2,1,1,2},{1,1,2,2}},
            {{2,1,1,3},{1,1,2,3}},
            {{2,2,1,1},{1,1,2,2}},
            {{2,2,1,2},{1,2,2,2}},
            {{2,2,1,3},{1,2,2,3}},
            {{2,3,1,1},{1,1,2,3}},
            {{2,3,1,2},{1,2,2,3}},
            {{2,3,1,3},{1,3,2,3}},
            {{2,3,2,2},{2,2,2,3}},
            {{2,3,3,2},{2,2,3,3}},
            {{3,1,1,3},{1,1,3,3}},
            {{3,2,1,2},{1,2,3,2}},
            {{3,2,1,3},{1,2,3,3}},
            {{3,2,2,3},{2,2,3,3}},
            {{3,3,1,1},{1,1,3,3}},
            {{3,3,1,2},{1,2,3,3}},
            {{3,3,1,3},{1,3,3,3}},
            {{3,3,2,2},{2,2,3,3}},
            {{3,3,2,3},{2,3,3,3}}};

cpl[[6]] = {{{1,1,2,1},{1,1,1,2}},
            {{1,1,3,1},{1,1,1,3}},
            {{1,1,3,2},{1,1,2,3}},
            {{1,2,3,1},{1,1,2,3}},
            {{2,1,1,1},{1,1,1,2}},
            {{2,1,2,1},{1,2,1,2}},
            {{2,1,2,2},{1,2,2,2}},
            {{2,1,2,3},{1,2,3,2}},
            {{2,1,3,1},{1,2,1,3}},
            {{2,1,3,2},{1,2,2,3}},
            {{2,1,3,3},{1,2,3,3}},
            {{2,2,2,1},{1,2,2,2}},
            {{2,2,3,1},{1,2,2,3}},
            {{2,2,3,2},{2,2,2,3}},
            {{2,3,2,1},{1,2,3,2}},
            {{2,3,3,1},{1,2,3,3}},
            {{3,1,1,1},{1,1,1,3}},
            {{3,1,1,2},{1,1,2,3}},
            {{3,1,2,1},{1,2,1,3}},
            {{3,1,2,2},{1,2,2,3}},
            {{3,1,2,3},{1,2,3,3}},
            {{3,1,3,1},{1,3,1,3}},
            {{3,1,3,2},{1,3,2,3}},
            {{3,1,3,3},{1,3,3,3}},
            {{3,2,1,1},{1,1,2,3}},
            {{3,2,2,1},{1,2,2,3}},
            {{3,2,2,2},{2,2,2,3}},
            {{3,2,3,1},{1,3,2,3}},
            {{3,2,3,2},{2,3,2,3}},
            {{3,2,3,3},{2,3,3,3}},
            {{3,3,2,1},{1,2,3,3}},
            {{3,3,3,1},{1,3,3,3}},
            {{3,3,3,2},{2,3,3,3}}};

(* B- violating special case qque *)
ind[[7]] = {{{2,1,1,1},{1,2,1,1}},
            {{2,1,1,2},{1,2,1,2}},
            {{2,1,1,3},{1,2,1,3}},
            {{2,1,2,1},{1,2,2,1}},
            {{2,1,2,2},{1,2,2,2}},
            {{2,1,2,3},{1,2,2,3}},
            {{2,1,3,1},{1,2,3,1}},
            {{2,1,3,2},{1,2,3,2}},
            {{2,1,3,3},{1,2,3,3}},
            {{3,1,1,1},{1,3,1,1}},
            {{3,1,1,2},{1,3,1,2}},
            {{3,1,1,3},{1,3,1,3}},
            {{3,1,2,1},{1,3,2,1}},
            {{3,1,2,2},{1,3,2,2}},
            {{3,1,2,3},{1,3,2,3}},
            {{3,1,3,1},{1,3,3,1}},
            {{3,1,3,2},{1,3,3,2}},
            {{3,1,3,3},{1,3,3,3}},
            {{3,2,1,1},{2,3,1,1}},
            {{3,2,1,2},{2,3,1,2}},
            {{3,2,1,3},{2,3,1,3}},
            {{3,2,2,1},{2,3,2,1}},
            {{3,2,2,2},{2,3,2,2}},
            {{3,2,2,3},{2,3,2,3}},
            {{3,2,3,1},{2,3,3,1}},
            {{3,2,3,2},{2,3,3,2}},
            {{3,2,3,3},{2,3,3,3}}};

(* B- violating special case qqql *)
ind[[8]] = {{{2,1,1,1},{1,1,2,1}},
            {{2,1,1,2},{1,1,2,2}},
            {{2,1,1,3},{1,1,2,3}},
            {{2,2,1,1},{1,2,2,1}},
            {{2,2,1,2},{1,2,2,2}},
            {{2,2,1,3},{1,2,2,3}},
            {{3,1,1,1},{1,1,3,1}},
            {{3,1,1,2},{1,1,3,2}},
            {{3,1,1,3},{1,1,3,3}},
            {{3,2,2,1},{2,2,3,1}},
            {{3,2,2,2},{2,2,3,2}},
            {{3,2,2,3},{2,2,3,3}},
            {{3,3,1,1},{1,3,3,1}},
            {{3,3,1,2},{1,3,3,2}},
            {{3,3,1,3},{1,3,3,3}},
            {{3,3,2,1},{2,3,3,1}},
            {{3,3,2,2},{2,3,3,2}},
            {{3,3,2,3},{2,3,3,3}}};

(* in case of qqql for some indices special replacement
   X -> Y + V - W *)
spec = {{{3,1,2,1},{2,3,1,1},{2,1,3,1},{1,3,2,1}},
        {{3,1,2,2},{2,3,1,2},{2,1,3,2},{1,3,2,2}},
        {{3,1,2,3},{2,3,1,3},{2,1,3,3},{1,3,2,3}},
        {{3,2,1,1},{1,3,2,1},{1,2,3,1},{2,3,1,1}},
        {{3,2,1,2},{1,3,2,2},{1,2,3,2},{2,3,1,2}},
        {{3,2,1,3},{1,3,2,3},{1,2,3,3},{2,3,1,3}}};

(* function body starts here *)
wc = Head[ Keys[ WC[[1]] ] ];
val = WC;
sub = {};

If [ NumberQ[wc @@ #[[2]] /. WC],
  AppendTo[ val, wc @@ #[[1]] -> wc @@ #[[2]] /. WC ];
] & /@ ind[[cat]];
  AppendTo[ sub, wc @@ #[[1]] -> wc @@ #[[2]] ] & /@ ind[[cat]];
			
If [ NumberQ[wc @@ #[[2]] /. WC],
  AppendTo[ val, wc @@ #[[1]] -> Conjugate[ wc @@ #[[2]] /. WC ] ];
] & /@ cpl[[cat]];
  AppendTo[ sub, wc @@ #[[1]] -> Conjugate[ wc @@ #[[2]] ] ] & /@ cpl[[cat]];

If[cat == 8,(* special qqql case *)
  If [ NumberQ[ (wc @@ #[[2]] + wc @@ #[[3]] - wc @@ #[[4]]) /. WC],
    AppendTo[ val, wc @@ #[[1]] -> (wc @@ #[[2]] +
                                    wc @@ #[[3]] - wc @@ #[[4]]) /. WC ];
  ] & /@ spec;
    AppendTo[ sub, wc @@ #[[1]] -> wc @@ #[[2]] +
                                   wc @@ #[[3]] - wc @@ #[[4]] ] & /@ spec;
];

val = Sort[ val ];
sub = Sort[ sub ];

{val,sub}

]
(* end of TensorWCSymmetrize *)
]

