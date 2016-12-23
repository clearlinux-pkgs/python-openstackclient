#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-openstackclient
Version  : 3.3.0
Release  : 32
URL      : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-3.3.0.tar.gz
Source0  : http://tarballs.openstack.org/python-openstackclient/python-openstackclient-3.3.0.tar.gz
Summary  : OpenStack Command-line Client
Group    : Development/Tools
License  : Apache-2.0
Requires: python-openstackclient-bin
Requires: python-openstackclient-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
===============
OpenStackClient
===============
.. image:: https://img.shields.io/pypi/v/python-openstackclient.svg
:target: https://pypi.python.org/pypi/python-openstackclient/
:alt: Latest Version

%package bin
Summary: bin components for the python-openstackclient package.
Group: Binaries

%description bin
bin components for the python-openstackclient package.


%package python
Summary: python components for the python-openstackclient package.
Group: Default

%description python
python components for the python-openstackclient package.


%prep
%setup -q -n python-openstackclient-3.3.0

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openstack

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
