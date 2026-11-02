# Some local theory

We could work over a general nonarchimedean normed field but we still do not have them in mathlib, so we stick to the case of interest which is the completion of a number field $K$ at a finite place $v$. Such a completion is a topological field $K_v$ equipped with a discrete valuation, a ring of integers $\mathcal{O}_v$ having a principal maximal ideal $(\varpi)$, and a finite residue field $k_v:=\mathcal{O}_v/(\varpi)$.

There is no formal Lean code for the lemmas in this section; I am slightly dragging my feet because it would seem more sensible to prove them in the right generality, and we don't have a definition of nonarchimedean local field yet.

- [NumberField.isOpenAdicCompletionIntegers](numberfield-isopenadiccompletionintegers.md)
- [M2.localFullLevel.isOpen](m2-localfulllevel-isopen.md)
- [M2.localFullLevel.isCompact](m2-localfulllevel-iscompact.md)
- [nolean-compactopen-GL2](nolean-compactopen-gl2.md)
- [nolean-compactopen-U1p](nolean-compactopen-u1p.md)
- [bijOn\_unipotent\_mul\_diagU1\_U1diagU1](bijon-unipotent-mul-diagu1-u1diagu1.md)
