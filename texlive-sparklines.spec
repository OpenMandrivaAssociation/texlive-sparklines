%global tl_name sparklines
%global tl_revision 42821

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Drawing sparklines: intense, simple, wordlike graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/sparklines
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sparklines.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sparklines.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Sparklines are intense, simple, wordlike graphics (so named by Edward
Tufte). In lieu of a more detailed introduction, Professor Tufte's site
has an early release of a chapter on sparklines. A PHP implementation
may be found at SourceForge. A sparkline can be added using the
sparkline environment. Also, you can add sparkling rectangles for the
median and special sparkling dots in red or blue. The package requires
pdfLaTeX; sparklines cannot appear in a dvi file. The sparklines package
uses pgf, and does not work with pictex.

