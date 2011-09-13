.PHONY: all clean re rpm

VERSION=5.5.0
RELEASE=1
TARBALL=apache-activemq-$(VERSION).tar.gz
SPEC=apache-activemq-$(VERSION)-$(RELEASE).spec
RPM=~/rpmbuild/RPMS/noarch/apache-activemq-$(VERSION)-$(RELEASE).noarch.rpm

all: $(TARBALL) $(RPM)

$(TARBALL):
	tar cfz $(TARBALL) etc usr var

clean:
	rm -f $(TARBALL)

re: clean all

rpm: $(RPM)

$(RPM): $(TARBALL) $(SPEC)
	cp $(TARBALL) ~/rpmbuild/SOURCES/
	rpmbuild -ba $(SPEC)
