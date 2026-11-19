---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.passes_iff, MIPRE.Tailored.Sofic.value_eq_sum, MIPRE.Tailored.Sofic.length_consWords_le'
statement: formalized
proof: formalized
---

# Passing a challenge under Checks 1–3

For an action passing Checks 1–3 everywhere, a point passes the challenge at $(x, y)$ exactly when the constraint words of the entries whose readable part is the point's readable value fix it; and there are at most $2^{\ell(x) + \ell(y) + 1} + 1$ constraint words.

## Depends on

- [The associated subgroup test; I:2086](def-assoc-test.md)

## Proof

The fixed literals and the readable literals of the point's own clause hold, and those of every other clause fail since $J$ moves every point.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.passes_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.passes_iff), [`MIPRE.Tailored.Sofic.value_eq_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.value_eq_sum), [`MIPRE.Tailored.Sofic.length_consWords_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.length_consWords_le').

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 263](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L263)
