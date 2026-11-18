---
declaration: module
origin: cited
lean: KleinGordon.integral_sineEvolution_marginal
statement: formalized
proof: formalized
---

# Descent from `d + k` to `d` space dimensions

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DimensionRaising.Descent`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Descent.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Descent.lean): 1 declaration, 1 with a docstring.

> Integrating the sine evolution in `d + k` space dimensions over the extra variables gives the sine
> evolution in `d` space dimensions of the integrated data.

## i. Overview

> Let `E'` be the Euclidean product of `E` and `F`. The Fourier transform of the integral over `F`
> of a function on `E'` is the restriction of its transform to the frequencies `(ξ, 0)`. The
> multiplier of the sine evolution depends on the norm of the frequency, so the restriction to
> `(ξ, 0)` is the multiplier of `E`. This is Hadamard's method of descent. It holds for every mass.

## ii. Key results

> - `integral_sineEvolution_marginal` : descent for the sine evolution, for every mass.

## iv. References

> None.

## A. Descent

> - `integral_sineEvolution_marginal` : descent for the sine evolution, for every mass.

**`KleinGordon.integral_sineEvolution_marginal`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Descent.lean#L57).

> **Descent.** Integrating the sine evolution in `E × F` over `F` gives the sine evolution in
> `E` of the integrated data.

```lean
lemma integral_sineEvolution_marginal {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ)
    (g' : 𝓢(WithLp 2 (E × F), ℂ)) (gb : 𝓢(E, ℂ))
    (hgb : ∀ x, gb x = ∫ y : F, g' (WithLp.toLp 2 (x, y))) (x : E) :
    ∫ y : F, sineEvolution ℂ r μ g' (WithLp.toLp 2 (x, y)) = sineEvolution ℂ r μ gb x
```

## Depends on

- [The free evolution](../part-01/freeevolution.md)

## Proof depends on

- [Klein–Gordon fields and causal propagation](../part-01/solution.md)
- [The Fourier transform under a linear change of variables](../../../mathematics/part-02/fourier/linearchange.md)
- [The marginal of a Schwartz function on a Euclidean product](../../../mathematics/part-02/fourier/marginal.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Descent.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Descent.lean)
