Summary:	GNOME application to manage long running tasks
Name:		mathusalem
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.student.montefiore.ulg.ac.be/~frecinau/tar/%{name}-%{version}.tar.bz2
# Source0-md5:	f21c30ac72dc7c98808d8bc0ec8f1817
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	eel-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	nautilus-devel >= 2.10.0
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper >= 0.3.14
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mathusalem, the upcoming long running task manager for GNOME.

%package devel
Summary:	mathusalem header files
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
mathusalem header files.

%package -n nautilus-extension-mathusalem
Summary:	mathusalem extension for Nautilus
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.10.0

%description -n nautilus-extension-mathusalem
Shows task progress using mathusalem.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nautilus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mathusalem
%attr(755,root,root) %{_libdir}/libmathusalem.so.*.*
%{_datadir}/dbus-1/services/*.service
%{_iconsdir}/hicolor/*/emblems/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmathusalem.so
%{_libdir}/libmathusalem.la
%{_includedir}/mathusalem-0
%{_pkgconfigdir}/mathusalem.pc

%files -n nautilus-extension-mathusalem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so*