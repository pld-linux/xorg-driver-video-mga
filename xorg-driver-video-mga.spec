Summary:	X.org video driver for Matrox video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Matrox
Name:		xorg-driver-video-mga
Version:	1.4.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.bz2
# Source0-md5:	41c9ca3d1e3eb91ca4165a31c9fe329a
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
Requires:	xorg-xserver-server >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Matrox video adapters. It supports PCI and AGP
video cards based on the following Matrox chips: MGA2064W, MGA1064SG
(Mystique), MGA2164W (Millennium II), G100 (Productiva G100), G200
(Millennium G200 and Mystique G200), G400 (Millenium G400, Millenium
G400 MAX, Millenium G450 and Marvel G450 eTV), G550 (Milenium G550 and
Millenium G500 Dual DVI).

%description -l pl
Sterownik obrazu X.org dla kart graficznych Matrox. Obsługuje karty
PCI i AGP oparte na następujących układach Matroksa: MGA2064W,
MGA1064SG (Mystique), MGA2164W (Millennium II), G100 (Productiva
G100), G200 (Millennium G200 i Mystique G200), G400 (Millenium G400,
Millenium G400 MAX, Millenium G450 i Marvel G450 eTV), G550 (Milenium
G550 i Millenium G500 Dual DVI).

%prep
%setup -q -n xf86-video-mga-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README_HALLIB
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.4*
