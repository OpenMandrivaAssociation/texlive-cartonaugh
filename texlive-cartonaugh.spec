%global tl_name cartonaugh
%global tl_revision 59938

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A LuaLaTeX package for drawing karnaugh maps with up to 6 variables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/cartonaugh
License:	cc-by-sa-3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cartonaugh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cartonaugh.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cartonaugh.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package, a fork of 2pi's karnaugh-map package, draws karnaugh maps
with 2, 3, 4, 5, and 6 variables. It also contains commands for filling
the karnaugh map with terms semi-automatically or manually. Last but not
least it contains commands for drawing implicants on top of the map. The
name "cartonaugh" is a portmanteau of "cartographer" and "karnaugh". The
package needs LuaLaTeX and depends on TikZ, xparse, and xstring.

