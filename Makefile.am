VERSION=0.6
LANG1=en
LANG2=es
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)

BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON = $(PREFIX1).automorf.bin $(PREFIX1).autobil.bin $(PREFIX1).autogen.bin \
                 $(PREFIX1).autopgen.bin $(PREFIX2).automorf.bin $(PREFIX2).autobil.bin \
                 $(PREFIX2).autogen.bin $(PREFIX2).autopgen.bin $(PREFIX1).lextormono.bin $(PREFIX2).lextormono.bin \
                 $(PREFIX1).lextorbil.bin $(PREFIX2).lextorbil.bin \
                 $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin \
                 $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin modes

$(BASENAME).$(LANG1).metadix: $(BASENAME).$(LANG1).metadix.xml en-dic/*.xml en-es-common/*.xml
	xmllint --xinclude $(LANG1)-dic/$(BASENAME).$(LANG1).metadix.xml > $(BASENAME).$(LANG1).metadix
$(BASENAME).$(LANG2).dix: $(BASENAME).$(LANG2).dix.xml es-dic/*.xml en-es-common/*.xml
	xmllint --xinclude $(LANG2)-dic/$(BASENAME).$(LANG2).dix.xml > $(BASENAME).$(LANG2).dix
$(BASENAME).$(LANG1)-$(LANG2).dix: $(BASENAME).$(LANG1)-$(LANG2).dix.xml en-es-dic/*.xml en-es-common/*.xml
	xmllint --xinclude $(LANG1)-$(LANG2)-dic/$(BASENAME).$(LANG1)-$(LANG2).dix.xml > $(BASENAME).$(LANG1)-$(LANG2).dix
     
TARGETS = $(TARGETS_COMMON) 

$(PREFIX1).automorf.bin: $(BASENAME).$(LANG1).metadix
	@xsltproc buscaPar.xsl apertium-en-es.en.metadix | uniq > tmp1gen.xsl 	 
	@xsltproc tmp1gen.xsl apertium-en-es.en.metadix >$(BASENAME).$(LANG1).dixtmp1 
	@rm tmp1gen.xsl
	apertium-validate-dictionary $(BASENAME).$(LANG1).dixtmp1
	lt-comp lr $(BASENAME).$(LANG1).dixtmp1 $@
#	@rm $(BASENAME).$(LANG1).dixtmp1

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

$(PREFIX2).automorf.bin: $(BASENAME).$(LANG2).dix
	apertium-validate-dictionary $(BASENAME).$(LANG2).dix
	lt-comp lr $(BASENAME).$(LANG2).dix $@
#	@rm $(BASENAME).$(LANG2).dix

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
##NO TOCAR	apertium-gen-oldbil $(BASENAME).$(PREFIX1).dix tmp$(PREFIX2).autobil.dix
	xsltproc translate-to-default-equivalent.xsl $(BASENAME).$(PREFIX1).dix >tmp$(PREFIX2).autobil.dix
	lt-comp rl tmp$(PREFIX2).autobil.dix $@
	rm tmp$(PREFIX2).autobil.dix

$(PREFIX2).autogen.bin: $(BASENAME).$(LANG1).metadix
	@xsltproc buscaPar.xsl apertium-en-es.en.metadix | uniq > tmp2gen.xsl 	 
	@xsltproc tmp2gen.xsl apertium-en-es.en.metadix >$(BASENAME).$(LANG1).dixtmp2
	@rm tmp2gen.xsl
	apertium-validate-dictionary $(BASENAME).$(LANG1).dixtmp2
	lt-comp rl $(BASENAME).$(LANG1).dixtmp2 $@
	@rm $(BASENAME).$(LANG1).dixtmp2
#	@rm $(BASENAME).$(LANG1).metadix
#	@rm $(BASENAME).$(LANG2).dix	
#	@rm $(BASENAME).$(LANG1)-$(LANG2).dix	

$(PREFIX2).autopgen.bin: $(BASENAME).post-$(LANG1).dix
	apertium-validate-dictionary $(BASENAME).post-$(LANG1).dix
	lt-comp lr $(BASENAME).post-$(LANG1).dix $@

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


EXTRA_DIST=$(BASENAME).$(LANG1).metadix.xml $(BASENAME).$(PREFIX1).dix.xml \
	   $(BASENAME).post-$(LANG1).dix $(BASENAME).post-$(LANG2).dix \
	   $(BASENAME).$(LANG2).dix.xml $(BASENAME).$(LANG1).tsx \
	   $(BASENAME).$(LANG2).tsx \
	   $(PREFIX1).prob $(PREFIX2).prob \
	   buscaPar.xsl principal.xsl \
           translate-to-default-equivalent.xsl \
	   $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x \
	   $(BASENAME).$(PREFIX1).t3x $(BASENAME).$(PREFIX2).t1x \
           $(BASENAME).$(PREFIX2).t2x $(BASENAME).$(PREFIX2).t3x \
           es-dic/apertium-en-es.es.acronyms.xml \
           es-dic/apertium-en-es.es.adjectives.xml \
           es-dic/apertium-en-es.es.adverbs.xml \
           es-dic/apertium-en-es.es.colloquial.xml \
           es-dic/apertium-en-es.es.conjunctions.xml \
           es-dic/apertium-en-es.es.determiners.xml \
           es-dic/apertium-en-es.es.dix.xml \
           es-dic/apertium-en-es.es.interjections.xml \
           es-dic/apertium-en-es.es.nouns.xml \
           es-dic/apertium-en-es.es.numerals.xml \
           es-dic/apertium-en-es.es.pardefs.xml \
           es-dic/apertium-en-es.es.prepositions.xml \
           es-dic/apertium-en-es.es.pronouns.xml \
           es-dic/apertium-en-es.es.proper-nouns-ant.xml \
           es-dic/apertium-en-es.es.proper-nouns.xml \
           es-dic/apertium-en-es.es.punctuation.xml \
           es-dic/apertium-en-es.es.symbols.xml \
           es-dic/apertium-en-es.es.verbs.xml \
           es-dic/apertium-en-es.pardefs-url.xml \
           es-dic/apertium-en-es.symbols.xml \
           en-dic/apertium-en-es.en.acronyms.xml \
           en-dic/apertium-en-es.en.adjectives.xml \
           en-dic/apertium-en-es.en.adverbs.xml \
           en-dic/apertium-en-es.en.colloquial.xml \
           en-dic/apertium-en-es.en.conjunctions.xml \
           en-dic/apertium-en-es.en.determiners.xml \
           en-dic/apertium-en-es.en.interjections.xml \
           en-dic/apertium-en-es.en.metadix.xml \
           en-dic/apertium-en-es.en.nouns.xml \
           en-dic/apertium-en-es.en.numerals.xml \
           en-dic/apertium-en-es.en.pardefs.xml \
           en-dic/apertium-en-es.en.prepositions.xml \
           en-dic/apertium-en-es.en.pronouns.xml \
           en-dic/apertium-en-es.en.proper-nouns-ant.xml \
           en-dic/apertium-en-es.en.proper-nouns.xml \
           en-dic/apertium-en-es.en.punctuation.xml \
           en-dic/apertium-en-es.en.symbols.xml \
           en-dic/apertium-en-es.en.verbs.xml \
           en-dic/apertium-en-es.pardefs-url.xml \
           en-dic/apertium-en-es.symbols.xml \
           en-es-dic/apertium-en-es.en-es.acronyms.xml \
           en-es-dic/apertium-en-es.en-es.adjectives.xml \
           en-es-dic/apertium-en-es.en-es.adverbs.xml \
           en-es-dic/apertium-en-es.en-es.colloquial.xml \
           en-es-dic/apertium-en-es.en-es.conjunctions.xml \
           en-es-dic/apertium-en-es.en-es.determiners.xml \
           en-es-dic/apertium-en-es.en-es.dix.xml \
           en-es-dic/apertium-en-es.en-es.interjections.xml \
           en-es-dic/apertium-en-es.en-es.nouns.xml \
           en-es-dic/apertium-en-es.en-es.numerals.xml \
           en-es-dic/apertium-en-es.en-es.pardefs.xml \
           en-es-dic/apertium-en-es.en-es.prepositions.xml \
           en-es-dic/apertium-en-es.en-es.pronouns.xml \
           en-es-dic/apertium-en-es.en-es.proper-nouns-ant.xml \
           en-es-dic/apertium-en-es.en-es.proper-nouns.xml \
           en-es-dic/apertium-en-es.en-es.punctuation.xml \
           en-es-dic/apertium-en-es.en-es.symbols.xml \
           en-es-dic/apertium-en-es.en-es.verbs.xml \
           en-es-dic/apertium-en-es.pardefs-url.xml \
           en-es-dic/apertium-en-es.symbols.xml \
           en-es-common/apertium-en-es.pardefs-url.xml \
           en-es-common/apertium-en-es.symbols.xml \
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
		    $(PREFIX1).prob $(PREFIX2).prob \
		    $(PREFIX1).t1x.bin $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin \
		    $(PREFIX2).t1x.bin $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin \
		    $(PREFIX1).mode $(PREFIX2).mode

apertium_en_esdir=$(prefix)/share/apertium/apertium-$(PREFIX1)/
apertium_en_modesdir=$(prefix)/share/apertium/modes/

$(PREFIX1).mode: modes.xml
	apertium-gen-modes modes.xml

$(PREFIX2).mode: modes.xml
	apertium-gen-modes modes.xml

modes: modes.xml
	apertium-gen-modes modes.xml

install-data-local:
	apertium-gen-modes modes.xml apertium-$(PREFIX1)
	$(INSTALL_DATA) $(PREFIX1).mode $(apertium_en_modesdir)
	$(INSTALL_DATA) $(PREFIX2).mode $(apertium_en_modesdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x $(apertium_en_esdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t3x $(BASENAME).$(PREFIX2).t1x $(apertium_en_esdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX2).t2x $(BASENAME).$(PREFIX2).t3x $(apertium_en_esdir)

CLEANFILES = -rf $(TARGETS) modes

