---
declaration: module
origin: cited
lean: TestFunction.compCLMofContinuousLinearEquiv, TestFunction.compCLMofContinuousLinearEquiv_apply
statement: formalized
proof: formalized
---

# TestFunction

The module `Physlib.Mathematics.ForMathlib.TestFunction`, [Physlib/Mathematics/ForMathlib/TestFunction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/TestFunction.lean): 2 declarations, 1 with a docstring.

## i. Overview

> In this module, we define a continuous linear map between spaces of test functions via the pullback
> of a test function `TestFunction Ω' F ⊤` along a linear equivalence`g : E ≃L[ℝ] E'`.

## ii. Key results

> - `compCLMofContinuousLinearEquiv` : A continuous linear map between spaces of test functions
>  `𝓓(Ω', F)` and `𝓓(Ω, F)`.

## iv. References

> * None.

## A. Continuous linear maps

**`TestFunction.compCLMofContinuousLinearEquiv`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/TestFunction.lean#L45).

> Given normed spaces `E` and `E'` and open subsets `Ω ⊆ E` and `Ω' ⊆ E'` and a map between
> them `g : E → E'`, define a continuous linear map between the spaces of test functions
> `𝓓(Ω', F)` and `𝓓(Ω, F)`.

```lean
noncomputable def compCLMofContinuousLinearEquiv {E E'} [NormedAddCommGroup E]
    [NormedAddCommGroup E'] [NormedSpace ℝ E] [NormedSpace ℝ E']
    {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Ω : Opens E} {Ω' : Opens E'} (g : E ≃L[ℝ] E')
    (h : g.invFun '' Ω' ⊆ ↑Ω) :
    TestFunction Ω' F ⊤ →L[ℝ] TestFunction Ω F ⊤
```

**`TestFunction.compCLMofContinuousLinearEquiv_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/TestFunction.lean#L120).

```lean
lemma compCLMofContinuousLinearEquiv_apply {E E'} [NormedAddCommGroup E]
    [NormedAddCommGroup E'] [NormedSpace ℝ E] [NormedSpace ℝ E']
    {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Ω : Opens E} {Ω' : Opens E'} (g : E ≃L[ℝ] E')
    (h : g.invFun '' Ω' ⊆ ↑Ω) (φ : TestFunction Ω' F ⊤) :
    compCLMofContinuousLinearEquiv g h φ = φ ∘ g
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/TestFunction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/TestFunction.lean)
