Name:		texlive-cartonaugh
Version:	59938
Release:	2
Summary:	A LuaLaTeX package for drawing karnaugh maps with up to 6 variables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cartonaugh
License:	cc-by-sa-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cartonaugh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cartonaugh.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cartonaugh.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package, a fork of 2pi's karnaugh-map package, draws
karnaugh maps with 2, 3, 4, 5, and 6 variables. It also
contains commands for filling the karnaugh map with terms
semi-automatically or manually. Last but not least it contains
commands for drawing implicants on top of the map. The name
"cartonaugh" is a portmanteau of "cartographer" and "karnaugh".
The package needs LuaLaTeX and depends on TikZ, xparse, and
xstring.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cartonaugh
%{_texmfdistdir}/tex/latex/cartonaugh
%doc %{_texmfdistdir}/doc/latex/cartonaugh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
