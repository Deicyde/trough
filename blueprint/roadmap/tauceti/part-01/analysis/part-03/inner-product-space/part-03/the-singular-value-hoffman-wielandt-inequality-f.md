---
declaration: theorem
origin: cited
lean: LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub
statement: formalized
proof: formalized
---

# The singular-value Hoffman–Wielandt inequality for arbitrary finite-dimensional maps

The sum may run over any initial segment of the singular values: beyond the smaller dimension,
both maps' singular values are zero.

```lean
LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  (A B : E →ₗ[𝕜] F) {k : ℕ} :
  ∑ i, (A.singularValues ↑i - B.singularValues ↑i) ^ 2 ≤
    (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E F) (A - B) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abel's inequality, comparison form](../../../../algebra/part-02/order/abels-inequality-comparison-form.md)
- [Courant–Fischer, lower direction](../part-01/courant-fischer-lower-direction.md)
- [Eckart–Young for Ky Fan gauges](../../../part-04/operator-ideal/eckart-young-for-ky-fan-gauges.md)
- [Ky Fan's maximum principle, attainment](../part-02/ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.html#LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub).

## Sources

- [Tau Ceti documentation: `LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.html#LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub)
- [Source of `LinearMap.sum_sq_singularValues_sub_le_sq_frobenius_apply_sub` in TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Singular.lean#L98)
