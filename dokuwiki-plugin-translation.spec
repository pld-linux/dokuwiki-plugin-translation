%define		plugin		translation
Summary:	DokuWiki translation plugin
Summary(pl.UTF-8):	Wtyczka translation dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20080812
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.splitbrain.org/download/snapshots/translation-plugin-latest.tgz
# Source0-md5:	9a00bea4664a9de916228611e56ec84d
Source1:	dokuwiki-find-lang.sh
URL:		http://wiki.splitbrain.org/plugin:translation
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Help with translation efforts in a multilingual wiki. Similar to
nsrelation.

%description -l pl.UTF-8
Wtyczka do dokuwiki ułatwiająca tworzenie wersji wielojęzykowych.
Podobna do wtyczki nsrelation.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{CREDITS,changelog}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc info
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
