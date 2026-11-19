---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_of_starConvex
statement: formalized
proof: formalized
---

# The smoothing theorem for an open set with star-convex image in the model

Let `U` be an
open set of the model space `H` of a model with corners `I` whose image `I '' U` is star-convex.
Then the inclusion of smooth singular chains of `U` into singular chains is a quasi-isomorphism.

```lean
TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_of_starConvex.{u, u_1, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {C : Type u_3}
  [CategoryTheory.Category.{u_4, u_3} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasCoproducts C] (R : C) [CategoryTheory.CategoryWithHomology C]
  {H : Type u} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {U : TopologicalSpace.Opens H}
  {c : E} (hU : StarConvex ℝ c (↑I '' ↑U)) :
  QuasiIso (SSet.chainComplexMap (TauCeti.smoothSingularSubcomplex I ↥U).ι R)
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](../part-01/tauceti-smoothsingularsubcomplex.md)

## Proof depends on

- [The smoothing theorem for a smoothly contractible manifold](../part-01/the-smoothing-theorem-for-a-smoothly-contractibl.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_of_starConvex`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Contractible.html#TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_%CE%B9_of_starConvex).

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_of_starConvex`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Contractible.html#TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_%CE%B9_of_starConvex)
- [Source of `TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_of_starConvex` in TauCeti/Geometry/Manifold/SmoothSingular/Contractible.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/Contractible.lean#L229)
