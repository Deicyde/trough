---
declaration: section
origin: cited
lean: Subgroup.mem_sup_zpowers_iff_of_central_sq_eq_one, CongruenceSubgroup.exists_mem_Gamma_map_eq_of_not_dvd, CongruenceSubgroup.neg_one_mem_Gamma1_iff, ModularGroup.exists_eq_conj_T_zpow_of_trace_sq_eq_four, CongruenceSubgroup.one_mem_strictPeriods_Gamma0
statement: formalized
proof: formalized
---

# Modular group and congruence subgroups

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html).

## Membership in a subgroup joined with a central involution

Membership in the join of a subgroup with the cyclic subgroup generated
by a central involution.

This is the computation behind "up to sign" arguments: for a subgroup
`Γ` of `SL(2, ℤ)`, an element lies in `Γ` adjoined with `-1` exactly when
it or its negative lies in `Γ`. The same pattern recurs for any group with
a central involution: spin groups, dihedral groups, and congruence
subgroups.

Formalized by `Subgroup.mem_sup_zpowers_iff_of_central_sq_eq_one`, a theorem declared in [MathlibExt/GroupTheory/Subgroup/SupZpowers.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/Subgroup/SupZpowers.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html#mem-sup-zpowers-iff-of-central-sq-eq-one).

## Reduction mod p maps Γ(N) onto SL(2, ℤ/pℤ) when p does not divide N

If `p` does not divide `N`, then reduction modulo `p` maps `Γ(N)` onto
`SL(2, ZMod p)`.

Formalized by `CongruenceSubgroup.exists_mem_Gamma_map_eq_of_not_dvd`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/CongruenceSubgroupReduction.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/CongruenceSubgroupReduction.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html#exists-mem-gamma-map-eq-of-not-dvd).

## −1 lies in Γ₁(N) exactly when N ≤ 2

`-1` lies in `Γ₁(N)` if and only if `N ≤ 2`.

Formalized by `CongruenceSubgroup.neg_one_mem_Gamma1_iff`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/CongruenceSubgroupReduction.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/CongruenceSubgroupReduction.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html#neg-one-mem-gamma1-iff).

## Parabolic elements of SL(2, ℤ) are conjugate to ± powers of T

Every element of `SL(2, ℤ)` whose trace squares to `4` is, up to a sign,
conjugate to a power of the translation `T`.

Formalized by `ModularGroup.exists_eq_conj_T_zpow_of_trace_sq_eq_four`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/ModularGroupParabolic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/ModularGroupParabolic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html#exists-eq-conj-t-zpow-of-trace-sq-eq-fou).

## 1 is a strict period of Γ₀(N)

`1` is a strict period of `Γ₀(N)`: the translation matrix `T` lies in
`Γ₀(N)`, and the strict periods then contain the integer multiples of `1`.

Formalized by `CongruenceSubgroup.one_mem_strictPeriods_Gamma0`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/StrictPeriodsGamma0.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/StrictPeriodsGamma0.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html#one-mem-strict-periods-gamma0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modular group and congruence subgroups](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-group-and-congruence-subgroups)
