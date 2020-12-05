Name: biosdisk
Version: 1.01
Release: 1
Summary: Creating BIOS flash floppy images for DELL machines
License: GPL
Group:   System/Kernel and hardware 
URL: 	 http://linux.dell.com/biosdisk/
Source:  https://github.com/dell/biosdisk/archive/%{version}/%{name}-%{version}.tar.gz
Requires: python
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.75-5mdv2011.0
+ Revision: 616773
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.75-4mdv2010.0
+ Revision: 424624
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.75-3mdv2009.0
+ Revision: 243319
- rebuild

* Mon Feb 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2008.1
+ Revision: 165154
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 0.65-2mdv2008.0
+ Revision: 63761
- Import biosdisk



* Sat Nov 26 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.65-2mdk
- fix description (#16579)

* Fri Jun 24 2005 Erwan Velu <velu@seanodes.com> 0.65-1mdk
- Initial release
