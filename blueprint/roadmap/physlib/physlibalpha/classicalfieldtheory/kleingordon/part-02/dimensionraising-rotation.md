---
declaration: module
origin: cited
lean: KleinGordon.multiplier_comp_isometry, KleinGordon.sineEvolution_comp_isometry, KleinGordon.isRadial_sineEvolution
statement: formalized
proof: formalized
---

# Rotation invariance of the sine evolution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DimensionRaising.Rotation`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean): 3 declarations, 2 with a docstring.

> The sine evolution commutes with linear isometries. It therefore maps radial functions to radial
> functions.

## i. Overview

> The multiplier of the sine evolution depends on the norm of the frequency. The Fourier transform
> commutes with linear isometries. So the sine evolution of a rotated function is the rotation of the
> sine evolution. A radial function is invariant under all rotations. So is its evolution.

## ii. Key results

> - `sineEvolution_comp_isometry` : the sine evolution commutes with linear isometries.
> - `isRadial_sineEvolution` : the sine evolution of a radial function is radial.

## iv. References

> None.

## A. Isometries

> - `sineEvolution_comp_isometry` : the sine evolution commutes with linear isometries.
> - `isRadial_sineEvolution` : the sine evolution of a radial function is radial.

**`KleinGordon.multiplier_comp_isometry`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean#L57).

```lean
lemma multiplier_comp_isometry (A : V ≃ₗᵢ[ℝ] W) (r μ : ℝ) (ξ : V) :
    multiplier r μ (A ξ) = multiplier r μ ξ
```

**`KleinGordon.sineEvolution_comp_isometry`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean#L63).

> **The sine evolution commutes with rotations.**

```lean
lemma sineEvolution_comp_isometry {μ : ℝ} (hμ : 0 ≤ μ) (A : V ≃ₗᵢ[ℝ] W) (r : ℝ) (g : 𝓢(W, ℂ))
    (x : V) :
    sineEvolution ℂ r μ (SchwartzMap.compCLMOfContinuousLinearEquiv ℂ A.toContinuousLinearEquiv g)
        x = sineEvolution ℂ r μ g (A x)
```

**`KleinGordon.isRadial_sineEvolution`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean#L79).

> **The sine evolution of a radial function is radial.**

```lean
lemma isRadial_sineEvolution {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ) {g : 𝓢(V, ℂ)} (hg : Function.IsRadial g) :
    Function.IsRadial (sineEvolution ℂ r μ g)
```

## Depends on

- [The free evolution](../part-01/freeevolution.md)

## Proof depends on

- [The Fourier transform under a linear change of variables](../../../mathematics/part-02/fourier/linearchange.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Rotation.lean)
