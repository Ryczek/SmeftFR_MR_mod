(* SmeftFR v4.0 package *)
(* predefined variables *)

SMEFT$MajorVersion      = "4";
SMEFT$MinorVersion      = "04";

(* general model version info *)

SMEFT$Version           = SMEFT$MajorVersion <> "." <> SMEFT$MinorVersion;

SMEFT$Authors      = "A. Dedes, J. Rosiek, M. Ryczkowski";
SMEFT$Date         = "01. 04. 2026";
SMEFT$Institutions = "University of Warsaw, University of Ioannina";
SMEFT$Emails       = "janusz.rosiek@fuw.edu.pl";
SMEFT$URLs         = "URL: www.fuw.edu.pl/smeft";
SMEFT$ModelName    = "SMEFT";
SMEFT$Citations    = "    - JHEP 1706 (2017) 143 (1704.03888)\n"<>
                     "    - Comput.Phys.Commun. 247 (2020) 106931, (1904.03204)\n"<>
                     "    - Comput.Phys.Commun. 294 (2024) 108943, (2302.01353)";

(* operator classes in string format, SMEFT naming *)

(* lists of currently implemented fermionic dim8 operators, users
should add names of new ones here after adding code for them in
"lagrangian" subdirectory; "classes" as defined in 2005.00059 *)

SMEFT$Dim8TwoFermionOperators = {
    (* class 9 - first column (leptonic G2/W2 + up-quark) *)
    "leG2phin1", "leG2phin2", "leW2phin1", "leW2phin2", "leW2phin3",
    "quG2phin1", "quG2phin2", "quG2phin3", "quG2phin4", "quG2phin5",
    "quGWphin1", "quGWphin2", "quGWphin3", "quGBphin1", "quGBphin2",
    "quGBphin3", "quW2phin1", "quW2phin2", "quW2phin3", "quWBphin1",
    "quWBphin2", "quWBphin3", "quB2phin1", "quB2phin2",
    (* class 9 - second column (leptonic WB/B2 + down-quark) *)
    "leWBphin1", "leWBphin2", "leWBphin3", "leB2phin1", "leB2phin2",
    "qdG2phin1", "qdG2phin2", "qdG2phin3", "qdG2phin4", "qdG2phin5",
    "qdGWphin1", "qdGWphin2", "qdGWphin3", "qdGBphin1", "qdGBphin2",
    "qdGBphin3", "qdW2phin1", "qdW2phin2", "qdW2phin3", "qdWBphin1",
    "qdWBphin2", "qdWBphin3", "qdB2phin1", "qdB2phin2",
    (* class 10 *)
    "leWphi3n1", "leWphi3n2", "leBphi3",
    "quGphi3", "quWphi3n1", "quWphi3n2", "quBphi3",
    "qdGphi3", "qdWphi3n1", "qdWphi3n2", "qdBphi3",
    (* class 11 *)
    "l2phi2D3n1", "l2phi2D3n2", "l2phi2D3n3", "l2phi2D3n4",
    "e2phi2D3n1", "e2phi2D3n2",
    "q2phi2D3n1", "q2phi2D3n2", "q2phi2D3n3", "q2phi2D3n4",
    "u2phi2D3n1", "u2phi2D3n2", "d2phi2D3n1", "d2phi2D3n2",
    "udphi2D3",
    (* class 12 *)
    "lephi5","quphi5","qdphi5",
    (* class 13 *)
    "l2phi4Dn1", "l2phi4Dn2", "l2phi4Dn3", "l2phi4Dn4",
    "e2phi4D",
    "q2phi4Dn1", "q2phi4Dn2", "q2phi4Dn3", "q2phi4Dn4",
    "u2phi4D", "d2phi4D", "udphi4D",
    (* class 14 - hadronic, first column *)
    "q2G2Dn1", "q2G2Dn2", "q2G2Dn3", "q2W2Dn1", "q2W2Dn2", "q2B2D",
    "u2G2Dn1", "u2G2Dn2", "u2G2Dn3", "u2W2D", "u2B2D",
    "d2G2Dn1", "d2G2Dn2", "d2G2Dn3", "d2W2D", "d2B2D",
    (* class 14 - hadronic, second column *)
    "q2G2Dn4", "q2G2Dn5",
    "q2GWDn1", "q2GWDn2", "q2GWDn3", "q2GWDn4",
    "q2GBDn1", "q2GBDn2", "q2GBDn3", "q2GBDn4",
    "q2W2Dn3", "q2W2Dn4",
    "q2WBDn1", "q2WBDn2", "q2WBDn3", "q2WBDn4",
    "u2G2Dn4", "u2G2Dn5", "u2GBDn1", "u2GBDn2", "u2GBDn3", "u2GBDn4",
    "d2G2Dn4", "d2G2Dn5", "d2GBDn1", "d2GBDn2", "d2GBDn3", "d2GBDn4",
    (* class 14 - leptonic *)
    "l2G2D", "l2W2Dn1", "l2W2Dn2", "l2W2Dn3", "l2W2Dn4", "l2B2D",
    "l2WBDn1", "l2WBDn2", "l2WBDn3", "l2WBDn4",
    "e2G2D", "e2W2D", "e2B2D",
    (* class 15 - (RR) X phi^2 D *)
    "e2Wphi2Dn1", "e2Wphi2Dn2", "e2Wphi2Dn3", "e2Wphi2Dn4",
    "e2Bphi2Dn1", "e2Bphi2Dn2", "e2Bphi2Dn3", "e2Bphi2Dn4",
    "u2Gphi2Dn1", "u2Gphi2Dn2", "u2Gphi2Dn3", "u2Gphi2Dn4",
    "u2Wphi2Dn1", "u2Wphi2Dn2", "u2Wphi2Dn3", "u2Wphi2Dn4",
    "u2Bphi2Dn1", "u2Bphi2Dn2", "u2Bphi2Dn3", "u2Bphi2Dn4",
    "d2Gphi2Dn1", "d2Gphi2Dn2", "d2Gphi2Dn3", "d2Gphi2Dn4",
    "d2Wphi2Dn1", "d2Wphi2Dn2", "d2Wphi2Dn3", "d2Wphi2Dn4",
    "d2Bphi2Dn1", "d2Bphi2Dn2", "d2Bphi2Dn3", "d2Bphi2Dn4",
    "udGphi2n1", "udGphi2n2", "udWphi2n1", "udWphi2n2",
    "udBphi2n1", "udBphi2n2",
    (* class 15 - (LL) X phi^2 D *)
    "l2Wphi2Dn1", "l2Wphi2Dn2", "l2Wphi2Dn3", "l2Wphi2Dn4",
    "l2Wphi2Dn5", "l2Wphi2Dn6", "l2Wphi2Dn7", "l2Wphi2Dn8",
    "l2Wphi2Dn9", "l2Wphi2Dn10", "l2Wphi2Dn11", "l2Wphi2Dn12",
    "l2Bphi2Dn1", "l2Bphi2Dn2", "l2Bphi2Dn3", "l2Bphi2Dn4",
    "l2Bphi2Dn5", "l2Bphi2Dn6", "l2Bphi2Dn7", "l2Bphi2Dn8",
    "q2Gphi2Dn1", "q2Gphi2Dn2", "q2Gphi2Dn3", "q2Gphi2Dn4",
    "q2Gphi2Dn5", "q2Gphi2Dn6", "q2Gphi2Dn7", "q2Gphi2Dn8",
    "q2Wphi2Dn1", "q2Wphi2Dn2", "q2Wphi2Dn3", "q2Wphi2Dn4",
    "q2Wphi2Dn5", "q2Wphi2Dn6", "q2Wphi2Dn7", "q2Wphi2Dn8",
    "q2Wphi2Dn9", "q2Wphi2Dn10", "q2Wphi2Dn11", "q2Wphi2Dn12",
    "q2Bphi2Dn1", "q2Bphi2Dn2", "q2Bphi2Dn3", "q2Bphi2Dn4",
    "q2Bphi2Dn5", "q2Bphi2Dn6", "q2Bphi2Dn7", "q2Bphi2Dn8",
    (* class 16 - psi^2 X H D^2 *)
    "leWHD2n1", "leWHD2n2", "leWHD2n3",
    "leBHD2n1", "leBHD2n2", "leBHD2n3",
    "quGHD2n1", "quGHD2n2", "quGHD2n3",
    "quWHD2n1", "quWHD2n2", "quWHD2n3",
    "quBHD2n1", "quBHD2n2", "quBHD2n3",
    "qdGHD2n1", "qdGHD2n2", "qdGHD2n3",
    "qdWHD2n1", "qdWHD2n2", "qdWHD2n3",
    "qdBHD2n1", "qdBHD2n2", "qdBHD2n3",
    (* class 17 - psi^2 H^3 D^2 *)
    "lephi3D2n1", "lephi3D2n2", "lephi3D2n3",
    "lephi3D2n4", "lephi3D2n5", "lephi3D2n6",
    "quphi3D2n1", "quphi3D2n2", "quphi3D2n3",
    "quphi3D2n4", "quphi3D2n5", "quphi3D2n6",
    "qdphi3D2n1", "qdphi3D2n2", "qdphi3D2n3",
    "qdphi3D2n4", "qdphi3D2n5", "qdphi3D2n6"};

SMEFT$Dim8TwoFermionBLVOperators  = {};

SMEFT$Dim8FourLeptonOperators = {
    (* class 18 *)
    "l4phi2n1",   (* LL LL *)
    "l4phi2n2",   (* LL LL *)
    "e4phi2",     (* RR RR *)
    "l2e2phi2n1", (* LL RR *)
    "l2e2phi2n2", (* LL RR *)
    "l2e2phi2n3", (* LR LR *)
    (* class 19 *)
    "l4Wn1",      (* LL LL *)
    "l2e2Wn1",    (* LL RR *)
    (* class 20 *)
    "l3eHDn1"
};

SMEFT$Dim8FourQuarkOperators = {
    (* class 18 *)
    "q4phi2n1",   (* LL LL *)
    "q4phi2n2",   (* LL LL *)
    "q4phi2n3",   (* LL LL *)
    "q4phi2n5",   (* LL LL *)
    "u4phi2",     (* RR RR *)
    "d4phi2",     (* RR RR *)
    "u2d2phi2n1", (* RR RR *)
    "u2d2phi2n2", (* RR RR *)
    "q2u2phi2n1", (* LL RR *)
    "q2u2phi2n2", (* LL RR *)
    "q2u2phi2n3", (* LL RR *)
    "q2u2phi2n4", (* LL RR *)
    "q2d2phi2n1", (* LL RR *)
    "q2d2phi2n2", (* LL RR *)
    "q2d2phi2n3", (* LL RR *)
    "q2d2phi2n4", (* LL RR *)
    "q2udphi2n1", (* LR LR *)
    "q2udphi2n2", (* LR LR *)
    "q2udphi2n3", (* LR LR *)
    "q2udphi2n4", (* LR LR *)
    "q2u2phi2n5", (* LR LR *)
    "q2u2phi2n6", (* LR LR *)
    "q2d2phi2n5", (* LR LR *)
    "q2d2phi2n6", (* LR LR *)
    "q2udphi2n5", (* LR RL *)
    "q2udphi2n6", (* LR RL *)
    (* class 19 *)
    "u4Gn1",      (* RR RR *)
    "q2u2Gn5",    (* LL RR *)
    "q2udGn1"     (* LR LR *)
};

SMEFT$Dim8TwoQuarkTwoLeptonOperators = {
    (* class 18 *)
    "leqdphi2n1", (* LR RL *)
    "leqdphi2n2", (* LR RL *)
    "l2udphi2",   (* LR RL *)
    "lequphi2n5", (* LR RL *)
    "l2q2phi2n1", (* LL LL *)
    "l2q2phi2n2", (* LL LL *)
    "l2q2phi2n3", (* LL LL *)
    "l2q2phi2n4", (* LL LL *)
    "l2q2phi2n5", (* LL LL *)
    "e2u2phi2",   (* RR RR *)
    "e2d2phi2",   (* RR RR *)
    "l2u2phi2n1", (* LL RR *)
    "l2u2phi2n2", (* LL RR *)
    "l2d2phi2n1", (* LL RR *)
    "l2d2phi2n2", (* LL RR *)
    "q2e2phi2n1", (* LL RR *)
    "q2e2phi2n2", (* LL RR *)
    "lequphi2n1", (* LR LR *)
    "lequphi2n2", (* LR LR *)
    "lequphi2n3", (* LR LR *)
    "lequphi2n4", (* LR LR *)
    "leqdphi2n3", (* LR LR *)
    "leqdphi2n4", (* LR LR *)
    (* class 19 *)
    "ledqGn1",    (* LR RL *)
    (* class 21 *)
    "leqdD2n1",
    "leqdD2n2"
};

SMEFT$Dim8FourFermionBLVOperators = {
    (* class 18 *)
     "lqudphi2n1",
     "lqudphi2n2",
     "eq2uphi2",
     "lq3phi2n1",
     "lq3phi2n2",
     "eu2dphi2",
     "lq3phi2n3",
     "lqu2phi2",
     "lqd2phi2",
     "eq2dphi2"
    (* class 19 *)
    (* class 20 *)
    (* class 21 *)
};


SMEFT$Dim8BLVMessengers = {};

(* *************************************************** *)
(*   lists of dim 5, dim 6 and bosonic dim 8 operators *)
(*   are complete, do not edit                         *)
(* *************************************************** *)

(* dim 5 level *)
SMEFT$Dim5TwoFermionBLVOperators  = {"vv"};

(* dim 6 level *)
SMEFT$Dim6BosonicOperators = { "G", "Gtilde", "W", "Wtilde", "phi",
 "phiBox", "phiD", "phiW", "phiB", "phiWB", "phiWtilde", "phiBtilde",
 "phiWtildeB", "phiGtilde", "phiG" };

SMEFT$Dim6TwoFermionOperators = { "ephi", "dphi", "uphi", "eW",
 "eB", "uG", "uW", "uB", "dG", "dW", "dB", "phil1", "phil3", "phie",
 "phiq1", "phiq3", "phiu", "phid", "phiud" };

(* sub-classes of 4-fermion operators *)
SMEFT$Dim6FourLeptonOperators = {"ll", "ee", "le"};

SMEFT$Dim6FourQuarkOperators = {"qq1", "qq3", "uu", "dd", "ud1",
"ud8", "qu1", "qu8", "qd1", "qd8", "quqd1", "quqd8"};

SMEFT$Dim6TwoQuarkTwoLeptonOperators = {"lq1", "lq3", "eu", "ed",
"lu", "ld", "qe", "ledq", "lequ1", "lequ3"};

SMEFT$Dim6FourFermionBLVOperators = {"duq", "qqu", "qqq", "duu",
"duq3", "qqu3", "qqq3", "duu3", "ll3"};

SMEFT$Dim6BLVMessengers = {"xduq", "xqqu", "xqqq", "xduu", "xll"};

(* bosonic dim8 operators *)

SMEFT$Dim8BosonicOperators = {"phi8", "phi6Box", "phi6D2", "G2phi4n1",
"G2phi4n2", "W2phi4n1", "W2phi4n2", "W2phi4n3", "W2phi4n4",
"WBphi4n1", "WBphi4n2", "B2phi4n1", "B2phi4n2", "G4n1", "G4n2",
"G4n3", "G4n4", "G4n5", "G4n6", "G4n7", "G4n8", "G4n9", "W4n1",
"W4n2", "W4n3", "W4n4", "W4n5", "W4n6", "B4n1", "B4n2", "B4n3",
"G3Bn1", "G3Bn2", "G3Bn3", "G3Bn4", "G2W2n1", "G2W2n2", "G2W2n3",
"G2W2n4", "G2W2n5", "G2W2n6", "G2W2n7", "G2B2n1", "G2B2n2", "G2B2n3",
"G2B2n4", "G2B2n5", "G2B2n6", "G2B2n7", "W2B2n1", "W2B2n2", "W2B2n3",
"W2B2n4", "W2B2n5", "W2B2n6", "W2B2n7", "phi4D4n1", "phi4D4n2",
"phi4D4n3", "G3phi2n1", "G3phi2n2", "W3phi2n1", "W3phi2n2",
"W2Bphi2n1", "W2Bphi2n2", "G2phi2D2n1", "G2phi2D2n2", "G2phi2D2n3",
"W2phi2D2n1", "W2phi2D2n2", "W2phi2D2n3", "W2phi2D2n4", "W2phi2D2n5",
"W2phi2D2n6", "WBphi2D2n1", "WBphi2D2n2", "WBphi2D2n3", "WBphi2D2n4",
"WBphi2D2n5", "WBphi2D2n6", "B2phi2D2n1", "B2phi2D2n2", "B2phi2D2n3",
"Wphi4D2n1", "Wphi4D2n2", "Wphi4D2n3", "Wphi4D2n4", "Bphi4D2n1",
"Bphi4D2n2"};

(* joint lists and special subclasses, not user-editable *)

SMEFT$Dim5FermionicOperators   =       SMEFT$Dim5TwoFermionBLVOperators;

SMEFT$Dim5Operators            =       SMEFT$Dim5FermionicOperators;

SMEFT$Dim6FourFermionOperators = Join[ SMEFT$Dim6FourLeptonOperators,
                                       SMEFT$Dim6FourQuarkOperators,
                                       SMEFT$Dim6TwoQuarkTwoLeptonOperators ];

SMEFT$Dim6FermionicOperators   = Join[ SMEFT$Dim6TwoFermionOperators,
                                       SMEFT$Dim6FourFermionOperators ];

SMEFT$Dim6Operators            = Join[ SMEFT$Dim6BosonicOperators,
                                       SMEFT$Dim6FermionicOperators,
                                       SMEFT$Dim6FourFermionBLVOperators];

SMEFT$Dim8FourFermionOperators = Join[ SMEFT$Dim8FourLeptonOperators,
                                       SMEFT$Dim8FourQuarkOperators,
                                       SMEFT$Dim8TwoQuarkTwoLeptonOperators ];

SMEFT$Dim8FermionicOperators   = Join[ SMEFT$Dim8TwoFermionOperators,
                                       SMEFT$Dim8FourFermionOperators ];

SMEFT$Dim8Operators            = Join[ SMEFT$Dim8BosonicOperators,
                                       SMEFT$Dim8FermionicOperators,
                                       SMEFT$Dim8FourFermionBLVOperators ];

SMEFT$FourFermionBLVOperators  = Join[ SMEFT$Dim6FourFermionBLVOperators,
                                       SMEFT$Dim8FourFermionBLVOperators ];

SMEFT$BosonicOperators         = Join[ SMEFT$Dim6BosonicOperators,
                                       SMEFT$Dim8BosonicOperators ];

SMEFT$FermionicOperators       = Join[ SMEFT$Dim6FermionicOperators,
                                       SMEFT$Dim8FermionicOperators ];

SMEFT$TwoFermionicOperators    = Join[ SMEFT$Dim5TwoFermionBLVOperators,
                                       SMEFT$Dim6TwoFermionOperators,
                                       SMEFT$Dim8TwoFermionOperators ];

SMEFT$FourFermionicOperators   = Join[ SMEFT$Dim6FourFermionOperators,
                                       SMEFT$Dim6FourFermionBLVOperators,
                                       SMEFT$Dim8FourFermionOperators,
                                       SMEFT$Dim8FourFermionBLVOperators ];

SMEFT$FourQuarkOperators       = Join[ SMEFT$Dim6FourQuarkOperators,
                                       SMEFT$Dim8FourQuarkOperators ];

SMEFT$FourLeptonOperators      = Join[ SMEFT$Dim6FourLeptonOperators,
                                       SMEFT$Dim8FourLeptonOperators ];

SMEFT$TwoQuarkTwoLeptonOperators = Join[ SMEFT$Dim6TwoQuarkTwoLeptonOperators,
                                         SMEFT$Dim8TwoQuarkTwoLeptonOperators ];

SMEFT$AllOperators             = Join[ SMEFT$Dim5Operators,
                                       SMEFT$Dim6Operators,
                                       SMEFT$Dim8Operators ];

SMEFT$BLVMessengers            = Join[ SMEFT$Dim6BLVMessengers, SMEFT$Dim8BLVMessengers ];

SMEFT$OperatorList = {};

(* special bosonic subclasses *)
GaugeBilinearOperators = { "phi", "phiBox", "phiD", "phiW",
"phiWtilde", "phiB", "phiBtilde", "phiWB", "phiWtildeB", "phiG",
"phiGtilde" };

GaugeBilinearOperators8 = { "phi8", "phi6Box", "phi6D2", "G2phi4n1",
"G2phi4n2", "W2phi4n1", "W2phi4n2", "W2phi4n3", "W2phi4n4",
"WBphi4n1", "WBphi4n2", "B2phi4n1", "B2phi4n2" };

GaugeTripleOperators = {"G", "Gtilde", "W", "Wtilde"};

GaugeQuadrupleOperators = {"G4n1", "G4n2", "G4n3", "G4n4", "G4n5",
"G4n6", "G4n7", "G4n8", "G4n9", "W4n1", "W4n2", "W4n3", "W4n4",
"W4n5", "W4n6", "B4n1", "B4n2", "B4n3", "G3Bn1", "G3Bn2", "G3Bn3",
"G3Bn4", "G2W2n1", "G2W2n2", "G2W2n3", "G2W2n4", "G2W2n5", "G2W2n6",
"G2W2n7", "G2B2n1", "G2B2n2", "G2B2n3", "G2B2n4", "G2B2n5", "G2B2n6",
"G2B2n7", "W2B2n1", "W2B2n2", "W2B2n3", "W2B2n4", "W2B2n5", "W2B2n6",
"W2B2n7", "B2phi2D2n1", "B2phi2D2n2", "B2phi2D2n3", "Bphi4D2n1",
"Bphi4D2n2", "G2phi2D2n1", "G2phi2D2n2", "G2phi2D2n3", "G3phi2n1",
"G3phi2n2", "phi4D4n1", "phi4D4n2", "phi4D4n3", "W2Bphi2n1", "W2Bphi2n2",
"W2phi2D2n1", "W2phi2D2n2", "W2phi2D2n3", "W2phi2D2n4", "W2phi2D2n5",
"W2phi2D2n6", "W3phi2n1", "W3phi2n2", "WBphi2D2n1", "WBphi2D2n2",
"WBphi2D2n3", "WBphi2D2n4", "WBphi2D2n5", "WBphi2D2n6", "Wphi4D2n1",
"Wphi4D2n2", "Wphi4D2n3", "Wphi4D2n4"};

(* special fermionic sub-classes - 2 fermion operators contributing to fermion masses *)
TwoFermionMassOperators  = {"ephi",  "uphi",  "dphi"};
TwoFermionMassOperators8 = {"lephi5", "quphi5", "qdphi5"};

(* special fermionic sub-classes - 2 fermion NOT operators contributing to fermion masses *)
TwoFermionOperators  = DeleteElements[ SMEFT$Dim6TwoFermionOperators,
                                       TwoFermionMassOperators ];
TwoFermionOperators8 = DeleteElements[ SMEFT$Dim8TwoFermionOperators,
                                       TwoFermionMassOperators8 ];

(* assigns expansion order to NP=1 or 2 to dim6 and dim8 operators *)
Module[{np1,np2,np3,i},
(*np1 = Rule @@@ Transpose[ SMEFT$Dim5Operators,
                            Table[1/2, {i, 1, Length[SMEFT$Dim5Operators]} ] ];*)
(* temporarily NP=1 for Cvv, fix later? *)
np1 = Rule @@@ Transpose[ {SMEFT$Dim5Operators,
                           Table[1, {i, 1, Length[SMEFT$Dim5Operators]} ]} ];
np2 = Rule @@@ Transpose[ {SMEFT$Dim6Operators,
                           Table[1, {i, 1, Length[SMEFT$Dim6Operators]} ]} ];
np3 = Rule @@@ Transpose[ {SMEFT$Dim8Operators,
                           Table[2, {i, 1, Length[SMEFT$Dim8Operators]} ]} ];
SMEFT$NPOrder= Association[ Join[ np1, np2, np3 ] ];
];

(* translation of WC names to WCxf JSON format *)

JSONName = { "vv"->"llphiphi", "duq"->"duql", "qqu"->"qque",
   "qqq"->"qqql", "duu"->"duue" };

(* symmetrization of fermionic WC's. Following D. Straub notation of WC "classes":

Class      Type
0          Scalar object
1          2F general 3x3 matrix
                ["uphi", "dphi", "ephi", "eW", "eB", "uG", "uW", "uB", "dG", "dW", "dB",
                 "phiud"]
2          2F Hermitian matrix
                ["phil1", "phil3", "phie", "phiq1", "phiq3", "phiu", "phid",]
3          2F symmetric matrix
                ["llphiphi"]
4          4F two identical ffbar currents
                ["ll", "qq1", "qq3", "uu", "dd"]
5          4F two independent ffbar currents
                ["lq1", "lq3", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1",
                 "qd1", "qu8", "qd8"]
6          4F two identical ffbar currents - special case ["ee"]
7          4F Baryon-number-violating - special case ["qque"]
8          4F Baryon-number-violating - special case ["qqql"]
9          4F general 3x3x3x3 object
                ["ledq", "quqd1", "quqd8", "lequ1", "lequ3", "duql", "duue"]

Collected below: indices of non-redundant tensorial fermionic
WC's. Last element in each sublist - False for complex and True for
real entries *)

TensorInd = Table[0,{i,1,9}];
TensorInd[[1]] = {{1, 1, False}, {1, 2, False}, {1, 3, False},
		  {2, 1, False}, {2, 2, False}, {2, 3, False},
		  {3, 1, False}, {3, 2, False}, {3, 3, False}};
TensorInd[[2]] = {{1, 1, True},  {1, 2, False}, {1, 3, False},
		  {2, 2, True},  {2, 3, False}, {3, 3, True}};
TensorInd[[3]] = {{1, 1, False}, {2, 2, False}, {3, 3, False}};
TensorInd[[4]] = {
   {1, 1, 1, 1, True},  {1, 1, 1, 2, False}, {1, 1, 1, 3, False},
   {1, 1, 2, 2, True},  {1, 1, 2, 3, False}, {1, 1, 3, 3, True},
   {1, 2, 1, 2, False}, {1, 2, 1, 3, False}, {1, 2, 2, 1, True},
   {1, 2, 2, 2, False}, {1, 2, 2, 3, False}, {1, 2, 3, 1, False},
   {1, 2, 3, 2, False}, {1, 2, 3, 3, False}, {1, 3, 1, 3, False},
   {1, 3, 2, 2, False}, {1, 3, 2, 3, False}, {1, 3, 3, 1, True},
   {1, 3, 3, 2, False}, {1, 3, 3, 3, False}, {2, 2, 2, 2, True},
   {2, 2, 2, 3, False}, {2, 2, 3, 3, True},  {2, 3, 2, 3, False},
   {2, 3, 3, 2, True},  {2, 3, 3, 3, False}, {3, 3, 3, 3, True}};
TensorInd[[5]] = {
   {1, 1, 1, 1, True},  {1, 1, 1, 2, False}, {1, 1, 1, 3, False},
   {1, 1, 2, 2, True},  {1, 1, 2, 3, False}, {1, 1, 3, 3, True},
   {1, 2, 1, 1, False}, {1, 2, 1, 2, False}, {1, 2, 1, 3, False},
   {1, 2, 2, 1, False}, {1, 2, 2, 2, False}, {1, 2, 2, 3, False},
   {1, 2, 3, 1, False}, {1, 2, 3, 2, False}, {1, 2, 3, 3, False},
   {1, 3, 1, 1, False}, {1, 3, 1, 2, False}, {1, 3, 1, 3, False},
   {1, 3, 2, 1, False}, {1, 3, 2, 2, False}, {1, 3, 2, 3, False},
   {1, 3, 3, 1, False}, {1, 3, 3, 2, False}, {1, 3, 3, 3, False},
   {2, 2, 1, 1, True},  {2, 2, 1, 2, False}, {2, 2, 1, 3, False},
   {2, 2, 2, 2, True},  {2, 2, 2, 3, False}, {2, 2, 3, 3, True},
   {2, 3, 1, 1, False}, {2, 3, 1, 2, False}, {2, 3, 1, 3, False},
   {2, 3, 2, 1, False}, {2, 3, 2, 2, False}, {2, 3, 2, 3, False},
   {2, 3, 3, 1, False}, {2, 3, 3, 2, False}, {2, 3, 3, 3, False},
   {3, 3, 1, 1, True},  {3, 3, 1, 2, False}, {3, 3, 1, 3, False},
   {3, 3, 2, 2, True},  {3, 3, 2, 3, False}, {3, 3, 3, 3, True}};
TensorInd[[6]] = {
   {1, 1, 1, 1, True},  {1, 1, 1, 2, False}, {1, 1, 1, 3, False},
   {1, 1, 2, 2, True},  {1, 1, 2, 3, False}, {1, 1, 3, 3, True},
   {1, 2, 1, 2, False}, {1, 2, 1, 3, False}, {1, 2, 2, 2, False},
   {1, 2, 2, 3, False}, {1, 2, 3, 2, False}, {1, 2, 3, 3, False},
   {1, 3, 1, 3, False}, {1, 3, 2, 3, False}, {1, 3, 3, 3, False},
   {2, 2, 2, 2, True},  {2, 2, 2, 3, False}, {2, 2, 3, 3, True},
   {2, 3, 2, 3, False}, {2, 3, 3, 3, False}, {3, 3, 3, 3, True}};
TensorInd[[7]] = {
   {1, 1, 1, 1, False}, {1, 1, 1, 2, False}, {1, 1, 1, 3, False},
   {1, 1, 2, 1, False}, {1, 1, 2, 2, False}, {1, 1, 2, 3, False},
   {1, 1, 3, 1, False}, {1, 1, 3, 2, False}, {1, 1, 3, 3, False},
   {1, 2, 1, 1, False}, {1, 2, 1, 2, False}, {1, 2, 1, 3, False},
   {1, 2, 2, 1, False}, {1, 2, 2, 2, False}, {1, 2, 2, 3, False},
   {1, 2, 3, 1, False}, {1, 2, 3, 2, False}, {1, 2, 3, 3, False},
   {1, 3, 1, 1, False}, {1, 3, 1, 2, False}, {1, 3, 1, 3, False},
   {1, 3, 2, 1, False}, {1, 3, 2, 2, False}, {1, 3, 2, 3, False},
   {1, 3, 3, 1, False}, {1, 3, 3, 2, False}, {1, 3, 3, 3, False},
   {2, 2, 1, 1, False}, {2, 2, 1, 2, False}, {2, 2, 1, 3, False},
   {2, 2, 2, 1, False}, {2, 2, 2, 2, False}, {2, 2, 2, 3, False},
   {2, 2, 3, 1, False}, {2, 2, 3, 2, False}, {2, 2, 3, 3, False},
   {2, 3, 1, 1, False}, {2, 3, 1, 2, False}, {2, 3, 1, 3, False},
   {2, 3, 2, 1, False}, {2, 3, 2, 2, False}, {2, 3, 2, 3, False},
   {2, 3, 3, 1, False}, {2, 3, 3, 2, False}, {2, 3, 3, 3, False},
   {3, 3, 1, 1, False}, {3, 3, 1, 2, False}, {3, 3, 1, 3, False},
   {3, 3, 2, 1, False}, {3, 3, 2, 2, False}, {3, 3, 2, 3, False},
   {3, 3, 3, 1, False}, {3, 3, 3, 2, False}, {3, 3, 3, 3, False}};
TensorInd[[8]] = {
   {1, 1, 1, 1, False}, {1, 1, 1, 2, False}, {1, 1, 1, 3, False},
   {1, 1, 2, 1, False}, {1, 1, 2, 2, False}, {1, 1, 2, 3, False},
   {1, 1, 3, 1, False}, {1, 1, 3, 2, False}, {1, 1, 3, 3, False},
   {1, 2, 1, 1, False}, {1, 2, 1, 2, False}, {1, 2, 1, 3, False},
   {1, 2, 2, 1, False}, {1, 2, 2, 2, False}, {1, 2, 2, 3, False},
   {1, 2, 3, 1, False}, {1, 2, 3, 2, False}, {1, 2, 3, 3, False},
   {1, 3, 1, 1, False}, {1, 3, 1, 2, False}, {1, 3, 1, 3, False},
   {1, 3, 2, 1, False}, {1, 3, 2, 2, False}, {1, 3, 2, 3, False},
   {1, 3, 3, 1, False}, {1, 3, 3, 2, False}, {1, 3, 3, 3, False},
   {2, 1, 2, 1, False}, {2, 1, 2, 2, False}, {2, 1, 2, 3, False},
   {2, 1, 3, 1, False}, {2, 1, 3, 2, False}, {2, 1, 3, 3, False},
   {2, 2, 2, 1, False}, {2, 2, 2, 2, False}, {2, 2, 2, 3, False},
   {2, 2, 3, 1, False}, {2, 2, 3, 2, False}, {2, 2, 3, 3, False},
   {2, 3, 1, 1, False}, {2, 3, 1, 2, False}, {2, 3, 1, 3, False},
   {2, 3, 2, 1, False}, {2, 3, 2, 2, False}, {2, 3, 2, 3, False},
   {2, 3, 3, 1, False}, {2, 3, 3, 2, False}, {2, 3, 3, 3, False},
   {3, 1, 3, 1, False}, {3, 1, 3, 2, False}, {3, 1, 3, 3, False},
   {3, 2, 3, 1, False}, {3, 2, 3, 2, False}, {3, 2, 3, 3, False},
   {3, 3, 3, 1, False}, {3, 3, 3, 2, False}, {3, 3, 3, 3, False}};
TensorInd[[9]] = {
   {1, 1, 1, 1, False}, {1, 1, 1, 2, False}, {1, 1, 1, 3, False},
   {1, 1, 2, 1, False}, {1, 1, 2, 2, False}, {1, 1, 2, 3, False},
   {1, 1, 3, 1, False}, {1, 1, 3, 2, False}, {1, 1, 3, 3, False},
   {1, 2, 1, 1, False}, {1, 2, 1, 2, False}, {1, 2, 1, 3, False},
   {1, 2, 2, 1, False}, {1, 2, 2, 2, False}, {1, 2, 2, 3, False},
   {1, 2, 3, 1, False}, {1, 2, 3, 2, False}, {1, 2, 3, 3, False},
   {1, 3, 1, 1, False}, {1, 3, 1, 2, False}, {1, 3, 1, 3, False},
   {1, 3, 2, 1, False}, {1, 3, 2, 2, False}, {1, 3, 2, 3, False},
   {1, 3, 3, 1, False}, {1, 3, 3, 2, False}, {1, 3, 3, 3, False},
   {2, 1, 1, 1, False}, {2, 1, 1, 2, False}, {2, 1, 1, 3, False},
   {2, 1, 2, 1, False}, {2, 1, 2, 2, False}, {2, 1, 2, 3, False},
   {2, 1, 3, 1, False}, {2, 1, 3, 2, False}, {2, 1, 3, 3, False},
   {2, 2, 1, 1, False}, {2, 2, 1, 2, False}, {2, 2, 1, 3, False},
   {2, 2, 2, 1, False}, {2, 2, 2, 2, False}, {2, 2, 2, 3, False},
   {2, 2, 3, 1, False}, {2, 2, 3, 2, False}, {2, 2, 3, 3, False},
   {2, 3, 1, 1, False}, {2, 3, 1, 2, False}, {2, 3, 1, 3, False},
   {2, 3, 2, 1, False}, {2, 3, 2, 2, False}, {2, 3, 2, 3, False},
   {2, 3, 3, 1, False}, {2, 3, 3, 2, False}, {2, 3, 3, 3, False},
   {3, 1, 1, 1, False}, {3, 1, 1, 2, False}, {3, 1, 1, 3, False},
   {3, 1, 2, 1, False}, {3, 1, 2, 2, False}, {3, 1, 2, 3, False},
   {3, 1, 3, 1, False}, {3, 1, 3, 2, False}, {3, 1, 3, 3, False},
   {3, 2, 1, 1, False}, {3, 2, 1, 2, False}, {3, 2, 1, 3, False},
   {3, 2, 2, 1, False}, {3, 2, 2, 2, False}, {3, 2, 2, 3, False},
   {3, 2, 3, 1, False}, {3, 2, 3, 2, False}, {3, 2, 3, 3, False},
   {3, 3, 1, 1, False}, {3, 3, 1, 2, False}, {3, 3, 1, 3, False},
   {3, 3, 2, 1, False}, {3, 3, 2, 2, False}, {3, 3, 2, 3, False},
   {3, 3, 3, 1, False}, {3, 3, 3, 2, False}, {3, 3, 3, 3, False}};

(* operator classes including flavor rotations for 2- and 4-fermion operators *)

SMEFT$ScalarWC = Join[ GaugeBilinearOperators, GaugeBilinearOperators8,
                       GaugeTripleOperators, GaugeQuadrupleOperators ];

(* SMEFT$TensorWC attributes in order: operator name,
1st/2nd(/3rd/4th) fermion chirality, , is it B or L violating?, Straub
class number.

Rotations are named VXY, X is the name of fermion (L,U,D), Y is its
chirality (L,R) *)

SMEFT$TensorWC = {
              (* dim5 *)
              {"vv",         {VVL,VVL},True,3},
	      (* dim6 2-fermion *)
	      {"ephi",       {VLL,VLR},False,1},
              {"dphi",       {VDL,VDR},False,1},
              {"uphi",       {VUL,VUR},False,1},
              {"eW",         {VLL,VLR},False,1},
              {"eB",         {VLL,VLR},False,1},
              {"uG",         {VUL,VUR},False,1},
              {"uW",         {VUL,VUR},False,1},
              {"uB",         {VUL,VUR},False,1},
              {"dG",         {VDL,VDR},False,1},
              {"dW",         {VDL,VDR},False,1},
              {"dB",         {VDL,VDR},False,1},
              {"phil1",      {VLL,VLL},False,2},
              {"phil3",      {VLL,VLL},False,2},
              {"phie",       {VLR,VLR},False,2},
              {"phiq1",      {VDL,VDL},False,2},
              {"phiq3",      {VDL,VDL},False,2},
              {"phiu",       {VUR,VUR},False,2},
              {"phid",       {VDR,VDR},False,2},
              {"phiud",      {VUR,VDR},False,1},
              (* dim 6 4-fermion *)
	      {"ll",         {VLL,VLL,VLL,VLL},False,4},
              {"qq1",        {VDL,VDL,VDL,VDL},False,4},
              {"qq3",        {VDL,VDL,VDL,VDL},False,4},
              {"lq1",        {VLL,VLL,VDL,VDL},False,5},
              {"lq3",        {VLL,VLL,VDL,VDL},False,5},
              {"ee",         {VLR,VLR,VLR,VLR},False,6},
              {"uu",         {VUR,VUR,VUR,VUR},False,4},
              {"dd",         {VDR,VDR,VDR,VDR},False,4},
              {"eu",         {VLR,VLR,VUR,VUR},False,5},
              {"ed",         {VLR,VLR,VDR,VDR},False,5},
              {"ud1",        {VUR,VUR,VDR,VDR},False,5},
              {"ud8",        {VUR,VUR,VDR,VDR},False,5},
              {"le",         {VLL,VLL,VLR,VLR},False,5},
              {"lu",         {VLL,VLL,VUR,VUR},False,5},
              {"ld",         {VLL,VLL,VDR,VDR},False,5},
              {"qe",         {VDL,VDL,VLR,VLR},False,5},
              {"qu1",        {VDL,VDL,VUR,VUR},False,5},
              {"qu8",        {VDL,VDL,VUR,VUR},False,5},
              {"qd1",        {VDL,VDL,VDR,VDR},False,5},
              {"qd8",        {VDL,VDL,VDR,VDR},False,5},
              {"ledq",       {VLL,VLR,VDR,VDL},False,9},
              {"quqd1",      {VDL,VUR,VDL,VDR},False,9},
              {"quqd8",      {VDL,VUR,VDL,VDR},False,9},
              {"lequ1",      {VLL,VLR,VDL,VUR},False,9},
              {"lequ3",      {VLL,VLR,VDL,VUR},False,9},
              (* triple vertices for Majorana neutrinos *)
              {"duq",        {VDR,VUR,VDL,VLL},True,9},
              {"qqu",        {VDL,VDL,VUR,VLR},True,7},
              {"qqq",        {VDL,VDL,VDL,VLL},True,8},
              {"duu",        {VDR,VUR,VUR,VLR},True,9},
              {"duq3",       {VDR,VUR,VDL,VLL},True,9},
              {"qqu3",       {VDL,VDL,VUR,VLR},True,7},
              {"qqq3",       {VDL,VDL,VDL,VLL},True,8},
              {"duu3",       {VDR,VUR,VUR,VLR},True,9},
              {"ll3",        {VLL,VLL,VLL,VLL},False,4},
              (* dim8 2-fermion *)
              (* class 9 *)
	      {"leG2phin1",  {VLL,VLR},False,1},
	      {"leG2phin2",  {VLL,VLR},False,1},
	      {"leW2phin1",  {VLL,VLR},False,1},
	      {"leW2phin2",  {VLL,VLR},False,1},
	      {"leW2phin3",  {VLL,VLR},False,1},
	      {"quG2phin1",  {VUL,VUR},False,1},
	      {"quG2phin2",  {VUL,VUR},False,1},
	      {"quG2phin3",  {VUL,VUR},False,1},
	      {"quG2phin4",  {VUL,VUR},False,1},
	      {"quG2phin5",  {VUL,VUR},False,1},
	      {"quGWphin1",  {VUL,VUR},False,1},
	      {"quGWphin2",  {VUL,VUR},False,1},
	      {"quGWphin3",  {VUL,VUR},False,1},
	      {"quGBphin1",  {VUL,VUR},False,1},
	      {"quGBphin2",  {VUL,VUR},False,1},
	      {"quGBphin3",  {VUL,VUR},False,1},
	      {"quW2phin1",  {VUL,VUR},False,1},
	      {"quW2phin2",  {VUL,VUR},False,1},
	      {"quW2phin3",  {VUL,VUR},False,1},
	      {"quWBphin1",  {VUL,VUR},False,1},
	      {"quWBphin2",  {VUL,VUR},False,1},
	      {"quWBphin3",  {VUL,VUR},False,1},
	      {"quB2phin1",  {VUL,VUR},False,1},
	      {"quB2phin2",  {VUL,VUR},False,1},
	      (* class 9 - second column *)
	      {"leWBphin1",  {VLL,VLR},False,1},
	      {"leWBphin2",  {VLL,VLR},False,1},
	      {"leWBphin3",  {VLL,VLR},False,1},
	      {"leB2phin1",  {VLL,VLR},False,1},
	      {"leB2phin2",  {VLL,VLR},False,1},
	      {"qdG2phin1",  {VDL,VDR},False,1},
	      {"qdG2phin2",  {VDL,VDR},False,1},
	      {"qdG2phin3",  {VDL,VDR},False,1},
	      {"qdG2phin4",  {VDL,VDR},False,1},
	      {"qdG2phin5",  {VDL,VDR},False,1},
	      {"qdGWphin1",  {VDL,VDR},False,1},
	      {"qdGWphin2",  {VDL,VDR},False,1},
	      {"qdGWphin3",  {VDL,VDR},False,1},
	      {"qdGBphin1",  {VDL,VDR},False,1},
	      {"qdGBphin2",  {VDL,VDR},False,1},
	      {"qdGBphin3",  {VDL,VDR},False,1},
	      {"qdW2phin1",  {VDL,VDR},False,1},
	      {"qdW2phin2",  {VDL,VDR},False,1},
	      {"qdW2phin3",  {VDL,VDR},False,1},
	      {"qdWBphin1",  {VDL,VDR},False,1},
	      {"qdWBphin2",  {VDL,VDR},False,1},
	      {"qdWBphin3",  {VDL,VDR},False,1},
	      {"qdB2phin1",  {VDL,VDR},False,1},
	      {"qdB2phin2",  {VDL,VDR},False,1},
              (* class 10 *)
              {"leWphi3n1",  {VLL,VLR},False,1},
              {"leWphi3n2",  {VLL,VLR},False,1},
              {"leBphi3",    {VLL,VLR},False,1},
              {"quGphi3",    {VUL,VUR},False,1},
              {"quWphi3n1",  {VUL,VUR},False,1},
              {"quWphi3n2",  {VUL,VUR},False,1},
              {"quBphi3",    {VUL,VUR},False,1},
              {"qdGphi3",    {VDL,VDR},False,1},
              {"qdWphi3n1",  {VDL,VDR},False,1},
              {"qdWphi3n2",  {VDL,VDR},False,1},
              {"qdBphi3",    {VDL,VDR},False,1},
              (* class 11 *)
              {"l2phi2D3n1", {VLL,VLL},False,2},
              {"l2phi2D3n2", {VLL,VLL},False,2},
              {"l2phi2D3n3", {VLL,VLL},False,2},
              {"l2phi2D3n4", {VLL,VLL},False,2},
              {"e2phi2D3n1", {VLR,VLR},False,2},
              {"e2phi2D3n2", {VLR,VLR},False,2},
              {"q2phi2D3n1", {VDL,VDL},False,2},
              {"q2phi2D3n2", {VDL,VDL},False,2},
              {"q2phi2D3n3", {VDL,VDL},False,2},
              {"q2phi2D3n4", {VDL,VDL},False,2},
              {"u2phi2D3n1", {VUR,VUR},False,2},
              {"u2phi2D3n2", {VUR,VUR},False,2},
              {"d2phi2D3n1", {VDR,VDR},False,2},
              {"d2phi2D3n2", {VDR,VDR},False,2},
              {"udphi2D3",   {VUR,VDR},False,1},
              (* class 12 *)
	      {"lephi5",     {VLL,VLR},False,1},
              {"qdphi5",     {VDL,VDR},False,1},
              {"quphi5",     {VUL,VUR},False,1},
              (* class 13 *)
              {"l2phi4Dn1",  {VLL,VLL},False,2},
              {"l2phi4Dn2",  {VLL,VLL},False,2},
              {"l2phi4Dn3",  {VLL,VLL},False,2},
              {"l2phi4Dn4",  {VLL,VLL},False,2},
              {"e2phi4D",    {VLR,VLR},False,2},
              {"q2phi4Dn1",  {VDL,VDL},False,2},
              {"q2phi4Dn2",  {VDL,VDL},False,2},
              {"q2phi4Dn3",  {VDL,VDL},False,2},
              {"q2phi4Dn4",  {VDL,VDL},False,2},
              {"u2phi4D",    {VUR,VUR},False,2},
              {"d2phi4D",    {VDR,VDR},False,2},
              {"udphi4D",    {VUR,VDR},False,1},
              (* class 14 - hadronic, first column *)
              {"q2G2Dn1",    {VDL,VDL},False,2},
              {"q2G2Dn2",    {VDL,VDL},False,2},
              {"q2G2Dn3",    {VDL,VDL},False,2},
              {"q2W2Dn1",    {VDL,VDL},False,2},
              {"q2W2Dn2",    {VDL,VDL},False,2},
              {"q2B2D",      {VDL,VDL},False,2},
              {"u2G2Dn1",    {VUR,VUR},False,2},
              {"u2G2Dn2",    {VUR,VUR},False,2},
              {"u2G2Dn3",    {VUR,VUR},False,2},
              {"u2W2D",      {VUR,VUR},False,2},
              {"u2B2D",      {VUR,VUR},False,2},
              {"d2G2Dn1",    {VDR,VDR},False,2},
              {"d2G2Dn2",    {VDR,VDR},False,2},
              {"d2G2Dn3",    {VDR,VDR},False,2},
              {"d2W2D",      {VDR,VDR},False,2},
              {"d2B2D",      {VDR,VDR},False,2},
              (* class 14 - hadronic, second column *)
              {"q2G2Dn4",    {VDL,VDL},False,2},
              {"q2G2Dn5",    {VDL,VDL},False,2},
              {"q2GWDn1",    {VDL,VDL},False,2},
              {"q2GWDn2",    {VDL,VDL},False,2},
              {"q2GWDn3",    {VDL,VDL},False,2},
              {"q2GWDn4",    {VDL,VDL},False,2},
              {"q2GBDn1",    {VDL,VDL},False,2},
              {"q2GBDn2",    {VDL,VDL},False,2},
              {"q2GBDn3",    {VDL,VDL},False,2},
              {"q2GBDn4",    {VDL,VDL},False,2},
              {"q2W2Dn3",    {VDL,VDL},False,2},
              {"q2W2Dn4",    {VDL,VDL},False,2},
              {"q2WBDn1",    {VDL,VDL},False,2},
              {"q2WBDn2",    {VDL,VDL},False,2},
              {"q2WBDn3",    {VDL,VDL},False,2},
              {"q2WBDn4",    {VDL,VDL},False,2},
              {"u2G2Dn4",    {VUR,VUR},False,2},
              {"u2G2Dn5",    {VUR,VUR},False,2},
              {"u2GBDn1",    {VUR,VUR},False,2},
              {"u2GBDn2",    {VUR,VUR},False,2},
              {"u2GBDn3",    {VUR,VUR},False,2},
              {"u2GBDn4",    {VUR,VUR},False,2},
              {"d2G2Dn4",    {VDR,VDR},False,2},
              {"d2G2Dn5",    {VDR,VDR},False,2},
              {"d2GBDn1",    {VDR,VDR},False,2},
              {"d2GBDn2",    {VDR,VDR},False,2},
              {"d2GBDn3",    {VDR,VDR},False,2},
              {"d2GBDn4",    {VDR,VDR},False,2},
              (* class 14 - leptonic *)
              {"l2G2D",      {VLL,VLL},False,2},
              {"l2W2Dn1",    {VLL,VLL},False,2},
              {"l2W2Dn2",    {VLL,VLL},False,2},
              {"l2W2Dn3",    {VLL,VLL},False,2},
              {"l2W2Dn4",    {VLL,VLL},False,2},
              {"l2B2D",      {VLL,VLL},False,2},
              {"l2WBDn1",    {VLL,VLL},False,2},
              {"l2WBDn2",    {VLL,VLL},False,2},
              {"l2WBDn3",    {VLL,VLL},False,2},
              {"l2WBDn4",    {VLL,VLL},False,2},
              {"e2G2D",      {VLR,VLR},False,2},
              {"e2W2D",      {VLR,VLR},False,2},
              {"e2B2D",      {VLR,VLR},False,2},
              (* class 15 - (RR) X phi^2 D *)
              {"e2Wphi2Dn1",   {VLR,VLR},False,2},
              {"e2Wphi2Dn2",   {VLR,VLR},False,2},
              {"e2Wphi2Dn3",   {VLR,VLR},False,2},
              {"e2Wphi2Dn4",   {VLR,VLR},False,2},
              {"e2Bphi2Dn1",   {VLR,VLR},False,2},
              {"e2Bphi2Dn2",   {VLR,VLR},False,2},
              {"e2Bphi2Dn3",   {VLR,VLR},False,2},
              {"e2Bphi2Dn4",   {VLR,VLR},False,2},
              {"u2Gphi2Dn1",   {VUR,VUR},False,2},
              {"u2Gphi2Dn2",   {VUR,VUR},False,2},
              {"u2Gphi2Dn3",   {VUR,VUR},False,2},
              {"u2Gphi2Dn4",   {VUR,VUR},False,2},
              {"u2Wphi2Dn1",   {VUR,VUR},False,2},
              {"u2Wphi2Dn2",   {VUR,VUR},False,2},
              {"u2Wphi2Dn3",   {VUR,VUR},False,2},
              {"u2Wphi2Dn4",   {VUR,VUR},False,2},
              {"u2Bphi2Dn1",   {VUR,VUR},False,2},
              {"u2Bphi2Dn2",   {VUR,VUR},False,2},
              {"u2Bphi2Dn3",   {VUR,VUR},False,2},
              {"u2Bphi2Dn4",   {VUR,VUR},False,2},
              {"d2Gphi2Dn1",   {VDR,VDR},False,2},
              {"d2Gphi2Dn2",   {VDR,VDR},False,2},
              {"d2Gphi2Dn3",   {VDR,VDR},False,2},
              {"d2Gphi2Dn4",   {VDR,VDR},False,2},
              {"d2Wphi2Dn1",   {VDR,VDR},False,2},
              {"d2Wphi2Dn2",   {VDR,VDR},False,2},
              {"d2Wphi2Dn3",   {VDR,VDR},False,2},
              {"d2Wphi2Dn4",   {VDR,VDR},False,2},
              {"d2Bphi2Dn1",   {VDR,VDR},False,2},
              {"d2Bphi2Dn2",   {VDR,VDR},False,2},
              {"d2Bphi2Dn3",   {VDR,VDR},False,2},
              {"d2Bphi2Dn4",   {VDR,VDR},False,2},
              {"udGphi2n1",    {VUR,VDR},False,1},
              {"udGphi2n2",    {VUR,VDR},False,1},
              {"udWphi2n1",    {VUR,VDR},False,1},
              {"udWphi2n2",    {VUR,VDR},False,1},
              {"udBphi2n1",    {VUR,VDR},False,1},
              {"udBphi2n2",    {VUR,VDR},False,1},
              (* class 15 - (LL) X phi^2 D *)
              {"l2Wphi2Dn1",   {VLL,VLL},False,2},
              {"l2Wphi2Dn2",   {VLL,VLL},False,2},
              {"l2Wphi2Dn3",   {VLL,VLL},False,2},
              {"l2Wphi2Dn4",   {VLL,VLL},False,2},
              {"l2Wphi2Dn5",   {VLL,VLL},False,2},
              {"l2Wphi2Dn6",   {VLL,VLL},False,2},
              {"l2Wphi2Dn7",   {VLL,VLL},False,2},
              {"l2Wphi2Dn8",   {VLL,VLL},False,2},
              {"l2Wphi2Dn9",   {VLL,VLL},False,2},
              {"l2Wphi2Dn10",  {VLL,VLL},False,2},
              {"l2Wphi2Dn11",  {VLL,VLL},False,2},
              {"l2Wphi2Dn12",  {VLL,VLL},False,2},
              {"l2Bphi2Dn1",   {VLL,VLL},False,2},
              {"l2Bphi2Dn2",   {VLL,VLL},False,2},
              {"l2Bphi2Dn3",   {VLL,VLL},False,2},
              {"l2Bphi2Dn4",   {VLL,VLL},False,2},
              {"l2Bphi2Dn5",   {VLL,VLL},False,2},
              {"l2Bphi2Dn6",   {VLL,VLL},False,2},
              {"l2Bphi2Dn7",   {VLL,VLL},False,2},
              {"l2Bphi2Dn8",   {VLL,VLL},False,2},
              {"q2Gphi2Dn1",   {VDL,VDL},False,2},
              {"q2Gphi2Dn2",   {VDL,VDL},False,2},
              {"q2Gphi2Dn3",   {VDL,VDL},False,2},
              {"q2Gphi2Dn4",   {VDL,VDL},False,2},
              {"q2Gphi2Dn5",   {VDL,VDL},False,2},
              {"q2Gphi2Dn6",   {VDL,VDL},False,2},
              {"q2Gphi2Dn7",   {VDL,VDL},False,2},
              {"q2Gphi2Dn8",   {VDL,VDL},False,2},
              {"q2Wphi2Dn1",   {VDL,VDL},False,2},
              {"q2Wphi2Dn2",   {VDL,VDL},False,2},
              {"q2Wphi2Dn3",   {VDL,VDL},False,2},
              {"q2Wphi2Dn4",   {VDL,VDL},False,2},
              {"q2Wphi2Dn5",   {VDL,VDL},False,2},
              {"q2Wphi2Dn6",   {VDL,VDL},False,2},
              {"q2Wphi2Dn7",   {VDL,VDL},False,2},
              {"q2Wphi2Dn8",   {VDL,VDL},False,2},
              {"q2Wphi2Dn9",   {VDL,VDL},False,2},
              {"q2Wphi2Dn10",  {VDL,VDL},False,2},
              {"q2Wphi2Dn11",  {VDL,VDL},False,2},
              {"q2Wphi2Dn12",  {VDL,VDL},False,2},
              {"q2Bphi2Dn1",   {VDL,VDL},False,2},
              {"q2Bphi2Dn2",   {VDL,VDL},False,2},
              {"q2Bphi2Dn3",   {VDL,VDL},False,2},
              {"q2Bphi2Dn4",   {VDL,VDL},False,2},
              {"q2Bphi2Dn5",   {VDL,VDL},False,2},
              {"q2Bphi2Dn6",   {VDL,VDL},False,2},
              {"q2Bphi2Dn7",   {VDL,VDL},False,2},
              {"q2Bphi2Dn8",   {VDL,VDL},False,2},
              (* class 16 - psi^2 X H D^2 *)
              {"leWHD2n1",   {VLL,VLR},False,1},
              {"leWHD2n2",   {VLL,VLR},False,1},
              {"leWHD2n3",   {VLL,VLR},False,1},
              {"leBHD2n1",   {VLL,VLR},False,1},
              {"leBHD2n2",   {VLL,VLR},False,1},
              {"leBHD2n3",   {VLL,VLR},False,1},
              {"quGHD2n1",   {VUL,VUR},False,1},
              {"quGHD2n2",   {VUL,VUR},False,1},
              {"quGHD2n3",   {VUL,VUR},False,1},
              {"quWHD2n1",   {VUL,VUR},False,1},
              {"quWHD2n2",   {VUL,VUR},False,1},
              {"quWHD2n3",   {VUL,VUR},False,1},
              {"quBHD2n1",   {VUL,VUR},False,1},
              {"quBHD2n2",   {VUL,VUR},False,1},
              {"quBHD2n3",   {VUL,VUR},False,1},
              {"qdGHD2n1",   {VDL,VDR},False,1},
              {"qdGHD2n2",   {VDL,VDR},False,1},
              {"qdGHD2n3",   {VDL,VDR},False,1},
              {"qdWHD2n1",   {VDL,VDR},False,1},
              {"qdWHD2n2",   {VDL,VDR},False,1},
              {"qdWHD2n3",   {VDL,VDR},False,1},
              {"qdBHD2n1",   {VDL,VDR},False,1},
              {"qdBHD2n2",   {VDL,VDR},False,1},
              {"qdBHD2n3",   {VDL,VDR},False,1},
              (* class 17 - psi^2 H^3 D^2 *)
              {"lephi3D2n1", {VLL,VLR},False,1},
              {"lephi3D2n2", {VLL,VLR},False,1},
              {"lephi3D2n3", {VLL,VLR},False,1},
              {"lephi3D2n4", {VLL,VLR},False,1},
              {"lephi3D2n5", {VLL,VLR},False,1},
              {"lephi3D2n6", {VLL,VLR},False,1},
              {"quphi3D2n1", {VUL,VUR},False,1},
              {"quphi3D2n2", {VUL,VUR},False,1},
              {"quphi3D2n3", {VUL,VUR},False,1},
              {"quphi3D2n4", {VUL,VUR},False,1},
              {"quphi3D2n5", {VUL,VUR},False,1},
              {"quphi3D2n6", {VUL,VUR},False,1},
              {"qdphi3D2n1", {VDL,VDR},False,1},
              {"qdphi3D2n2", {VDL,VDR},False,1},
              {"qdphi3D2n3", {VDL,VDR},False,1},
              {"qdphi3D2n4", {VDL,VDR},False,1},
              {"qdphi3D2n5", {VDL,VDR},False,1},
              {"qdphi3D2n6", {VDL,VDR},False,1},
              (* dim8 4-fermion *)
              (* class 18 - (LR)(RL) phi^2 + h.c. *)
              {"leqdphi2n1", {VLL,VLR,VDR,VDL},False,9},
              {"leqdphi2n2", {VLL,VLR,VDR,VDL},False,9},
              {"l2udphi2",   {VLL,VDR,VUR,VLL},False,9},
              {"lequphi2n5", {VLL,VLR,VUR,VUL},False,9},
              {"q2udphi2n5", {VDL,VDR,VUR,VUL},False,9},
              {"q2udphi2n6", {VDL,VDR,VUR,VUL},False,9},
              (* class 18 - (LL)(LL) phi^2 *)
              {"l4phi2n1",   {VLL,VLL,VLL,VLL},False,4},
              {"l4phi2n2",   {VLL,VLL,VLL,VLL},False,9},
              {"q4phi2n1",   {VDL,VDL,VDL,VDL},False,4},
              {"q4phi2n2",   {VDL,VDL,VDL,VDL},False,9},
              {"q4phi2n3",   {VDL,VDL,VDL,VDL},False,4},
              {"l2q2phi2n1", {VLL,VLL,VDL,VDL},False,5},
              {"l2q2phi2n2", {VLL,VLL,VDL,VDL},False,5},
              {"l2q2phi2n3", {VLL,VLL,VDL,VDL},False,5},
              {"l2q2phi2n4", {VLL,VLL,VDL,VDL},False,5},
              {"l2q2phi2n5", {VLL,VLL,VDL,VDL},False,5},
              {"q4phi2n5",   {VDL,VDL,VDL,VDL},False,9},
              (* class 18 - (RR)(RR) phi^2 *)
	      {"e4phi2",     {VLR,VLR,VLR,VLR},False,6},
              {"u4phi2",     {VUR,VUR,VUR,VUR},False,4},
              {"d4phi2",     {VDR,VDR,VDR,VDR},False,4},
              {"e2u2phi2",   {VLR,VLR,VUR,VUR},False,5},
              {"e2d2phi2",   {VLR,VLR,VDR,VDR},False,5},
              {"u2d2phi2n1", {VUR,VUR,VDR,VDR},False,5},
              {"u2d2phi2n2", {VUR,VUR,VDR,VDR},False,5},
              (* class 18 - (LL)(RR) phi^2 *)
              {"l2e2phi2n1", {VLL,VLL,VLR,VLR},False,5},
              {"l2e2phi2n2", {VLL,VLL,VLR,VLR},False,5},
              {"l2u2phi2n1", {VLL,VLL,VUR,VUR},False,5},
              {"l2u2phi2n2", {VLL,VLL,VUR,VUR},False,5},
              {"l2d2phi2n1", {VLL,VLL,VDR,VDR},False,5},
              {"l2d2phi2n2", {VLL,VLL,VDR,VDR},False,5},
              {"q2e2phi2n1", {VDL,VDL,VLR,VLR},False,5},
              {"q2e2phi2n2", {VDL,VDL,VLR,VLR},False,5},
              {"q2u2phi2n1", {VDL,VDL,VUR,VUR},False,5},
              {"q2u2phi2n2", {VDL,VDL,VUR,VUR},False,5},
              {"q2u2phi2n3", {VDL,VDL,VUR,VUR},False,5},
              {"q2u2phi2n4", {VDL,VDL,VUR,VUR},False,5},
              {"q2d2phi2n1", {VDL,VDL,VDR,VDR},False,5},
              {"q2d2phi2n2", {VDL,VDL,VDR,VDR},False,5},
              {"q2d2phi2n3", {VDL,VDL,VDR,VDR},False,5},
              {"q2d2phi2n4", {VDL,VDL,VDR,VDR},False,5},
              (* class 18 - (LR)(LR) phi^2 + h.c. *)
              {"q2udphi2n1", {VUL,VUR,VDL,VDR},False,9},
              {"q2udphi2n2", {VUL,VUR,VDL,VDR},False,9},
              {"q2udphi2n3", {VUL,VUR,VDL,VDR},False,9},
              {"q2udphi2n4", {VUL,VUR,VDL,VDR},False,9},
              {"lequphi2n1", {VLL,VLR,VUL,VUR},False,9},
              {"lequphi2n2", {VLL,VLR,VUL,VUR},False,9},
              {"lequphi2n3", {VLL,VLR,VUL,VUR},False,9},
              {"lequphi2n4", {VLL,VLR,VUL,VUR},False,9},
              {"l2e2phi2n3", {VLL,VLR,VLL,VLR},False,9},
              {"leqdphi2n3", {VLL,VLR,VDL,VDR},False,9},
              {"leqdphi2n4", {VLL,VLR,VDL,VDR},False,9},
              {"q2u2phi2n5", {VUL,VUR,VUL,VUR},False,9},
              {"q2u2phi2n6", {VUL,VUR,VUL,VUR},False,9},
              {"q2d2phi2n5", {VDL,VDR,VDL,VDR},False,9},
              {"q2d2phi2n6", {VDL,VDR,VDL,VDR},False,9},
              (* class 18 BLV *)
              {"lqudphi2n1", {VDR,VUR,VDL,VLL},True,7},
              {"lqudphi2n2", {VDR,VUR,VDL,VLL},True,9},
              {"eq2uphi2",   {VDL,VDL,VUR,VLR},True,9},
              {"lq3phi2n1",  {VDL,VDL,VDL,VLL},True,9},
              {"lq3phi2n2",  {VDL,VDL,VDL,VLL},True,9},
              {"eu2dphi2",   {VDR,VUR,VUR,VLR},True,9},
              {"lq3phi2n3",  {VDL,VDL,VDL,VLL},True,9},
              {"lqu2phi2",   {VLL,VDL,VUR,VUR},True,9},
              {"lqd2phi2",   {VLL,VDL,VDR,VDR},True,9},
              {"eq2dphi2",   {VLR,VDR,VDL,VDL},True,9},
              (* class 19 *)
              {"l4Wn1",      {VLL,VLL,VLL,VLL},False,9},
              {"u4Gn1",      {VUR,VUR,VUR,VUR},False,9},
              {"l2e2Wn1",    {VLL,VLL,VLR,VLR},False,9},
              {"q2u2Gn5",    {VDL,VDL,VUR,VUR},False,9},
              {"q2udGn1",    {VDL,VUR,VDL,VDR},False,9},
              {"ledqGn1",    {VLL,VLR,VDR,VDL},False,9},
              (* class 20 *)
              {"l3eHDn1",    {VLL,VLL,VLL,VLR},False,9},
              (* class 21 *)
              {"leqdD2n1",   {VLL,VLR,VDR,VDL},False,9},
              {"leqdD2n2",   {VLL,VLR,VDR,VDL},False,9}
  };

SMEFT$TensorClass = (#[[1]] -> #[[4]]) & /@ SMEFT$TensorWC;
SMEFT$TensorIndex = Association[ {# -> TensorInd[[# /. SMEFT$TensorClass]]} & /@ SMEFT$TensorWC[[All,1]] ];

(* identities for field and parameter normalizations valid to all
   orders in SMEFT *)
SMEFT$Identities = {AZnorm[Index[SU2W,1],Index[SU2W,2]] -> G1 g1norm/GW/gwnorm AZnorm[Index[SU2W,2],Index[SU2W,2]],
(*AZnorm[Index[SU2W,2],Index[SU2W,1]] ->  (- 2 MZ/G0norm/vev +
    GW gwnorm AZnorm[Index[SU2W,1],Index[SU2W,1]])/G1/g1norm,
 GPnorm -> GW vev/2/MW,*)
                    Wnorm -> 1/gwnorm,
                    Gnorm -> 1/gsnorm};



(* welcome printout *)
SMEFT$WelcomePrint = True;

(* set sign of covariant derivative - do not edit *)
FR$DSign = -1;

(* WC first letter in Warsaw and mass basis *)
SMEFT$WB = "c";
SMEFT$MB = "C";

(* default: no user input scheme defined *)
SMEFT$UserInputInitialization = False;
SMEFT$InputListStatus = False;

(* Expansion order in 1/Lambda^2, default 1 - dim6 terms included. Set
   to 2 for dim6^2 terms added *)
SMEFT$ExpansionOrder = 1;

(* default CKM input scheme *)
SMEFT$CKMInput = "yes";
(* allowed size of CKM corrections, default value below is 20% *)
SMEFT$CKMTreshold = 0.2;

(* default PMNS input scheme *)
SMEFT$PMNSInput = "diagonal";

(* default maximal number of legs in vertices *)
SMEFT$MaxParticles = 6;

(* default: only real parts of model parameters are transferred to UFO output *)
SMEFT$UFORealParameters = True;

