---
declaration: theorem
origin: cited
lean: TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler
statement: formalized
proof: formalized
---

# Linearity is the Cartan--Poincaré identity over a semisimple degree-zero part

If `A` is
finite-dimensional and nonnegatively graded with semisimple degree-zero part, every `Sᵢ` has a
linear graded projective resolution exactly when `Cᵀ · P_tot(-q) = diagonal (fun i ↦ gdim(eᵢ • Sᵢ))`
for the total Ext Poincaré matrix `P_tot`, as in
`TauCeti.forall_isLinear_iff_cartan_poincare_maslovEuler`.

```lean
TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler.{uk, uA, uI} {k : Type uk} [Field k]
  {A : Type uA} [Ring A] [Algebra k A] {𝒜 : ℤ → Submodule k A} [GradedAlgebra 𝒜]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)] {I : Type uI} [Module.Finite k A] [Fintype I]
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
  [IsSemisimpleRing ↥(𝒜 0)]
  (h :
    TauCeti.IsGradedEulerAdmissibleOn (TauCeti.gradedFiniteModules 𝒜)
      (TauCeti.gradedFiniteModules 𝒜))
  (hneg : ∀ p < 0, 𝒜 p = ⊥) (hconc : ∀ (i : I) (p : ℤ), p ≠ 0 → (S i).obj.grading.piece ℤ p = ⊥)
  {b : ℕ}
  (hb :
    ∀ (i j : I),
      TauCeti.IsGradedExtBoundedBy (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj b) :
  (∀ (i : I), ∃ r, r.IsLinear) ↔
    (TauCeti.gradedCartanMatrix 𝒜 bP
            (TauCeti.gradedSimpleClassBasisOfNeZero S he he₀ hne hself hS)).transpose *
        (TauCeti.bigradedExtPoincareMatrix (fun i => (S i).obj) ⋯ b).map
          ⇑TauCeti.Bigraded.maslovEuler =
      Matrix.diagonal fun i => TauCeti.GradedModuleCat.smulGradedDimension (e i) (S i).obj
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)
- [TauCeti.GradedProjectiveResolution.IsLinear](tauceti-gradedprojectiveresolution-islinear.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.html#TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.html#TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler)
- [Source of `TauCeti.forall_exists_isLinear_iff_cartan_poincare_maslovEuler` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/ExtEuler/Linearity.lean#L216)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
