---
declaration: theorem
origin: cited
lean: TauCeti.ContCohomology.explicitCor1_mackey, TauCeti.ContCohomology.explicitCor2_mackey, TauCeti.ContCohomology.explicitCor0_mackey, TauCeti.ContinuousCohomology.corestriction_mackey
statement: formalized
proof: formalized
---

# The Mackey double-coset formula in degree one (NSW (1.5.6))

for an open subgroup `U` of
finite index and any subgroup `V`,
`res^G_V ∘ cor^G_U = ∑_{VsU} cor^V_{V ⊓ sUs⁻¹} ∘ (s)_* ∘ res` on `H¹(U, M)`, for any choice `r` of
representatives `s = r D` of the double cosets.

```lean
TauCeti.ContCohomology.explicitCor1_mackey.{u, v} (G : Type u) [Group G] (M : Type v)
  [AddCommGroup M] [DistribMulAction G M] (U V : Subgroup G) [U.FiniteIndex]
  (r : DoubleCoset.Quotient ↑V ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑V ↑U), DoubleCoset.mk V U (r D) = D) [TopologicalSpace G]
  [IsTopologicalGroup G] [TopologicalSpace M] [IsTopologicalAddGroup M] [ContinuousSMul G M]
  (hU : IsOpen ↑U) (x : TauCeti.ContCohomology.H1 (↥U) M) :
  (TauCeti.ContCohomology.explicitRes1 G M V) ((TauCeti.ContCohomology.explicitCor1 G M U hU) x) =
    ∑ D, (TauCeti.ContCohomology.explicitMackeyTerm1 G M U V hU (r D)) x
```

## Depends on

- [Shapiro's lemma in degree one](shapiros-lemma-in-degree-one.md)

## Informally uses

- [The Mackey formula for the degree-one corestriction cochain](the-mackey-formula-for-the-degree-one-corestrict.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitCor1_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.explicitCor1_mackey).

## Other forms

**The Mackey double-coset formula in degree two (NSW (1.5.6)).** Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitCor2_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.explicitCor2_mackey).

```lean
TauCeti.ContCohomology.explicitCor2_mackey.{u, v} (G : Type u) [Group G] (M : Type v)
  [AddCommGroup M] [DistribMulAction G M] (U V : Subgroup G) [U.FiniteIndex]
  (r : DoubleCoset.Quotient ↑V ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑V ↑U), DoubleCoset.mk V U (r D) = D) [TopologicalSpace G]
  [IsTopologicalGroup G] [TopologicalSpace M] [IsTopologicalAddGroup M] [ContinuousSMul G M]
  (hU : IsOpen ↑U) (x : TauCeti.ContCohomology.H2 (↥U) M) :
  (TauCeti.ContCohomology.explicitRes2 G M V) ((TauCeti.ContCohomology.explicitCor2 G M U hU) x) =
    ∑ D, (TauCeti.ContCohomology.explicitMackeyTerm2 G M U V hU (r D)) x
```

**The Mackey double-coset formula in degree zero (NSW (1.5.6)).** Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitCor0_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.explicitCor0_mackey).

```lean
TauCeti.ContCohomology.explicitCor0_mackey.{u, v} (G : Type u) [Group G] (M : Type v)
  [AddCommGroup M] [DistribMulAction G M] (U V : Subgroup G) [U.FiniteIndex]
  (r : DoubleCoset.Quotient ↑V ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑V ↑U), DoubleCoset.mk V U (r D) = D)
  (m : ↥(TauCeti.ContCohomology.H0 (↥U) M)) :
  (TauCeti.ContCohomology.explicitRes0 G M V) ((TauCeti.ContCohomology.explicitCor0 G M U) m) =
    ∑ D, (TauCeti.ContCohomology.explicitMackeyTerm0 G M U V (r D)) m
```

**The Mackey double-coset formula in every degree (NSW (1.5.6)).** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.corestriction_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/AllDegrees.html#TauCeti.ContinuousCohomology.corestriction_mackey).

```lean
TauCeti.ContinuousCohomology.corestriction_mackey.{u} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] (U V : Subgroup G)
  (M : Type u) [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] (hU : IsOpen ↑U) (hV : IsClosed ↑V) [U.FiniteIndex]
  (r : DoubleCoset.Quotient ↑V ↑U → G)
  (hr : ∀ (D : DoubleCoset.Quotient ↑V ↑U), DoubleCoset.mk V U (r D) = D) (n : ℕ) :
  CategoryTheory.CategoryStruct.comp (TauCeti.ContinuousCohomology.corestriction U M hU n)
      (TauCeti.ContinuousCohomology.res V (TauCeti.ofDiscreteModule ℤ G M) n) =
    ∑ D, TauCeti.ContinuousCohomology.mackeyTerm U V M hU hV (r D) n
```

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.explicitCor1_mackey`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.html#TauCeti.ContCohomology.explicitCor1_mackey)
- [Source of `TauCeti.ContCohomology.explicitCor1_mackey` in TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/Mackey/Basic.lean#L323)
