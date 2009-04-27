%define 	module	shapely
Summary:	Geospatial geometries, predicates, and operations for Python
Name:		python-%{module}
Version:	1.0.12
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
# Source0-md5:	0122c53ec3ba1c4b805afce43d0aa039
URL:		http://pypi.python.org/pypi/Shapely
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	geos >= 3.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shapely is a Python package for manipulation and analysis of 2D geospatial
geometries. It is based on GEOS. Shapely 1.0 is
not concerned with data formats or coordinate reference systems.

%prep
%setup -q -n Shapely-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name '*.py' \
	| grep -v ctypes_declarations | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt HISTORY.txt README.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/ctypes_declarations.py
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/geometry
%{py_sitescriptdir}/%{module}/geometry/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Shapely-*.egg-info
%endif
