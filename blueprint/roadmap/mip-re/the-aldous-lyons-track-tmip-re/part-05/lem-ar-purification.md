---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.satisfies_iff_pureEqn, MIPRE.Tailored.AnsRed.accepts_iff_pure
statement: formalized
proof: formalized
---

# Purification; fact:completeness_and_soundness_purification

A constraint holds of answers of the right lengths exactly when its purified equation holds of the table of their linear parts. So a tailored game accepts $(a^R a^L, b^R b^L)$ at $(x, y)$ exactly when the purified equations of $L_{xy}(a^R, b^R)$ hold of the table.

## Depends on

- [Purified, triangulated and decoupled systems](def-ar-linear.md)

## Proof depends on

- [Linear forms on windows, and the input's constraints re-indexed](../part-04/lem-intro-forms.md)

## Proof

The inner product of $c$ with $a^R a^L b^R b^L 1$ splits over the five windows; the readable windows and the affine coordinate are known, and in characteristic $2$ they move to the right.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.satisfies_iff_pureEqn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.satisfies_iff_pureEqn), [`MIPRE.Tailored.AnsRed.accepts_iff_pure`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.accepts_iff_pure).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2355](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2355)
