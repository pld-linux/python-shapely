# TODO: Package shapely/examples to _examplesdir ?
#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	shapely
Summary:	Geospatial geometries, predicates, and operations for Python
Summary(pl.UTF-8):	Geometrie, predykaty i operacje geoprzestrzenne dla Pythona
Name:		python-%{module}
# keep 1.7.x here for python2 support
Version:	1.7.1
Release:	6
License:	BSD
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
# Source0-md5:	2bf7bc1199b3a88b13c12109cd3d2429
URL:		https://pypi.org/project/Shapely
BuildRequires:	geos-devel >= 3.3
%if %{with python2}
BuildRequires:	python-Cython
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-numpy-devel
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-numpy-devel
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	geos >= 3.3
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shapely is a Python package for manipulation and analysis of 2D
geospatial geometries. It is based on GEOS. Shapely is not concerned
with data formats or coordinate reference systems.

%description -l pl.UTF-8
Pakiet do operacji i analizy dwuwymiarowych geometrii
geoprzestrzennych. Jest oparty na GEOS, nie zajmuje się formatami
danych czy układami odniesienia współrzędnych.

%package -n python3-%{module}
Summary:	Geospatial geometries, predicates, and operations for Python
Summary(pl.UTF-8):	Geometrie, predykaty i operacje geoprzestrzenne dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
Shapely is a Python package for manipulation and analysis of 2D
geospatial geometries. It is based on GEOS. Shapely is not concerned
with data formats or coordinate reference systems.

%description -n python3-%{module} -l pl.UTF-8
Pakiet do operacji i analizy dwuwymiarowych geometrii
geoprzestrzennych. Jest oparty na GEOS, nie zajmuje się formatami
danych czy układami odniesienia współrzędnych.

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

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/shapely/_geos.pxi
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/shapely/speedups/_speedups.{c,pyx}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/shapely/vectorized/_vectorized.{c,pyx}

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/shapely/_geos.pxi
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/shapely/speedups/_speedups.{c,pyx}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/shapely/vectorized/_vectorized.{c,pyx}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt LICENSE.txt README.rst
%dir %{py_sitedir}/%{module}
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
%attr(755,root,root) %{py_sitedir}/%{module}/vectorized/*.so
%{py_sitedir}/%{module}/vectorized/*.py[co]
%{py_sitedir}/Shapely-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt LICENSE.txt README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/__pycache__
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
