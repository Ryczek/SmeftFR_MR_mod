#!/usr/bin/perl

  while( <> ) {
    s/B,/B8,/g;
    s/B\ ,/B8,/g;
    s/Wi,/Wi8,/g;
    s/Wi\ ,/Wi8,/g;
    s/Gl,/Gl8,/g;
    s/Gl\ ,/Gl8,/g;
    s/Phi\[/Phi8\[/g;
    s/Phibar/Phi8bar/g;
    s/QL/QL8/g;
    s/LL/LL8/g;
    s/lR/lR8/g;
    s/dR/dR8/g;
    s/uR/uR8/g;
    s/SU2D/SU2D8/g;
    s/SU2W/SU2W8/g;
    s/Ta\[/Ta8\[/g;
    s/T\[/T8\[/g;

    print;
  }

exit 0;
