(* SmeftFR v3.0 package *)
(* SmeftFR interfaces - run smeft_fr_init.m prior to this code! *)

Quiet[Remove["Global`*"]];

(* hack for Mathematica 14.

   In version 14.3 of Mathematica there is a problem with definitions
   of Commutator and MatrixSymbol in FeynRules, they clash with new
   systemwide definitions. As a workaround, we use additional statement
*)

If[$VersionNumber>=14.0, 
   Unprotect[Commutator];
   Unprotect[MatrixSymbol];
   Print[Style["See comments in smeft_fr_init.m file header on warnings about Commutator and MatrixSymbol in Mathematica 14 version\n\n",12,Bold,Red]];
];

(* resulting Mathematica's warnings should be ignored. To avoid
   suchwarnings, alternatively one can hack two files in
   Feynrules/Core directory:

   Add Unprotect[Commutator] at the beginning of ExtractVertexTools.m
   Add Unprotect[MatrixSymbol] at the beginning of MassDiagonalization.m
*)


(* FeynRules and SmeftFR package installation paths - edit if necessary *)
$FeynRulesPath = FileNameJoin[{"/home","rosiek","FeynRules"}];
SMEFT$MajorVersion      = "3";
SMEFT$MinorVersion      = "03";
SMEFT$Path = FileNameJoin[{$FeynRulesPath, "Models", "SMEFT_" <> 
                SMEFT$MajorVersion <> "_" <> SMEFT$MinorVersion}];
If[ ! DirectoryQ[SMEFT$Path], 
  Print["Directory " <> SMEFT$Path <> "does not exist, please check package setup"];
  Abort[];
];

(* Load FeynRules and SMEFT packages *)
Get[ FileNameJoin[{$FeynRulesPath,"FeynRules.m"}] ];
Get[ FileNameJoin[{ SMEFT$Path, "code", "smeft_package.m"}] ];

(* initialize time counter *)     
CPUTime = TimeUsed[];

(* initialize mass basis model files and Lagrangian
Expansion option can be "none", "smeft" or "user" *)
SMEFTInitializeMB[ Expansion->"user",
		   Include4Fermion->True,
		   IncludeBL4Fermion->False
		 ];
Print["\nMass basis Lagrangian loaded, time = ", TimeUsed[] - CPUTime,"\n"];

(* WCxf output *)
SMEFTToWCXF[ FileNameJoin[ { SMEFT$Path, "output", "smeft_par_MB.fr" } ],
             FileNameJoin[ { SMEFT$Path, "output", "smeft_wcxf_MB.json" } ] ];
Print["\nParameters stored in WCXF file, time = ", TimeUsed[] - CPUTime];

(* Latex output *)
SMEFTToLatex[ Expansion -> "smeft" (*, ScreenOutput->True*) ];
Print["\nLatex output generated, time = ", TimeUsed[] - CPUTime];  

(* UFO output *)
SMEFTToUFO[ SMEFT$MBLagrangian,
	    Output -> FileNameJoin[{SMEFT$Path, "output", "UFO"}],
	    CorrectIO -> True ];
Print["\nUFO output generated, time = ", TimeUsed[] - CPUTime,"\n"];

(* FeynArts output *)
WriteFeynArtsOutput[ SMEFT$MBLagrangian,
		     Output -> FileNameJoin[{SMEFT$Path, "output", "FeynArts", "FeynArts"}] ];
Print["\nVertices stored in FeynArts format in directory ", 
       Style[FileNameJoin[{SMEFT$Path, "output", "FeynArts"}] ,Bold] ];
Print["\nTotal CPU time used = ", TimeUsed[] - CPUTime];



