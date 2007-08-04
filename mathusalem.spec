Summary:	GNOME application to manage long running tasks
Summary(pl.UTF-8):	Aplikacja GNOME do zarządzania długo działającymi zadaniami
Name:		mathusalem
Version:	0.0.4
Release:	1
License:	GPL v2+
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
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mathusalem, the upcoming long running task manager for GNOME.

%description -l pl.UTF-8
Mathusalem - zarządca długo działających zadań dla GNOME.

%package devel
Summary:	mathusalem header files
Summary(pl.UTF-8):	Pliki nagłówkowe mathusalem
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.60
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libnotify-devel >= 0.4.2

%description devel
mathusalem header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe mathusalem.

%package -n nautilus-extension-mathusalem
Summary:	mathusalem extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie mathusalem dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.10.0

%description -n nautilus-extension-mathusalem
Shows task progress using mathusalem.

%description -n nautilus-extension-mathusalem -l pl.UTF-8
Rozszerzenie mathusalem dla Nautilusa.

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
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
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
