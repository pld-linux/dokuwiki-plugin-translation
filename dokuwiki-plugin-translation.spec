%define		plugin		translation
%define		snap		2008.04.01
Summary:	DokuWiki translation plugin
Summary(pl.UTF-8):	Wtyczka translation dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	%{snap}
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.splitbrain.org/download/snapshots/translation-plugin-latest.tgz
# Source0-md5:	9a00bea4664a9de916228611e56ec84d
Source1:	dokuwiki-find-lang.sh
URL:		http://wiki.splitbrain.org/plugin:translation
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{plugin}

%description
Plugin for DokuWiki.

%description -l pl.UTF-8
Wtyczka dla DokuWiki

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}
rm -f $RPM_BUILD_ROOT%{_plugindir}/{CREDITS,changelog}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc info.txt
%dir %{_plugindir}
%{_plugindir}/*.php
%{_plugindir}/*.css
%{_plugindir}/conf
