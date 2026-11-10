---
declaration: theorem
origin: cited
lean: WeierstrassCurve.modularity_of_semistableModel
statement: formalized
proof: formalized
---

# WeierstrassCurve.modularity_of_semistableModel

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem WeierstrassCurve.modularity_of_semistableModel (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0) (hW : W.IsSemistableModel) : (W.map (Int.castRingHom ℚ)).IsModular
```

*Quoted from [Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean#L131) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Wiles”, “Taylor-Wiles”, “modularity theorem”, “semistable modularity”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.isResiduallyModularOfLevel_of_switch](weierstrasscurve-isresiduallymodularoflevel-of-s.md)
- [WeierstrassCurve.isResiduallyModular_three_and_noInertiaFixedTorsion_and_not_cube_dvd_of_isSemistableModel](weierstrasscurve-isresiduallymodular-three-and-n.md)
- [WeierstrassCurve.modThreeOrFiveIrreducible](weierstrasscurve-modthreeorfiveirreducible.md)
- [WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_inertia_moves_torsion_of_eq_three_of_not_cube_dvd](weierstrasscurve-modularityliftingatconductor-th.md)
- [WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd](weierstrasscurve-modularityliftingatconductor-th-2.md)
- [WeierstrassCurve.threeFiveSwitchCurve](weierstrasscurve-threefiveswitchcurve.md)

## Lean

`WeierstrassCurve.modularity_of_semistableModel`, stated in [Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean#L131) and proved in [P2M/Sol/S_WeierstrassCurve_modularity_of_semistableModel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_modularity_of_semistableModel.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.modularity_of_semistableModel` in Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modularity_of_semistableModel.lean#L131)
- [Proof of `WeierstrassCurve.modularity_of_semistableModel` in P2M/Sol/S_WeierstrassCurve_modularity_of_semistableModel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_modularity_of_semistableModel.lean)
- [The repository's documentation page for `WeierstrassCurve.modularity_of_semistableModel`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.modularity_of_semistableModel)
