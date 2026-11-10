---
declaration: theorem
origin: cited
lean: FreyPackage.level_lowering_to_two
statement: formalized
proof: formalized
---

# Level lowering

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.level_lowering_to_two (P : FreyPackage) (hmod : P.freyCurve.IsModular) (hirr : GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p) : ∃ f : CuspForm (CongruenceSubgroup.Gamma0 2) 2, f ≠ 0
```

*Quoted from [Theorems/Thm_FreyPackage_level_lowering_to_two.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_to_two.lean#L131) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Ribet”, “level lowering”, “epsilon conjecture”.

PROOF-PATH.md names it in [5. Level lowering](README.md), as the theorem that carries step 5.

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.level_lowering_to_two_of_conductorLevel](freypackage-level-lowering-to-two-of-conductorle.md)
- [FreyPackage.modularRepOfConductorLevel](freypackage-modularrepofconductorlevel.md)

## Lean

`FreyPackage.level_lowering_to_two`, stated in [Theorems/Thm_FreyPackage_level_lowering_to_two.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_to_two.lean#L131) and proved in [P2M/Sol/S_FreyPackage_level_lowering_to_two.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_level_lowering_to_two.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.level_lowering_to_two` in Theorems/Thm_FreyPackage_level_lowering_to_two.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_to_two.lean#L131)
- [Proof of `FreyPackage.level_lowering_to_two` in P2M/Sol/S_FreyPackage_level_lowering_to_two.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_level_lowering_to_two.lean)
- [The repository's documentation page for `FreyPackage.level_lowering_to_two`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.level_lowering_to_two)
