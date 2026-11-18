---
declaration: module
origin: cited
lean: Space.oddNormIteratedLaplacianCoeff, Space.oddNormIteratedLaplacianCoeff_ne_zero, Space.iterated_distLaplacian_norm_zpow_odd_eq_smul_diracDelta
statement: formalized
proof: formalized
---

# Iterated Laplacians of norm distributions

The module `Physlib.SpaceAndTime.Space.Norm.IteratedLaplacian`, [Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean): 3 declarations, 3 with a docstring; 3 private, not shown.

## i. Overview

> This file proves the distributional identity corresponding to the classical odd-dimensional
> formula that, in dimension `2 * m + 1`, applying the Laplacian `m + 1` times to the norm
> gives a nonzero constant multiple of the Dirac delta at the origin.

## ii. Key results

> - `iterated_distLaplacian_norm_zpow_odd_eq_smul_diracDelta` : The `(m + 1)`-fold
>   Laplacian of the norm in dimension `2 * m + 1` is a nonzero multiple of the Dirac delta.

## iv. References

> * None.

## A. The odd-dimensional iterated Laplacian of the norm

**`Space.oddNormIteratedLaplacianCoeff`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean#L50).

> The scalar factor in the odd-dimensional iterated Laplacian of the norm.

```lean
noncomputable def oddNormIteratedLaplacianCoeff (m : ℕ) : ℝ
```

**`Space.oddNormIteratedLaplacianCoeff_ne_zero`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean#L67).

> The scalar factor in the odd-dimensional iterated Laplacian of the norm is nonzero.

```lean
lemma oddNormIteratedLaplacianCoeff_ne_zero (m : ℕ) :
    oddNormIteratedLaplacianCoeff m ≠ 0
```

**`Space.iterated_distLaplacian_norm_zpow_odd_eq_smul_diracDelta`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean#L145).

> In dimension `2 * m + 1`, the `(m + 1)`-fold distributional Laplacian of the
> distribution induced by the norm is a nonzero multiple of the Dirac delta at the origin.

```lean
lemma iterated_distLaplacian_norm_zpow_odd_eq_smul_diracDelta (m : ℕ) :
    ((distLaplacian (d := 2 * m + 1))^[m + 1])
      (distOfFunction (fun x : Space (2 * m + 1) => ‖x‖ ^ (1 : ℤ))
        (IsDistBounded.pow 1 (by omega))) =
      oddNormIteratedLaplacianCoeff m • diracDelta ℝ 0
```

## Depends on

- [The Laplacian operator on `Space d`](../part-01/derivatives-laplacian.md)

## Proof depends on

- [The norm on space](norm-basic.md)

## Sources

- [Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/IteratedLaplacian.lean)
