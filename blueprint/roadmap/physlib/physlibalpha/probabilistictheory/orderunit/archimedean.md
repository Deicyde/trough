---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace, PhyslibAlpha.ProbabilisticTheory.instArchimedeanOrderUnitSpaceReal, PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds, PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm, PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_bddBelow, PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_le, PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_nonempty, PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_nonneg
statement: formalized
proof: formalized
---

# Archimedean order-unit spaces (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Archimedean`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean): 31 declarations, 28 with a docstring.

## i. Overview

> The Archimedean condition is a regularity assumption on an order-unit space that rules out
> infinitesimal elements. With it, the order and the distinguished unit `1` determine a natural
> norm,
>
> `‖A‖₁ = inf {r ≥ 0 | -r • 1 ≤ A ≤ r • 1}`.
>
> Thus the unit interval sets the scale of the theory: `[-1, 1]` is exactly the closed unit ball. For
> self-adjoint matrices, this recovers the usual operator norm. Concretely, this is the Minkowski
> functional of the order interval `[-1, 1]`: convexity of that interval gives the triangle
> inequality, and its symmetry gives homogeneity, for free. The Archimedean condition is only needed
> afterwards, to upgrade this from a seminorm to a genuine norm.

## ii. Key results

> - `ArchimedeanOrderUnitSpace.orderUnitNorm_eq_zero_iff` : the order-unit norm separates points.
> - `ArchimedeanOrderUnitSpace.closedIciTopology` : the positive cone is closed in the order-unit-norm
>   topology.

## iv. References

## A. Archimedean order units

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace`**, a class, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L58).

> An order-unit space whose distinguished order unit is Archimedean.

```lean
class ArchimedeanOrderUnitSpace (E : Type*) extends OrderUnitSpace E where
  /-- If `A` is smaller than every positive multiple of `1`, `A` is already `≤ 0`. -/
  le_zero_of_forall_pos_smul_one_le : ∀ A : E, (∀ ε : ℝ, 0 < ε → A ≤ ε • (1 : E)) → A ≤ 0
```

**`PhyslibAlpha.ProbabilisticTheory.instArchimedeanOrderUnitSpaceReal`**, an instance, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L63).

> The real numbers form an Archimedean order-unit space.

```lean
instance instArchimedeanOrderUnitSpaceReal : ArchimedeanOrderUnitSpace ℝ
```

## B. The order-unit bounds and norm

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L89).

> The nonnegative scalars that bound an element on both sides by the order unit.

```lean
def orderUnitBounds (A : E) : Set ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L93).

> The order-unit norm is the infimum of the order-unit bounds.

```lean
noncomputable def orderUnitNorm (A : E) : ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_bddBelow`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L97).

> The order-unit bounds are bounded below by `0`.

```lean
lemma orderUnitBounds_bddBelow (A : E) : BddBelow (orderUnitBounds A)
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_le`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L101).

> Any order-unit bound on `A` is an upper bound for `A`'s order-unit norm.

```lean
lemma orderUnitNorm_le {A : E} {r : ℝ} (hr : r ∈ orderUnitBounds A) :
    orderUnitNorm A ≤ r
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_nonempty`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L106).

> Every element has some order-unit bound.

```lean
lemma orderUnitBounds_nonempty (A : E) : (orderUnitBounds A).Nonempty
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_nonneg`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L113).

> The order-unit norm is an infimum of nonnegative reals, hence itself nonnegative.

```lean
lemma orderUnitNorm_nonneg (A : E) : 0 ≤ orderUnitNorm A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_zero`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L117).

```lean
lemma orderUnitNorm_zero : orderUnitNorm (0 : E) = 0
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_neg`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L124).

> Negation preserves the set of order-unit bounds: a symmetric interval bounding `A` bounds
> `-A` too.

```lean
lemma orderUnitBounds_neg (A : E) : orderUnitBounds (-A) = orderUnitBounds A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_neg`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L131).

```lean
lemma orderUnitNorm_neg (A : E) : orderUnitNorm (-A) = orderUnitNorm A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.add_mem_orderUnitBounds`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L136).

> A bound for `A` and a bound for `B` add up to a bound for `A + B`.

```lean
lemma add_mem_orderUnitBounds {A B : E} {r s : ℝ} (hr : r ∈ orderUnitBounds A)
    (hs : s ∈ orderUnitBounds B) : r + s ∈ orderUnitBounds (A + B)
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.exists_orderUnitBound_lt`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L149).

> There is an order-unit bound on `A` within `ε` of its norm.

```lean
lemma exists_orderUnitBound_lt (A : E) {ε : ℝ} (hε : 0 < ε) :
    ∃ r ∈ orderUnitBounds A, r < orderUnitNorm A + ε
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_add_le`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L153).

```lean
lemma orderUnitNorm_add_le (A B : E) :
    orderUnitNorm (A + B) ≤ orderUnitNorm A + orderUnitNorm B
```

## C. Norm axioms

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.smul_one_mono`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L173).

> Scaling the unit by a larger nonnegative real gives a larger multiple: `r ↦ r • 1` is
> monotone.

```lean
lemma smul_one_mono {r s : ℝ} (hrs : r ≤ s) :
    r • (1 : E) ≤ s • (1 : E)
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.le_orderUnitNorm_smul_one`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L178).

> Every element is bounded above by its order-unit norm times `1`.

```lean
lemma le_orderUnitNorm_smul_one (A : E) : A ≤ orderUnitNorm A • (1 : E)
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.neg_orderUnitNorm_smul_one_le`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L190).

> `A` is also bounded below by `-(orderUnitNorm A • 1)`.

```lean
lemma neg_orderUnitNorm_smul_one_le (A : E) : -(orderUnitNorm A • (1 : E)) ≤ A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_mem_orderUnitBounds`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L197).

> The norm itself is an order-unit bound, i.e. the infimum defining `orderUnitNorm` is a
> minimum.

```lean
lemma orderUnitNorm_mem_orderUnitBounds (A : E) : orderUnitNorm A ∈ orderUnitBounds A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.le_smul_one_of_orderUnitNorm_lt`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L201).

> An element with order-unit norm strictly below `ε` is itself bounded above by `ε • 1`.

```lean
lemma le_smul_one_of_orderUnitNorm_lt {A : E} {ε : ℝ} (h : orderUnitNorm A < ε) :
    A ≤ ε • (1 : E)
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.neg_smul_one_le_of_orderUnitNorm_lt`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L206).

> The mirror image of `le_smul_one_of_orderUnitNorm_lt`.

```lean
lemma neg_smul_one_le_of_orderUnitNorm_lt {A : E} {ε : ℝ} (h : orderUnitNorm A < ε) :
    -(ε • (1 : E)) ≤ A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_le_iff`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L212).

> The order-unit norm is characterized exactly by its symmetric order interval.

```lean
lemma orderUnitNorm_le_iff {A : E} {r : ℝ} :
    orderUnitNorm A ≤ r ↔ 0 ≤ r ∧ -(r • (1 : E)) ≤ A ∧ A ≤ r • (1 : E)
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_eq_zero_iff`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L220).

> The order-unit norm is definite: `‖A‖₁ = 0` forces `A = 0`.

```lean
lemma orderUnitNorm_eq_zero_iff {A : E} : orderUnitNorm A = 0 ↔ A = 0
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_smul_le`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L227).

> Nonnegative scalar multiplication scales the order-unit norm from above.

```lean
lemma orderUnitNorm_smul_le {r : ℝ} (hr : 0 ≤ r) (A : E) :
    orderUnitNorm (r • A) ≤ r * orderUnitNorm A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_smul_of_pos`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L237).

> Positive scalar multiplication scales the order-unit norm.

```lean
lemma orderUnitNorm_smul_of_pos {r : ℝ} (hr : 0 < r) (A : E) :
    orderUnitNorm (r • A) = r * orderUnitNorm A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_smul`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L244).

> The order-unit norm is absolutely homogeneous.

```lean
lemma orderUnitNorm_smul (r : ℝ) (A : E) :
    orderUnitNorm (r • A) = |r| * orderUnitNorm A
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.exists_orderUnitNorm_le_one_smul_eq`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L254).

> Rescaling any nonzero element down to the unit ball: `(orderUnitNorm A)⁻¹ • A` has norm at
> most `1`, and scaling it back up by `orderUnitNorm A` recovers `A`.

```lean
lemma exists_orderUnitNorm_le_one_smul_eq {A : E} (hA : orderUnitNorm A ≠ 0) :
    ∃ B : E, orderUnitNorm B ≤ 1 ∧ orderUnitNorm A • B = A
```

## D. The induced normed space

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitAddGroupNorm`**, a def, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L268).

> The order-unit norm packaged as an additive-group norm.

```lean
noncomputable def orderUnitAddGroupNorm : AddGroupNorm E
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNormedAddCommGroup`**, an instance, [line 276](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L276).

> The normed additive group given by the order-unit norm.

```lean
noncomputable scoped instance orderUnitNormedAddCommGroup : NormedAddCommGroup E
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNormedSpace`**, an instance, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L280).

> The real normed space given by the order-unit norm.

```lean
noncomputable scoped instance orderUnitNormedSpace : NormedSpace ℝ E
```

## E. Order-closedness of the topology

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.isClosed_Ici_zero`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L290).

> The positive cone is closed in the order-unit-norm topology.

```lean
lemma isClosed_Ici_zero : IsClosed (Set.Ici (0 : E))
```

**`PhyslibAlpha.ProbabilisticTheory.ArchimedeanOrderUnitSpace.closedIciTopology`**, an instance, [line 303](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean#L303).

> Every upper set `[a, ∞)` is closed in the order-unit-norm topology.

```lean
scoped instance closedIciTopology : ClosedIciTopology E
```

## Depends on

- [Ordered vector spaces and order units (PhyslibAlpha)](basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Archimedean.lean)
