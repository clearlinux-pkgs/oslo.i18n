#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : oslo.i18n
Version  : 3.14.0
Release  : 40
URL      : http://tarballs.openstack.org/oslo.i18n/oslo.i18n-3.14.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.i18n/oslo.i18n-3.14.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.i18n/oslo.i18n-3.14.0.tar.gz.asc
Summary  : Oslo i18n library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.i18n-python
Requires: Babel
Requires: pbr
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.i18n.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the oslo.i18n package.
Group: Default

%description python
python components for the oslo.i18n package.


%prep
%setup -q -n oslo.i18n-3.14.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489784376
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489784376
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
