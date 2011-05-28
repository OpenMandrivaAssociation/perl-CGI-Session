%define upstream_name    CGI-Session
%define upstream_version 4.42

%define _requires_exceptions perl(DBD::Pg)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	Persistent session data in CGI applications
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(CGI)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(CGI::Simple)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description 
CGI-Session is a Perl5 library that provides an easy, reliable and
modular session management system across HTTP requests. Persistency is a
key feature for such applications as shopping carts,
login/authentication routines, and application that need to carry data
accross HTTP requests. CGI::Session does that and many more 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
