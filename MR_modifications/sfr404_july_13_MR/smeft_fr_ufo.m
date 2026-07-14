(* SmeftFR v4.0 package *)
(* UFO interface - run smeft_fr_init.m prior to this code! *)

Quiet[Remove["Global`*"]];

SMEFT$MajorVersion      = "4";
SMEFT$MinorVersion      = "04";

(* FeynRules and SmeftFR installation paths - set environment variable
   FeynRulesPath (e.g. in shell: export FeynRulesPath =
   /path/to/FeynRules) or alternatively edit hard-coded path *)

$FeynRulesPath = If [ StringQ[Environment["FeynRulesPath"]] && Environment["FeynRulesPath"] =!= "",
    Environment["FeynRulesPath"]
,
    FileNameJoin[{"/home","rosiek","FeynRules"}]
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

(* initialize time counter *)
CPUTime = TimeUsed[];

(* choose the handling of complex parameters. Default: only real parts
   of parameters are transferred to UFO to speed up calculations *)

SMEFT$UFORealParameters = True;
SMEFT$UFORealParameters = False;

If [SMEFT$UFORealParameters,
  Print[Style["Only real parts of CKM, PMNS and WC flavor matrices are
  transferred to UFO to speed up calculations\nFor calculations of CP
  violating processes, set ", Bold], Style["SMEFT$UFORealParameters =
  False", Bold, Red], Style[" in the header of ", Bold],
  Style["smeft_fr_ufo.m", Bold, Red], Style[" file", Bold]];
,
  Print[Style["Complex values of CKM, PMNS and WC flavor matrices are
  transferred to UFO, allowing to calculate CP violating processes but
  slowing down the calculations.\nTo speed them up, for CP conserving
  processes set ", Bold], Style["SMEFT$UFORealParameters = True",
  Bold, Red], Style[" in the header of ", Bold],
  Style["smeft_fr_ufo.m", Bold, Red], Style[" file", Bold]];
]

SMEFTModelFile = If [ SMEFT$UFORealParameters,
  FileNameJoin[ { SMEFT$Path, "output", "smeft_par_MB_real.fr" } ]
,
  FileNameJoin[ { SMEFT$Path, "output", "smeft_par_MB_complex.fr" } ]
];

(* initialize mass basis model files and Lagrangian Expansion option
   can be "none", "smeft" or "user" *)
SMEFTInitializeMB[ ModelFile -> SMEFTModelFile,
		   Expansion->"user",
		   Include4Fermion->True,
		   IncludeBL4Fermion->True ];

Print["\nMass basis Lagrangian loaded, time = ", TimeUsed[] - CPUTime,"\n"];

(* UFO output *)
SMEFTToUFO[ SMEFT$MBLagrangian,
	    Output -> FileNameJoin[{SMEFT$Path, "output", "UFO"}],
	    CorrectIO -> True ];
Print["\nUFO output generated, time = ", TimeUsed[] - CPUTime,"\n"];

