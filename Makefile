all: compress uncompress

uncompress compress : miniz.c Makefile
	gcc -DFUNCTION=mz_$@ -o $@ $<

