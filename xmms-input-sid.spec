Summary:	SIDPlay input plugin for X MultiMedia System
Summary(pl):	Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±ca muzykê na "SID-a"
Name:		xmms-input-sid
Version:	0.8.0beta10
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://tnsp.org/xs-files/xmms-sid-%{version}.tar.gz
# Source0-md5:	f4cbd537ea6731a0a7e15dafa1cbd9c0
URL:		http://www.tnsp.org/xmms-sid.php
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	libsidplay-devel
%ifnarch alpha amd64
# its static "builders" cannot be linked into shared module on some archs
BuildRequires:	libsidplay2-devel >= 2.1.0
%endif
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
# nanosid-devel - http://www.sid6581.org/NanoSID/ but no sources???
BuildRequires:	xmms-devel >= 1.2.5
Requires:	xmms-libs >= 1.2.5
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-nanosid \
%ifarch alpha amd64
	--without-sidplay2
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
