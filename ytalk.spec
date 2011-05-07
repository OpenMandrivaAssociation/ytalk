%define	name	ytalk
%define	release	%mkrel 9
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
