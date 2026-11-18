---
declaration: module
origin: cited
lean: Real.half_sq_le_norm_den, Real.norm_resolvent_le_two_div, Real.norm_resolvent_le, Real.integral_damped_sincPropagator
statement: formalized
proof: formalized
---

# Resolvent estimates for the sine propagation function

The module `PhyslibAlpha.Mathematics.SpecialFunctions.SincPropagator.Resolvent`, [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean): 4 declarations, 4 with a docstring.

> The damped time integral of the sine propagation function is a resolvent in the frequency.

## i. Overview

> The Laplace transform of the sine propagation function is `1 / (ω² - z²)`. Fourier inversion turns
> the damped time integral against a Schwartz function into an integral over the frequency. The
> resolvent `1 / (A - (b + i ε)²)` is bounded by `2 / ε²` for `A ≥ 0`. It is bounded by `2 / δ`
> when `A` stays at distance `δ` from `b²`.

## ii. Key results

> - `Real.integral_damped_sincPropagator` : the damped time integral as a frequency integral.
> - `Real.norm_resolvent_le_two_div` : the bound `2 / ε²` for every nonnegative `A`.
> - `Real.norm_resolvent_le` : the bound `2 / δ` away from the shell.

## iv. References

> None.

## A. Bounds of the resolvent

> - `Real.half_sq_le_norm_den` : the denominator is at least `ε² / 2`.
> - `Real.norm_resolvent_le_two_div` : the bound `2 / ε²` for every nonnegative `A`.
> - `Real.norm_resolvent_le` : the bound `2 / δ` away from the shell.

## B. The damped time integral

> - `Real.integral_damped_sincPropagator` : the damped time integral as a frequency integral.

**`Real.half_sq_le_norm_den`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean#L60).

> The denominator of the resolvent is bounded away from zero by `ε² / 2`.

```lean
lemma half_sq_le_norm_den {A : ℝ} (hA : 0 ≤ A) {ε : ℝ} (hε : 0 < ε) (b : ℝ) :
    ε ^ 2 / 2 ≤ ‖(A : ℂ) - (b + ε * Complex.I) ^ 2‖
```

**`Real.norm_resolvent_le_two_div`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean#L81).

> The resolvent is bounded by `2 / ε²` for every frequency.

```lean
lemma norm_resolvent_le_two_div {A : ℝ} (hA : 0 ≤ A) {ε : ℝ} (hε : 0 < ε) (b : ℝ) :
    ‖(1 : ℂ) / ((A : ℂ) - (b + ε * Complex.I) ^ 2)‖ ≤ 2 / ε ^ 2
```

**`Real.norm_resolvent_le`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean#L88).

> The resolvent stays bounded away from the mass shell.

```lean
lemma norm_resolvent_le {A w ε δ : ℝ} (hδ : 0 < δ) (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1)
    (hεδ : ε ≤ δ / 2) (h : δ ≤ |A - (2 * Real.pi * w) ^ 2|) :
    ‖(1 : ℂ) / ((A : ℂ) - (2 * Real.pi * w + ε * Complex.I) ^ 2)‖ ≤ 2 / δ
```

**`Real.integral_damped_sincPropagator`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean#L112).

> **Damped time integral.** The Fourier inversion and the Laplace transform of the sine
> propagation function turn the damped time integral into an integral over the frequency.

```lean
lemma integral_damped_sincPropagator {ε : ℝ} (hε : 0 < ε) (w₀ : ℝ) (g : 𝓢(ℝ, ℂ)) :
    ∫ s in Set.Ioi (0 : ℝ), (Real.exp (-(ε * s)) : ℂ) * ((s.sincPropagator w₀ : ℂ) * g s) =
      ∫ w : ℝ, 𝓕 g w * (1 / ((w₀ : ℂ) ^ 2 - (2 * Real.pi * w + ε * Complex.I) ^ 2))
```

## Depends on

- [The sine propagation function `t ↦ sin (ω t) / ω`](sincpropagator-basic.md)

## Proof depends on

- [Fourier inversion for Schwartz functions on the line](../fourier/inversion.md)
- [The Laplace transform of the sine propagation function](sincpropagator-laplace.md)

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/SincPropagator/Resolvent.lean)
