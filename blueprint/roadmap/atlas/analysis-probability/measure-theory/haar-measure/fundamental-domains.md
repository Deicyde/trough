---
declaration: section
origin: cited
lean: MeasureTheory.IsFundamentalDomain.iUnion_inv_smul_of_leftCosetRepresentatives, MeasureTheory.exists_measurableSet_isFundamentalDomain_op_of_discreteTopology, MeasureTheory.IsFundamentalDomain.setLIntegral_iUnion_inv_smul_eq_and_setIntegral_eq_of_leftCosetRepresentatives
statement: formalized
proof: formalized
---

# Fundamental domains

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/fundamental-domains/index.html).

## Fundamental domain for a subgroup of countable index

From a fundamental domain for `Γ₁`, a countable union of inverse
coset-representative translates gives a fundamental domain for a subgroup
`Γ₂ ≤ Γ₁` of countable index.

Formalized by `MeasureTheory.IsFundamentalDomain.iUnion_inv_smul_of_leftCosetRepresentatives`, a theorem declared in [MathlibExt/MeasureTheory/Group/FundamentalDomain.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Group/FundamentalDomain.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/fundamental-domains/index.html#i-union-inv-smul-of-left-coset-represent).

## Measurable fundamental domains for discrete subgroups

Every discrete subgroup of a second-countable Hausdorff topological group
admits a measurable fundamental domain for the opposite action, simultaneously
for every measure.

Formalized by `MeasureTheory.exists_measurableSet_isFundamentalDomain_op_of_discreteTopology`, a theorem declared in [MathlibExt/MeasureTheory/Group/FundamentalDomainExists.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Group/FundamentalDomainExists.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/fundamental-domains/index.html#exists-measurable-set-is-fundamental-dom).

## Integrals over a subgroup fundamental domain as sums over cosets

If `𝓕` is a fundamental domain for `Γ₁` and `R` is a system of
representatives for the left cosets of `Γ₂` in `Γ₁`, then integrals over
the union of the translates `((R i)⁻¹) • 𝓕` unfold into sums over `i` of
integrals over `𝓕`, for both `ℝ≥0∞`-valued and Bochner integrals.

Formalized by `MeasureTheory.IsFundamentalDomain.setLIntegral_iUnion_inv_smul_eq_and_setIntegral_eq_of_leftCosetRepresentatives`, a theorem declared in [MathlibExt/MeasureTheory/Group/FundamentalDomainIntegral.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Group/FundamentalDomainIntegral.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/fundamental-domains/index.html#set-lintegral-i-union-inv-smul-eq-and-se).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fundamental domains](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/fundamental-domains/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/haar-measure/fundamental-domains)
