%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

Name:           rpm-py311-macro-override
Summary:        RPM macros to build Python 3.11 on EL9
License:        GPL-3

Version:        1.0.0
Release:        1%{?dist}

# Macro files
Source001:      macros.aaa-python311-override

Source100:      LICENSE

URL:            https://github.com/Odilhao/rpm-py311-macro-override

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-devel
Requires: python3.11-rpm-macros

%description
%{summary}

%package -n python%{python3_pkgversion}-rpm-py311-macro-override
Summary:  %{summary}
%description -n python%{python3_pkgversion}-rpm-py311-macro-override
This package contains macros to build python 3.11 packages

%prep
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .

%build
# nothing to do, sources are not buildable

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -pm 644 macros.aaa-python311-override %{buildroot}%{_rpmmacrodir}/

%files
%{_rpmmacrodir}/macros.aaa-python311-override

%license LICENSE

%files -n python%{python3_pkgversion}-rpm-py311-macro-override
%{_rpmmacrodir}/macros.aaa-python311-override
%license LICENSE


%changelog
* Fri Nov 10 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-1
- Inital packages
