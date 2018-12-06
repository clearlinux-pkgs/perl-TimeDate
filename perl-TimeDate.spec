#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-TimeDate
Version  : 2.30
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/G/GB/GBARR/TimeDate-2.30.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GB/GBARR/TimeDate-2.30.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
This is the perl5 TimeDate distribution. It requires perl version 5.003
or later

%package dev
Summary: dev components for the perl-TimeDate package.
Group: Development
Provides: perl-TimeDate-devel = %{version}-%{release}

%description dev
dev components for the perl-TimeDate package.


%prep
%setup -q -n TimeDate-2.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Date/Format.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Afar.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Amharic.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Austrian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Brazilian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Bulgarian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Chinese.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Chinese_GB.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Czech.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Danish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Dutch.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/English.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Finnish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/French.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Gedeo.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/German.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Greek.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Hungarian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Icelandic.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Italian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Norwegian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Oromo.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Romanian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Russian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Russian_cp1251.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Russian_koi8r.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Sidama.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Somali.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Spanish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Swedish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Tigrinya.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/TigrinyaEritrean.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/TigrinyaEthiopian.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Language/Turkish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Date/Parse.pm
/usr/lib/perl5/vendor_perl/5.28.1/Time/Zone.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Date::Format.3
/usr/share/man/man3/Date::Language.3
/usr/share/man/man3/Date::Language::Bulgarian.3
/usr/share/man/man3/Date::Language::Hungarian.3
/usr/share/man/man3/Date::Parse.3
/usr/share/man/man3/Time::Zone.3
