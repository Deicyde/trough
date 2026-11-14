---
declaration: module
origin: cited
lean: KleinGordon.cosineFourier, KleinGordon.sineEvolution_mass_cos, KleinGordon.hasDerivAt_sineEvolution_zero, KleinGordon.cosineFourier_neg, KleinGordon.continuous_cosineFourier, KleinGordon.sineEvolution_mass_zero
statement: formalized
proof: formalized
---

# The massive sine evolution through the massless one

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.ClosedForm.MassDeformation`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean): 6 declarations, 4 with a docstring.

> The massive sine evolution is the massless sine evolution plus a Bessel average of the massless
> sine evolutions at smaller radii. This holds in every space dimension.

## i. Overview

> The massive multiplier is a Bessel average of the massless cosine multipliers
> (`Real.integral_besselSq_cos`). So the massive sine evolution is the Bessel average of the massless
> cosine evolution. The massless cosine evolution is the derivative of the massless sine evolution.
> Integration by parts moves the derivative to the Bessel weight.

## ii. Key results

> - `cosineFourier` : the massless cosine evolution as a Fourier integral.
> - `sineEvolution_mass_cos` : the massive sine evolution as a Bessel average of it.
> - `hasDerivAt_sineEvolution_zero` : the cosine evolution is the derivative of the sine evolution.
> - `sineEvolution_mass_zero` : the massive sine evolution through the massless one.

## iv. References

> None.

## A. The Bessel average of the cosine evolution

> - `cosineFourier` : the massless cosine evolution as a Fourier integral.
> - `sineEvolution_mass_cos` : the massive sine evolution as a Bessel average of it.

## B. The derivative of the sine evolution

> - `hasDerivAt_sineEvolution_zero` : the cosine evolution is the derivative of the sine evolution.

## C. Integration by parts

> - `sineEvolution_mass_zero` : the massive sine evolution through the massless one.

**`KleinGordon.cosineFourier`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean#L70).

> The cosine evolution of the massless wave equation, as a Fourier integral.

```lean
def cosineFourier (u : ℝ) (g : 𝓢(E, ℂ)) (x : E) : ℂ
```

**`KleinGordon.sineEvolution_mass_cos`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean#L74).

> **The massive sine evolution is a Bessel average of the massless cosine evolution.**

```lean
lemma sineEvolution_mass_cos {r : ℝ} (hr : 0 ≤ r) (m : ℝ) (g : 𝓢(E, ℂ)) (x : E) :
    sineEvolution ℂ r (m ^ 2) g x =
      ∫ u in (-r)..r, ((1 / 2 * Real.besselSq (m ^ 2 * (r ^ 2 - u ^ 2)) : ℝ) : ℂ) *
        cosineFourier u g x
```

**`KleinGordon.hasDerivAt_sineEvolution_zero`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean#L184).

> **The cosine evolution is the derivative of the sine evolution.**

```lean
lemma hasDerivAt_sineEvolution_zero (g : 𝓢(E, ℂ)) (x : E) (u₀ : ℝ) :
    HasDerivAt (fun u : ℝ => sineEvolution ℂ u 0 g x) (cosineFourier u₀ g x) u₀
```

**`KleinGordon.cosineFourier_neg`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean#L237).

```lean
lemma cosineFourier_neg (u : ℝ) (g : 𝓢(E, ℂ)) (x : E) :
    cosineFourier (-u) g x = cosineFourier u g x
```

**`KleinGordon.continuous_cosineFourier`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean#L243).

```lean
lemma continuous_cosineFourier (g : 𝓢(E, ℂ)) (x : E) : Continuous fun u => cosineFourier u g x
```

**`KleinGordon.sineEvolution_mass_zero`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean#L268).

> **The massive sine evolution in terms of the massless one.** The massive sine evolution is the
> massless one at the radius plus a Bessel average of the massless sine evolution over smaller
> radii.

```lean
lemma sineEvolution_mass_zero {r : ℝ} (hr : 0 ≤ r) (m : ℝ) (g : 𝓢(E, ℂ)) (x : E) :
    sineEvolution ℂ r (m ^ 2) g x = sineEvolution ℂ r 0 g x +
      ∫ u in (0 : ℝ)..r, ((2 * m ^ 2 * u * Real.besselSqDeriv (m ^ 2 * (r ^ 2 - u ^ 2)) : ℝ) : ℂ) *
        sineEvolution ℂ u 0 g x
```

## Depends on

- [The free evolution](freeevolution.md)
- [The Bessel function `J₀` and the massive sine propagation function on the line](../../../mathematics/part-02/specialfunctions/sincpropagator-bessel.md)

## Proof depends on

- [Integrals over a symmetric interval](../../../mathematics/part-01/calculus/symmetricinterval.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MassDeformation.lean)
