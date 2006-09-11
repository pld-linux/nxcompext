%define	_version_major	2.0.0
%define	_version_minor	33

Summary:	NX compression library extenstions
Summary(pl):	Rozszerzenia biblioteki kompresji NX
Name:		nxcompext
Version:	%{_version_major}.%{_version_minor}
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://64.34.161.181/download/%{_version_major}/sources/%{name}-%{_version_major}-%{_version_minor}.tar.gz
# Source0-md5:	d6738f330687d6c986600a9685e527cf
Patch0:		%{name}-xgetioerror.patch
URL:		http://www.nomachine.com/
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-Xserver-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nxcomp-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NX compression library extensions.

%description -l pl
Rozszerzenia biblioteki kompresji NX.

%package devel
Summary:	Header files for nxcompext
Summary(pl):	Pliki nag³ówkowe nxcompext
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nxcompext.

%description devel -l pl
Pliki nag³ówkowe nxcompext.

%package static
Summary:	Static nxcompext library
Summary(pl):	Statyczna biblioteka nxcompext
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nxcompext library.

%description static -l pl
Statyczna biblioteka nxcompext.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__autoconf}
%configure
sed -i -e 's#-I/usr/X11R6/include#-I/usr/X11R6/include -I/usr/X11R6/include/X11 -I/usr/X11R6/include/X11/Xserver/programs/Xserver/include#g' Makefile
sed -i -e 's#-L../nxcomp#-L/usr/X11R6/lib#' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -a lib*.so*	$RPM_BUILD_ROOT%{_libdir}
install lib*.a	$RPM_BUILD_ROOT%{_libdir}
install NX*.h	$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
