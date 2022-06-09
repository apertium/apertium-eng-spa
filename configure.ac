AC_PREREQ(2.52)

AC_INIT([apertium-eng-spa], [0.8.1], [])
AM_INIT_AUTOMAKE([apertium-eng-spa], [0.8.1], no-define)
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.8.0)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.6.0)
PKG_CHECK_MODULES(APERTIUM_LEX_TOOLS, apertium-lex-tools >= 0.3.0)

ALTXSL="alt.xsl";

AC_SUBST(ALTXSL)

PKG_CHECK_MODULES(REGTEST, apertium-regtest >= 0.0.1, [],
                  [AC_MSG_WARN([Running tests requires apertium-regtest])])

AP_MKINCLUDE

AC_OUTPUT([Makefile])
