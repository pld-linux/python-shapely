# TODO: Package examples to _examplesdir ?
%define 	module	shapely
Summary:	Geospatial geometries, predicates, and operations for Python
Name:		python-%{module}
Version:	1.3.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
# Source0-md5:	5ac028637fbd52b9752994bdbfd9446c
URL:		http://pypi.python.org/pypi/Shapely
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	geos >= 3.1
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shapely is a Python package for manipulation and analysis of 2D
geospatial geometries. It is based on GEOS. Shapely is not concerned
with data formats or coordinate reference systems.

%description -l pl.UTF-8
Pakiet do manipulacji i anlizy duwymiarowych geoptrzestrzennych
geometrii. Bazuje na GEOS, nie zajmuje się formatami danych czy
układami odniesnienia danych.

%prep
%setup -q -n Shapely-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

# install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc CHANGES.txt CREDITS.txt HISTORY.txt README.txt
%dir %{py_sitedir}/%{module}
# %{py_sitescriptdir}/%{module}/ctypes_declarations.py
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/geometry
%{py_sitedir}/%{module}/geometry/*.py[co]
%dir %{py_sitedir}/%{module}/algorithms
%{py_sitedir}/%{module}/algorithms/*.py[co]

%dir %{py_sitedir}/%{module}/speedups
%attr(755,root,root) %{py_sitedir}/%{module}/speedups/*.so
%{py_sitedir}/%{module}/speedups/*.py[co]

%dir %{py_sitedir}/%{module}/tests
%{py_sitedir}/%{module}/tests/*.py[co]
%dir %{py_sitedir}/%{module}/examples
%{py_sitedir}/%{module}/examples/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitedir}/Shapely-*.egg-info
%endif
