Summary:	X.org video driver for Matrox video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Matrox
Name:		xorg-driver-video-mga
Version:	1.2.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-mga-%{version}.tar.bz2
# Source0-md5:	cb5d789c9057d2c801ef2ab81daba155
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Matrox video adapters. It supports PCI and AGP
video cards based on the following Matrox chips: MGA2064W, MGA1064SG
(Mystique), MGA2164W (Millennium II), G100 (Productiva G100), G200
(Millennium G200 and Mystique G200), G400 (Millenium G400, Millenium
G400 MAX, Millenium G450 and Marvel G450 eTV), G550 (Milenium G550 and
Millenium G500 Dual DVI).

%description -l pl
Sterownik obrazu X.org dla kart graficznych Matrox. Obs³uguje karty
PCI i AGP oparte na nastêpuj±cych uk³adach Matroksa: MGA2064W,
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README_HALLIB
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.4x*
