%define	name	ytalk
%define	release	%mkrel 10
%define	version	3.3.0

Summary:	A chat program
Summary(de):	benutzt das Internet-Talk-Protokoll zum Erstellen von Multiuser-Chat-Sitzungen 
Summary(fr):	Utilise le protocole talk pour créer des discussions multi-utilisateurs
Summary(tr):	Talk protokolu kullanarak ikiden fazla kiþinin konuþmasýný saðlar
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License:	BSD
Group:		Networking/Chat
BuildRequires:	ncurses-devel
Source0:	http://www.impul.se/ytalk/%{name}-%{version}.tar.bz2
Source1:	ytalkrc
URL:		http://www.impul.se/ytalk/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The YTalk program is essentially a chat program for multiple users. YTalk works
just like the UNIX talk program and even communicates with the same talk
daemon(s), but YTalk allows for multiple connections (unlike UNIX talk). YTalk
also supports redirection of program output to other users as well as an
easy-to-use menu of commands.

Install the ytalk package if you need a chat program for multiple users.

%prep
%setup -q

%build
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-9mdv2011.0
+ Revision: 671950
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 3.3.0-8
+ Revision: 635104
- add back prep section
- drop lang description
- rebuild
- tighten BR

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-7mdv2011.0
+ Revision: 608281
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-6mdv2010.1
+ Revision: 519085
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-5mdv2009.1
+ Revision: 317955
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-4mdv2008.1
+ Revision: 178768
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-3mdv2008.0
+ Revision: 73367
- Import ytalk



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.3.0-3mdv2007.0
- Rebuild

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.3.0-2mdk
- Rebuild

* Thu Jul 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.3.0-1mdk
- New release 3.3.0

* Mon Jan 10 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 3.2.0-1mdk
- 3.2.0

* Fri Dec 24 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 3.1.5-1mdk
- 3.1.5
- update url

* Sun Jul 25 2004 Per Ø€yvind Karlsen <peroyvind@linux-mandrake.com> 3.1.2-1mdk
- 3.1.2
- update url
- update %%docs

* Sat Jul 12 2003 Per Ã˜yvind Karlsen <peroyvind@sintrax.net> 3.1.1-8mdk
- rebuild
- cosmetics

* Tue Jun 19 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.1-7mdk
- remove unused patches
- minor spec fixes (noreplace, license, ...)

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.1.1-6mdk
- automatically added BuildRequires


* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.1-5mdk
- use new macros
- BM

* Thu Apr 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1.1-4mdk
- new groups
- added url
- added documentation

* Thu Mar 30 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.1.1-3mdk
- build for new environment
- clean up spec file by means of spechelper

* Wed Nov 03 1999 Jerome Martin <jerome@mandrakesoft.com>
- Rebuild for new distribution

* Sun Jul 18 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Updated description/summary (fr/de/tr)
- 3.1.1 :
	    + Now looks a bit harder for the fqdn of the current machine.
	    + Fixed problems with ncurses resizing under Linux, and (again) with
	      Ytalk shells under Solaris.
	    + YTalk now complains (and prints the right hostname) if a
	      connection is answered from an unexpected host.
	    + Fixed the checks to prevent user duplication (getting twice the
	      same user in an n-way talk where n>=4).
	    + More portability fixes for 64-bit machines.
	    + Fixed the "readdress" option somewhat.


* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Nov 22 1998 Preston Brown <pbrown@redhat.com>
- upgrade to ytalk 3.1

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
