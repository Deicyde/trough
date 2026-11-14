---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.primrec_tabOfT, MIPRE.Tailored.computable_tabT, MIPRE.Tailored.presents_tabOfT, MIPRE.Tailored.presents_tabT, MIPRE.Tailored.mu_tabOfT, MIPRE.Tailored.dimOf_eq_of, MIPRE.Tailored.margN_eq_of, MIPRE.Tailored.lenIs_lenRun, MIPRE.Tailored.lpIs_lpRun, MIPRE.Tailored.lenOf_eq_lenRun, MIPRE.Tailored.consOf_eq_lpRun
statement: formalized
proof: formalized
---

# The tabulation is computable, and correct on bounded verifiers

The tabulation is primitive recursive in its parameters, and the tabulation of a description string is computable in the string and the index. For a tailored verifier whose three programs run within the budget at index $n$, the tabulation presents its doubled $n$-th game; in particular the tabulation of the description of a $\lambda$-bounded verifier does, at every $n \geq 2$.

## Depends on

- [The tabulation of a tailored verifier](def-tailored-tabulation.md)
- [Presentations](def-tailored-presents.md)
- [Tailored gap compression, value form; II:1852](def-tailored-compression.md)

## Proof

Under its time bound each budgeted run returns the program's output. The weights are counted as in the tabulation of a normal form verifier (Definition [Game description](../../foundations/part-02/def-game-description.md)), the marginals at the sampler's level being normalized to the dimension, which only matters at level $0$, where the questions are empty. A vertex's question is read off its binary expansion, the tag being the lowest bit.

## Lean

Formalized as [`MIPRE.Tailored.primrec_tabOfT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.primrec_tabOfT), [`MIPRE.Tailored.computable_tabT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.computable_tabT), [`MIPRE.Tailored.presents_tabOfT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.presents_tabOfT), [`MIPRE.Tailored.presents_tabT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.presents_tabT), [`MIPRE.Tailored.mu_tabOfT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.mu_tabOfT), [`MIPRE.Tailored.dimOf_eq_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.dimOf_eq_of), [`MIPRE.Tailored.margN_eq_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.margN_eq_of), [`MIPRE.Tailored.lenIs_lenRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.lenIs_lenRun), [`MIPRE.Tailored.lpIs_lpRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.lpIs_lpRun), [`MIPRE.Tailored.lenOf_eq_lenRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.lenOf_eq_lenRun), [`MIPRE.Tailored.consOf_eq_lpRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.consOf_eq_lpRun).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 817](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L817)
