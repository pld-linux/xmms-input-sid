Summary:	SIDPlay input plugin for X MultiMedia System
Summary(pl):	Wtyczka wej¶ciowa SIDPlay dla X MultiMedia System
Name:		xmms-input-sid
Version:	0.8.0beta8
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://tnsp.org/xs-files/xmms-sid-%{version}.tar.gz
# Source0-md5:	764e05e33bae112f6e26cc3212d855df
URL:		http://www.tnsp.org/xmms-sid.php
BuildRequires:	libsidplay2-devel
BuildRequires:	xmms-devel >= 1.2.5
Requires:	xmms >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS-SID is a plugin for XMMS which provides support for playing the
so-called "SID tunes", which are music from old Commodore computer
programs like games, demos, etc.

%description -l pl
XMMS-SID jest wtyczk± dla XMMS-a, która umo¿liwia odtwarzanie tak
zwanej "muzyki na SID-a", tzn. muzyki ze starych programów na
Commodore - gier, dem, itp.

%prep
%setup -q -n xmms-sid-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README README.bugreport THANKS TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
