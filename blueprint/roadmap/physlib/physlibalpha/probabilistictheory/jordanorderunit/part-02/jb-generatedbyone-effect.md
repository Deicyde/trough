---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormedJordanAlgebra.jordanCfcEffect, ProbabilisticTheory.NormedJordanAlgebra.coe_jordanCfcEffect
statement: formalized
proof: formalized
---

# Effects from the functional calculus

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.GeneratedByOne.Effect`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/Effect.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/Effect.lean): 2 declarations, 2 with a docstring.

> A continuous `[0, 1]`-valued function of an observable in a JB-algebra is an effect.

## i. Overview

> A continuous function of an observable with values in `[0, 1]` is an effect.

## ii. Key results

> - `NormedJordanAlgebra.jordanCfcEffect` : the effect of a `[0, 1]`-valued function.
> - `NormedJordanAlgebra.coe_jordanCfcEffect` : the underlying observable is `f(a)`.

## iv. References

> * None.

## A. Effects from the functional calculus

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcEffect`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/Effect.lean#L54).

> The effect `f(a)` of a continuous function `f` with values in `[0, 1]`.

```lean
noncomputable def jordanCfcEffect [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) (hf0 : ∀ x, 0 ≤ f x) (hf1 : ∀ x, f x ≤ 1) : Effect E
```

**`ProbabilisticTheory.NormedJordanAlgebra.coe_jordanCfcEffect`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/Effect.lean#L65).

> Coercing the CFC effect forgets only its proved bounds.

```lean
lemma coe_jordanCfcEffect [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) (hf0 : ∀ x, 0 ≤ f x) (hf1 : ∀ x, f x ≤ 1) :
    (jordanCfcEffect a f hf0 hf1 : E) = jordanCfc a f
```

## Depends on

- [Continuous functional calculus in JB-algebras](jb-generatedbyone-cfc.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/Effect.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/Effect.lean)
