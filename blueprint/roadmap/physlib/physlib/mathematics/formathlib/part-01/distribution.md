---
declaration: module
origin: cited
lean: Distribution.compContinuousLinearEquiv, Distribution.compContinuousLinearEquiv_apply_apply
statement: formalized
proof: formalized
---

# Distribution

The module `Physlib.Mathematics.ForMathlib.Distribution`, [Physlib/Mathematics/ForMathlib/Distribution.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Distribution.lean): 2 declarations, 1 with a docstring.

## i. Overview

> In this module, we define continuous linear maps between spaces of distributions `𝓓'(Ω, F)`
> and `𝓓'(Ω', F)`, using `TestFunction.compCLMofContinuousLinearEquiv`.

## ii. Key results

> - `compContinuousLinearEquiv` : A continuous linear map between spaces of distributions `𝓓'(Ω, F)`
>   and `𝓓'(Ω', F)`.

## iv. References

> * None.

## A. Continuous linear maps

**`Distribution.compContinuousLinearEquiv`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Distribution.lean#L45).

> Having defined a CLM between test functions, we now define a continuous linear map between spaces
> of distributions `𝓓'(Ω, F)` and `𝓓'(Ω', F)`.

```lean
noncomputable def compContinuousLinearEquiv {E E'} [NormedAddCommGroup E]
    [NormedAddCommGroup E'] [NormedSpace ℝ E] [NormedSpace ℝ E']
    {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Ω : Opens E} {Ω' : Opens E'} (g : E ≃L[ℝ] E')
    (h : g.invFun '' Ω' ⊆ ↑Ω) :
    Distribution Ω F ⊤ →L[ℝ] Distribution Ω' F ⊤
```

**`Distribution.compContinuousLinearEquiv_apply_apply`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Distribution.lean#L53).

```lean
lemma compContinuousLinearEquiv_apply_apply {E E'} [NormedAddCommGroup E]
    [NormedAddCommGroup E'] [NormedSpace ℝ E] [NormedSpace ℝ E']
    {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Ω : Opens E} {Ω' : Opens E'} (g : E ≃L[ℝ] E')
    (h : g.invFun '' Ω' ⊆ ↑Ω) (T : Distribution Ω F ⊤)
    (κ : TestFunction Ω' ℝ ⊤):
    compContinuousLinearEquiv g h T κ =
    T (compCLMofContinuousLinearEquiv (F := ℝ) g h κ)
```

## Depends on

- [TestFunction](testfunction.md)

## Sources

- [Physlib/Mathematics/ForMathlib/Distribution.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Distribution.lean)
