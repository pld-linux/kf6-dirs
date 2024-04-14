#
# Conditional build:
%bcond_with	tests		# build with tests
%define		__spec_clean_body	%{nil}
%define		_enable_debug_packages	0
Summary:	KDE Frameworks - common directories
Name:		kf6-dirs
Version:	6.1.0
Release:	1
License:	LGPL
Group:		X11/Libraries
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Frameworks - common directories.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_includedir}/KF6 \
	$RPM_BUILD_ROOT%{_datadir}/kdevappwizard/templates \
	$RPM_BUILD_ROOT%{_datadir}/kf6/{kcookiejar,widgets/pics,locale} \
	$RPM_BUILD_ROOT%{_datadir}/kio/servicemenus \
	$RPM_BUILD_ROOT%{_datadir}/{kservicetypes6,knotifications6,kservices6/{ServiceMenus,kded,kontact,searchproviders},kxmlgui6} \
	$RPM_BUILD_ROOT%{_datadir}/kpackage/{kcms,genericqml} \
	$RPM_BUILD_ROOT%{_datadir}/ksmserver \
	$RPM_BUILD_ROOT%{_datadir}/kstyle/themes \
	$RPM_BUILD_ROOT%{_datadir}/plasma/{look-and-feel,packages,plasmoids,shells} \
	$RPM_BUILD_ROOT%{_datadir}/remoteview \
	$RPM_BUILD_ROOT%{_datadir}/solid/actions \
	$RPM_BUILD_ROOT%{_datadir}/solid/devices \
	$RPM_BUILD_ROOT%{_datadir}/emoticons/Glass \
	$RPM_BUILD_ROOT%{_libexecdir}/kf6 \
	$RPM_BUILD_ROOT%{_libdir}/kf6 \
	$RPM_BUILD_ROOT%{_libdir}/qt6/plugins/kf6/{kded,parts,propertiesdialog,urifilters,org.kde.kwindowsystem.platforms} \
	$RPM_BUILD_ROOT%{_libdir}/qt6/plugins/{kcms,org.kde.kdecoration2,script} \
	$RPM_BUILD_ROOT%{_libdir}/qt6/qml/org/kde/{kconfig,kio,draganddrop,kcoreaddons,kquickcontrols,kquickcontrolsaddons,kwindowsystem,private/kquickcontrols,runnermodel} \
	$RPM_BUILD_ROOT%{_libdir}/qt6/qml/org/kde/plasma/private \
	$RPM_BUILD_ROOT%{_libdir}/qt6/qml/QtQuick/Controls/Styles \
	$RPM_BUILD_ROOT%{_libdir}/qt6/platformqml/touch/org/kde/plasma \
	$RPM_BUILD_ROOT%{_docdir}/HTML/{af,ca,cs,da,de,el,en,eo,es,et,fr,gl,he,hu,it,ja,ko,lt,nds,nl,nn,pl,pt,pt_BR,ro,ru,sl,sr,sr@latin,sv,tr,uk,wa,xh} \
	$RPM_BUILD_ROOT%{_sysconfdir}/xdg/ui


%clean
cd $RPM_BUILD_ROOT
check_filesystem_dirs() {
	RPMFILE=%{name}-%{version}-%{release}.%{_target_cpu}.rpm
	TMPFILE=$(mktemp)
	# NOTE:	we must exclude from check all existing dirs belonging to FHS
	find | sed -e 's|^\.||g' -e 's|^$||g' | LC_ALL=C sort | grep -v $TMPFILE | grep -E -v '^/(usr|usr/include|usr/lib|usr/lib64|usr/libx32|usr/libexec|usr/share|usr/share/doc|usr/share/applications|usr/share/icons|usr/lib/qt6|usr/lib64/qt6|usr/libx32/qt6|usr/lib/qt6/imports|usr/lib64/qt6/imports|usr/libx32/qt6/imports|usr/lib/qt6/imports/org|usr/lib64/qt6/imports/org|usr/libx32/qt6/imports/org|usr/lib/qt6/plugins|usr/lib64/qt6/plugins|usr/libx32/qt6/plugins|usr/lib/qt6/qml|usr/lib64/qt6/qml|usr/libx32/qt6/qml|usr/lib/qt6/qml/QtQuick|usr/lib64/qt6/qml/QtQuick|usr/libx32/qt6/qml/QtQuick|etc|etc/xdg)$' > $TMPFILE

	# find finds also '.', so use option -B for diff
	if rpm -qpl %{_rpmdir}/$RPMFILE | grep -v '^/$' | LC_ALL=C sort | diff -uB $TMPFILE -; then
		rm -rf $RPM_BUILD_ROOT
	else
		echo -e "\nNot so good, some directories are not included in package\n"
		exit 1
	fi
	rm -f $TMPFILE
}
check_filesystem_dirs

%files
%defattr(644,root,root,755)
%dir %{_includedir}/KF6
%dir %{_datadir}/emoticons
%dir %{_datadir}/emoticons/Glass
%dir %{_datadir}/kdevappwizard
%dir %{_datadir}/kdevappwizard/templates
%dir %{_datadir}/kf6
%dir %{_datadir}/kf6/kcookiejar
%dir %{_datadir}/kf6/locale
%dir %{_datadir}/kf6/widgets
%dir %{_datadir}/kf6/widgets/pics
%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%dir %{_datadir}/kservicetypes6
%dir %{_datadir}/kservices6
%dir %{_datadir}/kservices6/ServiceMenus
%dir %{_datadir}/kservices6/kded
%dir %{_datadir}/kservices6/kontact
%dir %{_datadir}/kservices6/searchproviders
%dir %{_datadir}/knotifications6
%dir %{_datadir}/kxmlgui6
%dir %{_datadir}/kpackage
%dir %{_datadir}/kpackage/genericqml
%dir %{_datadir}/kpackage/kcms
%dir %{_datadir}/ksmserver
%dir %{_datadir}/kstyle
%dir %{_datadir}/kstyle/themes
%dir %{_datadir}/plasma
%dir %{_datadir}/plasma/look-and-feel
%dir %{_datadir}/plasma/packages
%dir %{_datadir}/plasma/plasmoids
%dir %{_datadir}/plasma/shells
%dir %{_datadir}/remoteview
%dir %{_datadir}/solid
%dir %{_datadir}/solid/actions
%dir %{_datadir}/solid/devices
%dir %{_libexecdir}/kf6
%dir %{_libdir}/kf6
%dir %{_libdir}/qt6/plugins/org.kde.kdecoration2
%dir %{_libdir}/qt6/plugins/script
%dir %{_libdir}/qt6/plugins/kcms
%dir %{_libdir}/qt6/plugins/kf6
%dir %{_libdir}/qt6/plugins/kf6/kded
%dir %{_libdir}/qt6/plugins/kf6/org.kde.kwindowsystem.platforms
%dir %{_libdir}/qt6/plugins/kf6/parts
%dir %{_libdir}/qt6/plugins/kf6/propertiesdialog
%dir %{_libdir}/qt6/plugins/kf6/urifilters
%dir %{_libdir}/qt6/qml/QtQuick/Controls
%dir %{_libdir}/qt6/qml/QtQuick/Controls/Styles
%dir %{_libdir}/qt6/qml/org
%dir %{_libdir}/qt6/qml/org/kde
%dir %{_libdir}/qt6/qml/org/kde/kio
%dir %{_libdir}/qt6/qml/org/kde/draganddrop
%dir %{_libdir}/qt6/qml/org/kde/kconfig
%dir %{_libdir}/qt6/qml/org/kde/kcoreaddons
%dir %{_libdir}/qt6/qml/org/kde/kquickcontrols
%dir %{_libdir}/qt6/qml/org/kde/kquickcontrolsaddons
%dir %{_libdir}/qt6/qml/org/kde/kwindowsystem
%dir %{_libdir}/qt6/qml/org/kde/plasma
%dir %{_libdir}/qt6/qml/org/kde/plasma/private
%dir %{_libdir}/qt6/qml/org/kde/private
%dir %{_libdir}/qt6/qml/org/kde/private/kquickcontrols
%dir %{_libdir}/qt6/qml/org/kde/runnermodel
%dir %{_libdir}/qt6/platformqml
%dir %{_libdir}/qt6/platformqml/touch
%dir %{_libdir}/qt6/platformqml/touch/org
%dir %{_libdir}/qt6/platformqml/touch/org/kde
%dir %{_libdir}/qt6/platformqml/touch/org/kde/plasma
%dir %{_sysconfdir}/xdg/ui
%dir %{_docdir}/HTML/
%lang(af) %dir %{_docdir}/HTML/af
%lang(ca) %dir %{_docdir}/HTML/ca
%lang(cs) %dir %{_docdir}/HTML/cs
%lang(da) %dir %{_docdir}/HTML/da
%lang(de) %dir %{_docdir}/HTML/de
%lang(el) %dir %{_docdir}/HTML/el
%lang(en) %dir %{_docdir}/HTML/en
%lang(eo) %dir %{_docdir}/HTML/eo
%lang(es) %dir %{_docdir}/HTML/es
%lang(et) %dir %{_docdir}/HTML/et
%lang(fr) %dir %{_docdir}/HTML/fr
%lang(gl) %dir %{_docdir}/HTML/gl
%lang(he) %dir %{_docdir}/HTML/he
%lang(hu) %dir %{_docdir}/HTML/hu
%lang(it) %dir %{_docdir}/HTML/it
%lang(ja) %dir %{_docdir}/HTML/ja
%lang(ko) %dir %{_docdir}/HTML/ko
%lang(lt) %dir %{_docdir}/HTML/lt
%lang(nds) %dir %{_docdir}/HTML/nds
%lang(nl) %dir %{_docdir}/HTML/nl
%lang(nn) %dir %{_docdir}/HTML/nn
%lang(pl) %dir %{_docdir}/HTML/pl
%lang(pt) %dir %{_docdir}/HTML/pt
%lang(pt_BR) %dir %{_docdir}/HTML/pt_BR
%lang(ro) %dir %{_docdir}/HTML/ro
%lang(ru) %dir %{_docdir}/HTML/ru
%lang(sl) %dir %{_docdir}/HTML/sl
%lang(sr) %dir %{_docdir}/HTML/sr
%lang(sr@latin) %dir %{_docdir}/HTML/sr@latin
%lang(sv) %dir %{_docdir}/HTML/sv
%lang(tr) %dir %{_docdir}/HTML/tr
%lang(uk) %dir %{_docdir}/HTML/uk
%lang(wa) %dir %{_docdir}/HTML/wa
%lang(xh) %dir %{_docdir}/HTML/xh
