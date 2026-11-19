---
declaration: theorem
origin: cited
lean: TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries
statement: formalized
proof: formalized
---

# Linearity is the unbounded Cartan–Poincaré identity over a semisimple degree-zero part

Over
a finite-dimensional nonnegatively graded algebra with semisimple degree-zero part, every member of
an exhaustive degree-zero simple family admits a linear graded projective resolution if and only if
`C_psᵀ * P_tot(-q) = diagonal (fun i ↦ dim_k(eᵢ • (Sᵢ)₀))` in `Matrix I I (PowerSeries ℤ)`. No
chosen resolutions or cohomological global-dimension bounds appear in the statement.

```lean
TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries.{uk, uA, uI} {k : Type uk}
  [Field k] {A : Type uA} [Ring A] [Algebra k A] {𝒜 : ℤ → Submodule k A} [GradedAlgebra 𝒜]
  [Module.Finite k A] [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)] {I : Type uI} [Fintype I]
  [DecidableEq I] (S : I → (TauCeti.gradedFiniteModules 𝒜).FullSubcategory) {e : I → A}
  (he : ∀ (i : I), IsIdempotentElem (e i)) (he₀ : ∀ (i : I), e i ∈ 𝒜 0)
  (hI : ∀ (i : I), Ideal.IsHomogeneous 𝒜 (Ideal.span {e i}))
  (hne : Pairwise fun i j => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S j).obj = 0)
  (hself : ∀ (i : I), TauCeti.GradedModuleCat.smulGradedDimension (e i) (S i).obj ≠ 0)
  (hS : TauCeti.IsExhaustiveGradedSimpleFamily S)
  (bP :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)))
  (hbP :
    ∀ (i : I),
      bP i =
        TauCeti.LaurentK0.of (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)
          { obj := TauCeti.GradedModuleCat.ofIdeal 𝒜 (Ideal.span {e i}) ⋯, property := ⋯ })
  [IsSemisimpleRing ↥(𝒜 0)] (hneg : ∀ p < 0, 𝒜 p = ⊥)
  (hconc : ∀ (i : I) (p : ℤ), p ≠ 0 → (S i).obj.grading.piece p = ⊥)
  (h :
    ∀ (i j : I),
      TauCeti.IsGradedExtInternallyFinite k (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj :=
    ⋯) :
  (∀ (i : I), ∃ r, r.IsLinear) ↔
    ((TauCeti.gradedCartanMatrix 𝒜 bP
                (TauCeti.gradedSimpleClassBasisOfNeZero S he he₀ hne hself hS)).map
            fun p => ↑(LaurentPolynomial.trunc p)).transpose *
        (TauCeti.bigradedExtPoincarePowerSeriesMatrix (fun i => (S i).obj) h).map
          ⇑TauCeti.Bigraded.maslovEulerPowerSeries =
      Matrix.diagonal fun i => PowerSeries.C ↑(Module.finrank k ↥(e i • (S i).obj.grading.piece 0))
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)
- [TauCeti.bigradedExtPoincarePowerSeries](tauceti-bigradedextpoincarepowerseries.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.Bigraded.eulerPowerSeries](tauceti-bigraded-eulerpowerseries.md)
- [The unbounded Cartan–Euler formal power-series identity](the-unbounded-cartan-euler-formal-power-series-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.html#TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.html#TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries)
- [Source of `TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEulerPowerSeries` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/PowerSeries.lean#L418)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
