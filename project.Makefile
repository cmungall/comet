## Add your own custom Makefile targets here

TTLS = $(wildcard examples/output/Dataset*.ttl)

t:
	echo $(TTLS)
# merge all in dir
examples/output/MERGED.ttl: $(TTLS)
	robot merge $(patsubst %, -i %, $(TTLS)) -i project/owl/comet.owl.ttl -o $@


examples/output/%-m.ttl: examples/output/%.ttl
	robot merge -i $< -i project/owl/comet.owl.ttl -o $@
