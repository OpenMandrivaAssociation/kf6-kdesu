%define libname %mklibname KF6Su
%define devname %mklibname KF6Su -d
%define git 20230818

Name: kf6-kdesu
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kdesu/-/archive/master/kdesu-master.tar.bz2#/kdesu-%{git}.tar.bz2
Summary: User interface for running shell commands with root privileges
URL: https://invent.kde.org/frameworks/kdesu
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
Requires: %{libname} = %{EVRD}

%description
User interface for running shell commands with root privileges

%package -n %{libname}
Summary: User interface for running shell commands with root privileges
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
User interface for running shell commands with root privileges

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

User interface for running shell commands with root privileges

%prep
%autosetup -p1 -n kdesu-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/ksu.categories

%files -n %{devname}
%{_includedir}/KF6/KDESu
%{_libdir}/cmake/KF6Su
%{_qtdir}/mkspecs/modules/qt_KDESu.pri
%{_qtdir}/doc/KF6Su.*

%files -n %{libname}
%{_libdir}/libKF6Su.so*
%{_libdir}/libexec/kf6/kdesu_stub
%{_libdir}/libexec/kf6/kdesud
