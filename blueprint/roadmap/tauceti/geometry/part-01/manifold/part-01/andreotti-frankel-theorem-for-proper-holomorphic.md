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

- [ContMDiff.restrictScalars](../../complex-manifolds-transport-quotients-bundles-an/contmdiff-restrictscalars.md)
- [Deformation of sublevels across a band without critical points (Milnor, Theorem 3.1)](../../morse-functions-sublevel-topology-and-morse-bott/deformation-of-sublevels-across-a-band-without-c.md)
- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](../../../../analysis/part-01/complex-morse-theory-affine-topology-and-weak-le/the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)
- [MDifferentiableAt.mfderiv_restrictScalars](../../complex-manifolds-transport-quotients-bundles-an/mdifferentiableat-mfderiv-restrictscalars.md)
- [Sard's lemma on the flat stratum](../../../../analysis/part-02/calculus/part-02/sards-lemma-on-the-flat-stratum.md)
- [TauCeti.criticalHessian](../../morse-functions-sublevel-topology-and-morse-bott/tauceti-criticalhessian.md)
- [TauCeti.leviForm](../../../../analysis/part-01/complex-morse-theory-affine-topology-and-weak-le/tauceti-leviform.md)
- [The weak Morse inequalities](../../morse-functions-sublevel-topology-and-morse-bott/the-weak-morse-inequalities.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/SublevelHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/SublevelHomology.html#TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion)
- [Source of `TauCeti.isZero_singularHomology_of_isProperMap_holomorphic_immersion` in TauCeti/Geometry/Manifold/Complex/SublevelHomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/SublevelHomology.lean#L200)
