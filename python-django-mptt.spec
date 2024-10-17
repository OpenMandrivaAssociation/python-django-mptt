%define	oname	django-mptt

Name:		python-%{oname}
Version:	0.6.1
Release:	2
Summary:	Modified Preorder Tree Traversal for Django models

Source0:	http://pypi.python.org/packages/source/d/django-mptt/django-mptt-%{version}.tar.gz

License:	BSD 
Group:		Development/Python
Url:		https://github.com/django-mptt/django-mptt
BuildArch:	noarch

BuildRequires:	pythonegg(setuptools)
BuildRequires:	pythonegg(sphinx)
BuildRequires:  pythonegg(django) >= 1.4.2

Requires: python(abi) = 2.7 
Requires: pythonegg(django) >= 1.4.2

%description
Utilities for implementing Modified Preorder Tree Traversal
with your Django Models and working with trees of Model instances.

%prep
%setup -q -n %{oname}-%{version}

%install
python setup.py install --root="%{buildroot}"

%check
cd tests
sh runtests.sh

%files
%doc LICENSE MANIFEST.in PKG-INFO README.rst
%{py_puresitedir}/django_mptt-%{version}-py2.*.egg-info
%{py_puresitedir}/mptt/__init__.py
%{py_puresitedir}/mptt/admin.py
%{py_puresitedir}/mptt/exceptions.py
%{py_puresitedir}/mptt/fields.py
%{py_puresitedir}/mptt/forms.py

%lang(de) %{py_puresitedir}/mptt/locale/de/LC_MESSAGES/django.mo
%{py_puresitedir}/mptt/locale/de/LC_MESSAGES/django.po
%lang(dk) %{py_puresitedir}/mptt/locale/dk/LC_MESSAGES/django.mo
%{py_puresitedir}/mptt/locale/dk/LC_MESSAGES/django.po
%lang(fr) %{py_puresitedir}/mptt/locale/fr/LC_MESSAGES/django.mo
%{py_puresitedir}/mptt/locale/fr/LC_MESSAGES/django.po
%lang(nb) %{py_puresitedir}/mptt/locale/nb/LC_MESSAGES/django.mo
%{py_puresitedir}/mptt/locale/nb/LC_MESSAGES/django.po
%lang(pl) %{py_puresitedir}/mptt/locale/pl/LC_MESSAGES/django.mo
%{py_puresitedir}/mptt/locale/pl/LC_MESSAGES/django.po
%{py_puresitedir}/mptt/managers.py
%{py_puresitedir}/mptt/models.py
%{py_puresitedir}/mptt/templates/admin/grappelli_mptt_change_list.html
%{py_puresitedir}/mptt/templates/admin/grappelli_mptt_change_list_results.html
%{py_puresitedir}/mptt/templates/admin/mptt_change_list.html
%{py_puresitedir}/mptt/templates/admin/mptt_change_list_results.html
%{py_puresitedir}/mptt/templatetags/__init__.py
%{py_puresitedir}/mptt/templatetags/mptt_admin.py
%{py_puresitedir}/mptt/templatetags/mptt_tags.py
%{py_puresitedir}/mptt/utils.py



