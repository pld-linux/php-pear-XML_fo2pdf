%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	fo2pdf
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - converts a xsl-fo file to pdf/ps/pcl/text/etc
Summary(pl):	%{_pearname} - konwersja xsl-fo na pdf/ps/pcl/text/etc
Name:		php-pear-%{_pearname}
Version:	0.98
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	a7ba81edf4149ab88819657cb9fab8f4
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/XML_fo2pdf/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a xsl-fo file to pdf/ps/pcl/text/etc with the help of
apache-fop.

%description -l pl
Konwertuje pliki xsl-fo na pdf/ps/pcl/text/etc przy pomocy apache-fop.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README*,*.fo}
%{php_pear_dir}/%{_class}/*.php
