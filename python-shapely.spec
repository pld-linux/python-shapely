# TODO: Package examples to _examplesdir ?
#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	shapely
Summary:	Geospatial geometries, predicates, and operations for Python
Name:		python-%{module}
Version:	1.6.4
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
# Source0-md5:	7581ef2d0fb346f9ed157f3efc75f6a4
URL:		http://pypi.python.org/pypi/Shapely
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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

%package -n python3-%{module}
Summary:	Geospatial geometries, predicates, and operations for Python
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Shapely is a Python package for manipulation and analysis of 2D
geospatial geometries. It is based on GEOS. Shapely is not concerned
with data formats or coordinate reference systems.

%description -n python3-%{module} -l pl.UTF-8
Pakiet do manipulacji i anlizy duwymiarowych geoptrzestrzennych
geometrii. Bazuje na GEOS, nie zajmuje się formatami danych czy
układami odniesnienia danych.

%prep
%setup -q -n Shapely-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

#%if %{with python2}
#install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{pypi_name}-%{version}
#cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-%{pypi_name}-%{version}
#find $RPM_BUILD_ROOT%{_examplesdir}/python-%{pypi_name}-%{version} -name '*.py' \
#	| xargs sed -i '1s|^#!.*python\b|#!%{__python}|'
#%endif
#%if %{with python3}
#install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{pypi_name}-%{version}
#cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{pypi_name}-%{version}
#find $RPM_BUILD_ROOT%{_examplesdir}/python3-%{pypi_name}-%{version} -name '*.py' \
#	| xargs sed -i '1s|^#!.*python\b|#!%{__python3}|'
#%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
# %doc CHANGES.txt CREDITS.txt HISTORY.txt README.txt
%dir %{py_sitedir}/%{module}
# %{py_sitescriptdir}/%{module}/ctypes_declarations.py
%{py_sitedir}/%{module}/*.py[co]

%dir %{py_sitedir}/%{module}/algorithms
%{py_sitedir}/%{module}/algorithms/*.py[co]
%dir %{py_sitedir}/%{module}/examples
%{py_sitedir}/%{module}/examples/*.py[co]
%dir %{py_sitedir}/%{module}/geometry
%{py_sitedir}/%{module}/geometry/*.py[co]
%dir %{py_sitedir}/%{module}/speedups
%attr(755,root,root) %{py_sitedir}/%{module}/speedups/*.so
%{py_sitedir}/%{module}/speedups/*.py[co]
%dir %{py_sitedir}/%{module}/vectorized
%{py_sitedir}/%{module}/vectorized/*.py[co]
%{py_sitedir}/Shapely-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/__pycache__
# %{py_sitescriptdir}/%{module}/ctypes_declarations.py
%{py3_sitedir}/%{module}/*.py

%dir %{py3_sitedir}/%{module}/algorithms
%{py3_sitedir}/%{module}/algorithms/__pycache__
%{py3_sitedir}/%{module}/algorithms/*.py
%dir %{py3_sitedir}/%{module}/examples
%{py3_sitedir}/%{module}/examples/__pycache__
%{py3_sitedir}/%{module}/examples/*.py
%dir %{py3_sitedir}/%{module}/geometry
%{py3_sitedir}/%{module}/geometry/__pycache__
%{py3_sitedir}/%{module}/geometry/*.py
%dir %{py3_sitedir}/%{module}/speedups
%{py3_sitedir}/%{module}/speedups/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/speedups/*.so
%{py3_sitedir}/%{module}/speedups/*.py
%dir %{py3_sitedir}/%{module}/vectorized
%{py3_sitedir}/%{module}/vectorized/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/vectorized/*.so
%{py3_sitedir}/%{module}/vectorized/*.py
%{py3_sitedir}/Shapely-*.egg-info
%endif
