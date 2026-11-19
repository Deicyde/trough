---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.dotL_toBits, MIPRE.Tailored.Intro.regForm, MIPRE.Tailored.Intro.dotL_regForm, MIPRE.Tailored.Intro.satisfies_regForms_iff, MIPRE.Tailored.Intro.projEqCons, MIPRE.Tailored.Intro.projEqCons_iff, MIPRE.Tailored.Intro.dualCons, MIPRE.Tailored.Intro.dualCons_iff
statement: formalized
proof: formalized
---

# Comparisons of registers as linear constraints

Let two registers $x, y \in \mathbb{F}_2^s$ sit at known offsets of the two answers. For a coordinate set $S$, the constraints $x_i = y_i$, $i \in S$, hold exactly when $x$ and $y$ agree on $S$. For a linear map $L$ on the coordinates $S$ and a list of vectors spanning its kernel, the constraints $\sum_i z_i (x - y)_i = 0$ on $S$, one for each listed $z$, hold exactly when the dual readouts of $L$ at $x$ and at $y$ agree.

## Depends on

- [Linear forms on windows, and the input's constraints re-indexed](lem-intro-forms.md)
- [Orthogonal and canonical complements](../../structure-of-the-proof/part-01/def-cl-canonical.md)
- [The two complements](../../structure-of-the-proof/part-01/lem-cl-canonical.md)
- [Pauli mixing with a retained classical fibre](../../structure-of-the-proof/part-02/lem-pauli-mixing.md)

## Proof

The inner product of two windows is the $\mathbb{F}_2$ sum of the products of their entries. The dual readouts agree exactly when $x - y$, restricted to $S$, is orthogonal to the kernel of $L$; a linear functional vanishing on a spanning list vanishes on the span.

## Lean

Formalized as [`MIPRE.Tailored.Intro.dotL_toBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_toBits), [`MIPRE.Tailored.Intro.regForm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.regForm), [`MIPRE.Tailored.Intro.dotL_regForm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_regForm), [`MIPRE.Tailored.Intro.satisfies_regForms_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.satisfies_regForms_iff), [`MIPRE.Tailored.Intro.projEqCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.projEqCons), [`MIPRE.Tailored.Intro.projEqCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.projEqCons_iff), [`MIPRE.Tailored.Intro.dualCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dualCons), [`MIPRE.Tailored.Intro.dualCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dualCons_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1695](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1695)
