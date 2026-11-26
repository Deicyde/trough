---
declaration: module
origin: cited
lean: ProbabilisticTheory.le_zero_of_forall_pos_smul_one_le, ProbabilisticTheory.orderUnitBounds, ProbabilisticTheory.orderUnitNorm, ProbabilisticTheory.orderUnitBounds_bddBelow, ProbabilisticTheory.orderUnitNorm_le, ProbabilisticTheory.orderUnitBounds_nonempty, ProbabilisticTheory.orderUnitNorm_nonneg, ProbabilisticTheory.orderUnitNorm_zero
statement: formalized
proof: formalized
---

# Archimedean order-unit spaces (Physlib)

The module `Physlib.ProbabilisticTheory.OrderUnit.Archimedean`, [Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean): 30 declarations, 27 with a docstring.

## i. Overview

> The Archimedean condition is a regularity assumption on an order-unit space that rules out
> infinitesimal elements. With it, the order and the distinguished unit `1` determine a natural
> norm,
>
> `‖A‖₁ = inf {r ≥ 0 | -r • 1 ≤ A ≤ r • 1}`.
>
> Thus the unit interval sets the scale for the observables: `[-1, 1]` is exactly the closed unit
> ball. For self-adjoint matrices, this recovers the usual operator norm. Concretely, this is the
> Minkowski functional of the order interval `[-1, 1]`: convexity of that interval gives the triangle
> inequality, and its symmetry gives homogeneity, for free. The Archimedean condition is only needed
> afterwards, to upgrade this from a seminorm to a genuine norm.

## ii. Key results

> - `ProbabilisticTheory.orderUnitNorm_eq_zero_iff` : the order-unit norm separates points.
> - `ProbabilisticTheory.closedIciTopology` : the positive cone is closed in the order-unit-norm
>   topology.

## iv. References

## A. Archimedean order units

**`ProbabilisticTheory.le_zero_of_forall_pos_smul_one_le`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L60).

> An observable below every positive multiple of the certain outcome is nonpositive.

```lean
lemma le_zero_of_forall_pos_smul_one_le (A : P.Observables)
    (h : ∀ ε : ℝ, 0 < ε → A ≤ ε • (1 : P.Observables)) : A ≤ 0
```

## B. The order-unit bounds and norm

**`ProbabilisticTheory.orderUnitBounds`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L71).

> The nonnegative scalars that bound an element on both sides by the order unit.

```lean
def orderUnitBounds (A : P.Observables) : Set ℝ
```

**`ProbabilisticTheory.orderUnitNorm`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L75).

> The order-unit norm is the infimum of the order-unit bounds.

```lean
noncomputable def orderUnitNorm (A : P.Observables) : ℝ
```

**`ProbabilisticTheory.orderUnitBounds_bddBelow`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L79).

> The order-unit bounds are bounded below by `0`.

```lean
lemma orderUnitBounds_bddBelow (A : P.Observables) : BddBelow (orderUnitBounds A)
```

**`ProbabilisticTheory.orderUnitNorm_le`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L83).

> Any order-unit bound on `A` is an upper bound for `A`'s order-unit norm.

```lean
lemma orderUnitNorm_le {A : P.Observables} {r : ℝ} (hr : r ∈ orderUnitBounds A) :
    orderUnitNorm A ≤ r
```

**`ProbabilisticTheory.orderUnitBounds_nonempty`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L88).

> Every element has some order-unit bound.

```lean
lemma orderUnitBounds_nonempty (A : P.Observables) : (orderUnitBounds A).Nonempty
```

**`ProbabilisticTheory.orderUnitNorm_nonneg`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L95).

> The order-unit norm is an infimum of nonnegative reals, hence itself nonnegative.

```lean
lemma orderUnitNorm_nonneg (A : P.Observables) : 0 ≤ orderUnitNorm A
```

**`ProbabilisticTheory.orderUnitNorm_zero`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L99).

```lean
lemma orderUnitNorm_zero : orderUnitNorm (0 : P.Observables) = 0
```

**`ProbabilisticTheory.orderUnitBounds_neg`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L106).

> Negation preserves the set of order-unit bounds: a symmetric interval bounding `A` bounds
> `-A` too.

```lean
lemma orderUnitBounds_neg (A : P.Observables) : orderUnitBounds (-A) = orderUnitBounds A
```

**`ProbabilisticTheory.orderUnitNorm_neg`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L113).

```lean
lemma orderUnitNorm_neg (A : P.Observables) : orderUnitNorm (-A) = orderUnitNorm A
```

**`ProbabilisticTheory.add_mem_orderUnitBounds`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L118).

> A bound for `A` and a bound for `B` add up to a bound for `A + B`.

```lean
lemma add_mem_orderUnitBounds {A B : P.Observables} {r s : ℝ} (hr : r ∈ orderUnitBounds A)
    (hs : s ∈ orderUnitBounds B) : r + s ∈ orderUnitBounds (A + B)
```

**`ProbabilisticTheory.exists_orderUnitBound_lt`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L127).

> There is an order-unit bound on `A` within `ε` of its norm.

```lean
lemma exists_orderUnitBound_lt (A : P.Observables) {ε : ℝ} (hε : 0 < ε) :
    ∃ r ∈ orderUnitBounds A, r < orderUnitNorm A + ε
```

**`ProbabilisticTheory.orderUnitNorm_add_le`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L131).

```lean
lemma orderUnitNorm_add_le (A B : P.Observables) :
    orderUnitNorm (A + B) ≤ orderUnitNorm A + orderUnitNorm B
```

## C. Norm axioms

**`ProbabilisticTheory.smul_one_mono`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L151).

> Scaling the unit by a larger nonnegative real gives a larger multiple: `r ↦ r • 1` is
> monotone.

```lean
lemma smul_one_mono {r s : ℝ} (hrs : r ≤ s) :
    r • (1 : P.Observables) ≤ s • (1 : P.Observables)
```

**`ProbabilisticTheory.le_orderUnitNorm_smul_one`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L156).

> Every element is bounded above by its order-unit norm times `1`.

```lean
lemma le_orderUnitNorm_smul_one (A : P.Observables) :
    A ≤ orderUnitNorm A • (1 : P.Observables)
```

**`ProbabilisticTheory.neg_orderUnitNorm_smul_one_le`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L170).

> `A` is also bounded below by `-(orderUnitNorm A • 1)`.

```lean
lemma neg_orderUnitNorm_smul_one_le (A : P.Observables) :
    -(orderUnitNorm A • (1 : P.Observables)) ≤ A
```

**`ProbabilisticTheory.orderUnitNorm_mem_orderUnitBounds`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L178).

> The norm itself is an order-unit bound, i.e. the infimum defining `orderUnitNorm` is a
> minimum.

```lean
lemma orderUnitNorm_mem_orderUnitBounds (A : P.Observables) : orderUnitNorm A ∈ orderUnitBounds A
```

**`ProbabilisticTheory.le_smul_one_of_orderUnitNorm_lt`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L182).

> An element with order-unit norm strictly below `ε` is itself bounded above by `ε • 1`.

```lean
lemma le_smul_one_of_orderUnitNorm_lt {A : P.Observables} {ε : ℝ} (h : orderUnitNorm A < ε) :
    A ≤ ε • (1 : P.Observables)
```

**`ProbabilisticTheory.neg_smul_one_le_of_orderUnitNorm_lt`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L187).

> The mirror image of `le_smul_one_of_orderUnitNorm_lt`.

```lean
lemma neg_smul_one_le_of_orderUnitNorm_lt {A : P.Observables} {ε : ℝ} (h : orderUnitNorm A < ε) :
    -(ε • (1 : P.Observables)) ≤ A
```

**`ProbabilisticTheory.orderUnitNorm_le_iff`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L194).

> The order-unit norm is characterized exactly by its symmetric order interval.

```lean
lemma orderUnitNorm_le_iff {A : P.Observables} {r : ℝ} :
    orderUnitNorm A ≤ r ↔ 0 ≤ r ∧ -(r • (1 : P.Observables)) ≤ A ∧ A ≤ r • (1 : P.Observables)
```

**`ProbabilisticTheory.orderUnitNorm_eq_zero_iff`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L202).

> The order-unit norm is definite: `‖A‖₁ = 0` forces `A = 0`.

```lean
lemma orderUnitNorm_eq_zero_iff {A : P.Observables} : orderUnitNorm A = 0 ↔ A = 0
```

**`ProbabilisticTheory.orderUnitNorm_smul_le`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L209).

> Nonnegative scalar multiplication scales the order-unit norm from above.

```lean
lemma orderUnitNorm_smul_le {r : ℝ} (hr : 0 ≤ r) (A : P.Observables) :
    orderUnitNorm (r • A) ≤ r * orderUnitNorm A
```

**`ProbabilisticTheory.orderUnitNorm_smul_of_pos`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L219).

> Positive scalar multiplication scales the order-unit norm.

```lean
lemma orderUnitNorm_smul_of_pos {r : ℝ} (hr : 0 < r) (A : P.Observables) :
    orderUnitNorm (r • A) = r * orderUnitNorm A
```

**`ProbabilisticTheory.orderUnitNorm_smul`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L226).

> The order-unit norm is absolutely homogeneous.

```lean
lemma orderUnitNorm_smul (r : ℝ) (A : P.Observables) :
    orderUnitNorm (r • A) = |r| * orderUnitNorm A
```

**`ProbabilisticTheory.exists_orderUnitNorm_le_one_smul_eq`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L236).

> Rescaling any nonzero element down to the unit ball: `(orderUnitNorm A)⁻¹ • A` has norm at
> most `1`, and scaling it back up by `orderUnitNorm A` recovers `A`.

```lean
lemma exists_orderUnitNorm_le_one_smul_eq {A : P.Observables} (hA : orderUnitNorm A ≠ 0) :
    ∃ B : P.Observables, orderUnitNorm B ≤ 1 ∧ orderUnitNorm A • B = A
```

## D. The induced normed space

**`ProbabilisticTheory.orderUnitAddGroupNorm`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L250).

> The order-unit norm packaged as an additive-group norm.

```lean
noncomputable def orderUnitAddGroupNorm : AddGroupNorm P.Observables
```

**`ProbabilisticTheory.orderUnitNormedAddCommGroup`**, an instance, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L258).

> The normed additive group given by the order-unit norm.

```lean
noncomputable scoped instance orderUnitNormedAddCommGroup : NormedAddCommGroup P.Observables
```

**`ProbabilisticTheory.orderUnitNormedSpace`**, an instance, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L262).

> The real normed space given by the order-unit norm.

```lean
noncomputable scoped instance orderUnitNormedSpace : NormedSpace ℝ P.Observables
```

## E. Order-closedness of the topology

**`ProbabilisticTheory.isClosed_Ici_zero`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L272).

> The positive cone is closed in the order-unit-norm topology.

```lean
lemma isClosed_Ici_zero : IsClosed (Set.Ici (0 : P.Observables))
```

**`ProbabilisticTheory.closedIciTopology`**, an instance, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L285).

> Every upper set `[a, ∞)` is closed in the order-unit-norm topology.

```lean
scoped instance closedIciTopology : ClosedIciTopology P.Observables
```

## Depends on

- [Probabilistic theories](../basic.md)

## Proof depends on

- [Ordered vector spaces and order units (Physlib)](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean)
