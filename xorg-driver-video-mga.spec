Summary:	X.org video driver for Matrox video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych Matrox
Name:		xorg-driver-video-mga
Version:	2.1.0
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.xz
# Source0-md5:	5b2e85f46dfc46b03d5d9f90f76d3678
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
# checked, but not used
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.18.0
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-libglx >= 1.18.0
Requires:	xorg-xserver-server >= 1.18.0
Provides:	xorg-driver-video
Obsoletes:	X11-driver-mga < 1:7.0.0
Obsoletes:	XFree86-driver-mga < 1:7.0.0
Obsoletes:	XFree86-mga < 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Matrox video adapters. It supports PCI and AGP
video cards based on the following Matrox chips:
- MGA2064W,
- MGA1064SG (Mystique),
- MGA2164W (Millennium II),
- G100 (Productiva G100),
- G200 (Millennium G200 and Mystique G200),
- G400 (Millenium G400, Millenium G400 MAX, Millenium G450 and Marvel
  G450 eTV),
- G550 (Milenium G550 and Millenium G500 Dual DVI).

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych Matrox. Obsługuje karty
PCI i AGP oparte na następujących układach Matroksa:
- MGA2064W,
- MGA1064SG (Mystique),
- MGA2164W (Millennium II),
- G100 (Productiva G100),
- G200 (Millennium G200 i Mystique G200),
- G400 (Millenium G400, Millenium G400 MAX, Millenium G450 i Marvel
  G450 eTV),
- G550 (Milenium G550 i Millenium G500 Dual DVI).

%prep
%setup -q -n xf86-video-mga-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.4*
