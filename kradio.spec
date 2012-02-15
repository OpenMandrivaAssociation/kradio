%define	name	kradio
%define	version 4.0.3
%define	release	1
%define	Summary	A V4L/V4L2-Radio Application for KDE 4.x

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPLv2+
Url:		http://sourceforge.net/projects/kradio/
Source0:	http://freefr.dl.sourceforge.net/sourceforge/kradio/%{name}4-%{version}.tar.bz2
Patch2:		kradio-fix-invalid-desktop.patch
Patch3:		kradio4-install-desktop.patch
BuildRequires:	kdelibs4-devel >= 2:4.1.83
BuildRequires:	libsndfile-devel
BuildRequires:	libalsa-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libmms-devel
BuildRequires:	lirc-devel
BuildRequires:	oggvorbis-devel

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
%setup -q -n %{name}4-%{version}
%patch2 -p1 -b .xdg
%patch3 -p1 -b .install

%build
%cmake_kde4
%make
 
%install
%makeinstall_std -C build

rm -fr %buildroot%_datadir/doc/*

%find_lang %name --all-name
 
%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%{_kde_bindir}/*
%{_kde_libdir}/%{name}4
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/pixmaps/kradio4.png
%{_kde_appsdir}/%{name}4
%{_kde_iconsdir}/*/*/*/*
