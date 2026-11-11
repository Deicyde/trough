---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.norm_forwardShiftCLM_pow_apply, MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.norm_backwardShiftCLM_pow_apply_le, MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.smul_backwardShiftCLM_pow_apply, MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.dense_span_single, MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.exists_forall_eq_zero_of_mem_span_single, MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.isHypercyclic_smul_backwardShiftCLM_iff, MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.smul_backwardCLM_pow_apply_coord, MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.smul_backwardCLM_pow
statement: formalized
proof: formalized
---

# Rolewicz backward shifts

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html).

## Powers of the forward shift preserve norms

Powers of the forward shift preserve norms.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.norm_forwardShiftCLM_pow_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#norm-forward-shift-clm-pow-apply).

## Powers of the backward shift do not increase norms

Powers of the backward shift do not increase norms.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.norm_backwardShiftCLM_pow_apply_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#norm-backward-shift-clm-pow-apply-le).

## Powers of a scalar multiple of the backward shift

Powers of a scalar multiple of the backward shift, applied pointwise.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.smul_backwardShiftCLM_pow_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#smul-backward-shift-clm-pow-apply).

## Finitely supported vectors are dense in $\ell^2(\mathbb{N})$

The span of the single-coordinate vectors is dense in `ℓ²(ℕ, 𝕜)`:
every vector is the sum of its canonical series.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.dense_span_single`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#dense-span-single).

## Vectors in the span of coordinate vectors have finite support

Every vector in the span of the single-coordinate vectors is
eventually zero: it has finite support.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.exists_forall_eq_zero_of_mem_span_single`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#exists-forall-eq-zero-of-mem-span-single).

## Rolewicz's theorem

The scalar multiple `μ • B` of the backward
shift on `ℓ²(ℕ, 𝕜)` is hypercyclic if and only if `‖μ‖ > 1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Rolewicz.isHypercyclic_smul_backwardShiftCLM_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Rolewicz.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#is-hypercyclic-smul-backward-shift-clm-i).

## Coordinates of powers of a scaled backward shift

Coordinate form of a power of a scalar multiple of the backward shift.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.smul_backwardCLM_pow_apply_coord`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#smul-backward-clm-pow-apply-coord).

## Powers of a scaled backward shift as operators

A power of a scalar multiple of the backward shift, as an operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.smul_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#smul-backward-clm-pow).

## Zero is a periodic point of every operator

`0` is a periodic point of every period for every operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.isPeriodicPoint_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#is-periodic-point-zero).

## Periodic approximant of a truncated sequence

The periodic extension of the truncation of `y` to its first `N`
coordinates: the geometric series over forward shifts by blocks of
length `N`, with coefficients `(μ⁻¹ ^ N) ^ m`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.periodicApprox`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#periodic-approx).

## Geometric ratio of the periodic approximant is below 1

The geometric ratio `‖μ⁻¹ ^ N‖` is `< 1` when `‖μ‖ > 1` and `N > 0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.norm_inv_pow_lt_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#norm-inv-pow-lt-one).

## Summability of the geometric bound for periodic approximants

The geometric series bounding the periodic approximant terms is summable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.summable_geom_trunc`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#summable-geom-trunc).

## Norm of a term of the periodic approximant

The norm of a term of the periodic approximant.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.norm_periodicApprox_term`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#norm-periodic-approx-term).

## Summability of the periodic approximant terms

Summability of the terms of the periodic approximant.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.summable_periodicApprox_terms`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#summable-periodic-approx-terms).

## First term of the periodic approximant is the truncation

The `m = 0` term of the periodic approximant is the truncation.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.periodicApprox_term_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#periodic-approx-term-zero).

## Backward shift annihilates truncations after $N$ steps

Applying the backward shift `N` times to a truncation gives `0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.backwardCLM_pow_trunc`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#backward-clm-pow-trunc).

## Action of the scaled backward shift power on approximant terms

How `(μ • B) ^ N` acts on a term of the periodic approximant:
the `m = 0` term is killed, and every later term shifts down by one.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.periodicApprox_step`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#periodic-approx-step).

## Summability of the shifted periodic approximant terms

Summability of the terms of the periodic approximant after applying
`(μ • B) ^ N`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.summable_periodicApprox_map`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#summable-periodic-approx-map).

## Periodic approximant is a periodic point

The periodic approximant is periodic of period `N` when `‖μ‖ > 1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.periodicApprox_isPeriodicPoint`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#periodic-approx-is-periodic-point).

## Distance from the periodic approximant to the truncation

The distance from the periodic approximant to the truncation is at
most the geometric tail `(r / (1 - r)) * ‖y‖`, where `r = ‖μ‖⁻¹ ^ N`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.norm_periodicApprox_sub_trunc`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#norm-periodic-approx-sub-trunc).

## Dense periodic points of the Rolewicz operator for $|\mu| > 1$

The periodic points of `μ • B` are dense when `‖μ‖ > 1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.dense_periodicPoints_of_one_lt_norm`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#dense-periodic-points-of-one-lt-norm).

## Coordinate recurrence for periodic points of $\mu B$

If `x` is periodic for `μ • B`, its coordinates satisfy
`x k = μ ^ (n * m) * x (k + n * m)` for all `m`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.periodic_coord_iterate`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#periodic-coord-iterate).

## Coordinates of an $\ell^2$ vector tend to zero

The coordinates of an `ℓ²` vector tend to `0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.tendsto_norm_coord`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#tendsto-norm-coord).

## No nonzero periodic points of $\mu B$ when $|\mu| \le 1$

The only periodic point of `μ • B` is `0` when `‖μ‖ ≤ 1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.eq_zero_of_isPeriodicPoint_of_norm_le_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#eq-zero-of-is-periodic-point-of-norm-le).

## Periodic points of $\mu B$ are dense iff $|\mu| > 1$

The periodic points of `μ • B` are dense if and only if `‖μ‖ > 1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RolewiczPeriodic.dense_periodicPoints_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RolewiczPeriodic.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html#dense-periodic-points-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rolewicz backward shifts](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/rolewicz-backward-shifts)
