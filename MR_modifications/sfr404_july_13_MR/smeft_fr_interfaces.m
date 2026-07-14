(* SmeftFR v4.0 package *)
(* WCXF, Latex and FeynArts interfaces - run smeft_fr_init.m prior to
this code! *)

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

SMEFTModelFile = FileNameJoin[ { SMEFT$Path, "output", "smeft_par_MB.fr" } ];

(* initialize mass basis model files and Lagrangian
Expansion option can be "none", "smeft" or "user" *)
SMEFTInitializeMB[ ModelFile -> SMEFTModelFile,
		   Expansion -> "user",
		   Include4Fermion -> True,
		   IncludeBL4Fermion -> True
		 ];
Print["\nMass basis Lagrangian loaded, time = ", TimeUsed[] - CPUTime,"\n"];

(* WCxf output *)
SMEFTToWCXF[ SMEFTModelFile, FileNameJoin[ { SMEFT$Path, "output", "smeft_wcxf_MB.json" } ] ];
Print["\nParameters stored in WCXF file, time = ", TimeUsed[] - CPUTime];

(* Latex output *)
SMEFTToLatex[ Expansion -> "smeft" (*, ScreenOutput->True*) ];
Print["\nLatex output generated, time = ", TimeUsed[] - CPUTime];

(* FeynArts output *)
WriteFeynArtsOutput[ SMEFT$MBLagrangian,
		     Output -> FileNameJoin[{SMEFT$Path, "output", "FeynArts", "FeynArts"}] ];
Print["\nVertices stored in FeynArts format in directory ",
       Style[FileNameJoin[{SMEFT$Path, "output", "FeynArts"}] ,Bold] ];
Print["\nTotal CPU time used = ", TimeUsed[] - CPUTime];



