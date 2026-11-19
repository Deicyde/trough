---
declaration: corollary
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.ceilDiv, MIPRE.Tailored.Sofic.Measure.approx_of_bounds, MIPRE.Tailored.Sofic.Measure.sofValueApproximable_of, MIPRE.Tailored.Sofic.Measure.sofValueApproximable_of_aldousLyons
statement: formalized
proof: formalized
---

# Aldous–Lyons makes the sofic value approximable; Corollary I:605

If the Aldous–Lyons conjecture holds, the sofic value is approximable.

## Depends on

- [The sofic value is at most the ergodic value, with equality under Aldous–Lyons; Corollary I:550](cor-sof-eq-erg.md)
- [Main Theorem I (1): the sofic value is approximable from below; I:594](thm-main-theorem-i-lower.md)
- [Main Theorem I (2): the ergodic value is approximable from above; I:594](thm-main-theorem-i-upper.md)
- [Approximating the sofic value](../part-01/def-sofic-approximable.md)

## Proof

Under the conjecture both sequences converge to the same value from either side; run them until their gap is at most $1/(k+1)$, which happens, and output a point between them.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.ceilDiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.ceilDiv), [`MIPRE.Tailored.Sofic.Measure.approx_of_bounds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.approx_of_bounds), [`MIPRE.Tailored.Sofic.Measure.sofValueApproximable_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.sofValueApproximable_of), [`MIPRE.Tailored.Sofic.Measure.sofValueApproximable_of_aldousLyons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.sofValueApproximable_of_aldousLyons).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 567](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L567)
