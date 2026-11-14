---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyInverseMap, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyInverseMap_cayleyMap, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_injective, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.CayleySupported, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_cayleyInverseMap_of_supported, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_cayleySupported, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMeasureEquiv
statement: formalized
proof: formalized
---

# Spectral measures and the Cayley transform

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Cayley.Measure`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean): 9 declarations, 5 with a docstring.

> Spectral measures on ℝ correspond to Cayley-supported spectral measures on ℂ.

## i. Overview

> Spectral measures on `ℝ` push forward along the Cayley transform to spectral measures on `ℂ`
> supported on the unit circle away from `1`. Pulling back along the inverse Cayley transform undoes
> this, which gives an equivalence between spectral measures on `ℝ` and such measures on `ℂ`.

## ii. Key results

> - `cayleyMap`, `cayleyInverseMap` : pushing forward along the Cayley transform and its inverse.
> - `cayleyMap_injective` : the pushforward is injective.
> - `CayleySupported` : a spectral measure on `ℂ` supported on the unit circle away from `1`.
> - `cayleyMeasureEquiv` : the equivalence between spectral measures on `ℝ` and Cayley-supported ones
>   on `ℂ`.

## iv. References

> * None.

## A. Pushforward and pullback along the Cayley transform

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L59).

> The bounded spectral measure obtained from a real spectral measure by the Cayley map.

```lean
def cayleyMap (μS : WOTSpectralMeasure ℝ H) : WOTSpectralMeasure ℂ H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyInverseMap`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L63).

> Pull a complex spectral measure back to a real variable using the inverse Cayley coordinate.

```lean
def cayleyInverseMap (ν : WOTSpectralMeasure ℂ H) : WOTSpectralMeasure ℝ H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyInverseMap_cayleyMap`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L66).

```lean
lemma cayleyInverseMap_cayleyMap (μS : WOTSpectralMeasure ℝ H) :
    cayleyInverseMap (cayleyMap μS) = μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_injective`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L86).

> The Cayley pushforward is injective on real spectral measures. Thus a real spectral measure
> is completely recoverable from its bounded Cayley-side measure; this is the basic uniqueness
> half of the Cayley equivalence used by the unbounded spectral theorem.

```lean
lemma cayleyMap_injective {μS νS : WOTSpectralMeasure ℝ H}
    (h : cayleyMap μS = cayleyMap νS) : μS = νS
```

## B. The Cayley equivalence of spectral-measure data

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.CayleySupported`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L98).

> A spectral measure on `ℂ` is Cayley supported when it lives on the unit circle and gives no mass
> to `1`.

```lean
def CayleySupported (ν : WOTSpectralMeasure ℂ H) : Prop
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_cayleyInverseMap_of_supported`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L102).

```lean
lemma cayleyMap_cayleyInverseMap_of_supported
    {ν : WOTSpectralMeasure ℂ H} (hν : CayleySupported ν) :
    cayleyMap (cayleyInverseMap ν) = ν
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_cayleySupported`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L126).

```lean
lemma cayleyMap_cayleySupported (μS : WOTSpectralMeasure ℝ H) :
    CayleySupported (cayleyMap μS)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMeasureEquiv`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L149).

> The Cayley transform is an equivalence between spectral measures on `ℝ` and Cayley-supported
> spectral measures on `ℂ`.

```lean
def cayleyMeasureEquiv :
    WOTSpectralMeasure ℝ H ≃ {ν : WOTSpectralMeasure ℂ H // CayleySupported ν}
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.cayleyMap_weakIntegral`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean#L156).

```lean
lemma cayleyMap_weakIntegral {μS : WOTSpectralMeasure ℝ H}
    (g : ℂ → ℝ) (x y : H)
    (hg : AEStronglyMeasurable g ((μS.scalarMeasure x y).variation.map cayley))
    (hgi : (μS.scalarMeasure x y).Integrable (g ∘ cayley)) :
    (cayleyMap μS).weakIntegral g x y = μS.weakIntegral (g ∘ cayley) x y
```

## Depends on

- [The Cayley transform](unbounded-cayley-basic.md)
- [The vector-measure integral against a scalar matrix coefficient](unbounded-weakintegral.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Cayley/Measure.lean)
