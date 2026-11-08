---
declaration: theorem
origin: cited
lean: LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le, LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_min
statement: formalized
proof: formalized
---

# The singular-value Hoffman–Wielandt inequality

**The singular-value Hoffman–Wielandt inequality** when the domain dimension does not exceed
the codomain dimension. The squared distance between the ordered singular values is at most the
squared Frobenius seminorm of the difference.

```lean
LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] (A B : E →ₗ[𝕜] F) (hEF : Module.finrank 𝕜 E ≤ Module.finrank 𝕜 F) :
  ∑ i, (A.singularValues ↑i - B.singularValues ↑i) ^ 2 ≤
    (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E F) (A - B) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abel's inequality, comparison form](../../../../algebra/other-results/abels-inequality-comparison-form.md)
- [ContinuousLinearMap.singularValue](../../../part-01/operator-theory/continuouslinearmap-singularvalue.md)
- [Courant–Fischer, lower direction](../part-01/courant-fischer-lower-direction.md)
- [Eckart–Young](../../operator-ideal/eckart-young.md)
- [Ky Fan's maximum principle, attainment](../part-02/ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.html#LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le).

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

## Sources

- [Tau Ceti documentation: `LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.html#LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le)
- [Source of `LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub_of_finrank_le` in TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.lean#L44)
