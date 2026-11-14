---
declaration: module
origin: cited
lean: TestFunction.precompLinearEquivSupportedCLM, TestFunction.precompLinearEquivCLM, TestFunction.precompLinearEquivCLM_apply, TestFunction.weightedTestBCFLinear, TestFunction.weightedTestBCF, TestFunction.weightedTestBCF_apply, TestFunction.smoothWeightTest, TestFunction.smoothWeightTest_apply
statement: formalized
proof: formalized
---

# Operations on test functions

The module `PhyslibAlpha.Mathematics.Distribution.TestFunction`, [PhyslibAlpha/Mathematics/Distribution/TestFunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean): 8 declarations, 7 with a docstring.

## i. Overview

> Multiplication by a weight and composition with a linear equivalence are continuous on test
> functions.

## ii. Key results

> - `precompLinearEquivSupportedCLM` : Pullback between fixed-support smooth test spaces by an
>   invertible linear coordinate map.
> - `precompLinearEquivCLM` : Pullback by an invertible continuous linear coordinate change is
>   continuous on smooth tests.
> - `weightedTestBCFLinear` : Weight a compact smooth test field and retain its bounded continuous
>   representative.
> - `weightedTestBCF` : Arbitrary continuous weights give continuous maps from the native LF
>   test-function space into the uniform norm.
> - `smoothWeightTest` : Multiplication by a smooth weight is continuous in the native LF test
>   topology.

## iv. References

> None.

## A. Continuous linear changes of test-function coordinates

> - `precompLinearEquivSupportedCLM` : Pullback between fixed-support smooth test spaces by an
>   invertible linear coordinate map.
> - `precompLinearEquivCLM` : Pullback by an invertible continuous linear coordinate change is
>   continuous on smooth tests.
>
> Lemmas: `precompLinearEquivCLM_apply`.

## B. Weighted test functions in the uniform norm

> - `weightedTestBCFLinear` : Weight a compact smooth test field and retain its bounded continuous
>   representative.
> - `weightedTestBCF` : Arbitrary continuous weights give continuous maps from the native LF
>   test-function space into the uniform norm.
> - `smoothWeightTest` : Multiplication by a smooth weight is continuous in the native LF test
>   topology.
>
> Lemmas: `weightedTestBCF_apply`, `smoothWeightTest_apply`.

**`TestFunction.precompLinearEquivSupportedCLM`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L78).

> Pullback between fixed-support smooth test spaces by an invertible linear coordinate map.

```lean
def precompLinearEquivSupportedCLM (e : A ≃L[ℝ] B) (K : Compacts B) :
    ContDiffMapSupportedIn B F ⊤ K →L[ℝ]
      ContDiffMapSupportedIn A F ⊤ (K.map e.symm e.symm.continuous)
```

**`TestFunction.precompLinearEquivCLM`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L111).

> Pullback by an invertible continuous linear coordinate change is continuous on smooth tests.

```lean
def precompLinearEquivCLM (e : A ≃L[ℝ] B) :
    𝓓((⊤ : Opens B), F) →L[ℝ] 𝓓((⊤ : Opens A), F)
```

**`TestFunction.precompLinearEquivCLM_apply`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L124).

```lean
lemma precompLinearEquivCLM_apply (e : A ≃L[ℝ] B) (f : 𝓓((⊤ : Opens B), F)) (x : A) :
    precompLinearEquivCLM e f x = f (e x)
```

**`TestFunction.weightedTestBCFLinear`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L133).

> Weight a compact smooth test field and retain its bounded continuous representative.

```lean
def weightedTestBCFLinear (w : E → ℝ) (hw : Continuous w) :
    _root_.TestFunction (⊤ : TopologicalSpace.Opens E) V ⊤ →ₗ[ℝ] (E →ᵇ V)
```

**`TestFunction.weightedTestBCF`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L142).

> Arbitrary continuous weights give continuous maps from the native LF test-function space
> into the uniform norm. No global bound on the weight is required.

```lean
def weightedTestBCF (w : E → ℝ) (hw : Continuous w) :
    _root_.TestFunction (⊤ : TopologicalSpace.Opens E) V ⊤ →L[ℝ] (E →ᵇ V)
```

**`TestFunction.weightedTestBCF_apply`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L169).

> The weighted embedding retains the pointwise weighted field.

```lean
lemma weightedTestBCF_apply (w : E → ℝ) (hw : Continuous w)
    (φ : _root_.TestFunction (⊤ : TopologicalSpace.Opens E) V ⊤) (x : E) :
    weightedTestBCF w hw φ x = w x • φ x
```

**`TestFunction.smoothWeightTest`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L174).

> Multiplication by a smooth weight is continuous in the native LF test topology.

```lean
def smoothWeightTest (w : E → ℝ) (hw : ContDiff ℝ ∞ w) :
    _root_.TestFunction (⊤ : TopologicalSpace.Opens E) V ⊤ →L[ℝ]
      _root_.TestFunction (⊤ : TopologicalSpace.Opens E) V ⊤
```

**`TestFunction.smoothWeightTest_apply`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean#L195).

> The LF-continuous weight map is pointwise scalar multiplication.

```lean
lemma smoothWeightTest_apply (w : E → ℝ) (hw : ContDiff ℝ ∞ w)
    (φ : _root_.TestFunction (⊤ : TopologicalSpace.Opens E) V ⊤) (p : E) :
    smoothWeightTest w hw φ p = w p • φ p
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Distribution/TestFunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TestFunction.lean)
