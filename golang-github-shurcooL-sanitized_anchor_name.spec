#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-shurcooL-sanitized_anchor_name
Version  : 10ef21a441db47d8b13ebcc5fd2310f636973c77
Release  : 6
URL      : https://github.com/shurcooL/sanitized_anchor_name/archive/10ef21a441db47d8b13ebcc5fd2310f636973c77.tar.gz
Source0  : https://github.com/shurcooL/sanitized_anchor_name/archive/10ef21a441db47d8b13ebcc5fd2310f636973c77.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT

%description
# sanitized_anchor_name [![Build Status](https://travis-ci.org/shurcooL/sanitized_anchor_name.svg?branch=master)](https://travis-ci.org/shurcooL/sanitized_anchor_name) [![GoDoc](https://godoc.org/github.com/shurcooL/sanitized_anchor_name?status.svg)](https://godoc.org/github.com/shurcooL/sanitized_anchor_name)

%prep
%setup -q -n sanitized_anchor_name-10ef21a441db47d8b13ebcc5fd2310f636973c77

%build
export LANG=C

%install
gopath="/usr/lib/golang-dist"
library_path="github.com/shurcooL/sanitized_anchor_name"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang-dist/src/github.com/shurcooL/sanitized_anchor_name/main.go
/usr/lib/golang-dist/src/github.com/shurcooL/sanitized_anchor_name/main_test.go
