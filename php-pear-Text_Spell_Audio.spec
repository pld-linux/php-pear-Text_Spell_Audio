%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Spell_Audio
%define		_status		alpha
%define		_pearname	Text_Spell_Audio
Summary:	%{_pearname} - Generates a sound clip saying the contents of a string of characters
Summary(pl.UTF-8):	%{_pearname} - generowanie nagrania dźwiękowego z wymową zadanego łańcucha znaków
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c518dad23ca88ab2af6c81c2beb8c224
URL:		http://pear.php.net/package/Text_Spell_Audio/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Joins up multiple wav file sound clips of letters/numbers being
spoken, optionally adding distortion and echo. This could be use to
compliment an image-based CAPTCHA to enable people who are unable to
read the security image hear it read out instead.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten łączy wiele plików dźwiękowych w formacie wav zawierających
wymowę liter/cyfr, opcjonalnie dodając zniekształcenie bądź echo.
Dzięki temu możliwe jest stworzenie uzupełnienia do obrazkowego
CAPTCHA umożliwiając osobom, które z różnych względów nie są w stanie
odczytać obrazka, odsłuchanie zawartej w nim treści.

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
%doc install.log docs/Text_Spell_Audio/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/Spell/Audio.php
%{php_pear_dir}/data/Text_Spell_Audio
