---
declaration: theorem
origin: cited
lean: TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion
statement: formalized
proof: formalized
---

# Andreotti–Frankel theorem for proper holomorphic immersions

If a complex manifold `M` of
complex dimension `n` admits a smooth proper holomorphic immersion into a proper complex inner
product space `F`, then `Hₖ(M; R) = 0` for `k > n` and every coefficient object `R` of an abelian
category with coproducts and exact sequential colimits.

```lean
TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion.{u, v, w, u_1, u_2}
  {E : Type u_1} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E]
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] [T2Space M]
  {A : Type v} [CategoryTheory.Category.{w, v} A] [CategoryTheory.Abelian A]
  [CategoryTheory.Limits.HasCoproducts A] [CategoryTheory.Limits.HasColimitsOfShape ℕ A]
  [CategoryTheory.HasExactColimitsOfShape ℕ A] {F : Type u_2} [NormedAddCommGroup F]
  [InnerProductSpace ℂ F] [ProperSpace F] {i : M → F}
  (hi : ContMDiff (modelWithCornersSelf ℂ E) (modelWithCornersSelf ℂ F) (↑⊤) i)
  (hinj : ∀ (x : M), Function.Injective ⇑(d% i x)) (hip : IsProperMap i) (R : A) {k : ℕ}
  (hk : Module.finrank ℂ E < k) :
  CategoryTheory.Limits.IsZero (((AlgebraicTopology.singularHomologyFunctor A k).obj R).obj ↧M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Fermat's theorem on a manifold](../morse-functions-sublevel-topology-and-morse-bott/part-01/fermats-theorem-on-a-manifold.md)
- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [The inverse function theorem for a converging family](../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../../part-02/manifold/part-03/milnors-cell-attachment-theorem.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [Sard's lemma in equal dimensions](../../../analysis/part-03/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/SublevelHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/SublevelHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion)
- [Source of `TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion` in TauCeti/Geometry/Manifold/Complex/SublevelHomology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/SublevelHomology.lean#L212)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
