Name: apache-activemq
Version: 5.5.0
Release: 1
Summary: Apache ActiveMQ
License: unknown
Distribution: Redhat
Group: Converted/unknown
Source: %{name}-%{version}.tar.gz
#Packager:
Buildarch: noarch
Requires: /sbin/chkconfig

%description
Apache ActiveMQ

%prep 
%setup -q -c %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mv * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/apache-activemq-5.5.0
/usr/local/activemq-instances
/etc/rc.d/init.d/activemq
/var/log/activemq

%post
/sbin/chkconfig --add activemq
chomd 1777 /var/log/activemq

%preun
/sbin/chkconfig --del activemq

%changelog
* Thu Sep 13 2011 Alexandre Bodin
- Initial package
