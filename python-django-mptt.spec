%define	module	django-mptt

Summary:	Modified Preorder Tree Traversal for Django models

Name:		python-%{module}
Version:	0.6.1
Release:	1
Source0:	http://pypi.python.org/packages/source/d/django-mptt/django-mptt-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/django-mptt/
BuildArch:	noarch
Requires:	python-django
BuildRequires:	python-sphinx

%description
Utilities for implementing Modified Preorder Tree Traversal with your
Django Models and working with trees of Model instances.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
make html
popd

%clean

%files -f FILE_LIST
%doc LICENSE NOTES README.rst build/docs/html



