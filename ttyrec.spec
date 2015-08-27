Name:		ttyrec
Version:	1.0.8
Release:	2
Summary:	A tty recorder
Group:		Text tools
URL:		http://namazu.org/~satoru/ttyrec/index.html.en
Source0:	http://namazu.org/~satoru/ttyrec/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
License:	BSD
BuildRequires:	libbsd-devel

%description
ttyrec is a tty recorder that records your terminal sessions with 
microsecond accuracy. It can record emacs -nw, vi, lynx, or any
programs running on a terminal.

%prep
%setup -q 
%patch0 -p1

%build
%make CFLAGS=-DHAVE_getpt

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m 644 *.1 %{buildroot}%{_mandir}/man1
install -m 755 ttyrec %{buildroot}%{_bindir}
install -m 755 ttyplay %{buildroot}%{_bindir}
install -m 755 ttytime %{buildroot}%{_bindir}

%files
%{_bindir}/*
%{_mandir}/man1/*



