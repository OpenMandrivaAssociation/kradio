%define	name	kradio
%define pre	beta3b
%define	version 1.0 
%define	release	%mkrel -c %{pre} 2 
%define	Summary	A V4L/V4L2-Radio Application for KDE 3.x

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPL
Url:		http://sourceforge.net/projects/kradio/
Source0:	%{name}-%{version}%{pre}.tar.bz2
Patch1:		kradio-1.0beta1-unblacklist-gcc.patch
BuildRequires:	arts-devel kdelibs-devel libsndfile-devel qt3-devel
BuildRequires:	jpeg-devel X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Comfortable Radio Application for KDE 3.x

KRadio is a comfortable radio application for KDE 3.x.
It has support for V4L and V4L2 radio cards drivers.

KRadio currently provides:

* V4L/V4L2 Radio support
* Remote Control support (LIRC)
* Alarms, Sleep Countdown
* Several GUI Controls (Docking Menu, Station Quickbar, Radio Display)
* Recording Capabilities
* Extendable Plugin Architecture

This Package also includes a growing collection of station preset.
files for many cities around the world contributed by KRadio Users.

As KRadio is based on an extendable plugin architecture.

%prep
%setup -q -n %{name}-%{version}%{pre}
%patch1 -p1 -b .blacklist
perl -pi -e 's#ACLOCAL="aclocal"#ACLOCAL="aclocal-1.9"#g' admin/detect-autoconf.sh
touch kradio3/src/libkradio-gui/radiostationlistview.h

%build
UNSERMAKE=no make -f Makefile.cvs
%configure2_5x	--disable-rpath \
		--enable-final \
		--with-qt-dir=%{_prefix}/lib/qt3 \
%if "%{_lib}" != "lib"
		--enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})"
%endif

%make
 
%install
rm -rf %{buildroot}

%makeinstall_std

# rm dup docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/kradio

install -m644 kradio3/src/hi48-app-kradio.png -D %{buildroot}%{_liconsdir}/%{name}.png
install -m644 kradio3/src/hi32-app-kradio.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 kradio3/src/hi16-app-kradio.png -D %{buildroot}%{_miconsdir}/%{name}.png

desktop-file-install	--vendor="" \
			--add-category="X-MandrivaLinux-Multimedia-Sound" \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/kde/*

%find_lang %{name}-%{version}%{pre}

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}
 
%files -f %{name}-%{version}%{pre}.lang
%defattr(-,root,root)
%doc kradio3/AUTHORS kradio3/ChangeLog kradio3/README kradio3/TODO
%{_bindir}/convert-presets
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/*/%{name}.desktop
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png 
%{_iconsdir}/*/*/apps/*.png
