.PHONY: all clean re rpm tar

VERSION=5.5.0
RELEASE=1
TARBALL=apache-activemq-$(VERSION).tar.gz
TARBALL_ROOTS=etc usr var
SPEC=apache-activemq-$(VERSION)-$(RELEASE).spec
RPM=~/rpmbuild/RPMS/noarch/apache-activemq-$(VERSION)-$(RELEASE).noarch.rpm

all: tar rpm

tar: $(TARBALL)

$(TARBALL): $(shell find $(TARBALL_ROOTS))
	tar cfz $(TARBALL) $(TARBALL_ROOTS)

clean:
	rm -f $(TARBALL)

re: clean all

rpm: $(RPM)

$(RPM): $(TARBALL) $(SPEC)
	cp $(TARBALL) ~/rpmbuild/SOURCES/
	rpmbuild -ba $(SPEC)
