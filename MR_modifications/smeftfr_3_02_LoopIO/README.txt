*****************************************************************
* SmeftFR 3.0 - Feynman rules generator for the Standard Model  *
* Effective Field Theory                                        *
*****************************************************************

AUTHORS: A. Dedes, J. Rosiek, M. Ryczkowski, K. Suxho, L. Trifyllis

Latest version can be downloaded from www.fuw.edu.pl/smeft

Program maintainer: janusz.rosiek@fuw.edu.pl

SmeftFR is distributed under the GPLv3 license

*************************
* PACKAGE INSTALLATION: *
*************************

Running package requires installing Wolfram Mathematica. It has been
tested with Mathematica version 12.1 or later, earlier versions were
reported to have problems running this code.

SmeftFR package works using the FeynRules system.  A recent version
and installation instructions for the FeynRules package can be
downloaded from the address feynrules.irmp.ucl.ac.be.  SmeftFR has
been tested with FeynRules version 2.3.

After installing FeynRules:

1. Create subdirectory Models/SMEFT_3_02 in the main FeynRules
installation directory.

2. Unpack SmefrFR distribution into Models/SMEFT_3_02 subdirectory.

3. Edit the $FeynRulesPath variable at the top of SmeftFR-init.nb and
SmeftFR-interfaces.nb Mathematica notebooks (both files located in
Models/SMEFT_3_02 subdirectory). $FeynRulesPath should be equal to the
absolute path to the main FeynRules installation directory
(e.g. $FeynRulesPath = "/home/rosiek/FeynRules" etc.)

4. Run the SmeftFR-init.nb first to produce the output in Mathematica
format. Quit the Mathematica kernel and run SmeftFR-interfaces.nb in
the new kernel to get the output in other supported formats.

Steps 3 and 4 can be also performed editing and executing in
Mathematica window the text scripts

<< smeft_fr_init.m
<< smeft_fr_interfaces.m

Further user-defined options of the SmeftFR package are described in
the manual.


********************
* PACKAGE CONTENT: *
********************

Models/SMEFT_3_02 subdirectory contains the following files and
subdirectories:

*** SmeftFR-init.nb (smeft_fr_init.m) -- notebook and equivalent text
script generating SMEFT Lagrangian in mass basis and Feynman rules in
Mathematica format.

*** SmeftFR-interfaces.nb (smeft_fr_interfaces.m) -- notebook and
equivalent text script with routines for exporting Feynman rules in
various formats: WCxf, Latex, UFO and FeynArts.

*** SmeftFR_v3.pdf --  package manual in pdf format

*** README.txt -- brief installation instructions

*** code -- subdirectory with package code and utilities

*** lagrangian -- subdirectory with expressions for the SM Lagrangian and
dimension-5, 6 and 8 operators coded in FeynRules format

*** definitions -- subdirectory with templates of SMEFT ``model files''
and example of numerical input for Wilson coefficients in WCxf format

*** output -- subdirectory with dynamically generated ``parameter files''
and output for Feynman rules in various formats, by default
Mathematica, Latex, UFO and FeynArts are generated.


=================================================================
MODIFICATION DESCRIPTION
=================================================================

PURPOSE:
  Enable tracking of loop-generated vs tree-level operators via
  InteractionOrder (IO) tags in FeynRules/UFO exports.

PROBLEM ADDRESSED:
  Standard SMEFT v3.0 does not distinguish between tree-level and
  loop-generated Wilson coefficients in the output. This is needed
  for proper ordering in Monte Carlo tools that use UFO files.

IMPLEMENTATION:
  - Modified code/smeft_io.m to support custom InteractionOrder tags
  - Added ability to flag operators as loop-generated (e.g., CphiG)

WORKFLOW (Manual workaround - see NOTE below):

  1. Run smeftfr_init as usual to generate base model files

  2. Edit the generated .fr parameter files:
     - Go to output/smeft_par_MB.fr and output/smeft_par_WB.fr
     - Add new InteractionOrder definitions at the end:
       
       M$InteractionOrderHierarchy = {{QCD, 4}, {NP, 2}, {QED, 3}, {QL, 1}}
       M$InteractionOrderLimit = {{QCD, 99}, {NP, 1}, {QED, 99}, {QL, 1}}

  3. For each loop-generated Wilson coefficient (e.g., CphiG), update
     its InteractionOrder property:
       
       CphiG == {
         ParameterType    -> External,
         Indices          -> {},
         InteractionOrder -> {{NP,1},{QL,1}},
         Value            -> 0.685863*^-8,
         ComplexParameter -> False,
         TeX              -> Superscript[C, \[Phi]G],
         Description      -> "QphiG WC coefficient"
       }

  4. Save changes and run smeft_fr_interfaces.m with CorrectIO->True

  5. UFO files with correct IO assignments will be generated in
     output/UFO_SmeftFR_LoopIO_v1/

EXAMPLE USE CASE:
  Considering CphiBox (tree-level, NP order) and CphiG (loop-generated,
  needs QL order). The example uses QL as the custom IO tag.

NOTE:
  This is a manual workaround. The process can be automated but
  currently requires hand-editing of .fr files for each model
  generation. For each loop-generated WC of interest, you must
  manually add the appropriate InteractionOrder tag.

STATUS:
  Functional but requires manual intervention. Future versions may
  automate this process.


