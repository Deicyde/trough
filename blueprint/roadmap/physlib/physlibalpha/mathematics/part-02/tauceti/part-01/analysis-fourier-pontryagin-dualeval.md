---
declaration: module
origin: cited
lean: TauCeti.PontryaginDual.continuous_coe_eval_const, TauCeti.PontryaginDual.integrable_coe_eval
statement: formalized
proof: formalized
---

# Evaluation of Pontryagin characters

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Fourier.Pontryagin.DualEval`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/DualEval.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/DualEval.lean): 2 declarations, 2 with a docstring.

> Evaluation at a fixed monoid element is continuous on the Pontryagin dual.

## i. Overview

> Evaluation at a fixed monoid element is continuous on the Pontryagin dual. Its complex-valued
> form is integrable against every finite measure. These lemmas supply the integrands for
> Fourier–Stieltjes transforms, and apply to arbitrary monoids with a topology.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`TauCeti.PontryaginDual.continuous_coe_eval_const`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/DualEval.lean#L47).

> Complex-valued evaluation of a Pontryagin character at a fixed monoid element is continuous.

```lean
lemma continuous_coe_eval_const (g : G) :
    Continuous (fun χ : _root_.PontryaginDual G => (χ g : ℂ))
```

**`TauCeti.PontryaginDual.integrable_coe_eval`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/DualEval.lean#L55).

> Complex-valued evaluation of a Pontryagin character is integrable against a finite measure.

```lean
lemma integrable_coe_eval
    {μ : Measure (_root_.PontryaginDual G)} [IsFiniteMeasure μ] (g : G) :
    Integrable (fun χ : _root_.PontryaginDual G => (χ g : ℂ)) μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/DualEval.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/DualEval.lean)
