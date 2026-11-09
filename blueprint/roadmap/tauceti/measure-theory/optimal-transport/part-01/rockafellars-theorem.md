---
declaration: theorem
origin: cited
lean: TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential, TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_innerₗ_subset_subdifferential
statement: formalized
proof: formalized
---

# Rockafellar's theorem

A cyclically monotone set lies in the graph of the
subdifferential of a Legendre–Fenchel conjugate `g⋆`, hence of a convex function that is lower
semicontinuous for every topology compatible with the pairing, and is never `⊥` as soon as the
set is nonempty (`TauCeti.apply_ne_bot_of_mem_subdifferential`).

```lean
TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [AddCommGroup E] [_root_.Module ℝ E] [AddCommMonoid F]
  [_root_.Module ℝ F] {B : E →ₗ[ℝ] F →ₗ[ℝ] ℝ} {Γ : Set (E × F)}
  (hΓ : TauCeti.IsCyclicallyMonotone (TauCeti.pairingCost B) Γ) :
  ∃ g, Γ ⊆ {p | p.2 ∈ TauCeti.subdifferential B (TauCeti.fenchelConjugate B.flip g) p.1}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fenchel–Young inequality](../../../analysis/part-02/convex/the-fenchel-young-inequality.md)
- [The theorem of Rockafellar and Rüschendorf](../part-02/the-theorem-of-rockafellar-and-ruschendorf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/CTransform/Rockafellar.html#TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential).

## Other forms

**Rockafellar's theorem for the quadratic cost.** Formalized in Tau Ceti as [`TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_innerₗ_subset_subdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/CTransform/Quadratic.html#TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_inner%E2%82%97_subset_subdifferential).

```lean
TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_innerₗ_subset_subdifferential.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] {S : Set (E × E)}
  (hS : TauCeti.IsCyclicallyMonotone (fun p => ‖p.1 - p.2‖ ^ 2 / 2) S) :
  ∃ g,
    S ⊆ {p | p.2 ∈ TauCeti.subdifferential (innerₗ E) (TauCeti.fenchelConjugate (innerₗ E) g) p.1}
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/CTransform/Rockafellar.html#TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential)
- [Source of `TauCeti.IsCyclicallyMonotone.exists_fenchelConjugate_subset_subdifferential` in TauCeti/MeasureTheory/OptimalTransport/CTransform/Rockafellar.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/CTransform/Rockafellar.lean#L72)
