---
declaration: module
origin: cited
lean: ProbabilisticTheory.complexExtension, ProbabilisticTheory.complexExtension_apply, ProbabilisticTheory.complexExtension_coe, ProbabilisticTheory.complexExtension_star, ProbabilisticTheory.realPart_linearMap, ProbabilisticTheory.imaginaryPart_linearMap
statement: formalized
proof: formalized
---

# Expectation values of non-self-adjoint operators

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.ComplexExtension`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean): 6 declarations, 5 with a docstring.

> A state is defined on the self-adjoint observables, and extends uniquely to a complex-linear
> functional on all operators.

## i. Overview

> A state assigns an expectation value to every observable, a self-adjoint operator. Correlation
> functions such as `⟨A B(t)⟩` involve products of observables, which are not self-adjoint, and so
> need the expectation value of an arbitrary operator `a`. Every operator is uniquely a combination
> `a = ℜ a + i ℑ a` of two self-adjoint operators, its real and imaginary parts, and the expectation
> value is extended by linearity: `⟨a⟩ = ⟨ℜ a⟩ + i ⟨ℑ a⟩`. This is the unique complex-linear extension
> of the state that is compatible with taking adjoints, `⟨a*⟩ = conj ⟨a⟩`.

## ii. Key results

> - `complexExtension` : the complex-linear functional extending an expectation value.
> - `complexExtension_coe` : on self-adjoint operators it is the original expectation value.
> - `complexExtension_star` : the expectation value of the adjoint is the complex conjugate.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1, 2nd ed.,
>   Chapter 2.

## A. The extension

**`ProbabilisticTheory.complexExtension`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean#L61).

> The complex-linear extension of an expectation value on self-adjoint operators to all
> operators: `⟨a⟩ = ⟨ℜ a⟩ + i ⟨ℑ a⟩`.

```lean
noncomputable def complexExtension (φ : selfAdjoint A →ₗ[ℝ] ℝ) : A →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.complexExtension_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean#L71).

```lean
lemma complexExtension_apply (φ : selfAdjoint A →ₗ[ℝ] ℝ) (a : A) :
    complexExtension φ a = φ (ℜ a) + Complex.I * φ (ℑ a)
```

## B. Properties

**`ProbabilisticTheory.complexExtension_coe`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean#L81).

> On self-adjoint operators the extension is the original expectation value.

```lean
lemma complexExtension_coe (φ : selfAdjoint A →ₗ[ℝ] ℝ) (a : selfAdjoint A) :
    complexExtension φ (a : A) = φ a
```

**`ProbabilisticTheory.complexExtension_star`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean#L86).

> The expectation value of the adjoint is the complex conjugate of the expectation value.

```lean
lemma complexExtension_star (φ : selfAdjoint A →ₗ[ℝ] ℝ) (a : A) :
    complexExtension φ (star a) = starRingEnd ℂ (complexExtension φ a)
```

## C. Compatibility with `*`-linear maps

**`ProbabilisticTheory.realPart_linearMap`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean#L108).

> A complex-linear map commuting with the adjoint maps the real part of an operator to the real
> part of its image.

```lean
lemma realPart_linearMap (f : C →ₗ[ℂ] D) (hf : ∀ a, f (star a) = star (f a)) (a : C) :
    ((ℜ (f a) : selfAdjoint D) : D) = f (ℜ a : C)
```

**`ProbabilisticTheory.imaginaryPart_linearMap`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean#L115).

> A complex-linear map commuting with the adjoint maps the imaginary part of an operator to the
> imaginary part of its image.

```lean
lemma imaginaryPart_linearMap (f : C →ₗ[ℂ] D) (hf : ∀ a, f (star a) = star (f a)) (a : C) :
    ((ℑ (f a) : selfAdjoint D) : D) = f (ℑ a : C)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/ComplexExtension.lean)
