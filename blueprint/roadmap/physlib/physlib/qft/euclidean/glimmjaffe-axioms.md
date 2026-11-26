---
declaration: module
origin: cited
lean: GlimmJaffe.FieldMeasure.OS0Analyticity, GlimmJaffe.FieldMeasure.TwoPointIntegrable, GlimmJaffe.FieldMeasure.OS1Regularity, GlimmJaffe.FieldMeasure.OS2EuclideanInvariance, GlimmJaffe.FieldMeasure.OS3ReflectionPositivity, GlimmJaffe.FieldMeasure.OS4Ergodicity, GlimmJaffe.FieldMeasure.GlimmJaffeAxioms
statement: formalized
proof: formalized
---

# Glimm–Jaffe axioms

The module `Physlib.QFT.Euclidean.GlimmJaffe.Axioms`, [Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean): 7 declarations, 7 with a docstring.

> The measure and generating-functional formulation of the Euclidean field axioms.

## i. Overview

> This is a formalization of the Glimm–Jaffe variation of the Osterwalder–Schrader axioms,
> as presented in Glimm and Jaffe, *Quantum Physics*, Chapter 6. [ref: glimm1987quantum]
> This formalism is on the generating functional, while the original OS axioms are on the
> Schwinger functions.
>
> We port the predicates in `OSforGFF/OS/Axioms.lean`: analyticity (OS0), regularity
> (OS1), full Euclidean invariance (OS2), complex reflection positivity (OS3), and
> ergodicity (OS4).
>
> Here `d` counts spatial dimensions, so the source total dimension is `d + 1`.
> Reflection positivity, ergodicity and the bundle assume `1 ≤ d`, retaining the source
> minimum of two total dimensions.
>
> OS4 uses exponentials without a factor of `i`, whereas the characteristic functional
> in OS0–OS3 includes that factor.
> This numbering differs from the distributional Osterwalder–Schrader axioms E0–E4.

## ii. Key results

> * `FieldMeasure.GlimmJaffeAxioms`: the five Glimm–Jaffe conditions OS0–OS4, with ergodicity
>   as OS4.
> * `FieldMeasure.TwoPointIntegrable`: the explicit mollifier-limit condition at the OS1 endpoint.
> * `FieldMeasure.OS4Ergodicity`: convergence of centered time averages in mean square.

## iv. References

> * Glimm and Jaffe, *Quantum Physics*, Chapter 6. [ref: glimm1987quantum]
> * Cherkis et al., *OSforGFF*, `OS/Axioms.lean`. [ref: osforgff]

## A. Analyticity and regularity

**`GlimmJaffe.FieldMeasure.OS0Analyticity`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L75).

> OS0: the characteristic functional is entire on every finite-dimensional complex
> family of Schwartz tests.

```lean
def OS0Analyticity (μ : FieldMeasure d) : Prop
```

**`GlimmJaffe.FieldMeasure.TwoPointIntegrable`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L81).

> The endpoint condition for OS1: mollified second moments converge at every nonzero
> separation to a locally integrable function. No limit is required at coincidence.

```lean
def TwoPointIntegrable (μ : FieldMeasure d) : Prop
```

**`GlimmJaffe.FieldMeasure.OS1Regularity`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L89).

> OS1: exponential growth controlled by the integrals of `‖f‖` and `‖f‖^p`,
> for some `1 ≤ p ≤ 2`, with the additional two-point condition when `p = 2`.

```lean
def OS1Regularity (μ : FieldMeasure d) : Prop
```

## B. Euclidean invariance and reflection positivity

**`GlimmJaffe.FieldMeasure.OS2EuclideanInvariance`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L99).

> OS2: invariance of the characteristic functional under the full Euclidean group.

```lean
def OS2EuclideanInvariance (μ : FieldMeasure d) : Prop
```

**`GlimmJaffe.FieldMeasure.OS3ReflectionPositivity`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L107).

> OS3 in the source's complex formulation: the real part of every reflected
> quadratic form is nonnegative. Reflection includes complex conjugation of the test.
> The dimension assumption retains the source's requirement of at least one spatial dimension.

```lean
def OS3ReflectionPositivity [Fact (1 ≤ d)] (μ : FieldMeasure d) : Prop
```

## C. Ergodicity

**`GlimmJaffe.FieldMeasure.OS4Ergodicity`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L118).

> OS4 ergodicity: centered time averages of finite linear combinations of
> `exp(⟨ω, f⟩)` converge to zero in mean square. This retains the source's integral
> formulation, with the centering inside the time integral. The dimension restriction retains
> the source's domain of at least two total dimensions.

```lean
def OS4Ergodicity [Fact (1 ≤ d)] (μ : FieldMeasure d) : Prop
```

## D. Bundled axioms

**`GlimmJaffe.FieldMeasure.GlimmJaffeAxioms`**, a structure, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean#L131).

> The Glimm–Jaffe axioms OS0–OS4, with ergodicity as the OS4 condition.

```lean
structure GlimmJaffeAxioms [Fact (1 ≤ d)] (μ : FieldMeasure d) : Prop where
  /-- OS0: entire dependence on finite families of complex tests. -/
  analytic : OS0Analyticity μ
  /-- OS1: the exponential bound and endpoint two-point condition. -/
  regular : OS1Regularity μ
  /-- OS2: full Euclidean invariance. -/
  euclideanInvariant : OS2EuclideanInvariance μ
  /-- OS3: reflection positivity for complex positive-time tests and coefficients. -/
  reflectionPositive : OS3ReflectionPositivity μ
  /-- OS4: mean-square ergodicity under time translation. -/
  ergodic : OS4Ergodicity μ
```

## Depends on

- [Glimm–Jaffe Euclidean fields](glimmjaffe-basic.md)
- [Standard bump sequence](glimmjaffe-standardbump.md)

## Sources

- [Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Axioms.lean)
