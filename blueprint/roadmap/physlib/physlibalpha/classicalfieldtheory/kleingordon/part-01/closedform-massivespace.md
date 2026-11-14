---
declaration: module
origin: cited
lean: KleinGordon.sineEvolution_mass_three, KleinGordon.solution_mass_three, KleinGordon.solution_mass_three_besselJ1
statement: formalized
proof: formalized
---

# The massive Kirchhoff formula for every test source

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.ClosedForm.MassiveSpace`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean): 3 declarations, 3 with a docstring.

> In three space dimensions the massive retarded solution of any test source is the massless
> Kirchhoff solution plus a Bessel average of the Kirchhoff propagators.

## i. Overview

> In three space dimensions the massless sine evolution is Kirchhoff's spherical mean. Inserting it
> into the Bessel average of `ClosedForm.MassDeformation` gives the retarded Green function
> `δ(t - r) / (4π r) - m J₁ (m √(t² - r²)) / (4π √(t² - r²)) Θ (t - r)` as an identity for the
> retarded solution of any test source at any point.

## ii. Key results

> - `sineEvolution_mass_three` : the Kirchhoff–Bessel formula for the sine evolution.
> - `solution_mass_three` : the Kirchhoff–Bessel formula for the retarded solution.
> - `solution_mass_three_besselJ1` : the same formula with `J₁`.

## iv. References

> None.

## A. Three space dimensions

> - `sineEvolution_mass_three` : the Kirchhoff–Bessel formula for the sine evolution.
> - `solution_mass_three` : the Kirchhoff–Bessel formula for the retarded solution.
> - `solution_mass_three_besselJ1` : the same formula with `J₁`.

**`KleinGordon.sineEvolution_mass_three`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean#L62).

> **The Kirchhoff–Bessel formula for the sine evolution on `Space 3`.** For every Schwartz
> source the massive sine evolution is the Kirchhoff propagator at the radius plus a Bessel
> average of the Kirchhoff propagators at smaller radii.

```lean
lemma sineEvolution_mass_three {r : ℝ} (hr : 0 ≤ r) (m : ℝ) (g : 𝓢(Space 3, ℂ)) (x : Space 3) :
    sineEvolution ℂ r (m ^ 2) g x = wavePropagator 1 r g x +
      ∫ u in (0 : ℝ)..r, ((2 * m ^ 2 * u * Real.besselSqDeriv (m ^ 2 * (r ^ 2 - u ^ 2)) : ℝ) : ℂ) *
        wavePropagator 1 u g x
```

**`KleinGordon.solution_mass_three`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean#L72).

> **The Kirchhoff–Bessel formula for the retarded solution of a test source.** In three space
> dimensions the massive retarded solution at `(t, x)` is the massless Kirchhoff solution plus a
> Bessel average of the Kirchhoff propagators of the slices.

```lean
lemma solution_mass_three (m : ℝ) (ψ : TestFunction (⊤ : Opens (ℝ × Space 3)) ℂ ⊤) (t : ℝ)
    (x : Space 3) :
    solution ℂ ψ (m ^ 2) t x = ∫ s in Set.Iic t, (wavePropagator 1 (t - s) (slice ℂ ψ s) x +
      ∫ u in (0 : ℝ)..(t - s),
        ((2 * m ^ 2 * u * Real.besselSqDeriv (m ^ 2 * ((t - s) ^ 2 - u ^ 2)) : ℝ) : ℂ) *
          wavePropagator 1 u (slice ℂ ψ s) x)
```

**`KleinGordon.solution_mass_three_besselJ1`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean#L87).

> **The Kirchhoff–Bessel formula with `J₁`.** For `m ≠ 0` the retarded solution of a test source
> in three space dimensions is the Duhamel integral of
> `wavePropagator 1 τ g x - m ∫₀^τ u J₁ (m √(τ² - u²)) / √(τ² - u²) wavePropagator 1 u g x du`.
> The first term is the Green function `δ(t - r) / (4π r)`. The second is
> `- m J₁ (m √(t² - r²)) / (4π √(t² - r²)) Θ (t - r)`.

```lean
lemma solution_mass_three_besselJ1 {m : ℝ} (hm : m ≠ 0)
    (ψ : TestFunction (⊤ : Opens (ℝ × Space 3)) ℂ ⊤) (t : ℝ) (x : Space 3) :
    solution ℂ ψ (m ^ 2) t x = ∫ s in Set.Iic t, (wavePropagator 1 (t - s) (slice ℂ ψ s) x -
      (m : ℂ) * ∫ u in (0 : ℝ)..(t - s),
        ((u * (Real.besselJ1 (m * Real.sqrt ((t - s) ^ 2 - u ^ 2)) /
          Real.sqrt ((t - s) ^ 2 - u ^ 2)) : ℝ) : ℂ) * wavePropagator 1 u (slice ℂ ψ s) x)
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)
- [Waves propagating along spheres](../../waveequation/kirchhoff-setting.md)
- [The Bessel function `J₀` and the massive sine propagation function on the line](../../../mathematics/part-02/specialfunctions/sincpropagator-bessel.md)

## Proof depends on

- [The massive sine evolution through the massless one](closedform-massdeformation.md)
- [Kirchhoff's formula for the massless retarded solution in three dimensions](closedform-masslessspace.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveSpace.lean)
