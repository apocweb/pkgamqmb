.PHONY: all clean re

TARBALL=apache-activemq-5.5.0.tar.gz

all: $(TARBALL)

$(TARBALL):
	tar cfz $(TARBALL) etc usr var

clean:
	rm -f $(TARBALL)

