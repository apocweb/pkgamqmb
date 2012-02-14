Name: apache-activemq
Version: 5.5.0
Release: 4
Summary: Apache ActiveMQ
License: unknown
Distribution: Redhat
Group: Converted/unknown
Source: %{name}-%{version}.tar.gz
Buildroot: /var/tmp/%{name}-root
Packager: Alexandre Bodin
Buildarch: noarch
Requires: /sbin/chkconfig

%description
Apache ActiveMQ

%prep
# preparation step: untar the source tarball
%setup -q -c %{name}-%{version}

%build
# nothing to build

%install
# install step
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mv * $RPM_BUILD_ROOT

%clean
# clean step
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/apache-activemq-5.5.0
/usr/local/activemq-instances
/etc/rc.d/init.d/activemq

%post
# post install script (will be run as root)
/sbin/chkconfig --add activemq

%preun
# pre uninstall script (will be run as root)
/etc/rc.d/init.d/activemq stop
/sbin/chkconfig --del activemq

%changelog
* Tue Feb 14 2012 Alexandre Bodin
- Changing the log directory location
* Fri Oct 28 2011 Grégoire Barbier
- Fixed variable name in configuration (JVM_PARAMS instead of JVM_PARAMETERS)
- Added JMX remote parameter in default/sample configuration
* Wed Oct 12 2011 Alexandre Bodin
- Adding Oracle JDBC master slave sample mode
- Removing Pure master slave sample mode
* Thu Sep 13 2011 Alexandre Bodin
- Initial package
