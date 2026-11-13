---
declaration: module
origin: cited
lean: WaveEquation.Kirchhoff.phase, WaveEquation.Kirchhoff.phase_add, WaveEquation.Kirchhoff.norm_phase, WaveEquation.Kirchhoff.continuous_phase, WaveEquation.Kirchhoff.phase_eq_fourierChar, WaveEquation.Kirchhoff.WaveOperator, WaveEquation.Kirchhoff.HasWaveFourierMultiplier, WaveEquation.Kirchhoff.HasFinitePropagationSpeed
statement: formalized
proof: formalized
---

# Fourier properties of wave propagation

The module `PhyslibAlpha.ClassicalFieldTheory.WaveEquation.Kirchhoff.Phase`, [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean): 10 declarations, 7 with a docstring.

> The spectral description uses the Fourier phase and the sine multiplier of the wave propagator.

## i. Overview

> The spectral description uses the Fourier phase and the sine multiplier of the wave propagator.

## ii. Key results

> * `phase`: The Fourier phase as a complex exponential.
> * `phase_add`.
> * `norm_phase`.
> * `phase_eq_fourierChar` : the phase is the Fourier character.
> * `IsWavePropagator`: Fourier multiplier, finite propagation speed and Huygens' principle.

## iv. References

> * Bär, [Green-hyperbolic operators on globally hyperbolic
>   spacetimes](https://arxiv.org/abs/1310.0738).

## A. Fourier properties of wave propagation

**`WaveEquation.Kirchhoff.phase`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L49).

> The Fourier phase as a complex exponential.

```lean
noncomputable def phase (t : ℝ) : ℂ
```

**`WaveEquation.Kirchhoff.phase_add`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L51).

```lean
lemma phase_add (s t : ℝ) : phase (s + t) = phase s * phase t
```

**`WaveEquation.Kirchhoff.norm_phase`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L58).

```lean
lemma norm_phase (t : ℝ) : ‖phase t‖ = 1
```

**`WaveEquation.Kirchhoff.continuous_phase`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L63).

```lean
lemma continuous_phase : Continuous phase
```

**`WaveEquation.Kirchhoff.phase_eq_fourierChar`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L68).

> The phase is the Fourier character at `-u`.

```lean
lemma phase_eq_fourierChar (u : ℝ) : phase u = (𝐞 (-u) : ℂ)
```

**`WaveEquation.Kirchhoff.WaveOperator`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L75).

> An operator on scalar fields on `ℝ³`.

```lean
abbrev WaveOperator
```

**`WaveEquation.Kirchhoff.HasWaveFourierMultiplier`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L79).

> The operator acts on Schwartz functions as the Fourier multiplier `sin(ω t) / ω` with
> `ω = 2π c |ξ|`. Frequencies `ξ = 0` are excluded. There the multiplier has the limit `t`.

```lean
def HasWaveFourierMultiplier (c t : ℝ) (T : WaveOperator) : Prop
```

**`WaveEquation.Kirchhoff.HasFinitePropagationSpeed`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L87).

> Finite propagation speed for `c > 0`: if `f` vanishes outside the ball of radius `ρ` about `x₀`,
> then `T f` vanishes outside the ball of radius `ρ + c |t|`.

```lean
def HasFinitePropagationSpeed (c t : ℝ) (T : WaveOperator) : Prop
```

**`WaveEquation.Kirchhoff.SatisfiesHuygensPrinciple`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L94).

> Huygens' principle for `c > 0`: if `f` vanishes outside the ball of radius `ρ` about `x₀`, then
> `T f` vanishes inside the ball of radius `c |t| - ρ`. The wavefront is a shell of width `2ρ`
> with no wave behind it.

```lean
def SatisfiesHuygensPrinciple (c t : ℝ) (T : WaveOperator) : Prop
```

**`WaveEquation.Kirchhoff.IsWavePropagator`**, a structure, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean#L101).

> The three properties of the free wave propagator in three dimensions: the Fourier multiplier,
> finite propagation speed and Huygens' principle. This is a bundle of properties of one operator and
> not a characterisation of wave propagators.

```lean
structure IsWavePropagator (c t : ℝ) (T : WaveOperator) : Prop where
  /-- The Fourier multiplier is `sin(ω t) / ω`. -/
  multiplier : HasWaveFourierMultiplier c t T
  /-- Signals travel at most at speed `c`. -/
  finiteSpeed : HasFinitePropagationSpeed c t T
  /-- The wave vanishes behind the wavefront. -/
  huygens : SatisfiesHuygensPrinciple c t T
```

## Depends on

- [The structure of a module on Space](../../../physlib/spaceandtime/space/part-01/module.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Phase.lean)
