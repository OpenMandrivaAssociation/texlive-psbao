Name:		texlive-psbao
Version:	55013
Release:	1
Summary:	Draw Bao diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/psbao
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psbao.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psbao.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/psbao
%doc %{_texmfdistdir}/doc/latex/psbao

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
