---
declaration: module
origin: cited
lean: KleinGordon.sineEvolution_of_kernel, KleinGordon.sineEvolution_mass_line, KleinGordon.solution_mass_line
statement: formalized
proof: formalized
---

# The retarded solution of the Klein–Gordon equation on the line

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.ClosedForm.MassiveLine`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean): 3 declarations, 3 with a docstring.

> The retarded Green function in one space dimension is `½ Θ(t - |x|) J₀(m √(t² - x²))`.

## i. Overview

> A multiplier that is the cosine transform of an even continuous kernel on `[-r, r]` is the
> convolution with that kernel. The Bessel identity says that the multiplier of the massive sine
> evolution is the cosine transform of `½ J₀(m √(r² - u²))`. So the sine evolution on the line is the
> average of the data against the Bessel kernel over `[x - r, x + r]`. The Duhamel integral then gives
> the retarded solution as the integral of the source against the retarded Green function over the
> backward light cone. For `m = 0` this is the d'Alembert formula.

## ii. Key results

> - `sineEvolution_of_kernel` : a cosine-transform multiplier is a convolution.
> - `sineEvolution_mass_line` : the sine evolution with mass on the line.
> - `solution_mass_line` : the retarded solution with mass on the line.

## iv. References

> None.

## A. Convolution kernels

> - `sineEvolution_of_kernel` : a cosine-transform multiplier is a convolution.

## B. The Bessel kernel

> - `sineEvolution_mass_line` : the sine evolution with mass on the line.
> - `solution_mass_line` : the retarded solution with mass on the line.

**`KleinGordon.sineEvolution_of_kernel`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean#L61).

> **A multiplier that is a cosine transform is a convolution.**

```lean
lemma sineEvolution_of_kernel {μ r : ℝ} (hμ : 0 ≤ μ) (hr : 0 ≤ r) (w : ℝ → ℝ) (W : ℝ)
    (hw : Continuous w) (hwb : ∀ u, |w u| ≤ W) (hwe : ∀ u, w (-u) = w u)
    (hm : ∀ ξ : ℝ, multiplier r μ ξ =
      ((∫ u in (-r)..r, w u * Real.cos (2 * Real.pi * ξ * u) : ℝ) : ℂ))
    (g : 𝓢(ℝ, ℂ)) (x : ℝ) :
    sineEvolution ℂ r μ g x = ∫ u in (-r)..r, (w u : ℂ) * g (x + u)
```

**`KleinGordon.sineEvolution_mass_line`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean#L171).

> **The massive sine evolution on the line.** The sine evolution of the mass `m` is the average
> of the data against the Bessel kernel `½ J₀ (m √(r² - u²))` over the interval of radius `r`.

```lean
lemma sineEvolution_mass_line {r : ℝ} (hr : 0 ≤ r) (m : ℝ) (g : 𝓢(ℝ, ℂ)) (x : ℝ) :
    sineEvolution ℂ r (m ^ 2) g x =
      ∫ u in (-r)..r, ((1 / 2 * Real.besselSq (m ^ 2 * (r ^ 2 - u ^ 2)) : ℝ) : ℂ) * g (x + u)
```

**`KleinGordon.solution_mass_line`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean#L223).

> **The retarded solution of the Klein–Gordon equation on the line.** The retarded solution at
> `(t, x)` is the integral of the source against the retarded Green function
> `½ Θ(t - s - |u|) J₀ (m √((t - s)² - u²))` over the backward light cone.

```lean
lemma solution_mass_line (m : ℝ) (ψ : TestFunction (⊤ : Opens (ℝ × ℝ)) ℂ ⊤) (t x : ℝ) :
    solution ℂ ψ (m ^ 2) t x = ∫ s in Set.Iic t, ∫ u in (-(t - s))..(t - s),
      ((1 / 2 * Real.besselSq (m ^ 2 * ((t - s) ^ 2 - u ^ 2)) : ℝ) : ℂ) * ψ (s, x + u)
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)
- [The Bessel function `J₀` and the massive sine propagation function on the line](../../../mathematics/part-02/specialfunctions/sincpropagator-bessel.md)

## Proof depends on

- [Fourier inversion for Schwartz functions on the line](../../../mathematics/part-02/fourier/inversion.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveLine.lean)
