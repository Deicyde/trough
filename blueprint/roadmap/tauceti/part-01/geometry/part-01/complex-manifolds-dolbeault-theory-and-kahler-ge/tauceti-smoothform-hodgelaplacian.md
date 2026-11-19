---
declaration: def
origin: cited
lean: TauCeti.SmoothForm.hodgeLaplacian
statement: formalized
---

# TauCeti.SmoothForm.hodgeLaplacian

The Hodge Laplacian `Δ = d*d + dd*` of smooth `k`-forms on an oriented Riemannian manifold of
dimension `m = k + l`. In degree `0` only `d*d` is present, and in the top degree `k = m` only
`dd*` is present, since there are no forms of negative degree and the `(m + 1)`-forms vanish; on
a zero-dimensional manifold it is zero. This is the nonnegative sign convention:
`0 ≤ ∫_M ⟨Δα, α⟩ vol` (`TauCeti.SmoothForm.integralTopForm_inner_hodgeLaplacian_self_nonneg`).
It is the Laplacian `TauCeti.SmoothForm.laplacian` of `D = d` and `δ = d*`.

```lean
TauCeti.SmoothForm.hodgeLaplacian.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m : ℕ}
  (o : TauCeti.Manifold.Orientation I M (Fin m)) {k l : ℕ} :
  k + l = m → TauCeti.SmoothForm I M ℝ k →ₗ[ℝ] TauCeti.SmoothForm I M ℝ k
```

## Depends on

- [TauCeti.SmoothForm.hodgeStar](tauceti-smoothform-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.hodgeLaplacian`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.hodgeLaplacian).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.hodgeLaplacian`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Codifferential.html#TauCeti.SmoothForm.hodgeLaplacian)
- [Source of `TauCeti.SmoothForm.hodgeLaplacian` in TauCeti/Geometry/Manifold/Riemannian/Codifferential.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Codifferential.lean#L354)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
