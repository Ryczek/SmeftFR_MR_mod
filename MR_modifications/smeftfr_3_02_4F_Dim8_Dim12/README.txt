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
  Enable dimension-12 operators for SMEFT studies extending beyond
  the standard dimension-6 and dimension-8 framework.

SPECIFIC OPERATORS:
  This modification includes the dimension-12 operator(s) referenced
  in arXiv:2509.02680 [hep-ph].

IMPLEMENTATION:
  - Added dim-12 operator definitions to the lagrangian/ directory
  - Updated smeft_fr_init.m to handle dimension-12 terms
  - Modified smeft_fr_interfaces.m for proper export of dim-12 operators
  - Ensured consistent EFT expansion and truncation at dim-12

RESEARCH CONTEXT:
  This modification supports the physics analysis presented in
  arXiv:2509.02680. The specific dim-12 operator(s) enable studies
  of higher-dimensional effects in SMEFT phenomenology.

USAGE:
  Follow the standard SmeftFR workflow. The dim-12 operators are
  automatically included in the model generation and Feynman rule
  extraction.

STATUS:
  Research-ready. Tested and validated for the specific operators
  referenced in arXiv:2509.02680.

REFERENCE:
  arXiv:2509.02680 [hep-ph]

