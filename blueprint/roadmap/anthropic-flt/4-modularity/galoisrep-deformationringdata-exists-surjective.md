---
declaration: theorem
origin: cited
lean: GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum
statement: formalized
proof: formalized
---

# GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum

```lean
theorem GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum {𝒪 : Type} [CommRing 𝒪] [IsDomain 𝒪] [IsDiscreteValuationRing 𝒪] [IsAdicComplete (IsLocalRing.maximalIdeal 𝒪) 𝒪] {ρbar : ResidualGaloisRep (IsLocalRing.ResidueField 𝒪)} {𝒟 : ∀ ⦃A : Type⦄ [CommRing A] [IsLocalRing A] [Algebra 𝒪 A], GaloisRepAdic A → Prop} (D : GaloisRep.DeformationRingData 𝒪 ρbar 𝒟) {N : ℕ} [NeZero N] {S : Set ℕ} {θ : CuspForm.heckeAlgebra N 2 S →+* IsLocalRing.ResidueField 𝒪} {T : Type} [CommRing T] [IsLocalRing T] [IsNoetherianRing T] [IsAdicComplete (IsLocalRing.maximalIdeal T) T] [Algebra 𝒪 T] [IsLocalHom (algebraMap 𝒪 T)] [Module.Finite 𝒪 T] [Module.Free 𝒪 T] (H : CuspForm.HeckeGaloisRepDatum N S 𝒪 θ T) (hS : ∀ q : ℕ, q.Prime → q ∣ N → q ∈ S) (h𝒟 : 𝒟 H.ρ) (hres : H.ρ.residual.IsEquiv (ρbar.baseChangeAlong (IsLocalRing.ResidueField.map (algebraMap 𝒪 T)))) : ∃ φ : D.R →ₐ[𝒪] T, Function.Surjective φ ∧ ∃ hφ : IsLocalHom (φ : D.R →+* T), (D.ρ.baseChangeAlong (φ : D.R →+* T) hφ).IsEquiv H.ρ
```

*Quoted from [Theorems/Thm_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean#L6) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “R=T”, “R = T”, “Taylor-Wiles patching”, “Diamond”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum`, stated in [Theorems/Thm_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean#L6) and proved in [P2M/Sol/S_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum` in Theorems/Thm_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean#L6)
- [Proof of `GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum` in P2M/Sol/S_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_GaloisRep_DeformationRingData_exists_surjective_algHom_of_heckeGaloisRepDatum.lean)
- [The repository's documentation page for `GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum)
