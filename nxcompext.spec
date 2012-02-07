%define	version_major	3.4.0
%define	version_minor	1
Summary:	NX compression library extenstions
Summary(pl.UTF-8):	Rozszerzenia biblioteki kompresji NX
Name:		nxcompext
Version:	%{version_major}.%{version_minor}
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://64.34.161.181/download/%{version_major}/sources/%{name}-%{version_major}-%{version_minor}.tar.gz
# Source0-md5:	605a8e2a136f89477f0059a0d2af4582
Patch0:		%{name}-xgetioerror.patch
Patch1:		%{name}-xorg-includes.patch
URL:		http://www.nomachine.com/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nxcomp-devel >= 2.0.0
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't satisfy xorg deps for the rest of the distro
%define		_noautoprovfiles	%{_libdir}/NX

# and as we don't provide them, don't require either
%define		_noautoreq libXcompext.so

%description
NX compression library extensions.

%description -l pl.UTF-8
Rozszerzenia biblioteki kompresji NX.

%package devel
Summary:	Header files for nxcompext
Summary(pl.UTF-8):	Pliki nagłówkowe nxcompext
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nxcompext.

%description devel -l pl.UTF-8
Pliki nagłówkowe nxcompext.

%package static
Summary:	Static nxcompext library
Summary(pl.UTF-8):	Statyczna biblioteka nxcompext
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nxcompext library.

%description static -l pl.UTF-8
Statyczna biblioteka nxcompext.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
sed -i -e 's#-I/usr/X11R6/include#-I/usr/include/X11 -I/usr/include/xorg#g' Makefile
sed -i -e 's#-L../nxcomp##' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/NX,%{_includedir}}

cp -a lib*.so*	$RPM_BUILD_ROOT%{_libdir}/NX
cp -a lib*.a	$RPM_BUILD_ROOT%{_libdir}/NX
install NX*.h	$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_libdir}/NX/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/NX/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/NX/*.a
