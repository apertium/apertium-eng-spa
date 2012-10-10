VERSION=0.8.0
LANG1=en
LANG1a=en_GB
LANG1b=en_US
LANG2=es
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)
PREFIX2b=$(LANG2)-$(LANG1b)
ALT=$(ALTXSL)

BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON = $(PREFIX1).automorf.bin $(PREFIX1).autobil.bin $(PREFIX1).autogen.bin \
                 $(PREFIX1).autopgen.bin $(PREFIX2).automorf.bin $(PREFIX2).autobil.bin \
                 $(PREFIX2).autogen.bin $(PREFIX2).autopgen.bin $(PREFIX1).lextormono.bin $(PREFIX2).lextormono.bin \
                 $(PREFIX2b).autogen.bin $(PREFIX1).genitive.bin \
                 $(PREFIX1).lextorbil.bin $(PREFIX2).lextorbil.bin \
                 $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin \
                 $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin modes \
		 $(BASENAME).$(LANG1)-lextor.dix $(BASENAME).$(LANG2)-lextor.dix \
		 $(BASENAME).$(PREFIX1)-lextor.dix $(BASENAME).$(PREFIX2)-lextor.dix


TARGETS = $(TARGETS_COMMON) 

$(BASENAME).$(LANG1)-lextor.dix: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	apertium-gen-lextormono rl $(BASENAME).$(PREFIX1).dix $@

$(BASENAME).$(LANG2)-lextor.dix: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	apertium-gen-lextormono lr $(BASENAME).$(PREFIX1).dix $@

$(BASENAME).$(PREFIX1)-lextor.dix: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	apertium-gen-lextorbil rl $(BASENAME).$(PREFIX1).dix $@

$(BASENAME).$(PREFIX2)-lextor.dix: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	apertium-gen-lextorbil lr $(BASENAME).$(PREFIX1).dix $@

.deps/$(LANG1).metadix: $(BASENAME).$(LANG1).metadix
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

#$(PREFIX1).automorf.bin: $(BASENAME).$(LANG1).metadix $(BASENAME).$(LANG1).acx
#	@xsltproc buscaPar.xsl apertium-en-es.en.metadix | uniq > tmp1gen.xsl 	 
#	@xsltproc tmp1gen.xsl apertium-en-es.en.metadix >$(BASENAME).$(LANG1).dixtmp1 
#	@rm tmp1gen.xsl
#	apertium-validate-acx $(BASENAME).$(LANG1).acx
#	apertium-validate-dictionary $(BASENAME).$(LANG1).dixtmp1
#	lt-comp lr $(BASENAME).$(LANG1).dixtmp1 $@ $(BASENAME).$(LANG1).acx
##	@rm $(BASENAME).$(LANG1).dixtmp1

$(PREFIX1).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
##NO TOCAR	apertium-gen-oldbil $(BASENAME).$(PREFIX1).dix tmp$(PREFIX1).autobil.dix
	xsltproc translate-to-default-equivalent.xsl $(BASENAME).$(PREFIX1).dix >tmp$(PREFIX1).autobil.dix
	lt-comp lr tmp$(PREFIX1).autobil.dix $@
	rm tmp$(PREFIX1).autobil.dix

$(PREFIX1).autogen.bin: $(BASENAME).$(LANG2).dix
	apertium-validate-dictionary $(BASENAME).$(LANG2).dix
	lt-comp rl $(BASENAME).$(LANG2).dix $@

$(PREFIX1).autopgen.bin: $(BASENAME).post-$(LANG2).dix
	apertium-validate-dictionary $(BASENAME).post-$(LANG2).dix
	lt-comp lr $(BASENAME).post-$(LANG2).dix $@

$(PREFIX2).automorf.bin: $(BASENAME).$(LANG2).dix $(BASENAME).$(LANG2).acx
	apertium-validate-acx $(BASENAME).$(LANG2).acx
	apertium-validate-dictionary $(BASENAME).$(LANG2).dix
	lt-comp lr $(BASENAME).$(LANG2).dix $@ $(BASENAME).$(LANG2).acx
#	@rm $(BASENAME).$(LANG2).dix

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
##NO TOCAR	apertium-gen-oldbil $(BASENAME).$(PREFIX1).dix tmp$(PREFIX2).autobil.dix
	xsltproc translate-to-default-equivalent.xsl $(BASENAME).$(PREFIX1).dix >tmp$(PREFIX2).autobil.dix
	lt-comp rl tmp$(PREFIX2).autobil.dix $@
	rm tmp$(PREFIX2).autobil.dix

$(PREFIX2).autogen.bin: .deps/$(LANG1).dix
	apertium-validate-dictionary .deps/$(LANG1).dix
	lt-comp rl .deps/$(LANG1).dix $@

$(PREFIX2b).autogen.bin: .deps/$(LANG1b).dix
	apertium-validate-dictionary .deps/$(LANG1b).dix
	lt-comp rl .deps/$(LANG1b).dix $@

#$(PREFIX2).autogen.bin: $(BASENAME).$(LANG1).metadix
#	@xsltproc buscaPar.xsl apertium-en-es.en.metadix | uniq > tmp2gen.xsl 	 
#	@xsltproc tmp2gen.xsl apertium-en-es.en.metadix >$(BASENAME).$(LANG1).dixtmp2
#	@rm tmp2gen.xsl
#	apertium-validate-dictionary $(BASENAME).$(LANG1).dixtmp2
#	lt-comp rl $(BASENAME).$(LANG1).dixtmp2 $@
#	@rm $(BASENAME).$(LANG1).dixtmp2
#	@rm $(BASENAME).$(LANG1).metadix
#	@rm $(BASENAME).$(LANG2).dix	
#	@rm $(BASENAME).$(LANG1)-$(LANG2).dix	

$(PREFIX2).autopgen.bin: $(BASENAME).post-$(LANG1).dix
	apertium-validate-dictionary $(BASENAME).post-$(LANG1).dix
	lt-comp lr $(BASENAME).post-$(LANG1).dix $@

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


EXTRA_DIST=$(BASENAME).post-$(LANG1).dix $(BASENAME).post-$(LANG2).dix \
	   $(BASENAME).$(LANG1).tsx \
	   $(BASENAME).$(LANG2).tsx \
	   $(PREFIX1).prob $(PREFIX2).prob \
	   buscaPar.xsl principal.xsl alt.xsl \
           translate-to-default-equivalent.xsl \
	   $(BASENAME).$(LANG1).metadix \
	   $(BASENAME).$(LANG2).dix \
	   $(BASENAME).$(PREFIX1).dix \
	   $(BASENAME).$(PREFIX1).genitive.t1x \
	   $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x \
	   $(BASENAME).$(PREFIX1).t3x $(BASENAME).$(PREFIX2).t1x \
           $(BASENAME).$(PREFIX2).t2x $(BASENAME).$(PREFIX2).t3x \
           $(BASENAME).$(LANG1).acx $(BASENAME).$(LANG2).acx \
	   modes.xml

clean-dicts:
	touch $(BASENAME).$(LANG1).dixtmp1 $(BASENAME).$(LANG1).metadix  $(BASENAME).$(LANG2).dix $(BASENAME).$(PREFIX1).dix $(BASENAME).$(PREFIX1).dix
	rm $(BASENAME).$(LANG1).dixtmp1
	rm $(BASENAME).$(LANG1).metadix
	rm $(BASENAME).$(LANG2).dix
	rm $(BASENAME).$(PREFIX1).dix

apertium_en_es_DATA=$(PREFIX1).automorf.bin $(PREFIX2).automorf.bin \
		    $(PREFIX1).autobil.bin $(PREFIX2).autobil.bin \
		    $(PREFIX1).autogen.bin $(PREFIX2).autogen.bin \
		    $(PREFIX1).autopgen.bin $(PREFIX2).autopgen.bin \
                    $(PREFIX2b).autogen.bin \
		    $(PREFIX1).prob $(PREFIX2).prob \
		    $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin \
		    $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin \
	            $(BASENAME).$(PREFIX1).genitive.t1x \
		    $(PREFIX1).genitive.bin  \
		    $(PREFIX1).mode $(PREFIX2).mode \
		    $(BASENAME).$(LANG1)-lextor.dix $(BASENAME).$(LANG2)-lextor.dix \
		    $(BASENAME).$(PREFIX1)-lextor.dix $(BASENAME).$(PREFIX2)-lextor.dix

apertium_en_esdir=$(prefix)/share/apertium/apertium-$(PREFIX1)/
apertium_en_modesdir=$(prefix)/share/apertium/modes/

$(PREFIX1).mode: modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

$(PREFIX2).mode: modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

$(PREFIX2b).mode: modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

modes: modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

install-data-local:
	apertium-gen-modes modes.xml apertium-$(PREFIX1)
	test -d $(DESTDIR)$(apertium_en_modesdir) || mkdir $(DESTDIR)$(apertium_en_modesdir)
	$(INSTALL_DATA) $(PREFIX1).mode $(DESTDIR)$(apertium_en_modesdir)
	$(INSTALL_DATA) $(PREFIX2).mode $(DESTDIR)$(apertium_en_modesdir)
	$(INSTALL_DATA) $(PREFIX2b).mode $(DESTDIR)$(apertium_en_modesdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).genitive.t1x $(DESTDIR)$(apertium_en_esdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x $(DESTDIR)$(apertium_en_esdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t3x $(BASENAME).$(PREFIX2).t1x $(DESTDIR)$(apertium_en_esdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX2).t2x $(BASENAME).$(PREFIX2).t3x $(DESTDIR)$(apertium_en_esdir)

CLEANFILES = -rf $(TARGETS) modes

