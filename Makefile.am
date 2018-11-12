VERSION=0.8.0
LANG1=eng
LANG1a=eng_GB
LANG1b=eng_US
LANG2=spa
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)
PREFIX2b=$(LANG2)-$(LANG1b)
ALT=$(ALTXSL)

BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON = $(PREFIX1).automorf.bin $(PREFIX1).autobil.bin $(PREFIX1).autogen.bin $(PREFIX1).autolex.bin \
                 $(PREFIX1).autopgen.bin $(PREFIX2).automorf.bin $(PREFIX2).autobil.bin $(PREFIX2).autolex.bin \
                 $(PREFIX2).autogen.bin $(PREFIX2).autopgen.bin \
                 $(PREFIX2b).autogen.bin $(PREFIX1).genitive.bin \
                 $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin \
                 $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin

TARGETS = $(TARGETS_COMMON) 

# This include defines goals for install-modes, .deps/.d, autobil.prefixes and .mode files:
@ap_include@

.deps/$(LANG1).metadix:  $(BASENAME).$(LANG1).metadix
	if [ ! -d .deps ]; then mkdir .deps; fi
	xsltproc --stringparam alt $(LANG1a) $(ALT) $(BASENAME).$(LANG1).metadix >$@

.deps/$(LANG1).dix: .deps/$(LANG1).metadix
	xsltproc buscaPar.xsl .deps/$(LANG1).metadix | uniq >$$$$tmp1 && \
	xsltproc $$$$tmp1 .deps/$(LANG1).metadix > $@ && rm $$$$tmp1

.deps/$(LANG1b).metadix: $(BASENAME).$(LANG1).metadix
	if [ ! -d .deps ]; then mkdir .deps; fi
	xsltproc --stringparam alt $(LANG1b) $(ALT) $(BASENAME).$(LANG1).metadix >$@

.deps/$(LANG1b).dix: .deps/$(LANG1b).metadix
	xsltproc buscaPar.xsl .deps/$(LANG1b).metadix | uniq >$$$$tmp1 && \
	xsltproc $$$$tmp1 .deps/$(LANG1b).metadix > $@ && rm $$$$tmp1

$(PREFIX1).automorf.bin: .deps/$(LANG1).dix
	apertium-validate-dictionary .deps/$(LANG1).dix
	apertium-validate-acx $(BASENAME).$(LANG1).acx
	lt-comp lr .deps/$(LANG1).dix $@ $(BASENAME).$(LANG1).acx


$(PREFIX1).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
##NO TOCAR	apertium-gen-oldbil $(BASENAME).$(PREFIX1).dix tmp$(PREFIX1).autobil.dix
#	xsltproc translate-to-default-equivalent.xsl $(BASENAME).$(PREFIX1).dix >tmp$(PREFIX1).autobil.dix
	lt-comp lr $(BASENAME).$(PREFIX1).dix $@
#	rm tmp$(PREFIX1).autobil.dix

$(PREFIX1).autogen.bin: $(AP_SRC2)/$(LANG2).autogen.bin
	cp $< $@

$(PREFIX1).autopgen.bin: $(AP_SRC2)/$(LANG2).autopgen.bin
	cp $< $@

$(PREFIX1).autolex.bin: $(BASENAME).$(PREFIX1).lrx
	lrx-comp $< $@

$(PREFIX2).autolex.bin: $(BASENAME).$(PREFIX2).lrx
	lrx-comp $< $@


$(PREFIX2).automorf.bin: $(AP_SRC2)/$(LANG2).automorf.bin $(PREFIX2).autobil.bin
	lt-trim $^ $@

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	lt-comp rl $(BASENAME).$(PREFIX1).dix $@

$(PREFIX2).autogen.bin: $(AP_SRC1)/$(LANG1).autogen.bin
	cp $< $@

$(PREFIX2b).autogen.bin: $(AP_SRC1)/$(LANG1b).autogen.bin
	cp $< $@

$(PREFIX2).autopgen.bin: $(AP_SRC1)/$(LANG1).autopgen.bin
	cp $< $@

$(PREFIX1).genitive.bin: $(BASENAME).$(PREFIX1).genitive.t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX1).genitive.t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).genitive.t1x $@

$(PREFIX1).t1x.bin: $(BASENAME).$(PREFIX1).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX1).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t1x $@

$(PREFIX1).t2x.bin: $(BASENAME).$(PREFIX1).t2x
	apertium-validate-interchunk $(BASENAME).$(PREFIX1).t2x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t2x $@

$(PREFIX1).t3x.bin: $(BASENAME).$(PREFIX1).t3x
	apertium-validate-postchunk $(BASENAME).$(PREFIX1).t3x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t3x $@

$(PREFIX2).t1x.bin: $(BASENAME).$(PREFIX2).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX2).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t1x $@

$(PREFIX2).t2x.bin: $(BASENAME).$(PREFIX2).t2x
	apertium-validate-interchunk $(BASENAME).$(PREFIX2).t2x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t2x $@

$(PREFIX2).t3x.bin: $(BASENAME).$(PREFIX2).t3x
	apertium-validate-postchunk $(BASENAME).$(PREFIX2).t3x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t3x $@


###############################################################################
## Distribution
###############################################################################

EXTRA_DIST=$(BASENAME).post-$(LANG1).dix $(BASENAME).post-$(LANG2).dix \
	   $(BASENAME).$(LANG1).tsx \
	   $(BASENAME).$(LANG2).tsx \
	   $(PREFIX1).prob $(PREFIX2).prob \
	   buscaPar.xsl principal.xsl alt.xsl \
	   $(BASENAME).$(LANG1).metadix \
	   $(BASENAME).$(LANG2).dix \
	   $(BASENAME).$(PREFIX1).dix \
	   $(BASENAME).$(PREFIX1).lrx \
	   $(BASENAME).$(PREFIX2).lrx \
	   $(BASENAME).$(PREFIX1).genitive.t1x \
	   $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x \
	   $(BASENAME).$(PREFIX1).t3x $(BASENAME).$(PREFIX2).t1x \
           $(BASENAME).$(PREFIX2).t2x $(BASENAME).$(PREFIX2).t3x \
           $(BASENAME).$(LANG1).acx $(BASENAME).$(LANG2).acx \
	   modes.xml




###############################################################################
## Installation
###############################################################################

apertium_eng_spadir=$(prefix)/share/apertium/apertium-$(PREFIX1)/
apertium_modesdir=$(prefix)/share/apertium/modes/

modes/$(PREFIX1).mode: modes.xml
	apertium-validate-modes modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

# All modes are created by the same goal, listing several will just give problems with make -j2
noinst_DATA=modes/$(PREFIX1).mode


# Files which should be installed to $(prefix)/share/apertium/$(BASENAME)/:
apertium_eng_spa_DATA=$(PREFIX1).automorf.bin $(PREFIX2).automorf.bin \
		    $(PREFIX1).autobil.bin $(PREFIX2).autobil.bin \
		    $(PREFIX1).autogen.bin $(PREFIX2).autogen.bin \
		    $(PREFIX1).autolex.bin $(PREFIX2).autolex.bin \
		    $(PREFIX1).autopgen.bin $(PREFIX2).autopgen.bin \
                    $(PREFIX2b).autogen.bin \
		    $(PREFIX1).prob $(PREFIX2).prob \
		    $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin \
		    $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin \
		    $(PREFIX1).genitive.bin \
	$(BASENAME).$(PREFIX1).genitive.t1x \
	$(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x \
	$(BASENAME).$(PREFIX1).t3x $(BASENAME).$(PREFIX2).t1x \
	$(BASENAME).$(PREFIX2).t2x $(BASENAME).$(PREFIX2).t3x

install-data-local:
	mv modes modes.bak
	apertium-gen-modes modes.xml apertium-$(PREFIX1)
	rm -rf modes
	mv modes.bak modes
	test -d $(DESTDIR)$(apertium_modesdir) || mkdir $(DESTDIR)$(apertium_modesdir)
	$(INSTALL_DATA) $(PREFIX1).mode $(DESTDIR)$(apertium_modesdir)
	$(INSTALL_DATA) $(PREFIX2).mode $(DESTDIR)$(apertium_modesdir)
	$(INSTALL_DATA) $(PREFIX2b).mode $(DESTDIR)$(apertium_modesdir)
	rm $(PREFIX1).mode $(PREFIX2).mode $(PREFIX2b).mode 


###############################################################################
## Cleanup
###############################################################################

clean-dicts:
	touch $(BASENAME).$(LANG1).dixtmp1 $(BASENAME).$(LANG1).metadix  $(BASENAME).$(LANG2).dix $(BASENAME).$(PREFIX1).dix $(BASENAME).$(PREFIX1).dix
	rm $(BASENAME).$(LANG1).dixtmp1
	rm $(BASENAME).$(LANG1).metadix
	rm $(BASENAME).$(LANG2).dix
	rm $(BASENAME).$(PREFIX1).dix

CLEANFILES = $(TARGETS_COMMON) *.mode
clean-local: 
	-rm -rf .deps modes

###############################################################################
## Test
###############################################################################

test: all
	echo  "Un malentendido."  | apertium -d . es-en | tee .test-mt
	@echo "A misunderstanding." > .test-ref
	@diff .test-ref .test-mt
	echo "Three sad tigers" | apertium -d . en-es | tee .test-mt
	@echo "Tres tigres tristes" > .test-ref
	@diff .test-ref .test-mt
	@rm .test-ref .test-mt
