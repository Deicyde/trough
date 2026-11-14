---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.dotL, MIPRE.Tailored.Intro.dotL_eq_odd, MIPRE.Tailored.Intro.satisfies_iff_dotL, MIPRE.Tailored.Intro.dotL_append, MIPRE.Tailored.Intro.satisfies_append_iff, MIPRE.Tailored.Intro.place, MIPRE.Tailored.Intro.length_place, MIPRE.Tailored.Intro.dotL_place, MIPRE.Tailored.Intro.unit, MIPRE.Tailored.Intro.dotL_unit, MIPRE.Tailored.Intro.eqCons, MIPRE.Tailored.Intro.eqCons_iff, MIPRE.Tailored.Intro.guardCons, MIPRE.Tailored.Intro.guardCons_iff, MIPRE.Tailored.Intro.place2, MIPRE.Tailored.Intro.dotL_place2, MIPRE.Tailored.Intro.inputOf, MIPRE.Tailored.Intro.reindex, MIPRE.Tailored.Intro.dotL_split_right, MIPRE.Tailored.Intro.satisfies_reindex_iff
statement: formalized
proof: formalized
---

# Linear forms on windows, and the input's constraints re-indexed

A constraint $\alpha \beta \gamma$ holds of $(a, b, 1)$ exactly when $\langle \alpha, a\rangle + \langle \beta, b\rangle = \gamma$; a vector placed at an offset pairs with a vector as it pairs with the window there; the bitwise equality of two windows of the two answers is a list of such constraints; a condition on the readable answers is the empty list or the rejecting constraint. An input constraint on the two input answers, re-indexed onto the windows of two Introspect answers in which the layout carries them (readable bits at $Q$, linear bits at $Q + R$), holds exactly when the original holds of the input answers read off those windows.

## Depends on

- [Tailored game; II:1243](../part-01/def-tailored-game.md)

## Proof

The inner product is additive over concatenation, and zero against zeros; the rest is cutting the vectors at the offsets.

## Lean

Formalized as [`MIPRE.Tailored.Intro.dotL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL), [`MIPRE.Tailored.Intro.dotL_eq_odd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_eq_odd), [`MIPRE.Tailored.Intro.satisfies_iff_dotL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.satisfies_iff_dotL), [`MIPRE.Tailored.Intro.dotL_append`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_append), [`MIPRE.Tailored.Intro.satisfies_append_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.satisfies_append_iff), [`MIPRE.Tailored.Intro.place`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.place), [`MIPRE.Tailored.Intro.length_place`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_place), [`MIPRE.Tailored.Intro.dotL_place`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_place), [`MIPRE.Tailored.Intro.unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.unit), [`MIPRE.Tailored.Intro.dotL_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_unit), [`MIPRE.Tailored.Intro.eqCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.eqCons), [`MIPRE.Tailored.Intro.eqCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.eqCons_iff), [`MIPRE.Tailored.Intro.guardCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.guardCons), [`MIPRE.Tailored.Intro.guardCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.guardCons_iff), [`MIPRE.Tailored.Intro.place2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.place2), [`MIPRE.Tailored.Intro.dotL_place2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_place2), [`MIPRE.Tailored.Intro.inputOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.inputOf), [`MIPRE.Tailored.Intro.reindex`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.reindex), [`MIPRE.Tailored.Intro.dotL_split_right`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dotL_split_right), [`MIPRE.Tailored.Intro.satisfies_reindex_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.satisfies_reindex_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1667](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1667)
