---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.Reps, MIPRE.Tailored.Sofic.rep, MIPRE.Tailored.Sofic.ind, MIPRE.Tailored.Sofic.ind_mul, MIPRE.Tailored.Sofic.ind_J, MIPRE.Tailored.Sofic.ind_fix_iff, MIPRE.Tailored.Sofic.indF, MIPRE.Tailored.Sofic.quotStrat, MIPRE.Tailored.Sofic.wordSP, MIPRE.Tailored.Sofic.ZStrat.toMatrix_wordSP_consWord
statement: formalized
proof: formalized
---

# The quotient by $J$

Let an action pass Checks 1–3 everywhere. Choosing one point of each $J$-orbit, every permutation commuting with $J$ induces a signed permutation of the representatives, multiplicatively, sending $J$ to $-1$, with sign $+$ at $r$ exactly when it fixes $r$. The variables induce a Z-aligned signed-permutation strategy, in which the matrix of a constraint is the signed permutation induced by its word.

## Depends on

- [Z-aligned signed-permutation strategies without commutation along edges](def-zstrat.md)
- [Signed permutation matrices](../../the-aldous-lyons-track-tmip-re/part-01/lem-signed-perm.md)
- [The trace identity](lem-trace-identity.md)
- [The associated subgroup test; I:2086](def-assoc-test.md)
- [Subgroup tests and their sofic value; I:439–520](def-subgroup-test.md)

## Proof

A permutation commuting with $J$ permutes the $J$-orbits; the readable variables act as the identity or as $J$, hence diagonally.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Reps`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Reps), [`MIPRE.Tailored.Sofic.rep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.rep), [`MIPRE.Tailored.Sofic.ind`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ind), [`MIPRE.Tailored.Sofic.ind_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ind_mul), [`MIPRE.Tailored.Sofic.ind_J`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ind_J), [`MIPRE.Tailored.Sofic.ind_fix_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ind_fix_iff), [`MIPRE.Tailored.Sofic.indF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.indF), [`MIPRE.Tailored.Sofic.quotStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.quotStrat), [`MIPRE.Tailored.Sofic.wordSP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.wordSP), [`MIPRE.Tailored.Sofic.ZStrat.toMatrix_wordSP_consWord`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.toMatrix_wordSP_consWord).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 280](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L280)
