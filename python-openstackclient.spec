#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : python-openstackclient
Version  : 3.14.2
Release  : 37
URL      : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-3.14.2.tar.gz
Source0  : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-3.14.2.tar.gz
Source99 : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-3.14.2.tar.gz.asc
Summary  : OpenStack Command-line Client
Group    : Development/Tools
License  : Apache-2.0
Requires: python-openstackclient-bin
Requires: python-openstackclient-python3
Requires: python-openstackclient-license
Requires: python-openstackclient-python
Requires: Babel
Requires: Sphinx
Requires: cliff
Requires: keystoneauth1
Requires: openstackdocstheme
Requires: openstacksdk
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-novaclient
Requires: reno
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-openstackclient package.
Group: Binaries
Requires: python-openstackclient-license

%description bin
bin components for the python-openstackclient package.


%package license
Summary: license components for the python-openstackclient package.
Group: Default

%description license
license components for the python-openstackclient package.


%package python
Summary: python components for the python-openstackclient package.
Group: Default
Requires: python-openstackclient-python3

%description python
python components for the python-openstackclient package.


%package python3
Summary: python3 components for the python-openstackclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-openstackclient package.


%prep
%setup -q -n python-openstackclient-3.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532382637
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-openstackclient
cp LICENSE %{buildroot}/usr/share/doc/python-openstackclient/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openstack

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-openstackclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
