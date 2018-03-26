Name:       debootstrap

Summary:    Debian bootstrap script
Version:    0
Release:    1
Group:      Tools
License:    GPL
URL:        http://anonscm.debian.org/gitweb/?p=d-i/debootstrap.git
Source0:    %{name}-%{version}.tar.gz
Source1:    devices.tar.gz

%description
Debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this by
downloading .deb files from a mirror site, and carefully unpacking them
into a directory which can eventually be chrooted into.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/debootstrap
mkdir -p $RPM_BUILD_ROOT%{_datadir}/debootstrap/scripts
# mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
/bin/cp -a scripts/* $RPM_BUILD_ROOT%{_datadir}/debootstrap/scripts
/bin/cp functions $RPM_BUILD_ROOT%{_datadir}/debootstrap
/bin/cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/debootstrap
# /bin/cat debootstrap.8 | gzip -9 > $RPM_BUILD_ROOT%{_mandir}/man8/debootstrap.8.gz
/bin/cat debootstrap | sed 's/@VERSION/%{version}/g' > $RPM_BUILD_ROOT%{_sbindir}/debootstrap
/bin/chmod +x $RPM_BUILD_ROOT%{_sbindir}/debootstrap

%files
%defattr(-,root,root,-)
%{_sbindir}/debootstrap
%dir %{_datadir}/debootstrap
%dir %{_datadir}/debootstrap/scripts
%{_datadir}/debootstrap/functions
%{_datadir}/debootstrap/devices.tar.gz
%{_datadir}/debootstrap/scripts/*
