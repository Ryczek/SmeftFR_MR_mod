(* ::Package:: *)

Quit[]


(* SmeftFR v4.0 package *)
(* main initialization sequence, generation of mass basis Lagrangian
and Feynman rules in Mathematica format *)

Quiet[Remove["Global`*"]];

SMEFT$MajorVersion      = "4";
SMEFT$MinorVersion      = "04";

(*Print[Environment["FeynRulesPath"]];*)

(* FeynRules installation path - set environment variable
   FeynRulesPath (e.g. in shell: export FeynRulesPath =
   /path/to/FeynRules) or alternatively edit hard-coded path *)

(* FeynRules and SmeftFR package installation paths - edit if necessary *)
$FeynRulesPath = FileNameJoin[{"/Users/michalryczkowski/Library/Mathematica/Applications/feynrules-current"}];
SMEFT$Path = FileNameJoin[{"/Users/michalryczkowski/Documents/Programming/GitHub/SmeftFR_MR_mod/MR_modifications/sfr404_july_13_MR"}];
If[ ! DirectoryQ[SMEFT$Path], 
  Print["Directory " <> SMEFT$Path <> "does not exist, please check package setup"];
  Abort[];
];

Get["smeft_directory_check.m"];

(* hack for Mathematica v14 *)

If[$VersionNumber >= 14.0,
   Unprotect[Commutator];
   Unprotect[MatrixSymbol];

   Print[Style["In Mathematica v14 definitions of Commutator and " <>
   "MatrixSymbol in FeynRules clash with systemwide definitions.\n\n" <>
   "Resulting warnings should be ignored. To avoid them, edit files " <>
   "in Feynrules/Core directory adding statements Unprotect[Commutator] " <>
   "at the top of ExtractVertexTools.m and Unprotect[MatrixSymbol] at " <>
   "the top of MassDiagonalization.m\n", 12, Bold, Red]];
];

(* Load FeynRules and SMEFT packages *)
Get[ FileNameJoin[{$FeynRulesPath,"FeynRules.m"}] ];

Get[ FileNameJoin[{ SMEFT$Path, "code", "smeft_package.m"}] ];

(* Choose operators to include, currently implemented are

 Dimension 6:

OpList6 = { "G", "Gtilde", "W", "Wtilde", "phi", "phiBox", "phiD",
 "phiW", "phiB", "phiWB", "phiWtilde", "phiBtilde", "phiWtildeB",
 "phiGtilde", "phiG", "ephi", "dphi", "uphi", "eW", "eB", "uG", "uW",
 "uB", "dG", "dW", "dB", "phil1", "phil3", "phie", "phiq1", "phiq3",
 "phiu", "phid", "phiud", "ll", "qq1", "qq3", "lq1", "lq3", "ee",
 "uu", "dd", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1",
 "qu8", "qd1", "qd8", "ledq", "quqd1", "quqd8", "lequ1", "lequ3",
 "vv", "duq", "qqu", "qqq", "duu" };

Dimension 8 bosonic:

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
 "Wphi4D2n3", "Wphi4D2n4", "Bphi4D2n1", "Bphi4D2n2",

Dimension 8 fermionic dim8 (sample only, "classes" as defined in
2005.00059):

Class 09: "leG2phin1", "leG2phin2", "leW2phin1", "leW2phin2",
          "leW2phin3", "quG2phin1", "quG2phin2", "quG2phin3",
          "quG2phin4", "quG2phin5", "quGWphin1", "quGWphin2",
          "quGWphin3", "quGBphin1", "quGBphin2", "quGBphin3",
          "quW2phin1", "quW2phin2", "quW2phin3", "quWBphin1",
          "quWBphin2", "quWBphin3", "quB2phin1", "quB2phin2",
          "leWBphin1", "leWBphin2", "leWBphin3", "leB2phin1",
          "leB2phin2", "qdG2phin1", "qdG2phin2", "qdG2phin3",
          "qdG2phin4", "qdG2phin5", "qdGWphin1", "qdGWphin2",
          "qdGWphin3", "qdGBphin1", "qdGBphin2", "qdGBphin3",
          "qdW2phin1", "qdW2phin2", "qdW2phin3", "qdWBphin1",
          "qdWBphin2", "qdWBphin3", "qdB2phin1", "qdB2phin2",
Class 10: "leWphi3n1", "leWphi3n2", "leBphi3", "quGphi3",
          "quWphi3n1", "quWphi3n2", "quBphi3", "qdGphi3",
          "qdWphi3n1", "qdWphi3n2", "qdBphi3",
Class 11: "l2phi2D3n1", "l2phi2D3n2", "l2phi2D3n3", "l2phi2D3n4",
          "e2phi2D3n1", "e2phi2D3n2", "q2phi2D3n1", "q2phi2D3n2",
          "q2phi2D3n3", "q2phi2D3n4", "u2phi2D3n1", "u2phi2D3n2",
          "d2phi2D3n1", "d2phi2D3n2", "udphi2D3",
Class 12: "lephi5", "quphi5", "qdphi5",
Class 13: "l2phi4Dn1", "l2phi4Dn2", "l2phi4Dn3", "l2phi4Dn4",
          "e2phi4D", "q2phi4Dn1", "q2phi4Dn2", "q2phi4Dn3",
          "q2phi4Dn4", "u2phi4D", "d2phi4D", "udphi4D",
Class 14: "q2G2Dn1", "q2G2Dn2", "q2G2Dn3", "q2G2Dn4", "q2G2Dn5",
          "q2W2Dn1", "q2W2Dn2", "q2W2Dn3", "q2W2Dn4", "q2B2D",
          "q2GWDn1", "q2GWDn2", "q2GWDn3", "q2GWDn4",
          "q2GBDn1", "q2GBDn2", "q2GBDn3", "q2GBDn4",
          "q2WBDn1", "q2WBDn2", "q2WBDn3", "q2WBDn4",
          "u2G2Dn1", "u2G2Dn2", "u2G2Dn3", "u2G2Dn4", "u2G2Dn5",
          "u2W2D", "u2B2D", "u2GBDn1", "u2GBDn2", "u2GBDn3", "u2GBDn4",
          "d2G2Dn1", "d2G2Dn2", "d2G2Dn3", "d2G2Dn4", "d2G2Dn5",
          "d2W2D", "d2B2D", "d2GBDn1", "d2GBDn2", "d2GBDn3", "d2GBDn4",
          "l2G2D", "l2W2Dn1", "l2W2Dn2", "l2W2Dn3", "l2W2Dn4", "l2B2D",
          "l2WBDn1", "l2WBDn2", "l2WBDn3", "l2WBDn4",
          "e2G2D", "e2W2D", "e2B2D",
Class 15: "e2Wphi2Dn1", "e2Wphi2Dn2", "e2Wphi2Dn3", "e2Wphi2Dn4",
          "e2Bphi2Dn1", "e2Bphi2Dn2", "e2Bphi2Dn3", "e2Bphi2Dn4",
          "u2Gphi2Dn1", "u2Gphi2Dn2", "u2Gphi2Dn3", "u2Gphi2Dn4",
          "u2Wphi2Dn1", "u2Wphi2Dn2", "u2Wphi2Dn3", "u2Wphi2Dn4",
          "u2Bphi2Dn1", "u2Bphi2Dn2", "u2Bphi2Dn3", "u2Bphi2Dn4",
          "d2Gphi2Dn1", "d2Gphi2Dn2", "d2Gphi2Dn3", "d2Gphi2Dn4",
          "d2Wphi2Dn1", "d2Wphi2Dn2", "d2Wphi2Dn3", "d2Wphi2Dn4",
          "d2Bphi2Dn1", "d2Bphi2Dn2", "d2Bphi2Dn3", "d2Bphi2Dn4",
          "udGphi2n1", "udGphi2n2", "udWphi2n1", "udWphi2n2",
          "udBphi2n1", "udBphi2n2",
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
Class 16: "leWHD2n1", "leWHD2n2", "leWHD2n3",
          "leBHD2n1", "leBHD2n2", "leBHD2n3",
          "quGHD2n1", "quGHD2n2", "quGHD2n3",
          "quWHD2n1", "quWHD2n2", "quWHD2n3",
          "quBHD2n1", "quBHD2n2", "quBHD2n3",
          "qdGHD2n1", "qdGHD2n2", "qdGHD2n3",
          "qdWHD2n1", "qdWHD2n2", "qdWHD2n3",
          "qdBHD2n1", "qdBHD2n2", "qdBHD2n3",
Class 17: "lephi3D2n1", "lephi3D2n2", "lephi3D2n3",
          "lephi3D2n4", "lephi3D2n5", "lephi3D2n6",
          "quphi3D2n1", "quphi3D2n2", "quphi3D2n3",
          "quphi3D2n4", "quphi3D2n5", "quphi3D2n6",
          "qdphi3D2n1", "qdphi3D2n2", "qdphi3D2n3",
          "qdphi3D2n4", "qdphi3D2n5", "qdphi3D2n6",
Class 18 BL conserving:
          "leqdphi2n1", "leqdphi2n2", "l2udphi2", "lequphi2n5",
          "q2udphi2n5", "q2udphi2n6",
          "l4phi2n1", "l4phi2n2", "q4phi2n1", "q4phi2n2", "q4phi2n3",
          "l2q2phi2n1", "l2q2phi2n2", "l2q2phi2n3", "l2q2phi2n4",
          "l2q2phi2n5", "q4phi2n5",
          "e4phi2", "u4phi2", "d4phi2", "e2u2phi2", "e2d2phi2",
          "u2d2phi2n1", "u2d2phi2n2",
          "l2e2phi2n1", "l2e2phi2n2", "l2u2phi2n1", "l2u2phi2n2",
          "l2d2phi2n1", "l2d2phi2n2", "q2e2phi2n1", "q2e2phi2n2",
          "q2u2phi2n1", "q2u2phi2n2", "q2u2phi2n3", "q2u2phi2n4",
          "q2d2phi2n1", "q2d2phi2n2", "q2d2phi2n3", "q2d2phi2n4",
          "q2udphi2n1", "q2udphi2n2", "q2udphi2n3", "q2udphi2n4",
          "lequphi2n1", "lequphi2n2", "lequphi2n3", "lequphi2n4",
          "l2e2phi2n3", "leqdphi2n3", "leqdphi2n4",
          "q2u2phi2n5", "q2u2phi2n6", "q2d2phi2n5", "q2d2phi2n6",
Class18 BL violating:
          "lqudphi2n1", "lqudphi2n2", "eq2uphi2", "lq3phi2n1",
          "lq3phi2n2", "eu2dphi2", "lq3phi2n3", "lqu2phi2",
          "lqd2phi2", "eq2dphi2",
Class 19 BL conserving:
          "l4Wn1", "l4Wn2", "q4Gn1", "q4Gn2",
          "q4Gn3", "q4Gn4", "q4Wn1", "q4Wn2", "q4Wn3", "q4Wn4",
          "l2q2Gn1", "l2q2Gn2", "l2q2Gn3", "l2q2Gn4", "l2q2Wn1",
          "l2q2Wn2", "l2q2Wn3", "l2q2Wn4", "l2q2Wn5", "l2q2Wn6",
          "l2q2Bn1", "l2q2Bn2", "l2q2Bn3", "l2q2Bn4", "l4Bn1", "l4Bn2",
          "q4Bn1", "q4Bn2", "q4Bn3", "q4Bn4", "u4Gn1", "u4Gn2", "d4Gn1",
          "d4Gn2", "e2u2Gn1", "e2u2Gn2", "e2u2Bn1", "e2u2Bn2",
          "e2d2Gn1", "e2d2Gn2", "e2d2Bn1", "e2d2Bn2", "u2d2Gn1",
          "u2d2Gn2", "u2d2Gn3", "u2d2Gn4", "u2d2Gn5", "u2d2Gn6",
          "u2d2Gn7", "u2d2Gn8", "u2d2Bn1", "u2d2Bn2", "u2d2Bn3",
          "u2d2Bn4", "e4Bn1", "e4Bn2", "u4Bn1", "u4Bn2", "d4Bn1",
          "d4Bn2", "l2e2Wn1", "l2e2Wn2", "l2e2Bn1", "l2e2Bn2",
          "l2u2Gn1", "l2u2Gn2", "l2u2Wn1", "l2u2Wn2", "l2u2Bn1",
          "l2u2Bn2", "l2d2Gn1", "l2d2Gn2", "l2d2Wn1", "l2d2Wn2",
          "l2d2Bn1", "l2d2Bn2", "q2e2Gn1", "q2e2Gn2", "q2e2Wn1",
          "q2e2Wn2", "q2e2Bn1", "q2e2Bn2", "q2u2Gn1", "q2u2Gn2",
          "q2u2Gn3", "q2u2Gn4", "q2u2Gn5", "q2u2Gn6", "q2u2Gn7",
          "q2u2Gn8", "q2u2Wn1", "q2u2Wn2", "q2u2Wn3", "q2u2Wn4",
          "q2u2Bn1", "q2u2Bn2", "q2u2Bn3", "q2u2Bn4", "q2d2Gn1",
          "q2d2Gn2", "q2d2Gn3", "q2d2Gn4", "q2d2Gn5", "q2d2Gn6",
          "q2d2Gn7", "q2d2Gn8", "q2d2Wn1", "q2d2Wn2", "q2d2Wn3",
          "q2d2Wn4", "q2d2Bn1", "q2d2Bn2", "q2d2Bn3", "q2d2Bn4",
          "ledqGn1", "ledqGn2", "ledqWn1", "ledqWn2", "ledqBn1",
          "ledqBn2", "q2udGn1", "q2udGn2", "q2udGn3", "q2udGn4",
          "q2udGn5", "q2udGn6", "q2udWn1", "q2udWn2", "q2udWn3",
          "q2udBn1", "q2udBn2", "q2udBn3", "lequGn1", "lequGn2",
          "lequGn3", "lequWn1", "lequWn2", "lequWn3", "lequBn1",
          "lequBn2", "lequBn3",
Class 19 BL violating:
          "lqudGn1", "lqudGn2", "lqudGn3",
          "lqudGn4", "lqudWn1", "lqudWn2", "lqudBn1", "lqudBn2",
          "eq2uGn1", "eq2uGn2", "eq2uWn1", "eq2uWn2", "eq2uBn1",
          "eq2uBn2", "lq3Gn1", "lq3Gn2", "lq3Gn3", "lq3Gn4", "lq3Wn1",
          "lq3Wn2", "lq3Wn3", "lq3Bn1", "lq3Bn2", "eu2dGn1", "eu2dGn2",
          "eu2dGn3", "eu2dBn1", "eu2dBn2",
Class 20 BL conserving:
          "l3eHDn1", "l3eHDn2", "l3eHDn3",
          "le3HDn1", "le3HDn2", "leq2HDn1", "leq2HDn2", "leq2HDn3",
          "leq2HDn4", "leq2HDn5", "leq2HDn6", "leu2HDn1", "leu2HDn2",
          "leu2HDn3", "led2HDn1", "led2HDn2", "led2HDn3", "leudHDn1",
          "leudHDn2", "leudHDn3", "l2quHDn1", "l2quHDn2", "l2quHDn3",
          "l2quHDn4", "l2quHDn5", "l2quHDn6", "e2quHDn1", "e2quHDn2",
          "e2quHDn3", "q3uHDn1", "q3uHDn2", "q3uHDn3", "q3uHDn4",
          "q3uHDn5", "q3uHDn6", "qu3HDn1", "qu3HDn2", "qu3HDn3",
          "qud2HDn1", "qud2HDn2", "qud2HDn3", "qud2HDn4", "qud2HDn5",
          "qud2HDn6", "l2qdHDn1", "l2qdHDn2", "l2qdHDn3", "l2qdHDn4",
          "l2qdHDn5", "l2qdHDn6", "e2qdHDn1", "e2qdHDn2", "e2qdHDn3",
          "q3dHDn1", "q3dHDn2", "q3dHDn3", "q3dHDn4", "q3dHDn5",
          "q3dHDn6", "qu2dHDn1", "qu2dHDn2", "qu2dHDn3", "qu2dHDn4",
          "qu2dHDn5", "qu2dHDn6", "qd3HDn1", "qd3HDn2", "qd3HDn3",
Class 20 BL violating:
          "lu2dHDn1", "lu2dHDn2", "lud2HDn1",
          "lud2HDn2", "lq2uHDn1", "lq2uHDn2", "lq2uHDn3", "lq2dHDn1",
          "lq2dHDn2", "lq2dHDn3", "eq3HD", "equ2HDn1", "equ2HDn2",
          "equdHDn1", "equdHDn2", "equdHDn3",
Class 21 BL conserving:
          "leqdD2n1", "leqdD2n2", "l4D2n1",
          "l4D2n2", "q4D2n1", "q4D2n2", "q4D2n3", "q4D2n4", "l2q2D2n1",
          "l2q2D2n2", "l2q2D2n3", "l2q2D2n4", "e4D2", "u4D2n1",
          "u4D2n2", "d4D2n1", "d4D2n2", "e2u2D2n1", "e2u2D2n2",
          "e2d2D2n1", "e2d2D2n2", "u2d2D2n1", "u2d2D2n2", "u2d2D2n3",
          "u2d2D2n4", "l2e2D2n1", "l2e2D2n2", "l2u2D2n1", "l2u2D2n2",
          "l2d2D2n1", "l2d2D2n2", "q2e2D2n1", "q2e2D2n2", "q2u2D2n1",
          "q2u2D2n2", "q2u2D2n3", "q2u2D2n4", "q2d2D2n1", "q2d2D2n2",
          "q2d2D2n3", "q2d2D2n4", "q2udD2n1", "q2udD2n2", "q2udD2n3",
          "lequD2n1", "lequD2n2", "lequD2n3",
Class 21 BL violating:
          "lqudD2n1", "lqudD2n2", "eq2uD2",
          "lq3D2", "eu2dD2n1", "eu2dD2n2"

*)

(* Example of subset of operators (using full list leads to lengthy
calculations (may never end for full dim-8 set)!) *)

OpList6 = {};

OpList8 = {"leWHD2n1"};

OpList = Union[OpList6, OpList8];

(* file with numerical values of SMEFT parameters in WCxf JSON format,
If equal to "wcxf_default.json" or does not exist, all WCs are by
initialized to 0 *)

WCXFInput = FileNameJoin[{SMEFT$Path, "definitions", "wcxf_example.json"}];

(* initialize time counter and calculate Feynman rules, consult manual for full list of options *)
CPUTime = TimeUsed[];
SMEFTInitializeModel[Operators -> OpList,
                     Gauge -> Unitary,
                     ExpansionOrder -> 2,
                     WCXFInitFile -> WCXFInput,
                     InputScheme -> "GF",
                     CKMInput -> "no",
		     MajoranaNeutrino -> False,
		     PMNSInput -> "diagonal",
                     MaxParticles -> 6];


SMEFTLoadModel[];
Print[Style["Lagrangian generation completed, time = ", Bold ], TimeUsed[] - CPUTime];

SMEFTFindMassBasis[];
Print[Style["Transformations to physical basis calculated, time = ", Bold ], TimeUsed[] - CPUTime];

SMEFTFeynmanRules[];
Print[Style["Feynman rules evaluated, time = ", Bold], TimeUsed[] - CPUTime];

SMEFTOutput[];
Print[Style["Output file generated, time = ", Bold], TimeUsed[] - CPUTime];

Abort[];

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
now necessary to Quit[] this session and run smeft_fr_interfaces.m or
smeft_fr_ufo.m in new Mathematica kernel *)




