(* SmeftFR v4.0 package *)
(* check FeynRules and SmeftFR installation paths *)

If[ ! DirectoryQ[$FeynRulesPath],
  Print["Directory " <> $FeynRulesPath <> "does not exist, please check FeynRules package setup"];
  Abort[]
,
  Print[ "Using FeynRules path: ", Style[ $FeynRulesPath, Bold ] ];
];

SMEFT$Path = FileNameJoin[{$FeynRulesPath, "Models", "SMEFT_" <>
                SMEFT$MajorVersion <> "_" <> SMEFT$MinorVersion}];

If[ ! DirectoryQ[SMEFT$Path],
  Print["Directory " <> SMEFT$Path <> "does not exist, please check package setup"];
  Abort[]
,
  Print[ "Using SmeftFR path: ", Style[ SMEFT$Path, Bold ] ];
];

