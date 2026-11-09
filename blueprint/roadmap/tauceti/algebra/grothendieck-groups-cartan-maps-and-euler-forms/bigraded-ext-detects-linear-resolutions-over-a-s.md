---
declaration: theorem
origin: cited
lean: TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal
statement: formalized
proof: formalized
---

# Bigraded Ext detects linear resolutions over a semisimple degree-zero part

Suppose that
`A` is finite-dimensional and nonnegatively graded, with semisimple degree-zero part. For an
exhaustive family of finite simple modules concentrated in degree zero, every simple admits a
linear graded projective resolution if and only if every entry of the full bigraded Ext Poincare
matrix has diagonal support.

Unlike `TauCeti.forall_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal`, this statement does not
take a preselected family of minimal resolutions: their existence, with finite-dimensional terms,
follows from semisimplicity of the degree-zero part.

```lean
TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal.{uk, uA, uI} {k : Type uk}
  [Field k] {A : Type uA} [Ring A] [Algebra k A] {𝒜 : ℤ → Submodule k A} [GradedAlgebra 𝒜]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)] {I : Type uI} [IsSemisimpleRing ↥(𝒜 0)]
  [Module.Finite k A] (S : I → (TauCeti.gradedFiniteModules 𝒜).FullSubcategory)
  (hS : TauCeti.IsExhaustiveGradedSimpleFamily S)
  (hSzero : ∀ (i : I) (p : ℤ), p ≠ 0 → (S i).obj.grading.piece ℤ p = ⊥)
  (h :
    TauCeti.IsGradedEulerAdmissibleOn (TauCeti.gradedFiniteModules 𝒜)
      (TauCeti.gradedFiniteModules 𝒜))
  (hneg : ∀ p < 0, 𝒜 p = ⊥) {b : ℕ}
  (hb :
    ∀ (i j : I),
      TauCeti.IsGradedExtBoundedBy (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj b) :
  (∀ (i : I), ∃ r, r.IsLinear) ↔
    ∀ (i j : I),
      TauCeti.Bigraded.IsDiagonal (TauCeti.bigradedExtPoincareMatrix (fun i => (S i).obj) ⋯ b i j)
```

## Depends on

- [TauCeti.GradedProjectiveResolution.IsLinear](tauceti-gradedprojectiveresolution-islinear.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/LinearResolution/Poincare.html#TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/LinearResolution/Poincare.html#TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal)
- [Source of `TauCeti.forall_exists_isLinear_iff_bigradedExtPoincareMatrix_isDiagonal` in TauCeti/Algebra/Category/GradedModuleCat/LinearResolution/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/LinearResolution/Poincare.lean#L195)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
