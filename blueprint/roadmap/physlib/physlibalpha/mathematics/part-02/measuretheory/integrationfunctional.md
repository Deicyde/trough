---
declaration: module
origin: cited
lean: MeasureTheory.integrable_continuousMap, MeasureTheory.integralCLM, MeasureTheory.integralCLM_apply
statement: formalized
proof: formalized
---

# Integration as a continuous functional

The module `PhyslibAlpha.Mathematics.MeasureTheory.IntegrationFunctional`, [PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean): 3 declarations, 1 with a docstring.

> Integration against a finite measure as a continuous linear functional on `C(X, ℝ)`.

## i. Overview

> On a compact space, integrating continuous functions against a finite measure is linear and
> continuous in the supremum norm.

## ii. Key results

> - `MeasureTheory.integralCLM` is integration against a finite measure on `C(X, ℝ)`.

## iv. References

> * None.

## A. Integration as a continuous functional

**`MeasureTheory.integrable_continuousMap`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean#L49).

```lean
lemma integrable_continuousMap (μ : Measure X) [IsFiniteMeasure μ] (g : C(X, ℝ)) :
    Integrable g μ
```

**`MeasureTheory.integralCLM`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean#L54).

> Integration of continuous functions against a finite measure, as a continuous functional.

```lean
noncomputable def integralCLM (μ : Measure X) [IsFiniteMeasure μ] : C(X, ℝ) →L[ℝ] ℝ
```

**`MeasureTheory.integralCLM_apply`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean#L61).

```lean
lemma integralCLM_apply (μ : Measure X) [IsFiniteMeasure μ] (g : C(X, ℝ)) :
    integralCLM μ g = ∫ x, g x ∂μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/IntegrationFunctional.lean)
