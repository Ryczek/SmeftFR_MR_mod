(* SmeftFR v4.0 package *)
(* Calculation of Feynman rules for 4-fermion and B+L violating vertices *)


Fierz4f = Function[{vertex},
(* 4-fermion Fierzing routines; "vertex" must have FeynRules syntax,
   field list followed by interaction formula *)
Module[{a,b,tmp,res,expr,flist,f,f1,f2,f3,f4},

flist = vertex[[1]];
expr  = vertex[[2]];

(* fierzed and not fierzed parts *)
tmp = expr /. TensDot[___][Index[Spin, Ext[1]], Index[Spin, Ext[2]]] -> 0;
res = expr - tmp // Expand;

(* gamma_mu P_L x gamma_mu P_L *)
tmp = tmp /. TensDot[Ga[Index[Lorentz,a_]],ProjM][Index[Spin,Ext[1]],Index[Spin,Ext[4]]] *
             TensDot[Ga[Index[Lorentz,a_]],ProjM][Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             TensDot[Ga[Index[Lorentz,a]], ProjM][Index[Spin,f1],Index[Spin,f2]] *
             TensDot[Ga[Index[Lorentz,a]], ProjM][Index[Spin,f3],Index[Spin,f4]];

(* gamma_mu P_R x gamma_mu P_R *)
tmp = tmp /. TensDot[Ga[Index[Lorentz,a_]],ProjP][Index[Spin,Ext[1]],Index[Spin,Ext[4]]] *
             TensDot[Ga[Index[Lorentz,a_]],ProjP][Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             TensDot[Ga[Index[Lorentz,a]], ProjP][Index[Spin,f1],Index[Spin,f2]] *
             TensDot[Ga[Index[Lorentz,a]], ProjP][Index[Spin,f3],Index[Spin,f4]];

(* gamma_mu P_L x gamma_mu P_R *)
tmp = tmp /. TensDot[Ga[Index[Lorentz,a_]],ProjM][Index[Spin,Ext[1]],Index[Spin,Ext[4]]] *
             TensDot[Ga[Index[Lorentz,a_]],ProjP][Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             - 2 ProjP[Index[Spin,f1],Index[Spin,f2]] ProjM[Index[Spin,f3],Index[Spin,f4]];

(* gamma_mu P_R x gamma_mu P_L *)
tmp = tmp /. TensDot[Ga[Index[Lorentz,a_]],ProjP][Index[Spin,Ext[1]],Index[Spin,Ext[4]]] *
             TensDot[Ga[Index[Lorentz,a_]],ProjM][Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             - 2 ProjM[Index[Spin,f1],Index[Spin,f2]] ProjP[Index[Spin,f3],Index[Spin,f4]];

(* P_L x P_R *)
tmp = tmp /. ProjM[Index[Spin,Ext[1]],Index[Spin,Ext[4]]] ProjP[Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             - 1/2 Module[{mu}, TensDot[Ga[Index[Lorentz,mu]],ProjP][Index[Spin,f1],Index[Spin,f2]] *
                                TensDot[Ga[Index[Lorentz,mu]],ProjM][Index[Spin,f3],Index[Spin,f4]] ];

(* P_R x P_L *)
tmp = tmp /. ProjP[Index[Spin,Ext[1]],Index[Spin,Ext[4]]] ProjM[Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             - 1/2 Module[{mu}, TensDot[Ga[Index[Lorentz,mu]],ProjM][Index[Spin,f1],Index[Spin,f2]] *
                                TensDot[Ga[Index[Lorentz,mu]],ProjP][Index[Spin,f3],Index[Spin,f4]] ];

(* P_R x P_R *)
tmp = tmp /. ProjP[Index[Spin,Ext[1]],Index[Spin,Ext[4]]] ProjP[Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             - 1/2 ProjP[Index[Spin,f1],Index[Spin,f2]] ProjP[Index[Spin,f3],Index[Spin,f4]] -
               1/8 Module[{mu,nu}, SIG[mu,nu,ProjP,f1,f2] SIG[mu,nu,ProjP,f3,f4] ];

(* P_L x P_L *)
tmp = tmp /. ProjM[Index[Spin,Ext[1]],Index[Spin,Ext[4]]] ProjM[Index[Spin,Ext[3]],Index[Spin,Ext[2]]] ->
             - 1/2 ProjM[Index[Spin,f1],Index[Spin,f2]] ProjM[Index[Spin,f3],Index[Spin,f4]] -
               1/8 Module[{mu,nu}, SIG[mu,nu,ProjM,f1,f2] SIG[mu,nu,ProjM,f3,f4] ];

(* sigma P_L x sigma P_L, the same as sigma x sigma P_L *)
tmp = tmp /. SIG[a_, b_, ProjM, Index[Spin,Ext[1]], Index[Spin,Ext[4]]] *
             SIG[a_, b_, ProjM, Index[Spin,Ext[3]] ,Index[Spin,Ext[2]]] ->
             - 6 ProjM[Index[Spin,f1],Index[Spin,f2]] ProjM[Index[Spin,f3],Index[Spin,f4]] +
               1/2 SIG[a,b,ProjM,f1,f2] SIG[a,b,ProjM,f3,f4];

(* sigma P_R x sigma P_R, the same as sigma x sigma P_R *)
tmp = tmp /. SIG[a_, b_, ProjP, Index[Spin,Ext[1]], Index[Spin,Ext[4]]] *
             SIG[a_, b_, ProjP, Index[Spin,Ext[3]] ,Index[Spin,Ext[2]]] ->
             - 6 ProjP[Index[Spin,f1],Index[Spin,f2]] ProjP[Index[Spin,f3],Index[Spin,f4]] +
               1/2 SIG[a,b,ProjP,f1,f2] SIG[a,b,ProjP,f3,f4];

(* swap non-spin external indices *)
tmp = tmp /. Ext[4] -> f;
tmp = tmp /. Ext[2] -> Ext[4];
tmp = tmp /. f      -> Ext[2];

(* swap 2nd and 4th field on the list *)
expr         = flist[[2,1]];
flist[[2,1]] = flist[[4,1]];
flist[[4,1]] = expr;

(* restore notation for external indices *)
tmp = tmp /. f1 -> Ext[1] /. f2 -> Ext[2] /. f3 -> Ext[3] /. f4 -> Ext[4];

{flist,tmp + res}

]
(* end of Fierz4f *)
]



SortFFFFIndices = Function[{wc,v,x,y,z},
(* apply index symmetries for WCs of 4 identical fermions: 1st
   external index always in the first index pair; if not present, 1st
   generation index in the 1st pair *)			
Module[{tmp,pos},

tmp = {v,x,y,z};
pos = Position[ tmp, Index[Generation, Generation$1] ];
If [ Length[pos]>0 && pos[[1,1]] > 2, tmp = {tmp[[3]],tmp[[4]],tmp[[1]],tmp[[2]]} ];
pos = Position[ tmp, Index[Generation, Ext[1]] ];
If [ Length[pos]>0 && pos[[1,1]] > 2, tmp = {tmp[[3]],tmp[[4]],tmp[[1]],tmp[[2]]} ];

wc @@ tmp

]
(* end of SortFFFFIndices *)
]
			

Gamma2ToSigma = Function[{vlist},
(* Dirac tensor simplifications, replace Gamma_mu Gamma_nu with sigma_munu *)
Module[{tmp,a,b,c,d,s1,s2},

tmp =  vlist //. TensDot[Ga[a_],Ga[b_],c_][s1_,s2_] ->
                 ME[a,b] c[s1,s2] - I SIG[a,b,c,s1,s2] // Expand;
tmp = tmp     /. ME[Index[Lorentz, a_],  Index[Lorentz, b_]] *
                 SIG[Index[Lorentz, a_], Index[Lorentz, b_], c__] -> 0;
tmp = tmp     /. ME[Index[Lorentz, b_],  Index[Lorentz, a_]] *
                 SIG[Index[Lorentz, a_], Index[Lorentz, b_], c__] -> 0;
tmp /.           SIG[Index[Lorentz, a_], Index[Lorentz, b_], c__] *
                 SIG[Index[Lorentz, b_], Index[Lorentz, a_], d__] ->
               - SIG[Index[Lorentz, a],  Index[Lorentz, b], c] *
                 SIG[Index[Lorentz, a],  Index[Lorentz, b], d]

]
(* end of Gamma2ToSigma *)
]



FindFourFermionVertices = Function[{oplist},
(* find 4-fermion Lagrangian and vertices for operators in oplist *)
Module[{i,lag,vert},

lag = 0;
For [i=1, i<Length[oplist]+1, i++,
   lag = lag + Lam^SMEFT$NPOrder[ oplist[[i]] ] ToExpression[ "LQ" <> oplist[[i]] ];
];
lag  = SU2Simplify[lag];
lag  = ReplaceFlavorRotations[lag] // Expand // SMEFTExpReduce;
lag = lag // OptimizeIndex;
vert = FeynmanRules[lag];
vert = Gamma2ToSigma[vert];

{lag,vert}

]
(* end of fermion vertices *)
]

			
FourFermionInteractions = Function[{},
(* 4-fermion couplings *)
Module[{a, b, c, d, s1, s2, i, tmp, ia1, ia2, oplist, WC, fun},

Print[Style["Calculating 4-fermion vertices...",Bold]];

(* four lepton vertices *)
{FourLeptonLagrangian, FourLeptonVertices} =
      FindFourFermionVertices[ Intersection[ SMEFT$OperatorList,
                                             SMEFT$FourLeptonOperators ] ];

If [ SMEFT$MajoranaNeutrino,
   i = Position[ FourLeptonVertices[[All, 1]], {{vl, 1}, {vl, 2}, {vl, 3}, {vl,4}} ];
   If[ Length[i]>0, FourLeptonVertices[[i[[1,1]], 2]] = Neutrino4Vertex[] ];
];

(* two quark two lepton vertices *)
{TwoQuarkTwoLeptonLagrangian, TwoQuarkTwoLeptonVertices} =
      FindFourFermionVertices[ Intersection[ SMEFT$OperatorList,
                                             SMEFT$TwoQuarkTwoLeptonOperators ] ];
(* skip color indices for 2-quark current, always delta_ab *)
TwoQuarkTwoLeptonVertices  = TwoQuarkTwoLeptonVertices /.
       IndexDelta[Index[Colour, Ext[a_]], Index[Colour, Ext[b_]]] -> 1;

(* four quark vertices *)
{FourQuarkLagrangian, FourQuarkVertices} =
      FindFourFermionVertices[ Intersection[ SMEFT$OperatorList,
                                             SMEFT$FourQuarkOperators ] ];

(* symmetrization of indices in operators with 4 identical fermions
   and WC symmetry C_ijkl = C_klij *)
Module[{},
  WC = ToExpression[SMEFT$MB <> #];
  FourLeptonVertices = FourLeptonVertices /. WC[a__] -> fun[WC, a];
  FourLeptonVertices = FourLeptonVertices /. fun -> SortFFFFIndices;
  FourQuarkVertices  = FourQuarkVertices  /. WC[a__] -> fun[WC, a];
  FourQuarkVertices  = FourQuarkVertices  /. fun -> SortFFFFIndices;
] & /@ SMEFT$FFFFOperators;

(* if present, transform dlvu vertex into quark x lepton current *)
oplist = { {{dqbar,1},{l,2},{vlbar,3},{uq,4}},
           {{dqbar,1},{l,2},{vl,3},{uq,4}},
	   {{lbar,1},{dq,2},{uqbar,3},{vl,4}} };
For[i=1, i < Length[TwoQuarkTwoLeptonVertices] + 1, i++,
  If[ MemberQ[ oplist, TwoQuarkTwoLeptonVertices[[i,1]] ],
    TwoQuarkTwoLeptonVertices[[i]] = Fierz4f[ TwoQuarkTwoLeptonVertices[[i]] ] // Expand;
  ];
];
					
(* hack - manual correction of wrong sign generated by FeynRules for
vertices with 4 identical fermions and in uudd vertex *)

If [ SMEFT$Correct4FermionSign,

For[i=1, i < Length[FourLeptonVertices] + 1, i++,
    If[ FourLeptonVertices[[i,1]] === {{lbar,1},{l,2},{lbar,3},{l,4}} ||
        FourLeptonVertices[[i,1]] === {{vlbar,1},{vl,2},{vlbar,3},{vl,4}},
        FourLeptonVertices[[i,2]] = FourLeptonVertices[[i,2]] /.
            TensDot[ia1_,ia2_][Index[Spin, Ext[1]], Index[Spin, Ext[4]]] ->
          - TensDot[ia1, ia2][Index[Spin, Ext[1]], Index[Spin, Ext[4]]];
    ];
];

For[i=1, i < Length[FourQuarkVertices] + 1, i++,
    If[ FourQuarkVertices[[i,1]] === {{uqbar,1},{uq,2},{uqbar,3},{uq,4}} ||
	FourQuarkVertices[[i,1]] === {{dqbar,1},{dq,2},{dqbar,3},{dq,4}} ||
	FourQuarkVertices[[i,1]] === {{dqbar,1},{dq,2},{uqbar,3},{uq,4}},
	FourQuarkVertices[[i,2]] = FourQuarkVertices[[i,2]] /.
	  TensDot[ia1_, ia2_][Index[Spin, Ext[1]], Index[Spin, Ext[4]]] ->
	- TensDot[ia1, ia2][Index[Spin, Ext[1]], Index[Spin, Ext[4]]];
	FourQuarkVertices[[i,2]] = FourQuarkVertices[[i,2]] /.
	  ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[4]]] ->
	- ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[4]]];
	FourQuarkVertices[[i,2]] = FourQuarkVertices[[i,2]] /.
	  ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[4]]] ->
	- ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[4]]];
    ];
  ];
,
(* if Correct4FermionSign = False and MajoranaNeutrino=True, revert
back manually evaluated proper sign to wrong one again ... *)

For[i=1, i < Length[FourLeptonVertices] + 1, i++,
    If[ FourLeptonVertices[[i,1]] === {{vl,1},{vl,2},{vl,3},{vl,4}},	
        FourLeptonVertices[[i,2]] = FourLeptonVertices[[i,2]] /.
	      TensDot[ia1_,ia2_][Index[Spin, Ext[1]], Index[Spin, Ext[4]]] ->
            - TensDot[ia1, ia2][Index[Spin, Ext[1]], Index[Spin, Ext[4]]]
    ];
  ];
];


(* fierzing, whenewer useful. Currently commented out, can affect
   evanescent operators!

For [ i=1, i < Length[FourLeptonVertices] + 1, i++,
    If [ FourLeptonVertices[[i,1]] === {{lbar,1},{l,2},{lbar,3},{l,4}} ||
	FourLeptonVertices[[i,1]] === {{vlbar,1},{vl,2},{vlbar,3},{vl,4}},
	FourLeptonVertices[[i]] = Fierz4f[ FourLeptonVertices[[i]] ] ];
];

For [ i=1, i < Length[FourQuarkVertices] + 1, i++,
    If [ FourQuarkVertices[[i,1]] === {{uqbar,1},{uq,2},{uqbar,3},{uq,4}} ||
	FourQuarkVertices[[i,1]] === {{dqbar,1},{dq,2},{dqbar,3},{dq,4}},
	FourQuarkVertices[[i]] = Fierz4f[ FourQuarkVertices[[i]] ] ];
];
*)

(* Final step - replace SIG -> SigmaX to restore gamma_mu gamma_nu
products instead of sigma_munu, avoiding crashes in UFO not compatible
with sigma_munu notation *)

FourLeptonVertices        = Map[OptimizeIndex, FourLeptonVertices /. SIG -> SigmaX // Expand, 2];
TwoQuarkTwoLeptonVertices = Map[OptimizeIndex, TwoQuarkTwoLeptonVertices /. SIG -> SigmaX // Expand, 2];
FourQuarkVertices         = Map[OptimizeIndex, FourQuarkVertices /. SIG -> SigmaX // Expand, 2];

];
(* end of FourFermionInteractions *)
];




BLViolating4FermionInteractions = Function[{},
(*  BL violatingfermion couplings *)
Module[{i,j,vlist},

Print[Style["Calculating B and L violating 4-fermion vertices...",Bold]];

{BLViolatingLagrangian, BLViolatingVertices} =
  FindFourFermionVertices[ Intersection[ SMEFT$OperatorList,
                                         SMEFT$FourFermionBLVOperators ] ];
(* C_qqu is symmetric in first 2 indices *)
BLViolatingVertices = BLViolatingVertices /.
       ToExpression[SMEFT$MB <> "qqu"][Index[Generation, Ext[1]], Index[Generation, Generation$1], i_, j_] ->
       ToExpression[SMEFT$MB <> "qqu"][Index[Generation, Generation$1], Index[Generation, Ext[1]], i, j];
BLViolatingVertices = BLViolatingVertices /.
       ToExpression[SMEFT$MB <> "qqu3"][Index[Generation, Ext[1]], Index[Generation, Generation$1], i_, j_] ->
       ToExpression[SMEFT$MB <> "qqu3"][Index[Generation, Generation$1], Index[Generation, Ext[1]], i, j];

];
(* end of BLViolating4FermionInteractions *)
];




Neutrino4Vertex = Function[{},
(* if neutrinos are Majorana particles, 4-neutrino interaction must be
properly symmetrized, easier to do manually just for this one case *)

2 I Lam (ToExpression[SMEFT$MB<>"ll"][Index[Generation, Generation$1],
 Index[Generation, Generation$2], Index[Generation, Generation$3],
 Index[Generation, Generation$4]] ( Conjugate[ Ul[Index[Generation,
 Generation$1], Index[Generation, Ext[1]]] ] Ul[Index[Generation,
 Generation$2], Index[Generation, Ext[2]]] Conjugate[
 Ul[Index[Generation, Generation$3], Index[Generation, Ext[3]]] ]
 Ul[Index[Generation, Generation$4], Index[Generation, Ext[4]]]
 TensDot[Ga[Index[Lorentz, mu$1]], ProjM][Index[Spin, Ext[1]],
 Index[Spin, Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjM][Index[Spin, Ext[3]], Index[Spin, Ext[4]]] - Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[2]]] ]
 Ul[Index[Generation, Generation$2], Index[Generation, Ext[1]]]
 Conjugate[ Ul[Index[Generation, Generation$3], Index[Generation,
 Ext[3]]] ] Ul[Index[Generation, Generation$4], Index[Generation,
 Ext[4]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjP][Index[Spin,
 Ext[1]], Index[Spin, Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjM][Index[Spin, Ext[3]], Index[Spin, Ext[4]]] - Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[1]]] ]
 Ul[Index[Generation, Generation$2], Index[Generation, Ext[2]]]
 Conjugate[ Ul[Index[Generation, Generation$3], Index[Generation,
 Ext[4]]] ] Ul[Index[Generation, Generation$4], Index[Generation,
 Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjM][Index[Spin,
 Ext[1]], Index[Spin, Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjP][Index[Spin, Ext[3]], Index[Spin, Ext[4]]] + Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[2]]] ]
 Ul[Index[Generation, Generation$2], Index[Generation, Ext[1]]]
 Conjugate[ Ul[Index[Generation, Generation$3], Index[Generation,
 Ext[4]]] ] Ul[Index[Generation, Generation$4], Index[Generation,
 Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjP][Index[Spin,
 Ext[1]], Index[Spin, Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjP][Index[Spin, Ext[3]], Index[Spin, Ext[4]]] ) -
 ToExpression[SMEFT$MB<>"ll"][Index[Generation, Generation$1],
 Index[Generation, Generation$4], Index[Generation, Generation$3],
 Index[Generation, Generation$2]] ( Conjugate[ Ul[Index[Generation,
 Generation$1], Index[Generation, Ext[1]]] ] Ul[Index[Generation,
 Generation$4], Index[Generation, Ext[4]]] Conjugate[
 Ul[Index[Generation, Generation$3], Index[Generation, Ext[3]]] ]
 Ul[Index[Generation, Generation$2], Index[Generation, Ext[2]]]
 TensDot[Ga[Index[Lorentz, mu$1]], ProjM][Index[Spin, Ext[1]],
 Index[Spin, Ext[4]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjM][Index[Spin, Ext[3]], Index[Spin, Ext[2]]] - Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[4]]] ]
 Ul[Index[Generation, Generation$4], Index[Generation, Ext[1]]]
 Conjugate[ Ul[Index[Generation, Generation$3], Index[Generation,
 Ext[3]]] ] Ul[Index[Generation, Generation$2], Index[Generation,
 Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjP][Index[Spin,
 Ext[1]], Index[Spin, Ext[4]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjM][Index[Spin, Ext[3]], Index[Spin, Ext[2]]] - Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[1]]] ]
 Ul[Index[Generation, Generation$4], Index[Generation, Ext[4]]]
 Conjugate[ Ul[Index[Generation, Generation$3], Index[Generation,
 Ext[2]]] ] Ul[Index[Generation, Generation$2], Index[Generation,
 Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjM][Index[Spin,
 Ext[1]], Index[Spin, Ext[4]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjP][Index[Spin, Ext[3]], Index[Spin, Ext[2]]] + Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[4]]] ]
 Ul[Index[Generation, Generation$4], Index[Generation, Ext[1]]]
 Conjugate[ Ul[Index[Generation, Generation$3], Index[Generation,
 Ext[2]]] ] Ul[Index[Generation, Generation$2], Index[Generation,
 Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjP][Index[Spin,
 Ext[1]], Index[Spin, Ext[4]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjP][Index[Spin, Ext[3]], Index[Spin, Ext[2]]] ) -
 ToExpression[SMEFT$MB<>"ll"][Index[Generation, Generation$1],
 Index[Generation, Generation$3], Index[Generation, Generation$2],
 Index[Generation, Generation$4]] ( Conjugate[ Ul[Index[Generation,
 Generation$1], Index[Generation, Ext[1]]] ] Ul[Index[Generation,
 Generation$3], Index[Generation, Ext[3]]] Conjugate[
 Ul[Index[Generation, Generation$2], Index[Generation, Ext[2]]] ]
 Ul[Index[Generation, Generation$4], Index[Generation, Ext[4]]]
 TensDot[Ga[Index[Lorentz, mu$1]], ProjM][Index[Spin, Ext[1]],
 Index[Spin, Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjM][Index[Spin, Ext[2]], Index[Spin, Ext[4]]] - Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[3]]] ]
 Ul[Index[Generation, Generation$3], Index[Generation, Ext[1]]]
 Conjugate[ Ul[Index[Generation, Generation$2], Index[Generation,
 Ext[2]]] ] Ul[Index[Generation, Generation$4], Index[Generation,
 Ext[4]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjP][Index[Spin,
 Ext[1]], Index[Spin, Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjM][Index[Spin, Ext[2]], Index[Spin, Ext[4]]] - Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[1]]] ]
 Ul[Index[Generation, Generation$3], Index[Generation, Ext[3]]]
 Conjugate[ Ul[Index[Generation, Generation$2], Index[Generation,
 Ext[4]]] ] Ul[Index[Generation, Generation$4], Index[Generation,
 Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjM][Index[Spin,
 Ext[1]], Index[Spin, Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjP][Index[Spin, Ext[2]], Index[Spin, Ext[4]]] + Conjugate[
 Ul[Index[Generation, Generation$1], Index[Generation, Ext[3]]] ]
 Ul[Index[Generation, Generation$3], Index[Generation, Ext[1]]]
 Conjugate[ Ul[Index[Generation, Generation$2], Index[Generation,
 Ext[4]]] ] Ul[Index[Generation, Generation$4], Index[Generation,
 Ext[2]]] TensDot[Ga[Index[Lorentz, mu$1]], ProjP][Index[Spin,
 Ext[1]], Index[Spin, Ext[3]]] TensDot[Ga[Index[Lorentz, mu$1]],
 ProjP][Index[Spin, Ext[2]], Index[Spin, Ext[4]]] ) ) // Expand //
 Simplify

(* end of Neutrino4Vertex *)
]



