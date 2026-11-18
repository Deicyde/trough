---
declaration: theorem
origin: cited
lean: TauCeti.degree_eq_of_homotopy
statement: formalized
proof: formalized
---

# Homotopy invariance of the degree

If `F : M × [0, 1] → N` is a smooth homotopy from `f`
to `g`, with `M` compact, then `f` and `g` have the same degree.

```lean
TauCeti.degree_eq_of_homotopy.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1} {H : Type u_2}
  {H' : Type u_3} {M : Type u_4} {N : Type u_5} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M]
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E H'} [TopologicalSpace N] [ChartedSpace H' N]
  [IsManifold J (↑⊤) N] [BoundarylessManifold J N] [T2Space N] [SigmaCompactSpace N]
  [ConnectedSpace N] {k : ℕ} [CompactSpace M] (o : TauCeti.Manifold.Orientation I M (Fin k))
  (o' : TauCeti.Manifold.Orientation J N (Fin k)) {f g : M → N} (hf : ContMDiff I J (↑⊤) f)
  (hg : ContMDiff I J (↑⊤) g) {F : M × ↑(Set.Icc 0 1) → N}
  (hF : ContMDiff (I.prod (modelWithCornersEuclideanHalfSpace 1)) J (↑⊤) F)
  (h₀ : ∀ (x : M), F (x, 0) = f x) (h₁ : ∀ (x : M), F (x, 1) = g x) :
  TauCeti.degree o o' f = TauCeti.degree o o' g
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

Formalized in Tau Ceti as [`TauCeti.degree_eq_of_homotopy`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/Global.html#TauCeti.degree_eq_of_homotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.degree_eq_of_homotopy`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/Global.html#TauCeti.degree_eq_of_homotopy)
- [Source of `TauCeti.degree_eq_of_homotopy` in TauCeti/Geometry/Manifold/Degree/Global.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Degree/Global.lean#L236)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
