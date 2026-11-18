---
declaration: module
origin: cited
lean: KleinGordon.multiplier_zero_eq, KleinGordon.sineEvolution_zero_mass_apply, KleinGordon.solution_zero_mass_line
statement: formalized
proof: formalized
---

# The retarded solution of the wave equation in one space dimension

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.ClosedForm.MasslessLine`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean): 3 declarations, 3 with a docstring.

> The massless retarded solution in one space dimension is one half of the integral of the source
> over the backward light cone.

## i. Overview

> The multiplier `sin (2π |ξ| r) / (2π |ξ|)` of the massless sine evolution is the average of
> `cos (2π ξ u)` over `u ∈ [-r, r]`. Fourier inversion turns it into the average of the data over the
> interval `[x - r, x + r]`. The Duhamel integral over the earlier times is then the integral of the
> source over the backward light cone. This is the retarded Green function `½ Θ(t - |x|)` of the wave
> equation on the line. It is the case `d = 1` and `m = 0` of the explicit kernels.

## ii. Key results

> - `multiplier_zero_eq` : the multiplier as an average of cosines.
> - `sineEvolution_zero_mass_apply` : the massless sine evolution on the line is the average of the
>   data over an interval.
> - `solution_zero_mass_line` : the massless retarded solution on the line is one half of the
>   integral of the source over the backward light cone.

## iv. References

> None.

## A. The multiplier

> - `multiplier_zero_eq` : the multiplier as an average of cosines.

## B. The sine evolution

> - `sineEvolution_zero_mass_apply` : the massless sine evolution on the line is the average of the
>   data over an interval.

## C. The retarded solution

> - `solution_zero_mass_line` : the massless retarded solution on the line is one half of the
>   integral of the source over the backward light cone.

**`KleinGordon.multiplier_zero_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean#L69).

> The massless multiplier on the line is the average of cosines over `[-r, r]`.

```lean
lemma multiplier_zero_eq (r : ℝ) (ξ : ℝ) :
    multiplier r 0 ξ = ((1 / 2 * ∫ u in (-r)..r, Real.cos (2 * Real.pi * ξ * u) : ℝ) : ℂ)
```

**`KleinGordon.sineEvolution_zero_mass_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean#L102).

> **The massless sine evolution on the line.** The sine evolution at the origin of the
> mass is the average of the data over the interval of radius `r`.

```lean
lemma sineEvolution_zero_mass_apply {r : ℝ} (hr : 0 ≤ r) (g : 𝓢(ℝ, ℂ)) (x : ℝ) :
    sineEvolution ℂ r 0 g x = 1 / 2 * ∫ y in (x - r)..(x + r), g y
```

**`KleinGordon.solution_zero_mass_line`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean#L200).

> **The retarded solution of the wave equation on the line.** The massless retarded solution
> at `(t, x)` is one half of the integral of the source over the backward light cone. This is the
> retarded Green function `½ Θ(t - |x|)`.

```lean
lemma solution_zero_mass_line (ψ : TestFunction (⊤ : Opens (ℝ × ℝ)) ℂ ⊤) (t x : ℝ) :
    solution ℂ ψ 0 t x =
      1 / 2 * ∫ s in Set.Iic t, ∫ y in (x - (t - s))..(x + (t - s)), ψ (s, y)
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)

## Proof depends on

- [Fourier inversion for Schwartz functions on the line](../../../mathematics/part-02/fourier/inversion.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessLine.lean)
