(* ::Package:: *)

MyStyle={Frame->True,GridLines->Automatic,GridLinesStyle->Directive[Dashed,RGBColor[0.2,1,0.2]],FrameStyle->Directive[Thickness[0.007],Bold],Axes->False,PlotStyle->Directive[Dashed,Thick](*,FrameLabel->{X,Y},PlotLabel->LBL*)};
MyListStyle={Frame->True,GridLines->Automatic,GridLinesStyle->Directive[Dashed,Thick,Green],FrameStyle->Directive[Thickness[0.007],Bold],Axes->False,PlotStyle->Blue,PlotMarkers->{"\[FilledCircle]",6},Method->{"GridLinesInFront"->False}(*,PlotLabel->LBL*),(*Joined->True,*) PlotRange -> Full};


SetOptions[Plot,MyStyle];
SetOptions[ListPlot,MyListStyle];
