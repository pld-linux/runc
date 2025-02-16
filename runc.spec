Summary:	CLI tool for spawning and running containers
Name:		runc
Version:	1.2.4
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/opencontainers/runc/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	24b46ef81d25aadf0d333896007a3ee4
URL:		https://www.opencontainers.org/
BuildRequires:	golang >= 1.22
BuildRequires:	libseccomp-devel
BuildRequires:	rpmbuild(macros) >= 2.009
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

%description
runc is a CLI tool for spawning and running containers on Linux
according to the OCI specification.

%prep
%setup -q

%build
%{__make} runc \
	GO="%__go"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	BINDIR="%{_bindir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGELOG,CONTRIBUTING,EMERITUS,MAINTAINERS_GUIDE,PRINCIPLES,README,SECURITY}.md
%attr(755,root,root) %{_bindir}/runc
