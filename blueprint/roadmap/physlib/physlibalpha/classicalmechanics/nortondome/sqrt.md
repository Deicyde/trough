---
declaration: module
origin: cited
lean: hasDerivAt_sqrt_pow_three, not_lipschitzOnWith_sqrt
statement: formalized
proof: formalized
---

# Calculus of the real square root near zero

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.Sqrt`, [PhyslibAlpha/ClassicalMechanics/NortonDome/Sqrt.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Sqrt.lean): 2 declarations, 2 with a docstring.

> The derivative of `√y ^ 3` everywhere, and the failure of the Lipschitz property of `√` at 0.

## i. Overview

> Two facts about the real square root at zero, where Mathlib's calculus does not reach: the
> cube `√y ^ 3` is differentiable everywhere, with derivative `(3/2) √x`, and `√` is not
> Lipschitz on any interval `[0, ε]`. The first gives the derivative of the potential of the
> Norton dome, the second the failure of the Picard–Lindelöf hypothesis for its force.

## ii. Key results

> - `hasDerivAt_sqrt_pow_three` is the derivative of `√y ^ 3` at every real number.
> - `not_lipschitzOnWith_sqrt` is the failure of the Lipschitz property of `√` on `[0, ε]`.

## iv. References

> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.

## A. The derivative of the cube of the square root

> To the left of zero the square root vanishes, to the right the chain rule applies, and at zero
> the difference quotient of `√t ^ 3 = t √t` is `√t`, which tends to zero.

**`hasDerivAt_sqrt_pow_three`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Sqrt.lean#L55).

> The cube of the real square root, `√y ^ 3`, has derivative `(3/2) √x` at every real `x`. It
> is differentiable at `0`, with derivative `0`, even though `√` is not.

```lean
lemma hasDerivAt_sqrt_pow_three (x : ℝ) :
    HasDerivAt (fun y : ℝ => √y ^ 3) (3 / 2 * √x) x
```

## B. The square root is not Lipschitz at zero

> A bound `√y ≤ K y` on `[0, ε]` gives `1 ≤ K √y` for every positive `y ≤ ε`, which fails at
> `y = min ε (1 / (2K + 1)²)`.

**`not_lipschitzOnWith_sqrt`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Sqrt.lean#L89).

> The real square root is not Lipschitz on any interval `[0, ε]` with `ε > 0`, for any
> Lipschitz constant.

```lean
lemma not_lipschitzOnWith_sqrt (K : NNReal) {ε : ℝ} (hε : 0 < ε) :
    ¬ LipschitzOnWith K (fun y : ℝ => √y) (Set.Icc 0 ε)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/Sqrt.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Sqrt.lean)
