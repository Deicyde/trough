---
declaration: theorem
origin: cited
lean: Erdos188.UpperBound.k42_real, OAI.EuclideanFiveColor.CommutingSpectral.adjoin_comm, OAI.PlaneFiveColor.Spectral.wild_line_average_zero, OAI.PlaneFiveColor.Spectral.wild_line_average_re_zero
statement: formalized
proof: formalized
---

# Erdős Problem 188

[plasma-ai/erdos-188](https://github.com/plasma-ai/erdos-188) at commit [e48d20e0](https://github.com/plasma-ai/erdos-188/tree/e48d20e03233f59794de44dcf2fa850820f40608), 2026-10-29.

> This Lean 4 project proves new bounds for [Erdős Problem 188](https://www.erdosproblems.com/188), as cataloged by Thomas F. Bloom. Let `K*` be the least `k` for which the plane can be colored red and blue with no two red points at distance one and no `k` blue points `z, z + d, …, z + (k - 1)d` with `|d| = 1`.

*Quoted from [README.md](https://github.com/plasma-ai/erdos-188/blob/e48d20e03233f59794de44dcf2fa850820f40608/README.md), Apache-2.0.*

## Depends on

- [Set](../../../data-structures/sets/set.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Strong pigeonhole principle](../../../combinatorics/pigeonhole-principles/strong-pigeonhole-principle.md)
- [Weierstrass trigonometric approximation theorem](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/weierstrass-trigonometric-approximation-theorem.md)
- [Newton's identities](../../../../undergraduate/ring-theory/polynomial-rings/newtons-identities.md)
- [Algebraic elements](../../../../undergraduate/ring-theory/field-theory/algebraic-elements.md)
- [Fourier transform on $\mathrm{L}^2(\R^d)$](../../../../undergraduate/measures-and-integral-calculus/fourier-analysis/fourier-transform-on-l-2-r-d.md)
- [Norm of a continuous linear map](../../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Fourier transform as an integral](../../fourier-analysis/fourier-transform-as-an-integral.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Erdos188.UpperBound.k42_real`](https://github.com/plasma-ai/erdos-188/blob/e48d20e03233f59794de44dcf2fa850820f40608/Erdos188/UpperBound/Final.lean#L26) (theorem)
- [`OAI.EuclideanFiveColor.CommutingSpectral.adjoin_comm`](https://github.com/plasma-ai/erdos-188/blob/e48d20e03233f59794de44dcf2fa850820f40608/OAI/Analysis/PlaneSpectrum/SpectralMeasure.lean#L114) (lemma)
- [`OAI.PlaneFiveColor.Spectral.wild_line_average_zero`](https://github.com/plasma-ai/erdos-188/blob/e48d20e03233f59794de44dcf2fa850820f40608/OAI/Analysis/PlaneSpectrum/Multipliers.lean#L276) (theorem)
- [`OAI.PlaneFiveColor.Spectral.wild_line_average_re_zero`](https://github.com/plasma-ai/erdos-188/blob/e48d20e03233f59794de44dcf2fa850820f40608/OAI/Analysis/PlaneSpectrum/FourierTests.lean#L145) (lemma)

No file its headlines import, directly or not (1559 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc4, Mathlib at [1f414401](https://github.com/leanprover-community/mathlib4/tree/1f414401f69059aa7eead47b53ee40bd38455eeb).
- 1,592 .lean files; its Lean libraries `OAI`, `Erdos188`, `Challenge`, `Solution` hold 1,592, declaring 4,556 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/plasma-ai/erdos-188/blob/e48d20e03233f59794de44dcf2fa850820f40608/LICENSE)).

## Builds on

- Mathlib, at [1f414401](https://github.com/leanprover-community/mathlib4/tree/1f414401f69059aa7eead47b53ee40bd38455eeb).

## Placement

Of its imports of Mathlib modules in an overview area, 49 of 123 are in Analysis, 1.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (49 of 123 imports, 1.5×), General algebra (40 of 123 imports, 0.9×). *Proof depends on* names 8 of the 69 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [plasma-ai/erdos-188 at e48d20e0](https://github.com/plasma-ai/erdos-188/tree/e48d20e03233f59794de44dcf2fa850820f40608)
