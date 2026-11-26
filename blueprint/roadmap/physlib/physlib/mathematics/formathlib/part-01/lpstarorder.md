---
declaration: module
origin: cited
lean: lp.instPartialOrder, lp.sqrtRe, lp.star_sqrtRe_mul_self, lp.instStarOrderedRing, lp.instCommCStarSubalgebra, lp.instStarOrderedSubalgebra
statement: formalized
proof: formalized
---

# The pointwise star order on bounded functions

The module `Physlib.Mathematics.ForMathlib.LpStarOrder`, [Physlib/Mathematics/ForMathlib/LpStarOrder.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean): 7 declarations (1 instance with no name), 7 with a docstring.

> Bounded complex functions are ordered pointwise, and this order is their star order.

## i. Overview

> The bounded complex functions `lp (fun _ : X ↦ ℂ) ∞` on a type `X` form a commutative
> C⋆-algebra. Ordering them pointwise makes them a star-ordered ring: a bounded function is
> positive exactly when it is the square of the square root of its real part. Every closed
> star subalgebra is then a commutative C⋆-algebra with the same star order.

## ii. Key results

> - `lp.instStarOrderedRing` : the pointwise order on bounded complex functions is the star order.
> - `lp.instStarOrderedSubalgebra` : a closed star subalgebra carries the pointwise star order.

## iv. References

## A. The pointwise order

**`lp.instPartialOrder`**, an instance, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L50).

> Bounded functions are ordered pointwise.

```lean
noncomputable instance instPartialOrder : PartialOrder (lp (fun _ : X ↦ ℂ) ∞)
```

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L54).

> Adding a bounded function preserves the pointwise order.

```lean
instance : IsOrderedAddMonoid (lp (fun _ : X ↦ ℂ) ∞)
```

**`lp.sqrtRe`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L58).

> The pointwise square root of the real part of a bounded function.

```lean
noncomputable def sqrtRe (f : lp (fun _ : X ↦ ℂ) ∞) : lp (fun _ : X ↦ ℂ) ∞
```

**`lp.star_sqrtRe_mul_self`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L65).

> A positive bounded function is the square of its square root.

```lean
lemma star_sqrtRe_mul_self {f : lp (fun _ : X ↦ ℂ) ∞} (hf : 0 ≤ f) :
    star (sqrtRe f) * sqrtRe f = f
```

**`lp.instStarOrderedRing`**, an instance, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L75).

> The pointwise order is the star order: positive bounded functions are squares.

```lean
noncomputable instance instStarOrderedRing : StarOrderedRing (lp (fun _ : X ↦ ℂ) ∞)
```

## B. Closed subalgebras

**`lp.instCommCStarSubalgebra`**, an instance, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L83).

> A closed algebra of bounded functions is a commutative C⋆-algebra.

```lean
noncomputable instance instCommCStarSubalgebra : CommCStarAlgebra S
```

**`lp.instStarOrderedSubalgebra`**, an instance, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean#L87).

> A closed algebra of bounded functions carries the pointwise star order.

```lean
noncomputable instance instStarOrderedSubalgebra : StarOrderedRing S
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/LpStarOrder.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/LpStarOrder.lean)
