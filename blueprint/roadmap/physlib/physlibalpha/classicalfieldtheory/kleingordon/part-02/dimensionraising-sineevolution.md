---
declaration: module
origin: cited
lean: KleinGordon.hasDerivAt_sineEvolution_radial
statement: formalized
proof: formalized
---

# Dimension raising for the sine evolution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DimensionRaising.SineEvolution`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SineEvolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SineEvolution.lean): 1 declaration, 1 with a docstring.

> The sine evolution in `d + 2` space dimensions is `-(1 / (2π ρ)) ∂ρ` of the one in `d` dimensions.

## i. Overview

> In one space dimension the massless retarded Green function is `½ Θ(t - |x|)`. In three space
> dimensions it is `δ(t - r) / (4π r)`. The second is `-(1 / (2π r)) ∂ᵣ` of the first. This holds in
> general: `G_{d+2} = -(1 / (2π r)) ∂ᵣ G_d` for every `d` and every mass.
>
> The proof has three steps. Descent (`Descent`) shows that the integral over the two extra
> variables of the sine evolution in `d + 2` dimensions is the sine evolution in `d` dimensions of
> the integrated data. The sine evolution of a radial function is radial (`Rotation`). The integral
> of a radial function over the plane is the tail integral of its profile, whose derivative is
> `-ρ Φ(ρ)` (`RadialPlane`). Together they give the identity on the sine evolutions of radial data.

## ii. Key results

> - `hasDerivAt_sineEvolution_radial` : dimension raising on the slices for every `d` and every mass.

## iv. References

> None.

## A. Radial slices in every dimension

> - `hasDerivAt_sineEvolution_radial` : dimension raising on the slices for every `d` and every mass.

**`KleinGordon.hasDerivAt_sineEvolution_radial`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SineEvolution.lean#L62).

> **Dimension raising on the slices.** Let `g'` be a radial Schwartz function on `E × ℝ²` and let
> `gb` be its integral over the plane. The sine evolution of `gb` along a ray has the derivative
> `-(2π ρ)` times the sine evolution of `g'` at distance `ρ`. This is `S\_\{d+2} g' = -(1 / (2π ρ))
> ∂ρ S\_d gb` for every dimension `d` and every mass.

```lean
lemma hasDerivAt_sineEvolution_radial {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ)
    (g' : 𝓢(WithLp 2 (E × EuclideanSpace ℝ (Fin 2)), ℂ)) (hrad : Function.IsRadial g')
    (gb : 𝓢(E, ℂ)) (hgb : ∀ x, gb x = ∫ y : EuclideanSpace ℝ (Fin 2),
      g' (WithLp.toLp 2 (x, y))) {e : E} (he : ‖e‖ = 1) {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun t : ℝ => sineEvolution ℂ r μ gb (t • e))
      (-(2 * Real.pi * ρ : ℝ) • sineEvolution ℂ r μ g' (WithLp.toLp 2 (ρ • e, 0))) ρ
```

## Depends on

- [The free evolution](../part-01/freeevolution.md)

## Proof depends on

- [Descent from `d + k` to `d` space dimensions](dimensionraising-descent.md)
- [Rotation invariance of the sine evolution](dimensionraising-rotation.md)
- [The integral of a radial function over the plane](../../../mathematics/part-02/measuretheory/radialplane.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SineEvolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SineEvolution.lean)
