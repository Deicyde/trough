---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.lift_wordFG, MIPRE.Tailored.Sofic.Measure.isClopen_passSet, SubgroupTestValue.SubgroupTestData.continuous_valOn, SubgroupTestValue.SubgroupTestData.valOn_of_eq, SubgroupTestValue.SubgroupTestData.valOn_finDesc, SubgroupTestValue.finDescIRS_subset_IRS
statement: formalized
proof: formalized
---

# The value is a continuous functional; I:550

The value against a measure is weak-$*$ continuous, and the value against $\Phi(\sigma)$ is the value of $\sigma$. Finitely described IRSs are IRSs.

## Depends on

- [The value of a measure, and the ergodic value; I:486–499](../part-01/def-erg-value.md)

## Proof

Each passing set is clopen in the product topology, so its measure is continuous in $\mu$; the value is a finite weighted sum of these.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.lift_wordFG`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.lift_wordFG), [`MIPRE.Tailored.Sofic.Measure.isClopen_passSet`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.isClopen_passSet), [`SubgroupTestValue.SubgroupTestData.continuous_valOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.continuous_valOn), [`SubgroupTestValue.SubgroupTestData.valOn_of_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.valOn_of_eq), [`SubgroupTestValue.SubgroupTestData.valOn_finDesc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.valOn_finDesc), [`SubgroupTestValue.finDescIRS_subset_IRS`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.finDescIRS_subset_IRS).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 417](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L417)
