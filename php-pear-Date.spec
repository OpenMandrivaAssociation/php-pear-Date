%define		_class		Date
%define		upstream_name	%{_class}

%define		_requires_exceptions pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	1.5.0a2
Release:	%mkrel 1
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

# cleanup
rm -f %{buildroot}%{_datadir}/pear/data/Date/README

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
