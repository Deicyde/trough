---
declaration: module
origin: cited
lean: Space.fderiv_cross_commute, Space.time_deriv_cross_commute, Space.inner_cross_self, Space.inner_self_cross
statement: formalized
proof: formalized
---

# The cross product on Euclidean vectors in three dimensions

The module `Physlib.SpaceAndTime.Space.CrossProduct`, [Physlib/SpaceAndTime/Space/CrossProduct.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/CrossProduct.lean): 4 declarations, 2 with a docstring.

## i. Overview

> In this module we define the cross product on `EuclideanSpace ℝ (Fin 3)`,
> and prove various properties about it related to time derivatives and inner products.

## ii. Key results

> - `⨯ₑ₃` : The cross product on `EuclideanSpace ℝ (Fin 3)`.
> - `time_deriv_cross_commute` : Time derivatives move out of cross products.
> - `inner_cross_self` : Inner product of a vector with the cross product of another vector
>   and itself is zero.
> - `inner_self_cross` : Inner product of a vector with the cross product of itself
>   and another vector is zero.

## iv. References

> * None.

## A. The notation for the cross product

## B. Time derivatives move out of cross products

**`Space.fderiv_cross_commute`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/CrossProduct.lean#L63).

> Cross product and fderiv commute.

```lean
lemma fderiv_cross_commute {t : Time} {s : EuclideanSpace ℝ (Fin 3)}
    {f : Time → EuclideanSpace ℝ (Fin 3)} (hf : Differentiable ℝ f) :
    s ⨯ₑ₃ (fderiv ℝ (fun t' => f t') t) 1
    = fderiv ℝ (fun t' => s ⨯ₑ₃ (f t')) t 1
```

**`Space.time_deriv_cross_commute`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/CrossProduct.lean#L102).

> Cross product and time derivative commute.

```lean
lemma time_deriv_cross_commute {s : EuclideanSpace ℝ (Fin 3)} {f : Time → EuclideanSpace ℝ (Fin 3)}
    (hf : Differentiable ℝ f) :
    s ⨯ₑ₃ (∂ₜ (fun t => f t) t) = ∂ₜ (fun t => s ⨯ₑ₃ (f t)) t
```

## C. Inner product of vectors with cross products involving themselves

**`Space.inner_cross_self`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/CrossProduct.lean#L115).

```lean
lemma inner_cross_self (v w : EuclideanSpace ℝ (Fin 3)) :
    inner ℝ v (w ⨯ₑ₃ v) = 0
```

**`Space.inner_self_cross`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/CrossProduct.lean#L123).

```lean
lemma inner_self_cross (v w : EuclideanSpace ℝ (Fin 3)) :
    inner ℝ v (v ⨯ₑ₃ w) = 0
```

## Depends on

- [Time Derivatives](../../time/derivatives.md)

## Sources

- [Physlib/SpaceAndTime/Space/CrossProduct.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/CrossProduct.lean)
