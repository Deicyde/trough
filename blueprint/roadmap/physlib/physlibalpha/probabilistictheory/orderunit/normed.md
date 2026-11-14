---
declaration: module
origin: cited
lean: ProbabilisticTheory.WithOrderUnitNorm, ProbabilisticTheory.ArchimedeanOrderUnitSpace.mem_orderUnitBounds_iff, ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_real, ProbabilisticTheory.WithOrderUnitNorm.linearEquiv, ProbabilisticTheory.WithOrderUnitNorm.linearEquiv_apply, ProbabilisticTheory.WithOrderUnitNorm.norm_eq_orderUnitNorm, ProbabilisticTheory.WithOrderUnitNorm.realLinearIsometryEquiv, ProbabilisticTheory.WithOrderUnitNorm.realLinearIsometryEquiv_apply
statement: formalized
proof: formalized
---

# The canonical normed copy of an order-unit space

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Normed`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean): 20 declarations (11 instances with no name), 9 with a docstring.

> The type synonym `WithOrderUnitNorm E` with the canonical order-unit norm; channels contract.

## i. Overview

> An Archimedean order-unit space already has a canonical order-unit norm, but the underlying type
> may carry a different norm for another purpose. `WithOrderUnitNorm E` is a type synonym that
> carries the canonical norm without changing the structures on `E` itself.

## ii. Key results

> - `WithOrderUnitNorm E` : the canonical normed copy of `E`.
> - `WithOrderUnitNorm.linearEquiv` : the identity linear equivalence with `E`.
> - `UnitalPositiveLinearMap.orderUnitNorm_map_le` : channels are contractive.

## iv. References

> * None.

## A. The normed copy

**`ProbabilisticTheory.WithOrderUnitNorm`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L50).

> A type synonym of `E` carrying its canonical order-unit norm.

```lean
def WithOrderUnitNorm (E : Type*)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.mem_orderUnitBounds_iff`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L57).

> Membership in the symmetric order-unit interval is equivalent to the norm bound.

```lean
lemma mem_orderUnitBounds_iff {A : E} {r : ℝ} :
    r ∈ orderUnitBounds A ↔ orderUnitNorm A ≤ r
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_real`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L63).

> For the classical order unit on `ℝ`, the order-unit norm is absolute value.

```lean
lemma orderUnitNorm_real (x : ℝ) : orderUnitNorm x = |x|
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L77).

```lean
instance : AddCommGroup (WithOrderUnitNorm E)
```

**An instance with no name**, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L78).

```lean
instance : Module ℝ (WithOrderUnitNorm E)
```

**An instance with no name**, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L79).

```lean
instance : PartialOrder (WithOrderUnitNorm E)
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L80).

```lean
instance : IsOrderedAddMonoid (WithOrderUnitNorm E)
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L81).

```lean
instance : PosSMulMono ℝ (WithOrderUnitNorm E)
```

**An instance with no name**, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L82).

```lean
instance : One (WithOrderUnitNorm E)
```

**An instance with no name**, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L83).

```lean
instance : OrderUnitSpace (WithOrderUnitNorm E)
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L84).

```lean
instance : ArchimedeanOrderUnitSpace (WithOrderUnitNorm E)
```

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L88).

> The canonical normed additive group on the order-unit-norm copy.

```lean
noncomputable instance : NormedAddCommGroup (WithOrderUnitNorm E)
```

**An instance with no name**, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L92).

> The canonical real normed-space structure on the order-unit-norm copy.

```lean
noncomputable instance : NormedSpace ℝ (WithOrderUnitNorm E)
```

**`ProbabilisticTheory.WithOrderUnitNorm.linearEquiv`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L96).

> The identity linear equivalence from `E` to its order-unit-norm copy.

```lean
def linearEquiv : E ≃ₗ[ℝ] WithOrderUnitNorm E
```

**`ProbabilisticTheory.WithOrderUnitNorm.linearEquiv_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L99).

```lean
lemma linearEquiv_apply (x : E) : linearEquiv x = x
```

**`ProbabilisticTheory.WithOrderUnitNorm.norm_eq_orderUnitNorm`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L102).

```lean
lemma norm_eq_orderUnitNorm (x : WithOrderUnitNorm E) :
    ‖x‖ = orderUnitNorm (show E from x)
```

## B. The real scalar case

**`ProbabilisticTheory.WithOrderUnitNorm.realLinearIsometryEquiv`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L108).

> The scalar order-unit-norm copy is linearly isometric to ordinary `ℝ`.

```lean
noncomputable def realLinearIsometryEquiv : WithOrderUnitNorm ℝ ≃ₗᵢ[ℝ] ℝ
```

**`ProbabilisticTheory.WithOrderUnitNorm.realLinearIsometryEquiv_apply`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L115).

```lean
lemma realLinearIsometryEquiv_apply (x : WithOrderUnitNorm ℝ) :
    realLinearIsometryEquiv x = (show ℝ from x)
```

**An instance with no name**, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L119).

> The scalar order-unit-norm copy is complete via its canonical isometry to `ℝ`.

```lean
noncomputable instance : CompleteSpace (WithOrderUnitNorm ℝ)
```

## C. Contractivity of channels

**`ProbabilisticTheory.UnitalPositiveLinearMap.orderUnitNorm_map_le`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean#L132).

> A unital positive map is contractive for the order-unit norms.

```lean
lemma orderUnitNorm_map_le (φ : Channel E F) (x : E) :
    orderUnitNorm (φ x) ≤ orderUnitNorm x
```

## Depends on

- [Archimedean order-unit spaces](../../../physlib/probabilistictheory/orderunit/archimedean.md)
- [Channels](../channel/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Normed.lean)
