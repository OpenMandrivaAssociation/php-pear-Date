%define		_class		Date
%define		upstream_name	%{_class}

%define		_requires_exceptions pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	1.4.7
Release:	%mkrel 9
Summary:	Date and time zone classes
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Date/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Generic classes for representation and manipulation of dates, times
and time zones without the need of timestamps, which is a huge
limitation for PHP programs. Includes time zone data, time zone
conversions and many date/time conversions. It does not rely on 32-bit
system date stamps, so you can display calendars and compare dates
that date pre 1970 and post 2038. This package also provides a class
to convert date strings between Gregorian and Human calendar formats.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-8mdv2011.0
+ Revision: 667493
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-7mdv2011.0
+ Revision: 607095
- rebuild

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.7-6mdv2010.1
+ Revision: 479264
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.7-5mdv2010.0
+ Revision: 426608
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-4mdv2009.1
+ Revision: 321807
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.7-3mdv2009.0
+ Revision: 224692
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-2mdv2008.1
+ Revision: 178505
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-1mdv2008.0
+ Revision: 15427
- fix a silly typo
- 1.4.7


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.6-1mdv2007.0
+ Revision: 81084
- Import php-pear-Date

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.6-1mdk
- 1.4.6
- new group (Development/PHP)

* Sun Nov 06 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-1mdk
- 1.4.5

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-8mdk
- rebuilt to fix auto deps

* Tue Aug 09 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-7mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sat Jul 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-6mdk
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-5mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-4mdk
- fix deps

* Thu Jun 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-3mdk
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.4.3-2mdk
- fix pre/post

* Wed Jan 19 2005 Pascal Terjan <pterjan@mandrake.org> 1.4.3-1mdk
- Updated

* Thu Feb 12 2004 Pascal Terjan <pterjan@mandrake.org> 1.4-4mdk
- Own tests/Date

* Sun Jan 04 2004 Pascal Terjan <pterjan@mandrake.org> 1.4-3mdk
- Register the package into pear

* Thu Jan 01 2004 Pascal Terjan <pterjan@mandrake.org> 1.4-2mdk
- Fix directories ownership

* Sun Dec 28 2003 Pascal Terjan <pterjan@mandrake.org> 1.4-1mdk
- First mdk package

