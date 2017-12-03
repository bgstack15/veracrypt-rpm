%global pname VeraCrypt
Name:		veracrypt
Version:	1.22
Release:	0%{?dist}
Summary:	Disk encryption with strong security based on TrueCrypt

Group:	Applications/File
License:	GPL 3.0 
URL:		http://bgstack15.wordpress.com/
Source0:	veracrypt.tgz
#Source1: https://github.com/veracrypt/VeraCrypt/archive/master.tar.gz
Source1:	https://albion320.no-ip.biz/smith122/repo/patch/%{name}/%{pname}-%{version}.tar.gz
Source2:	https://albion320.no-ip.biz/smith122/repo/patch/%{name}/%{pname}-%{version}%{?dist}.patch

Packager:	Bgstack15 <bgstack15@gmail.com>
Buildarch:	x86_64
BuildRequires: gcc-c++
BuildRequires: wxGTK3-devel
BuildRequires: yasm
BuildRequires: fuse-devel
BuildRequires: /usr/bin/7za
Requires:	wxGTK3

%description
VeraCrypt is a free open source disk encryption software for Windows, Mac OSX and Linux. Brought to you by IDRIX (https://www.idrix.fr) and based on TrueCrypt 7.1a.

#%global debug_package %{nil}

%prep
#%setup -q
%setup -c -n %{name}-%{version}
cd %{name}-%{version}/%{_datadir}/%{name}/source
tar -zxf %{SOURCE1}
cp %{SOURCE2} .
patch -p0 < %{SOURCE2}

%build
%make_build -C %{name}-%{version}/%{_datadir}/%{name}/source/%{pname}-master/src

%install
rm -rf %{buildroot}
rsync -av ./%{name}-%{version}/ %{buildroot}/ --exclude='**/.*.swp' --exclude='**/.git'
# this package really wants to work in PWD, because a make_install -C fails.
pushd %{name}-%{version}/%{_datadir}/%{name}/source/%{pname}-master/src
# make install fails without this directory despite that the package installs to Setup/Linux/usr
mkdir -p ./Main/Setup/Linux/usr
%make_install
cp -pr ./Setup/Linux%{_prefix} %{buildroot}%{_datadir}/%{name}/app%{_prefix}
popd
# clean up the source
find %{buildroot}%{_datadir}/%{name}/source/ -mindepth 1 ! -regex '.*\.patch' -exec /bin/rm -rf {} \; ||:

%clean
rm -rf %{buildroot}
exit 0

%post
# rpm post 2017-12-02

# Deploy app symlinks
ln -s %{_datadir}/%{name}/app%{_bindir}/%{name} %{_bindir}/%{name} ||:

# Deploy icons
ln -s %{_datadir}/%{name}/app%{_datadir}/pixmaps/%{name}.xpm %{_datadir}/pixmaps/%{name}.xpm ||:

# Deploy desktop files
desktop-file-install --rebuild-mime-info-cache %{_datadir}/%{name}/app%{_datadir}/applications/%{name}.desktop 1>/dev/null 2>&1 ||:

exit 0

%preun
# rpm preun 2017-12-02
exit 0

%postun
# rpm postun 2017-12-02
if test "$1" = "0";
then
{
   # total uninstall

   # Remove desktop files
   rm -f %{_datadir}/applications/%{name}.desktop
   which update-desktop-database && update-desktop-database -q %{_datadir}/applications &

   # Remove icons
   rm -f %{_datadir}/pixmaps/%{name}.xpm ||:

   # Remove app symlinks
   rm -f %{_bindir}/%{name} ||:

} 1>/dev/null 2>&1
fi 
exit 0

%files
%dir /usr/share/veracrypt
%dir /usr/share/veracrypt/build
%dir /usr/share/veracrypt/inc
%doc %attr(444, -, -) /usr/share/doc/veracrypt/REFERENCES.txt
%doc %attr(444, -, -) /usr/share/doc/veracrypt/README.txt
/usr/share/doc/veracrypt/version.txt
/usr/share/veracrypt/doc
/usr/share/veracrypt/build/get-files
/usr/share/veracrypt/build/files-for-versioning.txt
/usr/share/veracrypt/build/get-sources
/usr/share/veracrypt/build/veracrypt.spec
/usr/share/veracrypt/build/pack
/usr/share/veracrypt/app
/usr/share/veracrypt/inc/sha256sum.txt
/usr/share/veracrypt/inc/veracrypt_ver.txt
/usr/share/veracrypt/source
/usr/share/veracrypt/source/VeraCrypt-1.22.fc26.patch

%changelog
* Sat Dec  2 2017 B Stack <bgstack15@gmail.com> 1.22-0
- Initial rpm built.
