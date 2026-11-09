---
declaration: theorem
origin: cited
lean: WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd
statement: formalized
proof: formalized
---

# WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd

```lean
set_option autoImplicit false

open scoped WeierstrassCurve.Affine

theorem WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd (p : ℕ) (hp : p = 3 ∨ p = 5)
    (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0) (hW : W.IsSemistableModel) (hirr : W.ModRepIsIrreducible p)
    (M₀ : ℕ) [NeZero M₀] (hres₀ : W.IsResiduallyModularOfLevel p M₀)
    (hM₀ : ¬ p ^ 2 ∣ M₀)
    (hM₀3 : ∀ q : ℕ, q.Prime → q ≠ p → ¬ q ^ 3 ∣ M₀) :
    Mlc1IsModularModelOfExactConductorLevel W
```

*Quoted from [Theorems/Thm_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean, line 120](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean#L120) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “modularity lifting”, “R=T”, “R = T”, “Taylor-Wiles”, “p = 5”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [Algebra.PatchingDatum.nonempty_patchingLevel_bot](algebra-patchingdatum-nonempty-patchinglevel-bot.md)
- [CuspForm.newformBadPrimeCoeff](../5-level-lowering/cuspform-newformbadprimecoeff.md)
- [GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum](galoisrep-deformationringdata-exists-surjective.md)
- [ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd](residualgaloisrep-isabsolutelyirreducible-of-isi.md)
- [WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd](weierstrasscurve-ismodularmodeloflevel-conductor.md)
- [WeierstrassCurve.isModularModelOfLevel_of_patchingDatum](weierstrasscurve-ismodularmodeloflevel-of-patchi.md)
- [WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf](../5-level-lowering/weierstrasscurve-isresiduallymodularoflevel-div.md)
- [WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel](weierstrasscurve-nonempty-deformationringdata-or.md)

## Lean

`WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd`, stated in [Theorems/Thm_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean, line 120](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean#L120) and proved in [P2M/Sol/S_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd` in Theorems/Thm_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean#L120)
- [Proof of `WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd` in P2M/Sol/S_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd.lean)
- [The repository's documentation page for `WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd)
