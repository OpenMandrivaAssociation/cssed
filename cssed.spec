%define name	cssed
%define version	0.4.0
%define release 5

%define Summary CSS editor for web developers
%define title	Cssed

Summary:	%Summary
Name:           %name
Version:        %version
Release:        %mkrel %release
Group:          Development/Other
License:        GPLv2+
Url:            http://cssed.sourceforge.net

Source:         http://mesh.dl.sourceforge.net/sourceforge/cssed/%{name}-%{version}.tar.gz
Source1:	%name-16.png
Source2:	%name-32.png
Source3:	%name.png

BuildRoot:      %_tmppath/%{name}-%{version}-%{release}-buildroot

Buildrequires:   glib2-devel, gtk2-devel, expat, desktop-file-utils
 

%description
cssed is a tiny GTK+ CSS editor and validator for web developers.

%package -n %name-devel
Summary:	Cssed devel file
Requires:	%name = %version-%release
Group:		Development/Other
Provides:	%name-devel = %version-%release

%description -n %name-devel
Cssed devel file.

%prep
%setup -q

%build
%configure2_5x --with-plugin-headers
%make WARN_CFLAGS=""

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name --with-gnome

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Cssed
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=%{name} 
Terminal=false
Type=Application
Categories=GNOME;GTK;WebDevelopment;Development;
EOF

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir,%_datadir/pixmaps/}
install -m 644 %SOURCE3 %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus 
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang 
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*desktop
%{_datadir}/pixmaps/%name.png

%files -n %name-devel
%defattr(-,root,root)
%{_datadir}/%{name}/include
%{_libdir}/pkgconfig/%{name}.pc

