---
declaration: theorem
origin: cited
lean: FreyPackage.level_lowering_at_p_of_conductorLevel
statement: formalized
proof: formalized
---

# FreyPackage.level_lowering_at_p_of_conductorLevel

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.level_lowering_at_p_of_conductorLevel (P : FreyPackage) {N : ℕ} (hcond : P.IsConductorLevel N) (hpN : P.p ∣ N) (hirr : GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p) (hmod : P.ModularRepOfLevel N) : ∃ M : ℕ, M ∣ N ∧ ¬ P.p ∣ M ∧ P.ModularRepOfLevel M
```

*Quoted from [Theorems/Thm_FreyPackage_level_lowering_at_p_of_conductorLevel.lean, line 70](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_at_p_of_conductorLevel.lean#L70) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Mazur-Ribet”, “level lowering at p”.

PROOF-PATH.md names it in [5. Level lowering](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [CuspForm.newformBadPrimeCoeff](cuspform-newformbadprimecoeff.md)
- [FreyCurve.isPeuRamifieeAt_odd_of_integralForm](freycurve-ispeuramifieeat-odd-of-integralform.md)
- [FreyPackage.eigenformResidualAttachmentAtFamily](freypackage-eigenformresidualattachmentatfamily.md)
- [ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd](../4-modularity/residualgaloisrep-isabsolutelyirreducible-of-isi.md)

## Lean

`FreyPackage.level_lowering_at_p_of_conductorLevel`, stated in [Theorems/Thm_FreyPackage_level_lowering_at_p_of_conductorLevel.lean, line 70](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_at_p_of_conductorLevel.lean#L70) and proved in [P2M/Sol/S_FreyPackage_level_lowering_at_p_of_conductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_level_lowering_at_p_of_conductorLevel.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.level_lowering_at_p_of_conductorLevel` in Theorems/Thm_FreyPackage_level_lowering_at_p_of_conductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_level_lowering_at_p_of_conductorLevel.lean#L70)
- [Proof of `FreyPackage.level_lowering_at_p_of_conductorLevel` in P2M/Sol/S_FreyPackage_level_lowering_at_p_of_conductorLevel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_level_lowering_at_p_of_conductorLevel.lean)
- [The repository's documentation page for `FreyPackage.level_lowering_at_p_of_conductorLevel`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.level_lowering_at_p_of_conductorLevel)
