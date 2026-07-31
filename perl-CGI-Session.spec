%define upstream_name    CGI-Session
%define upstream_version 4.49
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBD::Pg\\)'
%else
%define _requires_exceptions perl(DBD::Pg)
%endif

Name:		perl-%{upstream_name}
Version:	4.49
Release:	28

Summary:	Persistent session data in CGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/cromedome/cgi-session
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Session-4.49.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DB_File)
BuildRequires:	perl(FreezeThaw)
BuildRequires:	perl(CGI::Simple)
BuildArch:	noarch

%description 
CGI-Session is a Perl5 library that provides an easy, reliable and
modular session management system across HTTP requests. Persistency is a
key feature for such applications as shopping carts,
login/authentication routines, and application that need to carry data
accross HTTP requests. CGI::Session does that and many more 

%prep
%setup -q -n CGI-Session-4.49

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%make_install
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes README INSTALL
%{perl_vendorlib}/CGI
%{_mandir}/*/*


