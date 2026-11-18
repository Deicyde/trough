---
declaration: theorem
origin: cited
lean: TauCeti.integralTopForm_mpullback_eq_degree_mul
statement: formalized
proof: formalized
---

# The degree formula [Lee, Thm. 17.35]

for a proper smooth map `f` and a compactly supported
smooth top form `φ` on `N`, `∫_M f^*φ = deg(f) ∫_N φ`.

```lean
TauCeti.integralTopForm_mpullback_eq_degree_mul.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  {H : Type u_2} {H' : Type u_3} {M : Type u_4} {N : Type u_5} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [BoundarylessManifold I M]
  [T2Space M] [TopologicalSpace H'] {J : ModelWithCorners ℝ E H'} [TopologicalSpace N]
  [ChartedSpace H' N] [IsManifold J (↑⊤) N] [BoundarylessManifold J N] [T2Space N]
  [SigmaCompactSpace N] [ConnectedSpace N] {k : ℕ} (o : TauCeti.Manifold.Orientation I M (Fin k))
  (o' : TauCeti.Manifold.Orientation J N (Fin k)) {f : M → N} (hf : ContMDiff I J (↑⊤) f)
  (hfp : IsProperMap f) {φ : TauCeti.RoughForm J N ℝ k} (hφ : TauCeti.IsSmoothForm J (↑⊤) φ)
  (hc : IsCompact (tsupport φ)) :
  TauCeti.integralTopForm o (TauCeti.mpullback I J f φ) =
    ↑(TauCeti.degree o o' f) * TauCeti.integralTopForm o' φ
```

## Depends on

- [TauCeti.degree](tauceti-degree.md)

## Proof depends on

- [The compactly supported Poincaré lemma on the line](../../../part-02/manifold/part-01/the-compactly-supported-poincare-lemma-on-the-li.md)
- [Independence of the regular value](independence-of-the-regular-value.md)
- [The inverse function theorem for manifolds](../../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Poincaré lemma on manifolds](../../../part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)
- [Sard's theorem](../../../part-02/manifold/part-04/sards-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integralTopForm_mpullback_eq_degree_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/Global.html#TauCeti.integralTopForm_mpullback_eq_degree_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.integralTopForm_mpullback_eq_degree_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/Global.html#TauCeti.integralTopForm_mpullback_eq_degree_mul)
- [Source of `TauCeti.integralTopForm_mpullback_eq_degree_mul` in TauCeti/Geometry/Manifold/Degree/Global.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Degree/Global.lean#L188)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
