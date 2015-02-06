%define upstream_name    CGI-Session
%define upstream_version 4.48

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBD::Pg\\)'
%else
%define _requires_exceptions perl(DBD::Pg)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 4.48
Release:	3

Summary:	Persistent session data in CGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI-Session-4.48.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f  t/g4_mysql.t # no database available for testing
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes README INSTALL
%{perl_vendorlib}/CGI
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 4.420.0-2mdv2011.0
+ Revision: 680696
- mass rebuild

* Mon Aug 31 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.420.0-1mdv2011.0
+ Revision: 422882
- update to 4.42

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.410.0-1mdv2010.0
+ Revision: 403004
- rebuild using %%perl_convert_version

* Wed May 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.41-1mdv2010.0
+ Revision: 372684
- update to new version 4.41

* Wed Jan 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.38-2mdv2009.1
+ Revision: 326511
- don't require DBD::Pg

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.38-1mdv2009.1
+ Revision: 299375
- update to new version 4.38

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.37-1mdv2009.1
+ Revision: 297537
- update to new version 4.37

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.36-1mdv2009.1
+ Revision: 292031
- update to new version 4.36

* Thu Jul 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.35-1mdv2009.0
+ Revision: 236715
- update to new version 4.35

* Thu Jul 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.33-1mdv2009.0
+ Revision: 233336
- update to new version 4.33

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.32-1mdv2009.0
+ Revision: 227967
- update to new version 4.32

* Sat May 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.30-1mdv2009.0
+ Revision: 205413
- update to new version 4.30

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.20-1mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.20-1mdv2007.0
+ Revision: 111628
- new version

* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 4.14-1mdv2007.1
+ Revision: 73407
- import perl-CGI-Session-4.14-1mdv2007.0

* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.14-1mdv2007.0
- new version

* Wed May 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 4.13-1mdk
- New release 4.13

* Sun Apr 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.12-1mdk
- New version
- better summary
- better source URL
- better buildrequires syntax

* Fri Mar 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.10-1mdk
- New release 4.10

* Sat Mar 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.09-1mdk
- New release 4.09

* Thu Mar 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.08-1mdk
- 4.08

* Wed Mar 08 2006 Oden Eriksson <oeriksson@mandriva.com> 4.03-3mdk
- fix deps

* Sat Oct 08 2005 Nicolas Lécureuil <neoclust@mandriva.org> 4.03-2mdk
- Fix BuildRequires
- %%mkrel

* Fri Oct 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 4.03-1mdk
- New release 4.03

* Wed Sep 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 4.02-1mdk
- New release 4.02
- spec cleanup
- tests
- better url

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.95-4mdk
- fix buildrequires in a backward compatible way

* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.95-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.95-2mdk
- fixed dir ownership (distlint)


