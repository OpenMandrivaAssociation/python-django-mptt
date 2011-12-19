%define	module	django-mptt
%define name	python-%{module}
%define version	0.5.2
%define release %mkrel 1

Summary:	Modified Preorder Tree Traversal for Django models
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/django-mptt/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-django
BuildRequires:	python-sphinx

%description
Utilities for implementing Modified Preorder Tree Traversal with your
Django Models and working with trees of Model instances.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
make html
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc LICENSE NOTES README.rst build/docs/html
