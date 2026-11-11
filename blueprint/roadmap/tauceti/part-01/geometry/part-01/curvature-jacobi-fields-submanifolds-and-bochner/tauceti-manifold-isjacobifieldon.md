---
declaration: structure
origin: cited
lean: TauCeti.Manifold.IsJacobiFieldOn
statement: formalized
---

# TauCeti.Manifold.IsJacobiFieldOn

A `C²` Jacobi field along a geodesic on `s`, for the Levi-Civita connection.
The geodesic supplies the unique-derivative hypothesis on the parameter set.

```lean
TauCeti.Manifold.IsJacobiFieldOn.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] (γ : ℝ → M)
  (V : (t : ℝ) → TangentSpace I (γ t)) (s : Set ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.IsJacobiFieldOn`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Basic.html#TauCeti.Manifold.IsJacobiFieldOn).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.IsJacobiFieldOn`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Basic.html#TauCeti.Manifold.IsJacobiFieldOn)
- [Source of `TauCeti.Manifold.IsJacobiFieldOn` in TauCeti/Geometry/Manifold/Riemannian/Jacobi/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Basic.lean#L57)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
