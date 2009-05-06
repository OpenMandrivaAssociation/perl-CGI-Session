%define module  CGI-Session
%define name	perl-%{module}
%define version 4.41
%define release %mkrel 1

%define _requires_exceptions perl(DBD::Pg)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary: 	Persistent session data in CGI applications
License: 	GPL or Artistic
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.bz2
BuildRequires:  perl(CGI)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(CGI::Simple)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
CGI-Session is a Perl5 library that provides an easy, reliable and
modular session management system across HTTP requests. Persistency is a
key feature for such applications as shopping carts,
login/authentication routines, and application that need to carry data
accross HTTP requests. CGI::Session does that and many more 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f  t/g4_mysql.t # no database available for testing
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README INSTALL
%{perl_vendorlib}/CGI
%{_mandir}/*/*



