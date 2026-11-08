---
declaration: theorem
origin: cited
lean: Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq, LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_min, LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le
statement: formalized
proof: formalized
---

# The singular-value Hoffman–Wielandt inequality for same-shaped rectangular matrices

the squared distance between their ordered singular values, summed up to the smaller dimension,
is bounded by the squared Frobenius norm of their difference.

```lean
Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq.{u_3, u_4, u_5}
  {m : Type u_3} {n : Type u_4} [Fintype m] [Fintype n] [DecidableEq n] {𝕜 : Type u_5} [RCLike 𝕜]
  (A B : Matrix m n 𝕜) :
  ∑ i,
      ((Matrix.toEuclideanLin A).singularValues ↑i - (Matrix.toEuclideanLin B).singularValues ↑i) ^
        2 ≤
    ‖A - B‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abel's inequality, comparison form](../../../algebra/other-results/abels-inequality-comparison-form.md)
- [ContinuousLinearMap.singularValue](../../part-01/operator-theory/part-01/continuouslinearmap-singularvalue.md)
- [Ky Fan's maximum principle](../../part-01/operator-theory/part-01/ky-fans-maximum-principle.md)

## Lean

Formalized in Tau Ceti as [`Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq).

## Other forms

**The singular-value Hoffman–Wielandt inequality for arbitrary finite-dimensional maps.** Formalized in Tau Ceti as [`LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_min`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.html#LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_min).

```lean
LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_min.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  (A B : E →ₗ[𝕜] F) :
  ∑ i, (A.singularValues ↑i - B.singularValues ↑i) ^ 2 ≤
    (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E F) (A - B) ^ 2
```

**The singular-value Hoffman–Wielandt inequality when the domain dimension does not exceed the codomain dimension.** Formalized in Tau Ceti as [`LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.html#LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le).

```lean
LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] (A B : E →ₗ[𝕜] F) (hEF : Module.finrank 𝕜 E ≤ Module.finrank 𝕜 F) :
  ∑ i, (A.singularValues ↑i - B.singularValues ↑i) ^ 2 ≤
    (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E F) (A - B) ^ 2
```

## Sources

- [Tau Ceti documentation: `Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq)
- [Source of `Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq` in TauCeti/Analysis/Matrix/HoffmanWielandt.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/HoffmanWielandt.lean#L64)
