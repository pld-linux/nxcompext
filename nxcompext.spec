#
Summary:	NX compression library extenstions
Name:		nxcompext
Version:	1.4.0_2
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.nomachine.com/download/snapshot/nxsources/%{name}-%(echo %{version} | tr _ -).tar.gz
# Source0-md5:	aec8b44cfd3e05fca529769f4f9f90e7
URL:		http://www.nomachine.com/
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-Xserver-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nxcomp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NX compression library extensions.

%package devel
Summary:	Header files and develpment documentation for nxcompext
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files needed for development using nxcompext.

%package static
Summary:	Static nxcompext library
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static nxcompext library.

%prep
%setup -q -n %{name}

%build
%configure
sed -i -e 's#-I/usr/X11R6/include#-I/usr/X11R6/include -I/usr/X11R6/include/X11 -I/usr/X11R6/include/X11/Xserver/programs/Xserver/include#g' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

cp -a lib*.so* $RPM_BUILD_ROOT%{_libdir}
install lib*.a $RPM_BUILD_ROOT%{_libdir}
install NX.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
