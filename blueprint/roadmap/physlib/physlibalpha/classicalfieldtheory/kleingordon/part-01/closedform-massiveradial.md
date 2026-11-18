---
declaration: module
origin: cited
lean: KleinGordon.sineEvolution_origin_radialSource, KleinGordon.solution_origin_radialSource, KleinGordon.solution_origin_radialSource_space, KleinGordon.solution_origin_radialSource_besselJ1
statement: formalized
proof: formalized
---

# The retarded Green function with mass in three space dimensions

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.ClosedForm.MassiveRadial`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean): 4 declarations, 4 with a docstring.

> The retarded Green function in three space dimensions is
> `δ(t - r) / (4π r) - m J₁(m √(t² - r²)) / (4π √(t² - r²)) Θ(t - r)`.

## i. Overview

> Dimension raising turns the one-dimensional Green function `½ Θ J₀(m √(t² - x²))` into the
> three-dimensional one by `-(1 / (2π r)) ∂ᵣ`. The derivative of the step gives the shell
> `δ(t - r) / (4π r)`. The derivative of `J₀` gives the tail with `J₁`.

## ii. Key results

> - `sineEvolution_origin_radialSource` : the Kirchhoff–Bessel formula for the sine evolution at
>   the origin.
> - `solution_origin_radialSource_space` : the Kirchhoff–Bessel formula for the retarded solution on
>   `Space 3`.
> - `solution_origin_radialSource_besselJ1` : the same formula with `J₁`.

## iv. References

> None.

## A. The formula at the origin

> - `sineEvolution_origin_radialSource` : the Kirchhoff–Bessel formula for the sine evolution at
>   the origin.
> - `solution_origin_radialSource` : the formula for the retarded solution on Euclidean three-space.
> - `solution_origin_radialSource_space` : the Kirchhoff–Bessel formula for the retarded solution on
>   `Space 3`.
> - `solution_origin_radialSource_besselJ1` : the same formula with `J₁`.

**`KleinGordon.sineEvolution_origin_radialSource`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean#L67).

> **The Kirchhoff–Bessel formula for the sine evolution at the origin.** For a radial source with
> the profile `Φ` the massive sine evolution at the origin is
> `τ Φ(τ) + 2 m² ∫₀^τ u² κ(m² (τ² - u²)) Φ(u) du`, where `κ = -J₁(z) / (2z)` at `y = z²`.

```lean
lemma sineEvolution_origin_radialSource (m : ℝ) {τ : ℝ} (hτ : 0 ≤ τ)
    (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (s : ℝ) :
    sineEvolution ℂ τ (m ^ 2) (slice ℂ (radialSource Eucl3 (liftProfile P)) s) 0 =
      (τ : ℂ) * liftProfile P (s, τ ^ 2) + ((2 * m ^ 2 : ℝ) : ℂ) *
        ∫ u in (0 : ℝ)..τ, ((u ^ 2 * Real.besselSqDeriv (m ^ 2 * (τ ^ 2 - u ^ 2)) : ℝ) : ℂ) *
          liftProfile P (s, u ^ 2)
```

**`KleinGordon.solution_origin_radialSource`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean#L244).

> **The Kirchhoff–Bessel formula for the retarded solution at the origin.** For a radial source
> `ψ'(s, x) = Q(s, ‖x‖²)` in three space dimensions the massive retarded solution at `(t, 0)` is
> `∫_{s ≤ t} [τ Φ(τ) + 2 m² ∫₀^τ u² κ(m² (τ² - u²)) Φ(u) du] ds` with `τ = t - s`,
> `Φ(u) = Q(s, u²)` and `κ(z²) = -J₁(z) / (2 z)`.

```lean
lemma solution_origin_radialSource (m : ℝ)
    (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (t : ℝ) :
    solution ℂ (radialSource Eucl3 (liftProfile P)) (m ^ 2) t 0 =
      ∫ s in Set.Iic t, ((((t - s : ℝ)) : ℂ) * liftProfile P (s, (t - s) ^ 2) +
        ((2 * m ^ 2 : ℝ) : ℂ) * ∫ u in (0 : ℝ)..(t - s),
          ((u ^ 2 * Real.besselSqDeriv (m ^ 2 * ((t - s) ^ 2 - u ^ 2)) : ℝ) : ℂ) *
            liftProfile P (s, u ^ 2))
```

**`KleinGordon.solution_origin_radialSource_space`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean#L256).

> **The Kirchhoff–Bessel formula on `Space 3`.**

```lean
lemma solution_origin_radialSource_space (m : ℝ)
    (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (t : ℝ) :
    solution ℂ (radialSource (Space 3) (liftProfile P)) (m ^ 2) t 0 =
      ∫ s in Set.Iic t, ((((t - s : ℝ)) : ℂ) * liftProfile P (s, (t - s) ^ 2) +
        ((2 * m ^ 2 : ℝ) : ℂ) * ∫ u in (0 : ℝ)..(t - s),
          ((u ^ 2 * Real.besselSqDeriv (m ^ 2 * ((t - s) ^ 2 - u ^ 2)) : ℝ) : ℂ) *
            liftProfile P (s, u ^ 2))
```

**`KleinGordon.solution_origin_radialSource_besselJ1`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean#L268).

> **The Kirchhoff–Bessel formula with `J₁`.** For `m ≠ 0` the retarded solution at the origin of
> a radial source is `∫_{s ≤ t} [τ Φ(τ) - m ∫₀^τ u² J₁(m √(τ² - u²)) / √(τ² - u²) Φ(u) du] ds`.

```lean
lemma solution_origin_radialSource_besselJ1 {m : ℝ} (hm : m ≠ 0)
    (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (t : ℝ) :
    solution ℂ (radialSource (Space 3) (liftProfile P)) (m ^ 2) t 0 =
      ∫ s in Set.Iic t, ((((t - s : ℝ)) : ℂ) * liftProfile P (s, (t - s) ^ 2) -
        (m : ℂ) * ∫ u in (0 : ℝ)..(t - s),
          ((u ^ 2 * (Real.besselJ1 (m * Real.sqrt ((t - s) ^ 2 - u ^ 2)) /
            Real.sqrt ((t - s) ^ 2 - u ^ 2)) : ℝ) : ℂ) * liftProfile P (s, u ^ 2))
```

## Depends on

- [Smooth radial lifts](../part-02/dimensionraising-radiallift.md)
- [The Bessel function `J₀` and the massive sine propagation function on the line](../../../mathematics/part-02/specialfunctions/sincpropagator-bessel.md)

## Proof depends on

- [The retarded solution of the Klein–Gordon equation on the line](closedform-massiveline.md)
- [Integrals over a symmetric interval](../../../mathematics/part-01/calculus/symmetricinterval.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassiveRadial.lean)
