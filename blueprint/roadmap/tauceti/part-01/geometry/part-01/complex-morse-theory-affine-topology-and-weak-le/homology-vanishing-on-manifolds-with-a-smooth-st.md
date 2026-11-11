---
declaration: theorem
origin: cited
lean: TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt
statement: formalized
proof: formalized
---

# Homology vanishing on manifolds with a smooth strongly `q`-pseudoconvex exhaustion

If `M`
carries a smooth proper bounded-below everywhere strongly `q`-pseudoconvex function `f : M → ℝ`
(not assumed to be Morse), then `Hₙ(M; R) = 0` for `n > finrank ℂ E + q`.

```lean
TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt.{u, v, w, u_1}
  {E : Type u_1} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E]
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] [T2Space M]
  {f : M → ℝ} {q : ℕ} (hf : ContMDiff (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  (hp : IsProperMap f) (hbdd : BddBelow (Set.range f))
  (hq : ∀ (x : M), TauCeti.IsManifoldStronglyPseudoconvexAt E q f x) {𝒜 : Type v}
  [CategoryTheory.Category.{w, v} 𝒜] [CategoryTheory.Abelian 𝒜]
  [CategoryTheory.Limits.HasCoproducts 𝒜] [CategoryTheory.Limits.HasColimitsOfShape ℕ 𝒜]
  [CategoryTheory.HasExactColimitsOfShape ℕ 𝒜] (R : 𝒜) {n : ℕ} (hn : Module.finrank ℂ E + q < n) :
  CategoryTheory.Limits.IsZero (((AlgebraicTopology.singularHomologyFunctor 𝒜 n).obj R).obj ↧M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The relative homology across a critical level is free on the critical points](../morse-functions-sublevel-topology-and-morse-bott/part-01/the-relative-homology-across-a-critical-level-is.md)
- [Relative Morse approximation in the strong Whitney topology](../morse-functions-sublevel-topology-and-morse-bott/part-01/relative-morse-approximation-in-the-strong-whitn.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt)
- [Source of `TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt` in TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.lean#L126)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
