%define name biosdisk
%define version 0.75
%define release %mkrel 3

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Creating BIOS flash floppy images for DELL machines
License: GPL
Group:   System/Kernel and hardware 
URL: 	 http://linux.dell.com/biosdisk/
Source:  http://linux.dell.com/biosdisk/%{name}-%{version}-2.tar.gz
Requires: python >= 2.2
Requires: dos2unix
Requires: syslinux
Requires: wget
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Biosdisk is a utility that can be used to make a FreeDOS floppy boot image
that can be used to flash a Dell system BIOS with Linux.


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/var/lib/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}


#place files
install -m 755 biosdisk %{buildroot}%{_sbindir}
install -m 755 blconf %{buildroot}%{_sbindir}
#install -m 755 geturl %{buildroot}/usr/sbin
install -m 644 dosdisk.img %{buildroot}%{_datadir}/%{name}
install -m 644 biosdisk.conf %{buildroot}%{_sysconfdir}
install -m 644 biosdisk-mkrpm-redhat-template.spec %{buildroot}%{_datadir}/%{name}
install -m 644 biosdisk-mkrpm-generic-template.spec %{buildroot}%{_datadir}/%{name}
install -m 644 biosdisk.8.gz %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%post
#copy memdisk to /boot
if ! [ -e /boot/memdisk ]; then
    for i in /usr/lib/syslinux/memdisk /usr/share/syslinux/memdisk
    do
        if [ -e $i ]; then
            cp -f $i /boot
        fi
    done
fi

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_sbindir}/biosdisk
%attr(0755,root,root) %{_sbindir}/blconf
#%attr(0755,root,root) %{_sbindir}geturl
/var/lib/%{name}/
%{_datadir}/%{name}/
%config(noreplace) %{_sysconfdir}/biosdisk.conf
%doc %{_mandir}/man8/biosdisk.8.*
%doc COPYING ChangeLog AUTHORS README INSTALL TODO README.dosdisk VERSION

