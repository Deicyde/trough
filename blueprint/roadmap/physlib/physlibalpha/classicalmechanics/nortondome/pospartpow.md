---
declaration: module
origin: cited
lean: hasDerivAt_max_sub_pow, contDiff_max_sub_pow
statement: formalized
proof: formalized
---

# Powers of the positive part

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.PosPartPow`, [PhyslibAlpha/ClassicalMechanics/NortonDome/PosPartPow.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PosPartPow.lean): 2 declarations, 2 with a docstring.

> The derivative and `C^(n+1)` regularity of `y ↦ max (y - c) 0 ^ (n + 2)`.

## i. Overview

> The function `y ↦ max (y - c) 0 ^ (n + 2)` vanishes to the left of `c` and is a polynomial to
> its right. It is differentiable everywhere, including at `c`, and is `C^(n+1)`. Functions of
> this shape are the standard witnesses for the failure of uniqueness of ODEs with a
> non-Lipschitz right-hand side, of which the Norton dome is the physical instance.

## ii. Key results

> - `hasDerivAt_max_sub_pow` is the derivative `(n + 2) max (y - c) 0 ^ (n + 1)`, at every point.
> - `contDiff_max_sub_pow` is the `C^(n+1)` regularity.

## iv. References

> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.

## A. The derivative

> By cases: to the left of `c` the function vanishes near the point, to the right it agrees near
> the point with `(y - c) ^ (n + 2)`, and at `c` the difference quotient is `max t 0 ^ (n + 1)`,
> which tends to zero.

**`hasDerivAt_max_sub_pow`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PosPartPow.lean#L58).

> The power `max (y - c) 0 ^ (n + 2)` of the positive part of `y - c` has derivative
> `(n + 2) max (x - c) 0 ^ (n + 1)` at every `x`, including the junction `x = c`.

```lean
lemma hasDerivAt_max_sub_pow (c : ℝ) (n : ℕ) (x : ℝ) :
    HasDerivAt (fun y : ℝ => max (y - c) 0 ^ (n + 2))
      (((n : ℝ) + 2) * max (x - c) 0 ^ (n + 1)) x
```

## B. Regularity

> By induction on `n`: the derivative of the `(n + 3)`-rd power is a constant multiple of the
> `(n + 2)`-nd, which is `C^(n+1)` by the induction hypothesis.

**`contDiff_max_sub_pow`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PosPartPow.lean#L103).

> The power `max (y - c) 0 ^ (n + 2)` of the positive part of `y - c` is `C^(n+1)`.

```lean
lemma contDiff_max_sub_pow (c : ℝ) (n : ℕ) :
    ContDiff ℝ (n + 1) (fun y : ℝ => max (y - c) 0 ^ (n + 2))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/PosPartPow.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PosPartPow.lean)
