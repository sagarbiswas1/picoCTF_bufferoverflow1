# picoCTF_bufferoverflow1
picoCTF 2022 Buffer Overflow 1 Binary Exploitation

# Usage
```
flag.py [ HOST ] [ PORT ]
```
If the file command or read elf command not found error occurs while running this script, you need to install them.

**:: Install readelf ::**

**Kali Linux**
```
apt-get install binutils-mipsisa32r6el-linux-gnu
```
**Ubuntu**
```
apt-get install binutils-2.26
```
**Debian**
```
apt-get install binutils-multiarch
```
**Alpine**
```
apk add binutils
```
**Arch Linux**
```
pacman -S aarch64-linux-gnu-binutils
```
**CentOS**
```
yum install binutils
```
**Fedora**
```
dnf install binutils-arc-linux-gnu
```
**OS X**
```
brew install binutils
```
**Raspbian**
```
apt-get install binutils-multiarch
```
**Docker**
```
docker run cmd.cat/readelf readelf
```

**:: Install file ::**

```sudo apt install file```
