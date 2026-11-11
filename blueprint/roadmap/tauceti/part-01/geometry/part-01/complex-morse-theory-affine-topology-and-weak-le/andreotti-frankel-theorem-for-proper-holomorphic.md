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

- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The relative homology across a critical level is free on the critical points](../morse-functions-sublevel-topology-and-morse-bott/part-01/the-relative-homology-across-a-critical-level-is.md)
- [Sard's lemma in equal dimensions](../../../analysis/part-02/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/SublevelHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/SublevelHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion)
- [Source of `TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion` in TauCeti/Geometry/Manifold/Complex/SublevelHomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/SublevelHomology.lean#L200)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
