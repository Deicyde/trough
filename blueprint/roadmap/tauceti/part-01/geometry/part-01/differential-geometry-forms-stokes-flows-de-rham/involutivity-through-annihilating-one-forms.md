---
declaration: theorem
origin: cited
lean: TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv
statement: formalized
proof: formalized
---

# Involutivity through annihilating one-forms

A smooth distribution `D` on a Hausdorff
manifold is involutive exactly when, for every smooth one-form `α` annihilating `D`, the
exterior derivative `dα` vanishes on pairs of vectors of `D`.

```lean
TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] {k : ℕ} {D : (x : M) → Submodule ℝ (TangentSpace I x)} [T2Space M]
  [IsManifold I (↑⊤) M] (hD : TauCeti.IsContMDiffDistribution I (↑⊤) k D) :
  TauCeti.IsInvolutiveDistribution I D ↔
    ∀ (α : TauCeti.RoughForm I M ℝ 1),
      TauCeti.IsSmoothForm I (↑⊤) α →
        (∀ (x : M), D x ≤ α.ker x) →
          ∀ (x : M), ∀ v ∈ D x, ∀ w ∈ D x, (TauCeti.mextDeriv α x) ![v, w] = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula for the Levi form](../../part-02/manifold/part-01/cartans-formula-for-the-levi-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Annihilator.html#TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Annihilator.html#TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv)
- [Source of `TauCeti.isInvolutiveDistribution_iff_forall_mextDeriv` in TauCeti/Geometry/Manifold/Distribution/Annihilator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Distribution/Annihilator.lean#L320)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
