=================================================================
MR_Modifications: Private SmeftFR v3 Modifications
=================================================================

This directory contains private, research-specific modifications to the
SmeftFR v3.0 package. Each subfolder represents a distinct modification
with its own purpose and scope.

-----------------------------------------------------------------
AVAILABLE MODIFICATIONS
-----------------------------------------------------------------

1. smeftfr_3_02_LoopIO
   - Purpose: Adds InteractionOrder (IO) tracking to distinguish
     loop-generated operators from tree-level operators
   - Key feature: Modified smeft_io.m to support custom IO tags
   - Use case: Enables proper ordering of loop-generated Wilson
     coefficients (e.g., CphiG) in UFO/FeynRules exports
   - Workaround: Requires manual addition of IO definitions to
     generated .fr files before running smeft_fr_interfaces.m
   - Documentation: See subfolder README.txt for detailed workflow

2. smeftfr_3_02_4F_Dim8
   - Purpose: Implementation of 4-fermion dimension-8 operators
   - Scope: Selected operators for ongoing research projects
   - Status: Work in progress
   - Documentation: See subfolder README.txt

3. smeftfr_3_02_4F_Dim8_Dim12
   - Purpose: Addition of dimension-12 operators relevant for
     arXiv:2509.02680
   - Key feature: Enables dim-12 operators in the SMEFT framework
   - Status: Research-ready
   - Documentation: See subfolder README.txt

-----------------------------------------------------------------
USAGE NOTES
-----------------------------------------------------------------

Each modification folder contains a complete copy of SmeftFR v3.0 with
the respective changes applied. Use the appropriate folder for your
specific research needs.

All modifications follow the standard SmeftFR two-stage workflow:
  1. Run SmeftFR-init.nb (or << smeft_fr_init.m)
  2. Quit Mathematica kernel
  3. Run SmeftFR-interfaces.nb (or << smeft_fr_interfaces.m)

See individual subfolder README files for modification-specific
instructions and caveats.