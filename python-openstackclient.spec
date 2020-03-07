#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : python-openstackclient
Version  : 5.0.0
Release  : 54
URL      : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-5.0.0.tar.gz
Source0  : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-5.0.0.tar.gz
Source1  : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-5.0.0.tar.gz.asc
Summary  : OpenStack Command-line Client
Group    : Development/Tools
License  : Apache-2.0
Requires: python-openstackclient-bin = %{version}-%{release}
Requires: python-openstackclient-license = %{version}-%{release}
Requires: python-openstackclient-python = %{version}-%{release}
Requires: python-openstackclient-python3 = %{version}-%{release}
Requires: Babel
Requires: cliff
Requires: keystoneauth1
Requires: openstacksdk
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-novaclient
Requires: six
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : keystoneauth1
BuildRequires : openstacksdk
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-cinderclient
BuildRequires : python-glanceclient
BuildRequires : python-keystoneclient
BuildRequires : python-novaclient
BuildRequires : six

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-openstackclient package.
Group: Binaries
Requires: python-openstackclient-license = %{version}-%{release}

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
Requires: python-openstackclient-python3 = %{version}-%{release}

%description python
python components for the python-openstackclient package.


%package python3
Summary: python3 components for the python-openstackclient package.
Group: Default
Requires: python3-core
Provides: pypi(python_openstackclient)
Requires: pypi(babel)
Requires: pypi(cliff)
Requires: pypi(keystoneauth1)
Requires: pypi(openstacksdk)
Requires: pypi(osc_lib)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(python_cinderclient)
Requires: pypi(python_glanceclient)
Requires: pypi(python_keystoneclient)
Requires: pypi(python_novaclient)
Requires: pypi(six)

%description python3
python3 components for the python-openstackclient package.


%prep
%setup -q -n python-openstackclient-5.0.0
cd %{_builddir}/python-openstackclient-5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583541987
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-openstackclient
cp %{_builddir}/python-openstackclient-5.0.0/LICENSE %{buildroot}/usr/share/package-licenses/python-openstackclient/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openstack

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-openstackclient/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
