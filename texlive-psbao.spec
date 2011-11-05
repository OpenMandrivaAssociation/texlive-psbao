# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/psbao
# catalog-date 2008-11-15 12:33:11 +0100
# catalog-license lppl
# catalog-version 0.17
Name:		texlive-psbao
Version:	0.17
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package draws Bao diagrams in LaTeX. The package is a
development of psgo, and uses PSTricks to draw the diagrams.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/psbao/psbao.sty
%doc %{_texmfdistdir}/doc/latex/psbao/Changes
%doc %{_texmfdistdir}/doc/latex/psbao/README
%doc %{_texmfdistdir}/doc/latex/psbao/psbaomanual.pdf
%doc %{_texmfdistdir}/doc/latex/psbao/psbaomanual.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
