%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	fo2pdf
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - converts a xsl-fo file to pdf/ps/pcl/text/etc
Summary(pl):	%{_pearname} - konwersja xsl-fo na pdf/ps/pcl/text/etc
Name:		php-pear-%{_pearname}
Version:	0.98
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a7ba81edf4149ab88819657cb9fab8f4
URL:		http://pear.php.net/package/XML_fo2pdf/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a xsl-fo file to pdf/ps/pcl/text/etc with the help of
apache-fop.

In PEAR status of this package is: %{_status}.

%description -l pl
Konwertuje pliki xsl-fo na pdf/ps/pcl/text/etc przy pomocy apache-fop.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
