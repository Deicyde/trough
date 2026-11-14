---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.LowIndDegPoly.onAxis, MIPRE.LIDT.LowIndDegPoly.eval_onAxis, MIPRE.LIDT.LowIndDegPoly.eval_shift_eq_eval_onAxis, MIPRE.LIDT.LowIndDegPoly.eval_eq_eval_onAxis, MIPRE.LIDT.LowIndDegPoly.natDegree_onAxis_le, MIPRE.LIDT.LowIndDegPoly.coeff_onAxis, MIPRE.LIDT.card_shift_eq_le, MIPRE.LIDT.card_pairs_shift_eq_le, MIPRE.LIDT.card_shift_ne_ge
statement: formalized
proof: formalized
---

# Shifting a polynomial along an axis

Let $g$ be a polynomial in $n$ variables of individual degree at most $d$ over a field with $q$ elements, with a nonzero coefficient on a monomial containing $X_i$. Then $g(u + t e_i) \neq g(u)$ for at least $q^n (q - (n + 1) d)$ of the pairs $(u, t) \in \mathbb{F}_q^n \times \mathbb{F}_q$.

## Depends on

- [Extracting exactly linear combined codewords](../../background-results/part-01/lem-lidt-ldc-extraction.md)

## Proof

Restricted to the axis-parallel line through $u$ in direction $i$, $g$ is a univariate polynomial of degree at most $d$, whose coefficient on the power of $X_i$ in that monomial is a nonzero polynomial $G$ evaluated at $u$. Where $G(u) \neq 0$ the restriction is not constant, so it takes the value $g(u)$ at most $d$ times; and $G(u) = 0$ at no more than $n d q^{n-1}$ points, by Schwartz–Zippel.

## Lean

Formalized as [`MIPRE.LIDT.LowIndDegPoly.onAxis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.onAxis), [`MIPRE.LIDT.LowIndDegPoly.eval_onAxis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.eval_onAxis), [`MIPRE.LIDT.LowIndDegPoly.eval_shift_eq_eval_onAxis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.eval_shift_eq_eval_onAxis), [`MIPRE.LIDT.LowIndDegPoly.eval_eq_eval_onAxis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.eval_eq_eval_onAxis), [`MIPRE.LIDT.LowIndDegPoly.natDegree_onAxis_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.natDegree_onAxis_le), [`MIPRE.LIDT.LowIndDegPoly.coeff_onAxis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.coeff_onAxis), [`MIPRE.LIDT.card_shift_eq_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.card_shift_eq_le), [`MIPRE.LIDT.card_pairs_shift_eq_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.card_pairs_shift_eq_le), [`MIPRE.LIDT.card_shift_ne_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.card_shift_ne_ge).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3277](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3277)
