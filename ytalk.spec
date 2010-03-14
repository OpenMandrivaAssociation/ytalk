%define	name	ytalk
%define	release	%mkrel 6
%define	version	3.3.0

Summary:	A chat program
Summary(de):	benutzt das Internet-Talk-Protokoll zum Erstellen von Multiuser-Chat-Sitzungen 
Summary(fr):	Utilise le protocole talk pour cr�er des discussions multi-utilisateurs
Summary(tr):	Talk protokolu kullanarak ikiden fazla ki�inin konu�mas�n� sa�lar
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
ytalk ist eine Erweiterung des herk�mmlichen Internet-'talk'-Protokolls, die
mehr als zwei Benutzer pro Unterhaltung und die Umleitung von Programmausgaben
an andere erm�glicht und ein einfaches Befehlsmen� enth�lt. Es verwendet
denselben Talk-D�mon wie das Standardprogramm.

%description -l fr
ytalk est une extension du protocole standard Internet 'talk' qui accepte plus
de deux utilisateurs par conversation, la redirection des affichages aux
autres, aussi bien que menus de commandes simples � utiliser. Il utilise le
m�me d�mon que le programme talk.

%description -l tr
ytalk, standart talk yaz�l�m�n�n geli�mi� bir s�r�m�d�r. �kiden fazla
ki�inin ayn� anda konu�malar�n� ve program ��kt�lar�n�n kullan�c�lara
y�nlendirilmelerini sa�lar. Kolay kullan�labilir bir komut men�s� i�erir.
Standart talkd daemon'u kullan�r.

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
