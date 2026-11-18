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

- [A maximal integral curve confined to a compact set is defined for all time](../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Fermat's theorem on a manifold](../morse-functions-sublevel-topology-and-morse-bott/part-01/fermats-theorem-on-a-manifold.md)
- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../../part-02/manifold/part-03/milnors-cell-attachment-theorem.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [Sard's lemma in equal dimensions](../../../analysis/part-03/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt)
- [Source of `TauCeti.isZero_singularHomology_of_isProperMap_of_isManifoldStronglyPseudoconvexAt` in TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/ExhaustionHomology.lean#L142)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
