---
declaration: theorem
origin: cited
lean: Isometry.contMDiff
statement: formalized
proof: formalized
---

# Myers–Steenrod: a distance-preserving map is smooth

A map between Riemannian manifolds
which preserves their Riemannian distances, into a complete manifold, is smooth.

```lean
Isometry.contMDiff.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3} [MetricSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] [IsRiemannianManifold I M]
  {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {H' : Type u_5}
  [TopologicalSpace H'] {J : ModelWithCorners ℝ F H'} [J.Boundaryless] {N : Type u_6}
  [MetricSpace N] [ChartedSpace H' N] [IsManifold J (↑⊤) N]
  [Bundle.RiemannianBundle fun y => TangentSpace J y]
  [IsContMDiffRiemannianBundle J (↑⊤) F fun y => TangentSpace J y] [IsRiemannianManifold J N]
  {f : M → N} [CompleteSpace N] (hf : Isometry f) : ContMDiff I J (↑⊤) f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gauss lemma](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/the-gauss-lemma.md)
- [The inverse function theorem for manifolds](../part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](the-koszul-formula.md)
- [TauCeti.Manifold.riemannianExp](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`Isometry.contMDiff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Isometry/Smooth.html#Isometry.contMDiff).

## Sources

- [Tau Ceti documentation: `Isometry.contMDiff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Isometry/Smooth.html#Isometry.contMDiff)
- [Source of `Isometry.contMDiff` in TauCeti/Geometry/Manifold/Riemannian/Isometry/Smooth.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Isometry/Smooth.lean#L166)
