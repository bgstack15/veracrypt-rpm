#Veracrypt README
Package source is the official veracrypt source on github, https://github.com/veracrypt/VeraCrypt

###How to maintain this package
####On the mirror server
Download the latest release tarball from:

    cd /mnt/public/www/smith122/repo/patch/veracrypt
    thisver=1.21
    curl -O https://github.com/veracrypt/VeraCrypt/archive/VeraCrypt_${thisver}.tar.gz
    # assemble patch file for each architecture (fc25, el7, etc.)
    # You need to cllect the sha256sum for each source object (tarball, patch, etc.) and put them in the usr/share/veracrypt/inc/sha256sum.txt file.
    sha256sum *.tar.gz *.tgz *.zip *.patch 1> sha256sum.txt 2>/dev/null

####On the rpmbuild server
curl http://albion320.no-ip.biz/smith122/repo/patch/veracrypt/sha256sum.txt > ~/rpmbuild/SOURCES/veracrypt-1.21-0/usr/share/veracrypt/inc/sha256sum.txt

###Reference
See REFERENCES.txt for full information about sources.

###Changelog
* Fri Dec  1 2017 B Stack <bgstack15@gmailcom> 1.21-0
- Initial rpm built.
