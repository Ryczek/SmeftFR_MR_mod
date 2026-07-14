(* SmeftFR v4.0 package *)
(* routines for WCxf input/output operations *)


(* make complex WC out of Re and Im in JSON file, scientific notation *)
SMEFTToComplex[x_] := If[NumberQ[x], x, ("Re" + I "Im") /. x ];



SMEFTToWCXF[ SourceFile_, TargetFile_,
	        OptionsPattern[ { FirstLetter -> SMEFT$MB } ] ] :=
(* WCxf JSON export function - reads from SMEFT model file and
   generates Wilson coefficients file in JSON format *)

Module[{il, it, WC, WN, tmp, date, values, output, oplist, stdl,
first, temp, mspar, ActiveS, Active2T, Active4T, ScalarVal,
Tensor2Val, Tensor4Val},

stdl = {"G1", "GW", "GS", "Gf", "vev", "hlambda", "MZ", "MW" , "MH",
  "MQT", "MQC", "MQU", "MQB", "MQS", "MQD", "MLT", "MLM", "MLE",
  "MVT", "MVM", "MVE", "mz", "mw" , "mh", "mqt", "mqc", "mqu", "mqb",
  "mqs", "mqd", "mlt", "mlm", "mle", "mvt", "mvm", "mve", "K", "U",
  "G0norm", "g1norm", "Gnorm", "GPnorm", "gsnorm", "gwnorm", "Hnorm",
  "AZnorm", "Kq", "Lam", "MG0", "MGP", "MgW", "MgZ", "Ul", "Wnorm",
  "xiA", "xiG", "xiW", "xiZ" };

If [ DeleteDuplicates[ (Head[#] & /@ {SourceFile, TargetFile} ) ] != {String},
  Print["File names in SMEFTToWCXF are not of string type, aborting..."];
  Abort[];
];

first = ToString[ OptionValue[FirstLetter] ];
(* first letter in WCs definition *)
If [ StringLength[first] != 1,
  Print["Option FirstLetter in SMEFTToWCXF is not a single character, aborting..."];
  Abort[];
];
	
If [ ! FileExistsQ[ SourceFile ],
  Print["File " <> SourceFile <> " does not exist, check its name and location"];
  Abort[];
];

Get[ SourceFile ];

(* find parameters with "Value" assigned *)
mspar = {};
temp = Value /. Values[ Rule @@@ M$Parameters ];
For[il=1, il < Length[temp] + 1, il++,
  If[ temp[[il]] =!= Value, AppendTo[ mspar, (Rule @@@ M$Parameters)[[il]] ] ];
];

(* find WC names only, skip other parameters *)
temp = Complement[  ToString /@ Keys[mspar], stdl ];
oplist = Intersection[ SMEFT$AllOperators, StringDrop[ temp, 1 ] ];

ActiveS = Intersection[ SMEFT$ScalarWC, oplist ];
ScalarVal = If[ Length[ActiveS] > 0, Value /. (ToExpression[StringInsert[ActiveS, first, 1]] /. mspar), 0 ];

Active2T = Intersection[ SMEFT$TwoFermionicOperators, oplist ];
Tensor2Val = If[ Length[Active2T] > 0, Association[ Flatten[ Value /. (ToExpression[StringInsert[Active2T, first, 1]] /. mspar) ] ], 0 ];

Active4T = Intersection[ SMEFT$FourFermionicOperators, oplist ];
Tensor4Val = If[ Length[Active4T] > 0, Association[ Flatten[ Value /. (ToExpression[StringInsert[Active4T, first, 1]] /. mspar) ] ], {} ];

Print["Wilson coefficients in WCXF format stored as ", Style[ TargetFile, Bold ] ];

output = {};

date = Date[];
AppendTo[ output, "eft" -> "SMEFT" ];
AppendTo[ output, "basis" -> "Warsaw mass" ];
AppendTo[ output, "metadata" -> { "generator" -> " SmeftFR v" <> SMEFT$Version <> ", SMEFTToWCXF routine",
			          "description" -> "Generated from the FeynRules model file " <>
	                           SourceFile <> " on " <> ToString[date[[3]]] <> "." <>
	                           ToString[date[[2]]] <> "." <> ToString[date[[1]]] <> " " <>
	                           ToString[date[[4]]] <> ":" <> ToString[date[[5]]] } ];

(* renormalization scale for WCs currently not defined in SMEFT model files

temp = If [ MemberQ[ Keys[mspar], Lam ], Sqrt[Value /. (Lam /. mspar)], Sqrt[Value] ];
AppendTo[ output, "scale" -> If[ NumberQ[temp], temp, 0 ] ];
*)
AppendTo[ output, "scale" -> 0 ];

values = {};

For[ il=1, il < Length[ActiveS] + 1, il++,
  If[ NumberQ[ ScalarVal[[il]]], AppendTo[ values, (ActiveS[[il]] /. JSONName) -> ScalarVal[[il]] ] ];
];

For[ il=1, il < Length[Active2T] + 1, il++,
  tmp = SMEFT$TensorIndex[ Active2T[[il]] ];
  For[ it=1, it < Length[tmp] + 1, it++,
    WN = (Active2T[[il]] /. JSONName) <> "_" <> ToString[ Row[ tmp[[it, 1;;2]] ] ];
    WC = Tensor2Val[ ToExpression[ first <> Active2T[[il]] ] @@ tmp[[it, 1;;2]] ];
    If[ NumberQ[WC],
      If[ tmp[[it,3]] && NumberQ[WC],
        AppendTo[ values, WN ->  WC];
      ,	
        AppendTo[ values, WN -> {"Re" -> Re[WC], "Im" -> Im[WC]} ];
      ];
    ];
  ];
];

For[ il=1, il < Length[Active4T] + 1, il++,
  tmp = SMEFT$TensorIndex[ Active4T[[il]] ];
  For[ it=1, it < Length[tmp] + 1, it++,
    WN = (Active4T[[il]] /. JSONName) <> "_" <> ToString[ Row[ tmp[[it, 1;;4]] ] ];
    WC = Tensor4Val[ ToExpression[ first <> Active4T[[il]] ] @@ tmp[[it, 1;;4]] ];
    If[ NumberQ[WC],
      If[ tmp[[it,5]],
        AppendTo[ values, WN ->  WC];
      ,	
        AppendTo[ values, WN -> {"Re" -> Re[WC], "Im" -> Im[WC]} ];
      ];
    ];
  ];
];

AppendTo[output, "values" -> values ];
Export[TargetFile, output, "json"];

]
(* end of SMEFTToWCXF *)





ReadWCXFInput[ SourceFile_, OptionsPattern[ { Operators -> SMEFT$AllOperators,
                                              Silent    -> False} ] ] :=
(* WCxf JSON import function - reads from JSON format and generates
   entries describing Wilson coefficients *)
Module[{JSONData, JSONWilson, JSONNum, il, tmp, WC, val, sub, oplist,
ind, ActiveWC},

If[ Head[SourceFile] =!= String, Print["Source file name must be string!"]; Abort[]; ];

If [ ! FileExistsQ[ SourceFile ],
  Print["File " <> SourceFile <> " does not exist, check its name and location"];
  Abort[];
];

If [ FileFormat[ SourceFile ] != "JSON",
  Print["File " <> SourceFile <> " not in JSON format or does not have extension .json or .JSON, please correct!"];
  Abort[];
];

oplist = OptionValue[Operators];
If[ Head[oplist] =!= List, Print["Option 'Operators' must be a list, aborting!"];Abort[];];

If [ OptionValue[Silent] =!= True, Print["Wilson coefficient values initialized from WCxf file ", Style[ SourceFile, Bold ] ] ];
JSONData = Import[ SourceFile ];
JSONWilson = SMEFTToComplex /@ Association["values" /. JSONData];
JSONNum[tmp_] := If[ NumberQ[tmp], tmp, 0];

SMEFT$ScalarVal = ToExpression[SMEFT$MB <> # ] ->
                  JSONNum[ JSONWilson[ # /. JSONName ] ] &
                  /@ Intersection[ SMEFT$ScalarWC, oplist ];

(* all scalar parameters should be real, no complex numbers allowed *)
tmp = False;
If [ ComplexListElementTest[ # /. Rule -> List ],
  tmp = True;
  Print[ "Scalar Wilson coefficient ", Style[#[[1]], Bold], " initialized to complex number."]
] & /@ SMEFT$ScalarVal;

If [ tmp,
  Print[ Style[ "Complex scalar WCs are not allowed, correct values in WCXF input file.  Aborting...", Bold, Red ] ];
  Abort[]
];

(* included 2-fermion WCs *)
ActiveWC = Intersection[ SMEFT$TwoFermionicOperators, oplist ];
SMEFT$Tensor2Par = {};
SMEFT$Tensor2Val = {};
SMEFT$Tensor2Sub = {};
For[ il = 1, il < Length[ActiveWC] + 1, il++,
  WC = ToExpression[ SMEFT$MB <> ActiveWC[[il]] ];
(* list of non-redundant indices for given WC *)
  ind = TensorInd[[ ActiveWC[[il]] /. SMEFT$TensorClass ]][[All,1;;2]];
(* non-redundant numerical values for 2-fermion operators *)
  val = (WC @@ #) -> JSONNum[ JSONWilson[ (ActiveWC[[il]] /. JSONName) <>
        "_" <> StringJoin[ ToString[#1] & /@ # ] ] ] & /@ ind;
(* special case "vv" operator, if present only diagonal entries initialized from WCXF file *)
If [ ActiveWC[[il]] === "vv",
  tmp = (WC @@ # -> 0) & /@ {{1,2},{1,3},{2,3}};
  val = Join[ val, tmp ];
];
(* reality check for WC entries *)
  If [ #[[3]] && ! RealValuedNumberQ[ WC @@ #[[1;;2]] /. val ],
    Print["Entry " <> (ToString /@ #[[1;;2]]), " of matrix " <>
          ToString[WC] <> " must be real!" ];
    Print[ Style["Aborting, correct numerical WC values in WCXF input file!",
                 Red, Bold] ];
    Abort[];
  ] & /@ TensorInd[[ ActiveWC[[il]] /. SMEFT$TensorClass]];
(* list of non redundant WCs *)
  AppendTo[SMEFT$Tensor2Par, ActiveWC[[il]] -> val];
(* add redundant numerical entries and symbolic substitutions *)
  {val,sub} = TensorWCSymmetrize[ val, ActiveWC[[il]] /. SMEFT$TensorClass ];
  AppendTo[SMEFT$Tensor2Val, ActiveWC[[il]] -> val];
  AppendTo[SMEFT$Tensor2Sub, ActiveWC[[il]] -> sub];
];

(* included 4-fermion WCs *)
ActiveWC = Intersection[ SMEFT$FourFermionicOperators, oplist ];
SMEFT$Tensor4Par = {};
SMEFT$Tensor4Val = {};
SMEFT$Tensor4Sub = {};
Tensor4Val = {};
For[ il = 1, il < Length[ActiveWC] + 1, il++,
  WC = ToExpression[ SMEFT$MB <> ActiveWC[[il]] ];
(* list of non-redundant indices for given WC *)
  ind = TensorInd[[ ActiveWC[[il]] /. SMEFT$TensorClass ]][[All,1;;4]];
(* non-redundant numerical values for 4-fermion operators *)
  val = (WC @@ #) -> JSONNum[ JSONWilson[ (ActiveWC[[il]] /. JSONName) <>
        "_" <> StringJoin[ ToString[#1] & /@ # ] ] ] & /@ ind;
(* reality check for WC entries *)
  If [ #[[5]] && ! RealValuedNumberQ[ WC @@ #[[1;;4]] /. val ],
    Print["Entry " <> (ToString /@ #[[1;;4]]), " of matrix " <>
          ToString[WC] <> " must be real!" ];
    Print[ Style["Aborting, correct numerical WC values in WCXF input file!",
                 Red, Bold] ];
    Abort[];
  ] & /@ TensorInd[[ ActiveWC[[il]] /. SMEFT$TensorClass]];
(* list of non redundant WCs *)
  AppendTo[SMEFT$Tensor4Par, ActiveWC[[il]] -> val];
(* add redundant numerical entries and symbolic substitutions *)
  {val,sub} = TensorWCSymmetrize[ val, ActiveWC[[il]] /. SMEFT$TensorClass ];
  AppendTo[SMEFT$Tensor4Val, ActiveWC[[il]] -> val];
  AppendTo[SMEFT$Tensor4Sub, ActiveWC[[il]] -> sub];
];

(* store all WC value substitutions in public variables *)
SMEFT$WCXFSource = SourceFile;
SMEFT$WCValues = Flatten[ Join[ SMEFT$ScalarVal,
                        Values[ SMEFT$Tensor2Val],
                        Values[ SMEFT$Tensor4Val],
                                {Lam->1} ] ];
(* end of ReadWCXFInput *)
]




WCXFToSMEFT[ TargetFile_, OptionsPattern[ { OverwriteTarget -> False,
				            RealParameters -> Default,
                                            Silent -> False} ] ] :=
(* generates SMEFT model file from variables created by reading WCxf input file*)
Module[{date,cfile,TargetExistsQ,wclist,sublist,key,val,aa,bb},

If [ ! MemberQ[ {Default, True, False}, OptionValue[RealParameters] ],
  Print["Option RealParameters of WCXFToSMEFT routine can be only Default, True or False."];
  Abort[];
];

If[ Head[TargetFile] =!= String, Print["WCXFToSMEFT: Target file name must be a string!"]; Abort[]; ];

If [ FileExistsQ[ TargetFile ] && (! OptionValue[OverwriteTarget]),
    Print["File " <> TargetFile <> " exists!"];
    TargetExistsQ = AskFunction[ Ask["Overwrite (y/n)?"-> "String"] ][];
];
If[ TargetExistsQ != "y", Print[ "Change name of parameter file generated from WCXF format and rerun" ]; Abort[]; ];
If [ OptionValue[Silent] =!= True,
  Print["Parameter file in mass basis generated as ",  Style[TargetFile, Bold ] ];
];

cfile = OpenWrite[TargetFile];

WriteLine[cfile, "(* Generated by WCXFToSMEFT routine from the file " <> SMEFT$WCXFSource <> " *)"];
date = Date[];
WriteLine[cfile, "(* " <> ToString[date[[3]]] <> "." <>
    ToString[date[[2]]] <> "." <> ToString[date[[1]]] <> " " <>
    ToString[date[[4]]] <> ":" <> ToString[date[[5]]] <> " *)\n\n"]

WriteLine[cfile, "(* Neutrino status (Dirac or Majorana): *)"];
WriteLine[cfile, "SMEFT$MajoranaNeutrino = " <>
	          ToString[SMEFT$MajoranaNeutrino] <> ";\n\n"];

WriteLine[cfile, "(* Active operators included in Feynman Rules: " <> ToString[SMEFT$OperatorList] <> " *)\n"];

Switch[OptionValue[RealParameters],
    True,  WriteLine[cfile, "(* Parameters in this model file are initialized to real values (imaginary parts are set to 0) for UFO format compatibility *)\n"],
    False, WriteLine[cfile, "(* Complex parameters in this model file are splitted into real and imaginary parts for UFO format compatibility *)\n"],
    _, WriteLine[cfile,""]
];

WriteString[cfile, ReadString[FileNameJoin[{SMEFT$Path, "definitions", "smeft_par_head_MB.fr"}]] ];
WriteLine[cfile, "\n"];

(* add input observables in preferred scheme to fix SM Lagrangian
   parameters; see file smeft_input_parameters.m; all input parameters
   must be real *)

WriteLine[cfile, "(* input observables *)\n"];
wclist = MapAt[Re, SM$InputParameters, {All, 2, 2, 2}] /. Re[aa_] -> aa;
WriteInputParameter[cfile,#] & /@ wclist;

(* SMEFT parametrization *)

(* SM parameters + field normalization constants and their numerical
   values. All quantities are real numbers *)
WriteLine[cfile, "(* SM parametrization and SMEFT field normalization constants *)\n"];
wclist = MapAt[Re, SMEFT$SMParameters, {All, 2, 2, 2}] /. Re[aa_] -> aa;
WriteInputParameter[cfile,#] & /@ wclist;

(* SM mixing angles, CKM *)
WriteLine[cfile, "(* SM CKM matrix *)\n"];
wclist = Value /. (Kq /. (SMEFT$SMMixing /. Equal -> Rule));
If [ OptionValue[RealParameters] === True, wclist = wclist /. Complex[aa_,bb_] -> aa ];
val = MemberQ[ Head /@  Flatten[ wclist /. Rule->List ], Complex ];
wclist = Kq -> wclist;
If[ SMEFT$CKMInput == "diagonal",
  WriteDiagonalMixingEntry[ cfile, wclist ]
,
  If [ OptionValue[RealParameters] === Default,
    WriteMixingEntry[ cfile, wclist ],
    If [ val && (OptionValue[RealParameters] === False),
      WriteComplexCKMEntry[ cfile, wclist ],
      WriteRealMixingEntry[ cfile, wclist ]
    ]
  ]
]

WriteLine[cfile, "(* SM PMNS matrix *)\n"];
wclist = Value /. (Ul /. (SMEFT$SMMixing /. Equal -> Rule));
If [ OptionValue[RealParameters] === True, wclist = wclist /. Complex[aa_,bb_] -> aa ];
val = MemberQ[ Head /@  Flatten[ wclist /. Rule->List ], Complex ];
wclist = Ul -> wclist;
If[ SMEFT$PMNSInput == "diagonal",
  WriteDiagonalMixingEntry[ cfile, wclist ]
,
  If [ OptionValue[RealParameters] === Default,
    WriteMixingEntry[ cfile, wclist ],
    If [ val && (OptionValue[RealParameters] === False),
      WriteComplexPMNSEntry[ cfile, wclist ],
      WriteRealMixingEntry[ cfile, wclist ]
    ]
  ]
]

(* Wilson coefficients, flavor independent *)
WriteLine[cfile, "(* redefined (mass basis) WC coefficients *)\n"];
WriteLine[cfile, "(* flavor independent (all real numbers as WCs of hermitian operators *)\n"];
WriteExternalScalarEntry[ cfile, # ] & /@ SMEFT$ScalarVal;

(* Wilson coefficients, 2-fermion currents *)
WriteLine[cfile, "(* flavor dependent *)\n"];
WriteLine[cfile, "(* 2 fermion operators *)\n"];
If [ OptionValue[RealParameters] === Default,
  WriteExternalTensorEntry[ cfile, #, False ] & /@ SMEFT$Tensor2Val;
,
  wclist  = SMEFT$Tensor2Par;
  sublist = SMEFT$Tensor2Sub;
  If [ OptionValue[RealParameters] === True,
    wclist  = wclist  /. Complex[aa_,bb_] -> aa;
    sublist = sublist /. Conjugate[aa_] -> aa;
  ];
  WriteUFOTensorEntry[ cfile, # /. wclist, # /. sublist, False, OptionValue[RealParameters] ] & /@ Keys[wclist];
];

(* Wilson coefficients, 4-fermion currents *)
WriteLine[cfile, "(* 4 fermion operators *)\n"];
If [ OptionValue[RealParameters] === Default,
  WriteExternalTensorEntry[ cfile, #, True ] & /@ SMEFT$Tensor4Val;
,
  wclist  = SMEFT$Tensor4Par;
  sublist = SMEFT$Tensor4Sub;
  If [ OptionValue[RealParameters] === True,
    wclist  = wclist  /. Complex[aa_,bb_] -> aa;
    sublist = sublist /. Conjugate[aa_] -> aa;
  ];
  WriteUFOTensorEntry[ cfile, # /. wclist, # /. sublist, True, OptionValue[RealParameters] ] & /@ Keys[wclist];
];


WriteLine[cfile, "(* Effective NP scale squared*)\n"];
WriteLine[cfile, "  Lam == {"];
WriteLine[cfile, "    ParameterType -> External,"];
(*
WriteLine[cfile, "    Value   -> " <> NumberToString[ ("scale" /. JSONData)^2 ] <> ","];
*)
WriteLine[cfile, "    Value   -> 1,"];
WriteLine[cfile, "    TeX           -> 1/\[CapitalLambda]^2,"];
WriteLine[cfile, "    Description   -> \"Effective NP scale squared\""];
WriteLine[cfile, "  }\n\n"];

WriteLine[cfile, "}\n"];

(* updates the correct maximal NP and CP interaction orders for model files *)
Get[ FileNameJoin[{SMEFT$Path, "definitions", "smeft_par_io.fr"}] ];
WriteLine[cfile, "M$InteractionOrderHierarchy = ", M$InteractionOrderHierarchy, "\n"];
WriteLine[cfile, "M$InteractionOrderLimit = ", M$InteractionOrderLimit /.
                                  {NP,__} -> {NP,SMEFT$ExpansionOrder} /.
                                  {CP,__} -> {CP,SMEFT$CPMaxOrder}, "\n"];

Close[TargetFile];

]
(* end of WCXFToSMEFT *)
