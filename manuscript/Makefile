SHELL := /bin/bash
SOURCE_DATE_EPOCH ?= 1786692694
TEX := r010_union_closed_bound.tex
PDF := r010_union_closed_bound.pdf

.PHONY: all clean

all: $(PDF)

$(PDF): $(TEX)
	SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) latexmk -pdf -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	latexmk -C $(TEX)
