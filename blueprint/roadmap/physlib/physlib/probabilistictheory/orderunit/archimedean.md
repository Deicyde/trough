---
declaration: module
origin: cited
lean: ProbabilisticTheory.ArchimedeanOrderUnitSpace, ProbabilisticTheory.instArchimedeanOrderUnitSpaceReal, ProbabilisticTheory.instArchimedeanOrderUnitSpace, ProbabilisticTheory.of, ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds, ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm, ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_bddBelow, ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_le
statement: formalized
proof: formalized
---

# Archimedean order-unit spaces

The module `Physlib.ProbabilisticTheory.OrderUnit.Archimedean`, [Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean): 33 declarations, 30 with a docstring.

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

> - `ProbabilisticTheory.instArchimedeanOrderUnitSpace` : the observables of a probabilistic theory
>   form an Archimedean order-unit space.
> - `ProbabilisticTheory.of` : an Archimedean order-unit space regarded as a probabilistic theory.
> - `ArchimedeanOrderUnitSpace.orderUnitNorm_eq_zero_iff` : the order-unit norm separates points.
> - `ArchimedeanOrderUnitSpace.closedIciTopology` : the positive cone is closed in the order-unit-norm
>   topology.

## iv. References

## A. Archimedean order units

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace`**, a class, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L61).

> An order-unit space whose distinguished order unit is Archimedean.

```lean
class ArchimedeanOrderUnitSpace (E : Type*) extends OrderUnitSpace E where
  /-- If `A` is smaller than every positive multiple of `1`, `A` is already `≤ 0`. -/
  le_zero_of_forall_pos_smul_one_le : ∀ A : E, (∀ ε : ℝ, 0 < ε → A ≤ ε • (1 : E)) → A ≤ 0
```

**`ProbabilisticTheory.instArchimedeanOrderUnitSpaceReal`**, an instance, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L66).

> The real numbers form an Archimedean order-unit space.

```lean
instance instArchimedeanOrderUnitSpaceReal : ArchimedeanOrderUnitSpace ℝ
```

**`ProbabilisticTheory.instArchimedeanOrderUnitSpace`**, an instance, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L78).

> The observables stored in a probabilistic theory form an Archimedean order-unit space.

```lean
instance instArchimedeanOrderUnitSpace (P : ProbabilisticTheory) :
    ArchimedeanOrderUnitSpace P.Observables
```

**`ProbabilisticTheory.of`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L83).

> Bundle an existing Archimedean order-unit space as a probabilistic theory.

```lean
abbrev of (E : Type*) [ArchimedeanOrderUnitSpace E] : ProbabilisticTheory
```

## B. The order-unit bounds and norm

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L105).

> The nonnegative scalars that bound an element on both sides by the order unit.

```lean
def orderUnitBounds (A : E) : Set ℝ
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L109).

> The order-unit norm is the infimum of the order-unit bounds.

```lean
noncomputable def orderUnitNorm (A : E) : ℝ
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_bddBelow`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L113).

> The order-unit bounds are bounded below by `0`.

```lean
lemma orderUnitBounds_bddBelow (A : E) : BddBelow (orderUnitBounds A)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_le`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L117).

> Any order-unit bound on `A` is an upper bound for `A`'s order-unit norm.

```lean
lemma orderUnitNorm_le {A : E} {r : ℝ} (hr : r ∈ orderUnitBounds A) :
    orderUnitNorm A ≤ r
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_nonempty`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L122).

> Every element has some order-unit bound.

```lean
lemma orderUnitBounds_nonempty (A : E) : (orderUnitBounds A).Nonempty
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_nonneg`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L129).

> The order-unit norm is an infimum of nonnegative reals, hence itself nonnegative.

```lean
lemma orderUnitNorm_nonneg (A : E) : 0 ≤ orderUnitNorm A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_zero`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L133).

```lean
lemma orderUnitNorm_zero : orderUnitNorm (0 : E) = 0
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitBounds_neg`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L140).

> Negation preserves the set of order-unit bounds: a symmetric interval bounding `A` bounds
> `-A` too.

```lean
lemma orderUnitBounds_neg (A : E) : orderUnitBounds (-A) = orderUnitBounds A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_neg`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L147).

```lean
lemma orderUnitNorm_neg (A : E) : orderUnitNorm (-A) = orderUnitNorm A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.add_mem_orderUnitBounds`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L152).

> A bound for `A` and a bound for `B` add up to a bound for `A + B`.

```lean
lemma add_mem_orderUnitBounds {A B : E} {r s : ℝ} (hr : r ∈ orderUnitBounds A)
    (hs : s ∈ orderUnitBounds B) : r + s ∈ orderUnitBounds (A + B)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.exists_orderUnitBound_lt`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L165).

> There is an order-unit bound on `A` within `ε` of its norm.

```lean
lemma exists_orderUnitBound_lt (A : E) {ε : ℝ} (hε : 0 < ε) :
    ∃ r ∈ orderUnitBounds A, r < orderUnitNorm A + ε
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_add_le`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L169).

```lean
lemma orderUnitNorm_add_le (A B : E) :
    orderUnitNorm (A + B) ≤ orderUnitNorm A + orderUnitNorm B
```

## C. Norm axioms

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.smul_one_mono`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L189).

> Scaling the unit by a larger nonnegative real gives a larger multiple: `r ↦ r • 1` is
> monotone.

```lean
lemma smul_one_mono {r s : ℝ} (hrs : r ≤ s) :
    r • (1 : E) ≤ s • (1 : E)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.le_orderUnitNorm_smul_one`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L194).

> Every element is bounded above by its order-unit norm times `1`.

```lean
lemma le_orderUnitNorm_smul_one (A : E) : A ≤ orderUnitNorm A • (1 : E)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.neg_orderUnitNorm_smul_one_le`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L206).

> `A` is also bounded below by `-(orderUnitNorm A • 1)`.

```lean
lemma neg_orderUnitNorm_smul_one_le (A : E) : -(orderUnitNorm A • (1 : E)) ≤ A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_mem_orderUnitBounds`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L213).

> The norm itself is an order-unit bound, i.e. the infimum defining `orderUnitNorm` is a
> minimum.

```lean
lemma orderUnitNorm_mem_orderUnitBounds (A : E) : orderUnitNorm A ∈ orderUnitBounds A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.le_smul_one_of_orderUnitNorm_lt`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L217).

> An element with order-unit norm strictly below `ε` is itself bounded above by `ε • 1`.

```lean
lemma le_smul_one_of_orderUnitNorm_lt {A : E} {ε : ℝ} (h : orderUnitNorm A < ε) :
    A ≤ ε • (1 : E)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.neg_smul_one_le_of_orderUnitNorm_lt`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L222).

> The mirror image of `le_smul_one_of_orderUnitNorm_lt`.

```lean
lemma neg_smul_one_le_of_orderUnitNorm_lt {A : E} {ε : ℝ} (h : orderUnitNorm A < ε) :
    -(ε • (1 : E)) ≤ A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_le_iff`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L228).

> The order-unit norm is characterized exactly by its symmetric order interval.

```lean
lemma orderUnitNorm_le_iff {A : E} {r : ℝ} :
    orderUnitNorm A ≤ r ↔ 0 ≤ r ∧ -(r • (1 : E)) ≤ A ∧ A ≤ r • (1 : E)
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_eq_zero_iff`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L236).

> The order-unit norm is definite: `‖A‖₁ = 0` forces `A = 0`.

```lean
lemma orderUnitNorm_eq_zero_iff {A : E} : orderUnitNorm A = 0 ↔ A = 0
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_smul_le`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L243).

> Nonnegative scalar multiplication scales the order-unit norm from above.

```lean
lemma orderUnitNorm_smul_le {r : ℝ} (hr : 0 ≤ r) (A : E) :
    orderUnitNorm (r • A) ≤ r * orderUnitNorm A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_smul_of_pos`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L253).

> Positive scalar multiplication scales the order-unit norm.

```lean
lemma orderUnitNorm_smul_of_pos {r : ℝ} (hr : 0 < r) (A : E) :
    orderUnitNorm (r • A) = r * orderUnitNorm A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNorm_smul`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L260).

> The order-unit norm is absolutely homogeneous.

```lean
lemma orderUnitNorm_smul (r : ℝ) (A : E) :
    orderUnitNorm (r • A) = |r| * orderUnitNorm A
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.exists_orderUnitNorm_le_one_smul_eq`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L270).

> Rescaling any nonzero element down to the unit ball: `(orderUnitNorm A)⁻¹ • A` has norm at
> most `1`, and scaling it back up by `orderUnitNorm A` recovers `A`.

```lean
lemma exists_orderUnitNorm_le_one_smul_eq {A : E} (hA : orderUnitNorm A ≠ 0) :
    ∃ B : E, orderUnitNorm B ≤ 1 ∧ orderUnitNorm A • B = A
```

## D. The induced normed space

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitAddGroupNorm`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L284).

> The order-unit norm packaged as an additive-group norm.

```lean
noncomputable def orderUnitAddGroupNorm : AddGroupNorm E
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNormedAddCommGroup`**, an instance, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L292).

> The normed additive group given by the order-unit norm.

```lean
noncomputable scoped instance orderUnitNormedAddCommGroup : NormedAddCommGroup E
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.orderUnitNormedSpace`**, an instance, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L296).

> The real normed space given by the order-unit norm.

```lean
noncomputable scoped instance orderUnitNormedSpace : NormedSpace ℝ E
```

## E. Order-closedness of the topology

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.isClosed_Ici_zero`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L306).

> The positive cone is closed in the order-unit-norm topology.

```lean
lemma isClosed_Ici_zero : IsClosed (Set.Ici (0 : E))
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.closedIciTopology`**, an instance, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean#L319).

> Every upper set `[a, ∞)` is closed in the order-unit-norm topology.

```lean
scoped instance closedIciTopology : ClosedIciTopology E
```

## Depends on

- [Ordered vector spaces and order units](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/OrderUnit/Archimedean.lean)
