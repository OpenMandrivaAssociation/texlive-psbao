# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/psbao
# catalog-date 2008-11-15 12:33:11 +0100
# catalog-license lppl
# catalog-version 0.17
Name:		texlive-psbao
Version:	0.17
Release:	10
Summary:	Draw Bao diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/psbao
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psbao.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psbao.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws Bao diagrams in LaTeX. The package is a
development of psgo, and uses PSTricks to draw the diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/psbao/psbao.sty
%doc %{_texmfdistdir}/doc/latex/psbao/Changes
%doc %{_texmfdistdir}/doc/latex/psbao/README
%doc %{_texmfdistdir}/doc/latex/psbao/psbaomanual.pdf
%doc %{_texmfdistdir}/doc/latex/psbao/psbaomanual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.17-2
+ Revision: 755143
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.17-1
+ Revision: 719316
- texlive-psbao
- texlive-psbao
- texlive-psbao
- texlive-psbao

