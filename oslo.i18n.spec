#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : oslo.i18n
Version  : 5.0.0
Release  : 58
URL      : http://tarballs.openstack.org/oslo.i18n/oslo.i18n-5.0.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.i18n/oslo.i18n-5.0.0.tar.gz
Source1  : http://tarballs.openstack.org/oslo.i18n/oslo.i18n-5.0.0.tar.gz.asc
Summary  : Oslo i18n library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.i18n-license = %{version}-%{release}
Requires: oslo.i18n-python = %{version}-%{release}
Requires: oslo.i18n-python3 = %{version}-%{release}
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : six

%description
Team and repository tags
        ========================

%package license
Summary: license components for the oslo.i18n package.
Group: Default

%description license
license components for the oslo.i18n package.


%package python
Summary: python components for the oslo.i18n package.
Group: Default
Requires: oslo.i18n-python3 = %{version}-%{release}

%description python
python components for the oslo.i18n package.


%package python3
Summary: python3 components for the oslo.i18n package.
Group: Default
Requires: python3-core
Provides: pypi(oslo.i18n)
Requires: pypi(pbr)
Requires: pypi(six)

%description python3
python3 components for the oslo.i18n package.


%prep
%setup -q -n oslo.i18n-5.0.0
cd %{_builddir}/oslo.i18n-5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591379056
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.i18n
cp %{_builddir}/oslo.i18n-5.0.0/LICENSE %{buildroot}/usr/share/package-licenses/oslo.i18n/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.i18n/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
