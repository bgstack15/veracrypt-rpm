# Veracrypt rpm README
Package source is the official veracrypt source on github, https://github.com/veracrypt/VeraCrypt

### How to maintain this package
#### On the mirror server
Download the latest source code:

    cd /mnt/public/www/smith122/repo/patch/veracrypt
    thisver=1.22
    /bin/rm -f ./VeraCrypt-master.*
    wget --content-disposition https://github.com/veracrypt/VeraCrypt/archive/master.tar.gz
    mv VeraCrypt-master.tar.gz VeraCrypt-${thisver}.tar.gz
    # assemble patch file for each architecture. See heading "Making a patch" below.
    # You need to collect the sha256sum for each source object (tarball, patch, etc.) and put them in the usr/share/veracrypt/inc/sha256sum.txt file.
    sha256sum *.tar.gz *.tgz *.zip *.patch 1> sha256sum.txt 2>/dev/null

#### On the rpmbuild server

    curl http://albion320.no-ip.biz/smith122/repo/patch/veracrypt/sha256sum.txt > ~/rpmbuild/SOURCES/veracrypt-1.22-0/usr/share/veracrypt/inc/sha256sum.txt

### Making a patch

    thisver=1.22
    mdkir ~/dev && cd ~/dev
    tar -zxf VeraCrypt-master.tar.gz
    cp -pr VeraCrypt-master VeraCrypt-fc26

Perform any changes to files in the second directory.

    cd ~/dev
    diff -Naur VeraCrypt-master VeraCrypt-fc26 > VeraCrypt-${thisver}.fc26.patch

And copy the files to the mirror server.

### Reference
See REFERENCES.txt for full information about sources.

### Changelog
* Sat Dec  2 2017 B Stack <bgstack15@gmail.com> 1.22-0
- Initial rpm built.
