%define	name	kradio
%define date	2009-02-08
%define pre	r562
%define	version 4.0.0
%define	release	%mkrel -c %{pre} 1
%define	Summary	A V4L/V4L2-Radio Application for KDE 4.x

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPLv2+
Url:		http://sourceforge.net/projects/kradio/
Source0:	http://www.nocabal.de/~emw/kradio/download/%{name}4-snapshot-%{date}-%{pre}.tar.gz
Patch2:		kradio-fix-invalid-desktop.patch
Patch3:		kradio4-install-desktop.patch
BuildRequires:	kdelibs4-devel >= 2:4.1.83
BuildRequires:	libsndfile-devel
BuildRequires:	libalsa-devel
BuildRequires:	lirc-devel
BuildRequires:	oggvorbis-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Comfortable Radio Application for KDE 4.x

KRadio is a comfortable radio application for KDE 4.x.
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

%prep
%setup -q -n %{name}4-snapshot-%{date}-%{pre}
%patch2 -p1 -b .xdg
%patch3 -p1 -b .install

%build
%cmake_kde4
%make
 
%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %name --all-name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif
 
%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_kde_bindir}/*
%{_kde_libdir}/%{name}
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/%{name}
%{_kde_iconsdir}/*/*/*/*
