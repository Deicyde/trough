---
declaration: corollary
origin: cited
lean: SubgroupTestValue.SubgroupTestData.valSof_le_valErg, SubgroupTestValue.SubgroupTestData.valSof_eq_valErg
statement: formalized
proof: formalized
---

# The sofic value is at most the ergodic value, with equality under Aldous–Lyons; Corollary I:550

For every test, $\mathrm{val}_{\mathrm{sof}}(T) \leq \mathrm{val}_{\mathrm{erg}}(T)$, and if the Aldous–Lyons conjecture holds they are equal.

## Depends on

- [The value is a continuous functional; I:550](lem-val-on-continuous.md)

## Proof

The finitely described IRSs are IRSs; under the conjecture every IRS is a weak-$*$ limit of finitely described ones, and the value is continuous.

## Lean

Formalized as [`SubgroupTestValue.SubgroupTestData.valSof_le_valErg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.valSof_le_valErg), [`SubgroupTestValue.SubgroupTestData.valSof_eq_valErg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.valSof_eq_valErg).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 434](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L434)
