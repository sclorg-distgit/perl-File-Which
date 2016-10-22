%{?scl:%scl_package perl-File-Which}

Name:           %{?scl_prefix}perl-File-Which
Version:        1.21
Release:        3%{?dist}
Summary:        Portable implementation of the 'which' utility
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-Which/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PL/PLICEASE/File-Which-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.60
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Env)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.80
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.60

# Remove under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /%{?scl_prefix}perl(File::Spec)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(File::Spec\\)$
%endif

%description
File::Which is a portable implementation (in Perl) of 'which', and can
be used to get the absolute filename of an executable program
installed somewhere in your PATH, or just check for its existence.

%prep
%setup -q -n File-Which-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Which.3*

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 1.21-3
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-2
- Perl 5.24 rebuild

* Thu Mar 03 2016 Tom Callaway <spot@fedoraproject.org> - 1.21-1
- update to 1.21

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Tom Callaway <spot@fedoraproject.org> - 1.19-1
- update to 1.19

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Paul Howarth <paul@city-fan.org> - 1.18-4
- No longer needs any non-core buildreqs, and hence bootstrapping
- Drop references to pwhich, which is no longer included
- This release by PLICEASE → update source URL

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-2
- Perl 5.22 rebuild

* Tue May 26 2015 Tom Callaway <spot@fedoraproject.org> - 1.18-1
- update to 1.18

* Thu Jan 15 2015 Petr Pisar <ppisar@redhat.com> - 1.09-19
- Specify all dependencies

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-18
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-15
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.09-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Petr Šabata <contyk@redhat.com> - 1.09-11
- Specify all dependencies
- Modernize spec
- Drop command macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.09-9
- Perl 5.16 re-rebuild of bootstrapped packages

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.09-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-6
- Perl mass rebuild
- add perl_bootstrap macro

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.09-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 1.09-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-4
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-3
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Dec 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-2
- find: fixed arguments order.

* Sun Dec 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build.
