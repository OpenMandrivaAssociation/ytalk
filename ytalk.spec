%define	name	ytalk
%define	release	%mkrel 6
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
BuildRequires:	X11-devel gpm-devel ncurses-devel
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

%description -l	de
ytalk ist eine Erweiterung des herkömmlichen Internet-'talk'-Protokolls, die
mehr als zwei Benutzer pro Unterhaltung und die Umleitung von Programmausgaben
an andere ermöglicht und ein einfaches Befehlsmenü enthält. Es verwendet
denselben Talk-Dämon wie das Standardprogramm.

%description -l fr
ytalk est une extension du protocole standard Internet 'talk' qui accepte plus
de deux utilisateurs par conversation, la redirection des affichages aux
autres, aussi bien que menus de commandes simples à utiliser. Il utilise le
même démon que le programme talk.

%description -l tr
ytalk, standart talk yazýlýmýnýn geliþmiþ bir sürümüdür. Ýkiden fazla
kiþinin ayný anda konuþmalarýný ve program çýktýlarýnýn kullanýcýlara
yönlendirilmelerini saðlar. Kolay kullanýlabilir bir komut menüsü içerir.
Standart talkd daemon'u kullanýr.

%prep
%setup -q

%build
%configure
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
