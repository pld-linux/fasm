%bcond_with	bootstrap 	# use included binary
Summary:	Flat assembler
Summary(pl):	"P�aski" assembler
Name:		fasm
Version:	1.54
Release:	1
License:	distributable
Group:		Development/Tools
Source0:	http://flatassembler.net/%{name}-%{version}.tar.gz
# Source0-md5:	407df366e89a4229f7689514d1d3ddbb
URL:		http://flatassembler.net/
%if %{without bootstrap}
BuildRequires:	fasm
%endif
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%description
The flat assembler is a fast and efficient self-assembling 80x86
assembler for DOS, Windows and Linux operating systems. Currently it
supports all 8086-80486/Pentium instructions with MMX, SSE, SSE2, SSE3
and 3DNow! extensions, can produce output in binary, MZ, PE, COFF or
ELF format. It includes the powerful but easy to use macroinstruction
support and does multiple passes to optimize the instruction codes for
size. The flat assembler is self-compilable and the full source code
is included.

%description -l pl
P�aski assembler jest szybkim i efektywnym, samo-assembluj�cy si�
assemblerem 80x86 dla DOS, Windows i Linux. Aktualnie obs�uguje
wszystkie instrukcje 8086-80486/Pentium z rozszerzeniami MMX, SSE,
SSE2, SSE3 i 3DNow! , mo�e produkowa� programy w formacie binarnym,
MZ, PE, COFF lub ELF. Zawiera pot�ne, ale proste wsparcie dla
makroinstrukcji oraz wielokrotnie optymalizuje kod dla rozmiaru.
P�aski assembler potrafi sam si� skompilowa� oraz zawiera pe�en kod
�r�d�owy.

%prep
%setup -q -n %{name}

%build
%if %{without bootstrap}
ASM=%{name}
%else
ASM=../../%{name}
%endif
cd source/Linux
$ASM %{name}.asm
chmod +x %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D source/Linux/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
