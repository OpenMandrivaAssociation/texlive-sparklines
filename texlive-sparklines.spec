# revision 16131
# category Package
# catalog-ctan /graphics/sparklines
# catalog-date 2009-11-22 10:21:09 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-sparklines
Version:	1.5
Release:	7
Summary:	Drawing sparklines: intense, simple, wordlike graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/sparklines
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sparklines.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sparklines.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sparklines are intense, simple, wordlike graphics (so named by
Edward Tufte). In lieu of a more detailed introduction,
Professor Tufte's site has an early release of a chapter on
sparklines. A PHP implementation may be found at SourceForge. A
sparkline can be added using the sparkline environment. Also,
you can add sparkling rectangles for the median and special
sparkling dots in red or blue. The package requires pdflatex;
sparklines cannot appear in a dvi file. The sparklines package
uses pgf, and does not work with pictex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sparklines/sparklines.sty
%doc %{_texmfdistdir}/doc/latex/sparklines/README
%doc %{_texmfdistdir}/doc/latex/sparklines/sparklines.pdf
%doc %{_texmfdistdir}/doc/latex/sparklines/sparklines.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 756152
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719562
- texlive-sparklines
- texlive-sparklines
- texlive-sparklines
- texlive-sparklines

