Name:                jasper
Version:             2.0.14
Release:             8
Summary:             Reference implementation of the codec specified in the JPEG-2000 standard, Part 1
License:             JasPer
URL:                 http://www.ece.uvic.ca/~frodo/jasper/
Source0:             http://www.ece.uvic.ca/~frodo/jasper/software/jasper-%{version}.tar.gz

Patch0001:           jasper-2.0.14-CVE-2016-9396.patch
Patch0002:           jasper-2.0.14-rpath.patch

BuildRequires:       cmake freeglut-devel libGLU-devel libjpeg-devel libXmu-devel libXi-devel
BuildRequires:       pkgconfig doxygen mesa-libGL-devel

Provides:            jasper-libs = %{version}-%{release}
Obsoletes:           jasper-libs < %{version}-%{release}
Conflicts:           jasper < 1.900.1-4

%description
The JasPer Project is an open-source initiative to provide a free software-based reference
implementation of the codec specified in the JPEG-2000 Part-1 standard.

%package devel
Summary:             Development files for jasper
Provides:            libjasper-devel = %{version}-%{release}
Requires:            %{name} = %{version}-%{release} libjpeg-devel pkgconfig

%description devel
Development files for jasper.

%package utils
Summary:             Nonessential utilities of jasper
Requires:            %{name} = %{version}-%{release}

%description utils
Nonessential utilities of jasper, including jiv and tmrdemo.

%package help
Summary:             Help documents for jasper

%description help
Help documents for jasper.

%prep
%autosetup -n %{name}-%{version} -p1 -S git

%build
install -d builder
cd builder
%cmake .. -DJAS_ENABLE_DOC:BOOL=OFF
cd -

%make_build -C builder

%install
make install/fast DESTDIR=%{buildroot} -C builder
%delete_la

%check
make test -C builder

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%doc COPYRIGHT LICENSE
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_docdir}/JasPer/*
%{_libdir}/libjasper.so.4*

%files devel
%doc doc/*
%{_includedir}/jasper/
%{_libdir}/pkgconfig/jasper.pc
%{_libdir}/libjasper.so
%exclude %{_docdir}/README

%files utils
%{_bindir}/jiv

%files help
%{_mandir}/man1/*
%doc README

%changelog
* Wed Apr 22 2020 leiju <leiju4@huawei.com> - 2.0.14-8
- Package init
