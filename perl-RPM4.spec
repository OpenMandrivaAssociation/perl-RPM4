# This spec is in the SVN
# $Id: perl-RPM4.spec 141783 2007-03-12 14:05:45Z nanardon $

%define module	RPM4
%define name	perl-%{module}
%define version	0.23
%define release %mkrel 3

%define rpm_version %(rpm -q --queryformat '%|EPOCH?{[%{EPOCH}:%{VERSION}]}:{%{VERSION}}|' rpm)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl bindings to use rpmlib and manage hdlist files
License:	GPL
Group:		Development/Perl
Source:		%{module}-%{version}.tar.gz
Patch0:		RPM4-0.23-fix-build-with-rpm4422.patch
Url:		http://search.cpan.org/dist/RPM4/
BuildRequires: perl-devel >= 5.8.0
BuildRequires: rpm-devel
BuildRequires: perl-Digest-SHA1
BuildRequires: librpmconstant-devel
BuildRequires: packdrake
BuildRequires: perl-MDV-Packdrakeng
BuildRequires: gnupg
Requires:	perl
# requires rpm used for build because librpm API is not that stable
# (but not requiring same release, hopefully we won't break it patching rpm)
Requires:	rpm = %{rpm_version}

%description
This module provides a perl interface to the rpmlib.

It allows to write scripts to:
  - query rpm headers,
  - query rpm database,
  - build rpm specs,
  - install/uninstall specfiles,
  - check dependencies.

It include:
- rpm_produced, give what rpm will be produced by a src.rpm or a specfile.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
PERL5DIR=`pwd`/src/blib/arch TMPDIR=/tmp %make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog README
%doc examples
%_bindir/*
%{perl_vendorarch}/*
%{_mandir}/*/*
