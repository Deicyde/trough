---
declaration: module
origin: cited
lean: TauCeti.innerRegular_map_of_continuousOn
statement: formalized
proof: formalized
---

# Inner regularity under almost everywhere continuous maps

The module `PhyslibAlpha.Mathematics.TauCeti.MeasureTheory.Measure.Regular`, [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/Regular.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/Regular.lean): 1 declaration, 1 with a docstring.

> A measurable map that is continuous on a measurable set of full measure sends an inner regular
> measure to an inner regular measure.

## i. Overview

> A measurable map that is continuous on a measurable set of full measure sends an inner regular
> measure to an inner regular measure. Global continuity is unnecessary: compact approximation
> can be performed inside the set where the map is continuous. This applies, for example, to
> spectral character assignments whose exceptional set has measure zero.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`TauCeti.innerRegular_map_of_continuousOn`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/Regular.lean#L49).

> A measurable map continuous on a measurable set of full measure preserves inner regularity.
> No separation, countability or finiteness assumption is required.

```lean
lemma innerRegular_map_of_continuousOn {μ : Measure α} [μ.InnerRegular]
    {f : α → β} {s : Set α} (hf : Measurable f) (hs : MeasurableSet s)
    (hcont : ContinuousOn f s) (hmem : ∀ᵐ x ∂μ, x ∈ s) :
    (Measure.map f μ).InnerRegular
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/Regular.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Measure/Regular.lean)
