---
declaration: module
origin: cited
lean: LinearMap.secondMomentForm, LinearMap.secondMomentForm_apply, LinearMap.covarianceForm, LinearMap.covarianceForm_apply, LinearMap.covarianceForm_isSymm, LinearMap.variance, LinearMap.covarianceForm_self, LinearMap.centered
statement: formalized
proof: formalized
---

# Statistics of a linear functional on a bilinear algebra

The module `PhyslibAlpha.ProbabilisticTheory.Algebra.Statistics`, [PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean): 10 declarations, 7 with a docstring.

> Second moments, covariance, variance and centering for a linear functional on a bilinear algebra.

## i. Overview

> Second moments and covariance use only a bilinear multiplication and a linear functional. They do
> not intrinsically require an order, positivity, associativity, commutativity, or the Jordan
> identity. This file defines them at that level so ordered Jordan algebras and self-adjoint parts of
> star algebras can share one canonical construction.
>
> For `omega : E ->_l[R] R`, the covariance is packaged as the bilinear form
>
> `(a, b) |-> omega (a * b) - omega a * omega b`.
>
> Commutativity of the product is used only to prove symmetry. A unit and the normalization
> `omega 1 = 1` are used only for centering identities. Positivity enters only for ordered
> algebras.

## ii. Key results

> - `LinearMap.secondMomentForm` : the second-moment bilinear form `(a, b) ↦ omega (a * b)`.
> - `LinearMap.covarianceForm` : the covariance bilinear form.
> - `LinearMap.variance` : the diagonal of the covariance form.
> - `LinearMap.centered` : the element `a - omega a • 1`.
> - `LinearMap.apply_centered` : a normalized functional vanishes on centered elements.
> - `LinearMap.apply_centered_mul_centered` : covariance is the value on a product of centered
>   elements.

## iv. References

> * None.

## A. Second moments and covariance

**`LinearMap.secondMomentForm`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L64).

> The second-moment bilinear form associated to a linear functional:
> `secondMomentForm omega a b = omega (a * b)`.

```lean
def secondMomentForm (omega : E →ₗ[ℝ] ℝ) : LinearMap.BilinForm ℝ E
```

**`LinearMap.secondMomentForm_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L79).

```lean
lemma secondMomentForm_apply (omega : E →ₗ[ℝ] ℝ) (a b : E) :
    secondMomentForm omega a b = omega (a * b)
```

**`LinearMap.covarianceForm`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L84).

> The covariance bilinear form associated to a linear functional:
> `covarianceForm omega a b = omega (a * b) - omega a * omega b`.

```lean
def covarianceForm (omega : E →ₗ[ℝ] ℝ) : LinearMap.BilinForm ℝ E
```

**`LinearMap.covarianceForm_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L108).

```lean
lemma covarianceForm_apply (omega : E →ₗ[ℝ] ℝ) (a b : E) :
    covarianceForm omega a b = omega (a * b) - omega a * omega b
```

**`LinearMap.covarianceForm_isSymm`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L112).

> The covariance form is symmetric when the multiplication is commutative.

```lean
lemma covarianceForm_isSymm (omega : E →ₗ[ℝ] ℝ) (hcomm : ∀ a b : E, a * b = b * a) :
    (covarianceForm omega).IsSymm
```

**`LinearMap.variance`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L118).

> The variance associated to a linear functional is the diagonal of its covariance form.

```lean
def variance (omega : E →ₗ[ℝ] ℝ) (a : E) : ℝ
```

**`LinearMap.covarianceForm_self`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L120).

```lean
lemma covarianceForm_self (omega : E →ₗ[ℝ] ℝ) (a : E) :
    covarianceForm omega a a = variance omega a
```

## B. Centering a normalized functional

**`LinearMap.centered`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L128).

> Center `a` at the value assigned by `omega`: `a - omega(a) • 1`.

```lean
def centered (omega : E →ₗ[ℝ] ℝ) (a : E) : E
```

**`LinearMap.apply_centered`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L133).

> A normalized linear functional sends every centered element to zero.

```lean
lemma apply_centered (omega : E →ₗ[ℝ] ℝ) (homega : omega 1 = 1) (a : E) :
    omega (centered omega a) = 0
```

**`LinearMap.apply_centered_mul_centered`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean#L138).

> For a normalized functional, covariance is its value on the product of centered elements.

```lean
lemma apply_centered_mul_centered (omega : E →ₗ[ℝ] ℝ) (homega : omega 1 = 1)
    (honeLeft : ∀ x : E, 1 * x = x) (honeRight : ∀ x : E, x * 1 = x) (a b : E) :
    omega (centered omega a * centered omega b) = covarianceForm omega a b
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Statistics.lean)
