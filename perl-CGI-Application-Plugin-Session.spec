#
# Conditional build:
%bcond_with	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Application-Plugin-Session
Summary:	CGI::Application::Plugin::Session
Name:		perl-CGI-Application-Plugin-Session
Version:	1.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	532eaa718148dde7648723df3ce79350
URL:		http://search.cpan.org/dist/CGI-Application-Plugin-Session/
BuildRequires:	perl-CGI-Application >= 3.21
BuildRequires:	perl-CGI-Session >= 3.95
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-build >= 4.3-0.20030515.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application::Plugin::Session - add CGI::Session support
to CGI::Application

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/CGI/Application/Plugin/*.pm
#%{perl_vendorlib}/CGI/Application/Plugin/Session
%{_mandir}/man3/*
