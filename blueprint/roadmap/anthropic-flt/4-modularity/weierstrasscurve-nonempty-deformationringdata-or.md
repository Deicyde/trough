---
declaration: theorem
origin: cited
lean: WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel
statement: formalized
proof: formalized
---

# WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
theorem WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel (p : ℕ) [Fact p.Prime] (hp2 : p ≠ 2) (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0)
    (hW : W.IsSemistableModel)
    (hcard₁ : Nat.card (Submodule.torsionBy ℤ
      ((W.map (Int.castRingHom ℚ))⁄(AlgebraicClosure ℚ)).Point p) = p ^ 2)
    (hker : GaloisFactorsThroughFiniteLevel
      (WeierstrassCurve.Affine.Point.galoisRepModuleEnd (K := AlgebraicClosure ℚ) ℚ
        (W.map (Int.castRingHom ℚ)) p))
    (S : Finset ℕ) (hS : ∀ q ∈ S, q.Prime) (hpS : p ∈ S)
    (hbadS : ∀ q : ℕ, q.Prime → (q : ℤ) ∣ W.Δ → q ∈ S)
    {𝒪 : Type} [CommRing 𝒪] [IsDomain 𝒪] [IsDiscreteValuationRing 𝒪]
    [IsAdicComplete (IsLocalRing.maximalIdeal 𝒪) 𝒪] [Finite (IsLocalRing.ResidueField 𝒪)]
    [CharZero 𝒪] (hp𝒪 : (p : 𝒪) ∈ IsLocalRing.maximalIdeal 𝒪)
    (ι : ZMod p →+* IsLocalRing.ResidueField 𝒪)
    (habs : (((W.map (Int.castRingHom ℚ)).residualGaloisRepOf p hcard₁ hker).baseChangeAlong
      ι).IsAbsolutelyIrreducible)
    (hord : ¬ W.IsGoodPrimeFor p ∨ ¬ (p : ℤ) ∣ W.apOfModel p) :
    Nonempty (GaloisRep.DeformationRingData 𝒪
      (((W.map (Int.castRingHom ℚ)).residualGaloisRepOf p hcard₁ hker).baseChangeAlong ι)
      (GaloisRep.ordinaryCondition 𝒪 p S))
```

*Quoted from [Theorems/Thm_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean, line 21](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean#L21) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel`, stated in [Theorems/Thm_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean, line 21](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean#L21) and proved in [P2M/Sol/S_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel` in Theorems/Thm_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean#L21)
- [Proof of `WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel` in P2M/Sol/S_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel.lean)
- [The repository's documentation page for `WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel)
