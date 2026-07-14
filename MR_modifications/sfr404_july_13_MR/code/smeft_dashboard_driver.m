(* ::Package:: *)

(* SmeftFR v4.0 dashboard driver *)
(* Reusable front-end helpers for running the existing SmeftFR workflow. *)


SMEFTDashboard::usage =
  "SMEFTDashboard[] opens an interactive Mathematica front end for selecting \
SmeftFR operators, generation options, and export steps.";

SMEFTDashboardDefaultConfig::usage =
  "SMEFTDashboardDefaultConfig[] returns the default configuration Association.";

SMEFTDashboardOperatorGroups::usage =
  "SMEFTDashboardOperatorGroups[] returns implemented operator names grouped \
by dimension and broad class.";

SMEFTPrepareEnvironment::usage =
  "SMEFTPrepareEnvironment[config] loads FeynRules and SmeftFR using the \
paths and version information in config.";

SMEFTRunGeneration::usage =
  "SMEFTRunGeneration[config] runs the model initialization, mass-basis \
generation, Feynman-rule generation, and SmeftFR Mathematica output.";

SMEFTRunInterfaces::usage =
  "SMEFTRunInterfaces[config] reloads the mass-basis output and runs selected \
WCXF, LaTeX, and FeynArts exports.";

SMEFTRunUFO::usage =
  "SMEFTRunUFO[config] reloads the mass-basis output and runs the UFO export.";


ClearAll[
  dashboardRoot,
  lookup,
  loadInGlobal,
  symbolOption,
  boolOption,
  nowMessage,
  knownFeynArtsRiskQ,
  selectedBLVQ,
  optSymbol,
  inferFeynRulesPath,
  SMEFTRunExternal,
  SMEFTRunGenerationExternal,
  SMEFTRunInterfacesExternal,
  SMEFTRunUFOExternal
];

dashboardRoot[] := Module[{input = $InputFileName, nbdir},
  nbdir = If[TrueQ[$Notebooks], NotebookDirectory[], $Failed];
  Which[
    StringQ[input] && input =!= "",
      DirectoryName[DirectoryName[input]],
    StringQ[nbdir],
      nbdir,
    True,
      Directory[]
  ]
];

inferFeynRulesPath[root_] := Module[{dir, candidates},
  dir = Quiet[Check[ExpandFileName[root], Directory[]]];
  candidates = DeleteDuplicates[NestWhileList[DirectoryName, dir, (# =!= DirectoryName[#]) &, 1, 20]];
  FirstCase[
    candidates,
    p_ /; FileExistsQ[FileNameJoin[{p, "FeynRulesPackage.m"}]] :> p,
    "/home/rosiek/FeynRules"
  ]
];

lookup[config_Association, key_, default_] := Lookup[config, key, default];
lookup[_, _, default_] := default;

loadInGlobal[file_String] :=
  Block[
    {
      $Context = "Global`",
      $ContextPath = DeleteDuplicates[Join[{"Global`", "System`"}, $ContextPath]]
    },
    Get[file]
  ];

symbolOption[value_String] := ToExpression[value];
symbolOption[value_] := value;

optSymbol[name_String] := ToExpression[name];

boolOption[value_] := TrueQ[value];

SMEFTRunExternal[config_Association, functionName_String, logName_String, outputKey_String, outputPath_] := Module[
  {root, driver, script, log, code, proc, cfg, output},
  root = lookup[config, "RootPath", dashboardRoot[]];
  driver = FileNameJoin[{root, "code", "smeft_dashboard_driver.m"}];
  If[! FileExistsQ[driver],
    Return[<|"ExitCode" -> -1, "Error" -> "Dashboard driver not found", "Driver" -> driver|>]
  ];
  If[! DirectoryQ[FileNameJoin[{root, "output"}]], CreateDirectory[FileNameJoin[{root, "output"}]]];
  script = FileNameJoin[{$TemporaryDirectory, "smeft_dashboard_" <> functionName <> "_" <>
      StringReplace[DateString[{"Year", "Month", "Day", "Hour", "Minute", "Second"}], ":" -> ""] <> ".m"}];
  log = FileNameJoin[{root, "output", logName}];
  cfg = config;
  output = outputPath;
  code = StringJoin[
    "SetDirectory[", ToString[InputForm[root]], "];\n",
    "Get[", ToString[InputForm[driver]], "];\n",
    functionName, "[", ToString[InputForm[cfg]], "];\n",
    "Print[\"external ", functionName, " finished\"];\n"
  ];
  Export[script, code, "Text"];
  proc = RunProcess[{"wolframscript", "-file", script}, All];
  Export[log, StringJoin[proc["StandardOutput"], "\n", proc["StandardError"]], "Text"];
  <|
    "ExitCode" -> proc["ExitCode"],
    "LogFile" -> log,
    outputKey -> output,
    "OutputExists" -> (proc["ExitCode"] === 0 && FileExistsQ[output])
  |>
];

SMEFTRunGenerationExternal[config_Association] :=
  SMEFTRunExternal[
    config,
    "SMEFTRunGeneration",
    "dashboard_generation.log",
    "OutputFile",
    FileNameJoin[{lookup[config, "RootPath", dashboardRoot[]], "output", "smeft_feynman_rules.m"}]
  ];

SMEFTRunInterfacesExternal[config_Association] :=
  SMEFTRunExternal[
    config,
    "SMEFTRunInterfaces",
    "dashboard_interfaces.log",
    "FeynArtsOutput",
    FileNameJoin[{lookup[config, "RootPath", dashboardRoot[]], "output", "FeynArts", "FeynArts.mod"}]
  ];

SMEFTRunUFOExternal[config_Association] :=
  SMEFTRunExternal[
    config,
    "SMEFTRunUFO",
    "dashboard_ufo.log",
    "UFOOutput",
    FileNameJoin[{lookup[config, "RootPath", dashboardRoot[]], "output", "UFO"}]
  ];

nowMessage[text_] :=
  Print[Style[text, Bold], "  time = ", DateString[{"Hour", ":", "Minute", ":", "Second"}]];

knownFeynArtsRiskQ[ops_List] :=
  Length[Intersection[ops, {
    "leG2phin2", "leW2phin2", "leWBphin2", "leB2phin2",
    "quG2phin2", "quG2phin4", "quGWphin2", "quGBphin2",
    "quW2phin2", "quWBphin2", "quB2phin2",
    "qdG2phin2", "qdG2phin4", "qdGWphin2", "qdGBphin2",
    "qdW2phin2", "qdWBphin2", "qdB2phin2"
  }]] > 0;

selectedBLVQ[selectedByGroup_Association] :=
  AnyTrue[
    Keys[selectedByGroup],
    StringContainsQ[#, "BLV"] && Length[Flatten[{selectedByGroup[#]}]] > 0 &
  ];

SMEFTDashboardDefaultConfig[] := <|
  "RootPath" -> dashboardRoot[],
  "FeynRulesPath" -> Automatic,
  "MajorVersion" -> "4",
  "MinorVersion" -> "03",
  "Operators6" -> {},
  "Operators8" -> {},
  "Gauge" -> "Unitary",
  "ExpansionOrder" -> 2,
  "WCXFInput" -> Automatic,
  "InputScheme" -> "GF",
  "CKMInput" -> "no",
  "PMNSInput" -> "diagonal",
  "MajoranaNeutrino" -> False,
  "MaxParticles" -> 6,
  "MBExpansion" -> "user",
  "Include4Fermion" -> True,
  "IncludeBL4Fermion" -> False,
  "ExportWCXF" -> True,
  "ExportLatex" -> True,
  "ExportFeynArts" -> False,
  "ExportUFO" -> True,
  "UFORealParameters" -> False,
  "UFOOutput" -> Automatic,
  "FeynArtsOutput" -> Automatic
|>;

SMEFTDashboardOperatorGroups[root_: Automatic] := Module[
  {base, vars, groups},
  base = Replace[root, Automatic :> dashboardRoot[]];
  vars = FileNameJoin[{base, "code", "smeft_variables.m"}];
  If[! FileExistsQ[vars],
    Return[<|"Error" -> {"Cannot find code/smeft_variables.m"}|>]
  ];

  Quiet[loadInGlobal[vars]];

  groups = <|
    "Dimension 6 / bosonic" -> Global`SMEFT$Dim6BosonicOperators,
    "Dimension 6 / two fermion" -> Global`SMEFT$Dim6TwoFermionOperators,
    "Dimension 6 / four fermion" -> Global`SMEFT$Dim6FourFermionOperators,
    "Dimension 6 / BLV four fermion" -> Global`SMEFT$Dim6FourFermionBLVOperators,
    "Dimension 8 / bosonic" -> Global`SMEFT$Dim8BosonicOperators,
    "Dimension 8 / two fermion" -> Global`SMEFT$Dim8TwoFermionOperators,
    "Dimension 8 / four fermion" -> Global`SMEFT$Dim8FourFermionOperators,
    "Dimension 8 / BLV four fermion" -> Global`SMEFT$Dim8FourFermionBLVOperators
  |>;

  Map[DeleteDuplicates[ToString /@ Flatten[{#}]] &, groups]
];

SMEFTPrepareEnvironment[config_: <||>] := Module[
  {base, frPath, envPath},
  base = lookup[config, "RootPath", dashboardRoot[]];
  envPath = Environment["FeynRulesPath"];
  frPath = lookup[config, "FeynRulesPath", Automatic];
  frPath = Replace[frPath, {
    "" :> If[StringQ[envPath] && envPath =!= "",
      envPath,
      inferFeynRulesPath[base]
    ],
    Automatic :> If[StringQ[envPath] && envPath =!= "",
      envPath,
      inferFeynRulesPath[base]
    ]
  }];


  Global`SMEFT$MajorVersion = lookup[config, "MajorVersion", "4"];
  Global`SMEFT$MinorVersion = lookup[config, "MinorVersion", "03"];
  Global`$FeynRulesPath = frPath;

  If[$VersionNumber >= 14.0,
    Unprotect[Commutator];
    Unprotect[MatrixSymbol];
    Print[Style[
      "Mathematica v14 note: FeynRules definitions of Commutator and " <>
      "MatrixSymbol may print harmless clash warnings.",
      12, Bold, Red
    ]];
  ];

  frPath = If[StringQ[frPath], StringTrim[frPath], frPath];
  If[! StringQ[frPath] || ! DirectoryQ[frPath],
    Print["FeynRules directory does not exist: ", frPath];
    Abort[]
  ];
  Global`$FeynRulesPath = frPath;
  Global`SMEFT$Path = FileNameJoin[{frPath, "Models", "SMEFT_" <> Global`SMEFT$MajorVersion <> "_" <> Global`SMEFT$MinorVersion}];
  If[! DirectoryQ[Global`SMEFT$Path],
    Print["SmeftFR model directory does not exist: ", Global`SMEFT$Path];
    Abort[]
  ];
  Print["Using FeynRules path: ", Style[Global`$FeynRulesPath, Bold]];
  Print["Using SmeftFR path: ", Style[Global`SMEFT$Path, Bold]];
  Get[FileNameJoin[{Global`$FeynRulesPath, "FeynRules.m"}]];
  loadInGlobal[FileNameJoin[{Global`SMEFT$Path, "code", "smeft_package.m"}]];

  <|"FeynRulesPath" -> Global`$FeynRulesPath, "SMEFTPath" -> Global`SMEFT$Path|>
];

SMEFTRunGeneration[config_Association] := Module[
  {
    paths, cpu, op6, op8, ops, wcxf, initOptions, maxParticles,
    majorana
  },
  paths = SMEFTPrepareEnvironment[config];
  cpu = TimeUsed[];

  op6 = lookup[config, "Operators6", {}];
  op8 = lookup[config, "Operators8", {}];
  ops = Union[op6, op8];
  maxParticles = lookup[config, "MaxParticles", 6];
  majorana = boolOption[lookup[config, "MajoranaNeutrino", False]];

  wcxf = lookup[config, "WCXFInput", Automatic];
  wcxf = Replace[wcxf, Automatic :>
    FileNameJoin[{Global`SMEFT$Path, "definitions", "wcxf_example.json"}]
  ];
  wcxf = Replace[wcxf, "" :>
    FileNameJoin[{Global`SMEFT$Path, "definitions", "wcxf_example.json"}]
  ];

  If[ops === {},
    Print[Style["No SMEFT operators selected. Running SM-only setup.", Darker[Orange]]];
  ];

  nowMessage["Initializing SmeftFR model"];
  initOptions = {
    optSymbol["Operators"] -> ops,
    optSymbol["Gauge"] -> symbolOption[lookup[config, "Gauge", "Unitary"]],
    optSymbol["ExpansionOrder"] -> lookup[config, "ExpansionOrder", 2],
    optSymbol["WCXFInitFile"] -> wcxf,
    optSymbol["InputScheme"] -> lookup[config, "InputScheme", "GF"],
    optSymbol["CKMInput"] -> lookup[config, "CKMInput", "no"],
    optSymbol["PMNSInput"] -> lookup[config, "PMNSInput", "diagonal"],
    optSymbol["MaxParticles"] -> maxParticles
  };
  If[majorana,
    initOptions = Join[initOptions, {optSymbol["MajoranaNeutrino"] -> True}]
  ];

  Global`SMEFTInitializeModel[Sequence @@ initOptions];

  nowMessage["Loading model"];
  Global`SMEFTLoadModel[];

  nowMessage["Finding mass basis"];
  Global`SMEFTFindMassBasis[];
  Print[Style["Mass-basis step completed, elapsed CPU time = ", Bold], TimeUsed[] - cpu];

  nowMessage["Evaluating Feynman rules"];
  Global`SMEFTFeynmanRules[];
  Print[Style["Feynman-rule step completed, elapsed CPU time = ", Bold], TimeUsed[] - cpu];

  nowMessage["Writing Mathematica/FeynRules output"];
  Global`SMEFTOutput[];
  Print[Style["Generation completed, elapsed CPU time = ", Bold], TimeUsed[] - cpu];

  Join[paths, <|"Operators" -> ops, "ElapsedCPUTime" -> TimeUsed[] - cpu|>]
];

SMEFTRunInterfaces[config_Association] := Module[
  {
    paths, cpu, modelFile, expansion, include4, includeBL, faOutput,
    ops, runWCXF, runLatex, runFeynArts, faOptions
  },
  paths = SMEFTPrepareEnvironment[config];
  cpu = TimeUsed[];

  modelFile = FileNameJoin[{Global`SMEFT$Path, "output", "smeft_par_MB.fr"}];
  expansion = lookup[config, "MBExpansion", "user"];
  include4 = boolOption[lookup[config, "Include4Fermion", True]];
  includeBL = boolOption[lookup[config, "IncludeBL4Fermion", False]];
  runWCXF = boolOption[lookup[config, "ExportWCXF", True]];
  runLatex = boolOption[lookup[config, "ExportLatex", True]];
  runFeynArts = boolOption[lookup[config, "ExportFeynArts", False]];
  ops = Union[lookup[config, "Operators6", {}], lookup[config, "Operators8", {}]];

  nowMessage["Loading mass-basis Lagrangian"];
  Global`SMEFTInitializeMB[
    optSymbol["ModelFile"] -> modelFile,
    optSymbol["Expansion"] -> expansion,
    optSymbol["Include4Fermion"] -> include4,
    optSymbol["IncludeBL4Fermion"] -> includeBL
  ];
  Print["Mass-basis Lagrangian loaded, elapsed CPU time = ", TimeUsed[] - cpu];

  If[runWCXF,
    nowMessage["Writing WCXF output"];
    Global`SMEFTToWCXF[
      modelFile,
      FileNameJoin[{Global`SMEFT$Path, "output", "smeft_wcxf_MB.json"}]
    ];
  ];

  If[runLatex,
    nowMessage["Writing LaTeX output"];
    Global`SMEFTToLatex[optSymbol["Expansion"] -> "smeft"];
  ];

  If[runFeynArts,
    If[knownFeynArtsRiskQ[ops],
      Print[Style[
        "Warning: selected operators include dual field-strength structures. " <>
        "FeynArts export may be extremely slow or hang.",
        12, Bold, Red
      ]];
    ];
    nowMessage["Writing FeynArts output"];
    faOutput = lookup[config, "FeynArtsOutput", Automatic];
    faOutput = Replace[faOutput, Automatic :>
      FileNameJoin[{Global`SMEFT$Path, "output", "FeynArts", "FeynArts"}]
    ];
    faOptions = {ToExpression["FeynRules`Output"] -> faOutput};
    If[KeyExistsQ[config, "FeynArtsMaxParticles"],
      faOptions = Join[faOptions, {ToExpression["FeynRules`MaxParticles"] -> config["FeynArtsMaxParticles"]}]
    ];
    ToExpression["FeynRules`WriteFeynArtsOutput"][Global`SMEFT$MBLagrangian, Sequence @@ faOptions];
    Print["Expected FeynArts files:"];
    Print[faOutput <> ".mod  exists: ", FileExistsQ[faOutput <> ".mod"]];
    Print[faOutput <> ".gen  exists: ", FileExistsQ[faOutput <> ".gen"]];
    Print[faOutput <> ".pars exists: ", FileExistsQ[faOutput <> ".pars"]];
  ];

  Print[Style["Interface exports completed, elapsed CPU time = ", Bold], TimeUsed[] - cpu];
  Join[paths, <|"ElapsedCPUTime" -> TimeUsed[] - cpu|>]
];

SMEFTRunUFO[config_Association] := Module[
  {
    paths, cpu, realParameters, modelFile, output, expansion, include4, includeBL
  },
  paths = SMEFTPrepareEnvironment[config];
  cpu = TimeUsed[];

  realParameters = boolOption[lookup[config, "UFORealParameters", False]];
  Global`SMEFT$UFORealParameters = realParameters;

  If[realParameters,
    Print[Style[
      "Only real parts of CKM, PMNS and WC flavor matrices are transferred to UFO.",
      Bold
    ]],
    Print[Style[
      "Complex CKM, PMNS and WC flavor matrices are transferred to UFO.",
      Bold
    ]]
  ];

  modelFile = If[realParameters,
    FileNameJoin[{Global`SMEFT$Path, "output", "smeft_par_MB_real.fr"}],
    FileNameJoin[{Global`SMEFT$Path, "output", "smeft_par_MB_complex.fr"}]
  ];
  Print["UFO parameter mode: ", If[realParameters, "real", "complex"]];
  Print["UFO model file: ", modelFile];
  output = lookup[config, "UFOOutput", Automatic];
  output = Replace[output, Automatic :>
    FileNameJoin[{Global`SMEFT$Path, "output", "UFO"}]
  ];
  expansion = lookup[config, "MBExpansion", "user"];
  include4 = boolOption[lookup[config, "Include4Fermion", True]];
  includeBL = boolOption[lookup[config, "IncludeBL4Fermion", False]];

  nowMessage["Loading mass-basis Lagrangian for UFO"];
  Global`SMEFTInitializeMB[
    optSymbol["ModelFile"] -> modelFile,
    optSymbol["Expansion"] -> expansion,
    optSymbol["Include4Fermion"] -> include4,
    optSymbol["IncludeBL4Fermion"] -> includeBL
  ];

  nowMessage["Writing UFO output"];
  Global`SMEFTToUFO[
    Global`SMEFT$MBLagrangian,
    optSymbol["Output"] -> output,
    optSymbol["CorrectIO"] -> True
  ];

  Print[Style["UFO export completed, elapsed CPU time = ", Bold], TimeUsed[] - cpu];
  Join[paths, <|"UFOOutput" -> output, "ElapsedCPUTime" -> TimeUsed[] - cpu|>]
];

SMEFTDashboard[] := DynamicModule[
  {
    cfg = SMEFTDashboardDefaultConfig[],
    groups,
    selected6 = {},
    selected8 = {},
    selectedGroup = "Dimension 6 / bosonic",
    selectedByGroup = <||>,
    gauge = "Unitary",
    expansionOrder = 2,
    maxParticles = 6,
    inputScheme = "GF",
    ckmInput = "no",
    pmnsInput = "diagonal",
    mbExpansion = "user",
    exportWCXF = True,
    exportLatex = True,
    exportFeynArts = False,
    exportUFO = True,
    ufoReal = False,
    feynRulesPath,
    wcxfInput,
    status = "Idle.",
    lastResult = <||>
  },

  groups = SMEFTDashboardOperatorGroups[cfg["RootPath"]];
  selectedByGroup = AssociationThread[Keys[groups], ConstantArray[{}, Length[groups]]];
  feynRulesPath = Replace[cfg["FeynRulesPath"], Automatic -> inferFeynRulesPath[cfg["RootPath"]]];
  wcxfInput = Replace[cfg["WCXFInput"], Automatic -> ""];

  Panel@Column[{
    Style["SmeftFR dashboard", 20, Bold],
    Style["Prototype front end for the existing SmeftFR two-stage workflow.", 11],

    Grid[{
      {"FeynRules path",
        InputField[Dynamic[feynRulesPath], String, FieldSize -> 55]},
      {"WCXF input",
        InputField[Dynamic[wcxfInput], String, FieldSize -> 55]},
      {"Gauge",
        PopupMenu[Dynamic[gauge], {"Unitary", "Rxi"}]},
      {"Expansion order",
        SetterBar[Dynamic[expansionOrder], {1, 2}]},
      {"MaxParticles",
        SetterBar[Dynamic[maxParticles], {3, 4, 5, 6, 7, 8}]},
      {"Input scheme",
        PopupMenu[Dynamic[inputScheme], {"GF", "AEM"}]},
      {"CKM input",
        PopupMenu[Dynamic[ckmInput], {"no", "yes"}]},
      {"PMNS input",
        PopupMenu[Dynamic[pmnsInput], {"diagonal", "yes", "no"}]}
    }, Alignment -> Left],

    Style["Operator selection", 14, Bold],
    Row[{
      "Group: ",
      PopupMenu[Dynamic[selectedGroup], Keys[groups]]
    }],
    Dynamic@Pane[
      CheckboxBar[
        Dynamic[selectedByGroup[selectedGroup]],
        Lookup[groups, selectedGroup, {}],
        Appearance -> "Vertical"
      ],
      {Automatic, 220},
      Scrollbars -> True
    ],
    Dynamic@If[knownFeynArtsRiskQ[Flatten[Values[selectedByGroup]]] && exportFeynArts,
      Style[
        "Warning: selected dual-field operators are known to be problematic for FeynArts export.",
        Red, Bold
      ],
      ""
    ],

    Style["Exports", 14, Bold],
    Grid[{
      {"Mass-basis expansion", PopupMenu[Dynamic[mbExpansion], {"none", "smeft", "user"}]},
      {"WCXF", Checkbox[Dynamic[exportWCXF]]},
      {"LaTeX", Checkbox[Dynamic[exportLatex]]},
      {"FeynArts", Checkbox[Dynamic[exportFeynArts]]},
      {"UFO", Checkbox[Dynamic[exportUFO]]},
      {"UFO real parameters only", Checkbox[Dynamic[ufoReal]]}
    }, Alignment -> Left],

    Row[{
      Button["Run generation",
        status = "Running generation...";
        selected6 = DeleteDuplicates[Flatten[Values[KeySelect[selectedByGroup, StringStartsQ[#, "Dimension 6"] &]]]];
        selected8 = DeleteDuplicates[Flatten[Values[KeySelect[selectedByGroup, StringStartsQ[#, "Dimension 8"] &]]]];
        cfg = Join[cfg, <|
          "FeynRulesPath" -> feynRulesPath,
          "WCXFInput" -> wcxfInput,
          "Operators6" -> selected6,
          "Operators8" -> selected8,
          "Gauge" -> gauge,
          "ExpansionOrder" -> expansionOrder,
          "MaxParticles" -> maxParticles,
          "InputScheme" -> inputScheme,
          "CKMInput" -> ckmInput,
          "PMNSInput" -> pmnsInput,
          "IncludeBL4Fermion" -> selectedBLVQ[selectedByGroup]
        |>];
        lastResult = SMEFTRunGenerationExternal[cfg];
        status = If[Lookup[lastResult, "ExitCode", -1] === 0 && TrueQ[Lookup[lastResult, "OutputExists", False]], "Generation completed. Log: output/dashboard_generation.log", "Generation failed; see output/dashboard_generation.log."];
        , Method -> "Queued"
      ],
      Spacer[10],
      Button["Run WCXF/LaTeX/FeynArts exports",
        status = "Running interface exports...";
        selected6 = DeleteDuplicates[Flatten[Values[KeySelect[selectedByGroup, StringStartsQ[#, "Dimension 6"] &]]]];
        selected8 = DeleteDuplicates[Flatten[Values[KeySelect[selectedByGroup, StringStartsQ[#, "Dimension 8"] &]]]];
        cfg = Join[cfg, <|
          "FeynRulesPath" -> feynRulesPath,
          "WCXFInput" -> wcxfInput,
          "Operators6" -> selected6,
          "Operators8" -> selected8,
          "MBExpansion" -> mbExpansion,
          "ExportWCXF" -> exportWCXF,
          "ExportLatex" -> exportLatex,
          "ExportFeynArts" -> exportFeynArts,
          "FeynArtsMaxParticles" -> maxParticles,
          "IncludeBL4Fermion" -> selectedBLVQ[selectedByGroup]
        |>];
        lastResult = SMEFTRunInterfacesExternal[cfg];
        status = If[Lookup[lastResult, "ExitCode", -1] === 0 && (!exportFeynArts || TrueQ[Lookup[lastResult, "OutputExists", False]]), "Interface exports completed. Log: output/dashboard_interfaces.log", "Interface exports failed or FeynArts.mod was not produced; see output/dashboard_interfaces.log."];
        , Method -> "Queued"
      ],
      Spacer[10],
      Button["Run UFO export",
        status = "Running UFO export...";
        selected6 = DeleteDuplicates[Flatten[Values[KeySelect[selectedByGroup, StringStartsQ[#, "Dimension 6"] &]]]];
        selected8 = DeleteDuplicates[Flatten[Values[KeySelect[selectedByGroup, StringStartsQ[#, "Dimension 8"] &]]]];
        cfg = Join[cfg, <|
          "FeynRulesPath" -> feynRulesPath,
          "WCXFInput" -> wcxfInput,
          "Operators6" -> selected6,
          "Operators8" -> selected8,
          "MBExpansion" -> mbExpansion,
          "UFORealParameters" -> ufoReal,
          "IncludeBL4Fermion" -> selectedBLVQ[selectedByGroup]
        |>];
        lastResult = SMEFTRunUFOExternal[cfg];
        status = If[Lookup[lastResult, "ExitCode", -1] === 0, "UFO export completed. Log: output/dashboard_ufo.log", "UFO export failed; see output/dashboard_ufo.log."];
        , Method -> "Queued"
      ]
    }],

    Dynamic@Style[status, Bold],
    Dynamic@If[AssociationQ[lastResult] && lastResult =!= <||>,
      Column[(Row[{#[[1]], ": ", #[[2]]}] &) /@ Normal[lastResult]],
      ""
    ]
  }, Spacings -> 1.2]
];
