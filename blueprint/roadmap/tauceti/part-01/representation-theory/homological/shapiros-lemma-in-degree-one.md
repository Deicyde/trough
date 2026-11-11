---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.explicitShapiro1, TauCeti.TateCohomology.herbrandQuotient_coind, TauCeti.ContinuousCohomology.indInflationShapiroIso, TauCeti.TateCohomology.coindIsoPos, TauCeti.TateCohomology.coindIso, TauCeti.ContinuousCohomology.bijective_shapiroMap_one, TauCeti.ContCohomology.explicitShapiro2, TauCeti.ContinuousCohomology.bijective_shapiroMap_two, TauCeti.ContCohomology.explicitShapiro0, TauCeti.ContinuousCohomology.bijective_shapiroMap_zero, TauCeti.ContinuousCohomology.bijective_shapiroMap_of_le_two, TauCeti.ContinuousCohomology.bijective_shapiroMap, TauCeti.ContinuousCohomology.isIso_shapiroMap, TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMap, TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMapTopRep, groupCohomology.map_id_eq_zero_iff_of_comp_eq_resCoindToHom
statement: formalized
---

# Shapiro's lemma in degree one

**Shapiro's lemma in degree one**, `H¹(G, Coind_U^G A) ≅ H¹(U, A)`, for a profinite `G` and a
closed subgroup `U`. The forward map is restriction to `U` followed by evaluation at `1`, and it
involves no choice; the continuous section of `G → G ⧸ U` is used only to prove it bijective.

```lean
TauCeti.ContCohomology.explicitShapiro1.{u, v} (G : Type u) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] (U : Subgroup G) (A : Type v) [AddCommGroup A] [TopologicalSpace A]
  [DiscreteTopology A] [DistribMulAction (↥U) A] [CompactSpace G] [ContinuousSMul (↥U) A]
  [TotallyDisconnectedSpace G] (hU : IsClosed ↑U) :
  TauCeti.ContCohomology.H1 G (TauCeti.DiscreteCoind G U A) ≃+ TauCeti.ContCohomology.H1 (↥U) A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shapiro's isomorphism on an adjunct](shapiros-isomorphism-on-an-adjunct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitShapiro1`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Basic.html#TauCeti.ContCohomology.explicitShapiro1).

## Other forms

**Shapiro's lemma for Herbrand quotients.** Formalized in Tau Ceti as [`TauCeti.TateCohomology.herbrandQuotient_coind`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.html#TauCeti.TateCohomology.herbrandQuotient_coind).

```lean
TauCeti.TateCohomology.herbrandQuotient_coind.{u} {R G : Type u} [CommRing R] [Group G] [Fintype G]
  [IsCyclic G] (S : Subgroup G) [Fintype ↥S] (A : Rep.{u, u, u} R ↥S) :
  TauCeti.TateCohomology.herbrandQuotient (Rep.coind.{u, u, u, u} S.subtype A) =
    TauCeti.TateCohomology.herbrandQuotient A
```

**Shapiro's lemma for inflated induced representations.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.indInflationShapiroIso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/FiniteQuotient.html#TauCeti.ContinuousCohomology.indInflationShapiroIso).

```lean
TauCeti.ContinuousCohomology.indInflationShapiroIso.{u, v} {R : Type v} [CommRing R]
  [TopologicalSpace R] [DiscreteTopology R] {G : Type (max u v)} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] {V : OpenNormalSubgroup G}
  {C : Subgroup (G ⧸ ↑V.toOpenSubgroup)} (B : Rep.{max u v, v, max u v} R ↥C) (n : ℕ) :
  continuousCohomology n
      (TopRep.res (QuotientGroup.mk' ↑V.toOpenSubgroup)
        (TauCeti.discreteTopRep R (G ⧸ ↑V.toOpenSubgroup) (Rep.ind C.subtype B))) ≅
    continuousCohomology n (TauCeti.ContinuousCohomology.comapInflation V C B).obj
```

**Shapiro's lemma for Tate cohomology in positive degrees.** Formalized in Tau Ceti as [`TauCeti.TateCohomology.coindIsoPos`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Shapiro.html#TauCeti.TateCohomology.coindIsoPos).

```lean
TauCeti.TateCohomology.coindIsoPos.{u} {R G : Type u} [CommRing R] [Group G] [Fintype G]
  (S : Subgroup G) [Fintype ↥S] (A : Rep.{u, u, u} R ↥S) (n : ℕ) [NeZero n] :
  tateCohomology (Rep.coind.{u, u, u, u} S.subtype A) ↑n ≅ tateCohomology A ↑n
```

**Shapiro's lemma for Tate cohomology of a finite cyclic group.** Formalized in Tau Ceti as [`TauCeti.TateCohomology.coindIso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Shapiro.html#TauCeti.TateCohomology.coindIso).

```lean
TauCeti.TateCohomology.coindIso.{u} {R G : Type u} [CommRing R] [Group G] [Fintype G]
  (S : Subgroup G) [Fintype ↥S] (A : Rep.{u, u, u} R ↥S) [IsCyclic G] (n : ℤ) :
  tateCohomology (Rep.coind.{u, u, u, u} S.subtype A) n ≅ tateCohomology A n
```

**Shapiro's lemma in degree one on the canonical carrier.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.bijective_shapiroMap_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Canonical.html#TauCeti.ContinuousCohomology.bijective_shapiroMap_one).

```lean
TauCeti.ContinuousCohomology.bijective_shapiroMap_one.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (U : Subgroup G) (A : Type u) [AddCommGroup A]
  [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥U) A] [CompactSpace G]
  [ContinuousSMul (↥U) A] [TotallyDisconnectedSpace G] (hU : IsClosed ↑U) :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.ContinuousCohomology.shapiroMap U A 1))
```

**Shapiro's lemma in degree two.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitShapiro2`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Basic.html#TauCeti.ContCohomology.explicitShapiro2).

```lean
TauCeti.ContCohomology.explicitShapiro2.{u, v} (G : Type u) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] (U : Subgroup G) (A : Type v) [AddCommGroup A] [DistribMulAction (↥U) A]
  [TopologicalSpace A] [DiscreteTopology A] [CompactSpace G] [ContinuousSMul (↥U) A]
  [TotallyDisconnectedSpace G] (hU : IsClosed ↑U) :
  TauCeti.ContCohomology.H2 G (TauCeti.DiscreteCoind G U A) ≃+ TauCeti.ContCohomology.H2 (↥U) A
```

**Shapiro's lemma in degree two on the canonical carrier.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.bijective_shapiroMap_two`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Canonical.html#TauCeti.ContinuousCohomology.bijective_shapiroMap_two).

```lean
TauCeti.ContinuousCohomology.bijective_shapiroMap_two.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (U : Subgroup G) (A : Type u) [AddCommGroup A]
  [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥U) A] [CompactSpace G]
  [ContinuousSMul (↥U) A] [TotallyDisconnectedSpace G] (hU : IsClosed ↑U) :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.ContinuousCohomology.shapiroMap U A 2))
```

**Shapiro's lemma in degree zero, `H⁰(G, Coind_U^G A) ≅ H⁰(U, A)`, by evaluation at `1`.** Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitShapiro0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Basic.html#TauCeti.ContCohomology.explicitShapiro0).

```lean
TauCeti.ContCohomology.explicitShapiro0.{u, v} (G : Type u) [Group G] [TopologicalSpace G]
  (U : Subgroup G) (A : Type v) [AddCommGroup A] [DistribMulAction (↥U) A]
  [SeparatelyContinuousMul G] :
  ↥(TauCeti.ContCohomology.H0 G (TauCeti.DiscreteCoind G U A)) ≃+
    ↥(TauCeti.ContCohomology.H0 (↥U) A)
```

**Shapiro's lemma in degree zero on the canonical carrier.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.bijective_shapiroMap_zero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Canonical.html#TauCeti.ContinuousCohomology.bijective_shapiroMap_zero).

```lean
TauCeti.ContinuousCohomology.bijective_shapiroMap_zero.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (U : Subgroup G) (A : Type u) [AddCommGroup A]
  [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥U) A] :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.ContinuousCohomology.shapiroMap U A 0))
```

**Shapiro's lemma in degrees at most two on the canonical carrier, in one statement.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.bijective_shapiroMap_of_le_two`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Canonical.html#TauCeti.ContinuousCohomology.bijective_shapiroMap_of_le_two).

```lean
TauCeti.ContinuousCohomology.bijective_shapiroMap_of_le_two.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (U : Subgroup G) (A : Type u) [AddCommGroup A]
  [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥U) A] [CompactSpace G]
  [ContinuousSMul (↥U) A] [TotallyDisconnectedSpace G] (hU : IsClosed ↑U) {n : ℕ} (hn : n ≤ 2) :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.ContinuousCohomology.shapiroMap U A n))
```

**Shapiro's lemma in every degree.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.bijective_shapiroMap`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/AllDegrees.html#TauCeti.ContinuousCohomology.bijective_shapiroMap).

```lean
TauCeti.ContinuousCohomology.bijective_shapiroMap.{u} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] (U : Subgroup G) [TotallyDisconnectedSpace G]
  (hU : IsClosed ↑U) (A : Type u) [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A]
  [DistribMulAction (↥U) A] [ContinuousSMul (↥U) A] (n : ℕ) :
  Function.Bijective
    ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.ContinuousCohomology.shapiroMap U A n))
```

**Shapiro's lemma in every degree, as an isomorphism of `TopModuleCat ℤ`.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.isIso_shapiroMap`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/AllDegrees.html#TauCeti.ContinuousCohomology.isIso_shapiroMap).

```lean
TauCeti.ContinuousCohomology.isIso_shapiroMap.{u} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] (U : Subgroup G) [TotallyDisconnectedSpace G]
  (hU : IsClosed ↑U) (A : Type u) [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A]
  [DistribMulAction (↥U) A] [ContinuousSMul (↥U) A] (n : ℕ) :
  CategoryTheory.IsIso (TauCeti.ContinuousCohomology.shapiroMap U A n)
```

**Shapiro's lemma in every degree, on cochains.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMap`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/AllDegrees.html#TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMap).

```lean
TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMap.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] (U : Subgroup G)
  [TotallyDisconnectedSpace G] (hU : IsClosed ↑U) (A : Type u) [AddCommGroup A] [TopologicalSpace A]
  [DiscreteTopology A] [DistribMulAction (↥U) A] [ContinuousSMul (↥U) A] :
  QuasiIso (TauCeti.ContinuousCohomology.shapiroCochainMap U A)
```

**Shapiro's lemma on cochains for smooth discrete representations over any ring.** Formalized in Tau Ceti as [`TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMapTopRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/AllDegrees.html#TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMapTopRep).

```lean
TauCeti.ContinuousCohomology.quasiIso_shapiroCochainMapTopRep.{u, v} {R : Type v} [Ring R]
  [TopologicalSpace R] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] (U : Subgroup G) [TotallyDisconnectedSpace G] (hU : IsClosed ↑U)
  (A : TauCeti.SmoothDiscreteTopRep R ↥U) :
  QuasiIso (TauCeti.ContinuousCohomology.shapiroCochainMapTopRep U A)
```

**Shapiro's lemma through an identification of the subgroup.** Formalized in Tau Ceti as [`groupCohomology.map_id_eq_zero_iff_of_comp_eq_resCoindToHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#groupCohomology.map_id_eq_zero_iff_of_comp_eq_resCoindToHom).

```lean
groupCohomology.map_id_eq_zero_iff_of_comp_eq_resCoindToHom.{u} {k G : Type u} [CommRing k]
  [Group G] (S : Subgroup G) {Γ : Type u} [Group Γ] {X M : Rep.{u, u, u} k G}
  {B : Rep.{u, u, u} k Γ} {f : ↥S →* Γ} (hf : Function.Bijective ⇑f) {r : Γ →* G}
  (hr : ∀ (s : ↥S), r (f s) = ↑s) (φ : Rep.res r X ⟶ B) (ψ : Rep.res S.subtype X ⟶ Rep.res f B)
  (hψ : (Rep.Hom.hom ψ).toLinearMap = (Rep.Hom.hom φ).toLinearMap) (u : X ⟶ M)
  (e : M ≅ Rep.coind.{u, u, u, u} S.subtype (Rep.res f B))
  (hu : CategoryTheory.CategoryStruct.comp u e.hom = Rep.resCoindToHom S.subtype X (Rep.res f B) ψ)
  (n : ℕ) (x : ↑(groupCohomology X n)) :
  (CategoryTheory.ConcreteCategory.hom (groupCohomology.map (MonoidHom.id G) u n)) x = 0 ↔
    (CategoryTheory.ConcreteCategory.hom (groupCohomology.map r φ n)) x = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.explicitShapiro1`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Basic.html#TauCeti.ContCohomology.explicitShapiro1)
- [Source of `TauCeti.ContCohomology.explicitShapiro1` in TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/Shapiro/Basic.lean#L417)
