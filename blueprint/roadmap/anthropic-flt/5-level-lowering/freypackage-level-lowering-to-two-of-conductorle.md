---
declaration: theorem
origin: cited
lean: FreyPackage.level_lowering_to_two_of_conductorLevel
statement: formalized
proof: formalized
---

# FreyPackage.level_lowering_to_two_of_conductorLevel

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.level_lowering_to_two_of_conductorLevel (P : FreyPackage) (hirr : GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p) {N : ℕ} (hcond : P.IsConductorLevel N) (hmod : P.ModularRepOfLevel N) : ∃ f : CuspForm (CongruenceSubgroup.Gamma0 2) 2, f ≠ 0
```

*Quoted from [Theorems/Thm_FreyPackage_level_lowering_to_two_of_conductorLevel.lean, line 91](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_to_two_of_conductorLevel.lean#L91) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

PROOF-PATH.md names it in [5. Level lowering](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.freyGaloisRep_isUnramifiedAt](freypackage-freygaloisrep-isunramifiedat.md)
- [FreyPackage.level_lowering_at_p_of_conductorLevel](freypackage-level-lowering-at-p-of-conductorleve.md)
- [FreyPackage.level_lowering_odd_prime_of_conductorLevel](freypackage-level-lowering-odd-prime-of-conducto.md)
- [S₂(Γ₀(2)) = 0](../6-s2-0-2-0/modularform-s2-gamma0-2-eq-zero.md)
- [ModularForm.S2_Gamma0_one_eq_zero](../6-s2-0-2-0/modularform-s2-gamma0-one-eq-zero.md)

## Lean

`FreyPackage.level_lowering_to_two_of_conductorLevel`, stated in [Theorems/Thm_FreyPackage_level_lowering_to_two_of_conductorLevel.lean, line 91](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_to_two_of_conductorLevel.lean#L91) and proved in [P2M/Sol/S_FreyPackage_level_lowering_to_two_of_conductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_level_lowering_to_two_of_conductorLevel.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.level_lowering_to_two_of_conductorLevel` in Theorems/Thm_FreyPackage_level_lowering_to_two_of_conductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_to_two_of_conductorLevel.lean#L91)
- [Proof of `FreyPackage.level_lowering_to_two_of_conductorLevel` in P2M/Sol/S_FreyPackage_level_lowering_to_two_of_conductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_level_lowering_to_two_of_conductorLevel.lean)
- [The repository's documentation page for `FreyPackage.level_lowering_to_two_of_conductorLevel`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.level_lowering_to_two_of_conductorLevel)
