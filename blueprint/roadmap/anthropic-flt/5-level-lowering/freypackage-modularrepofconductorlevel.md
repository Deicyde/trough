---
declaration: theorem
origin: cited
lean: FreyPackage.modularRepOfConductorLevel
statement: formalized
proof: formalized
---

# FreyPackage.modularRepOfConductorLevel

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.modularRepOfConductorLevel (P : FreyPackage) : ∃ N : ℕ, P.IsConductorLevel N ∧ P.ModularRepOfLevel N
```

*Quoted from [Theorems/Thm_FreyPackage_modularRepOfConductorLevel.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_modularRepOfConductorLevel.lean#L131) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “arises from level N”, “conductor level”.

PROOF-PATH.md names it in [5. Level lowering](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.isResiduallyModularOfLevel_of_switch](../4-modularity/weierstrasscurve-isresiduallymodularoflevel-of-s.md)
- [WeierstrassCurve.isResiduallyModular_three_and_noInertiaFixedTorsion_and_not_cube_dvd_of_isSemistableModel](../4-modularity/weierstrasscurve-isresiduallymodular-three-and-n.md)
- [WeierstrassCurve.modThreeOrFiveIrreducible](../4-modularity/weierstrasscurve-modthreeorfiveirreducible.md)
- [WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_inertia_moves_torsion_of_eq_three_of_not_cube_dvd](../4-modularity/weierstrasscurve-modularityliftingatconductor-th.md)
- [WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd](../4-modularity/weierstrasscurve-modularityliftingatconductor-th-2.md)
- [WeierstrassCurve.threeFiveSwitchCurve](../4-modularity/weierstrasscurve-threefiveswitchcurve.md)

## Lean

`FreyPackage.modularRepOfConductorLevel`, stated in [Theorems/Thm_FreyPackage_modularRepOfConductorLevel.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_modularRepOfConductorLevel.lean#L131) and proved in [P2M/Sol/S_FreyPackage_modularRepOfConductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_modularRepOfConductorLevel.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.modularRepOfConductorLevel` in Theorems/Thm_FreyPackage_modularRepOfConductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_modularRepOfConductorLevel.lean#L131)
- [Proof of `FreyPackage.modularRepOfConductorLevel` in P2M/Sol/S_FreyPackage_modularRepOfConductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_modularRepOfConductorLevel.lean)
- [The repository's documentation page for `FreyPackage.modularRepOfConductorLevel`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.modularRepOfConductorLevel)
