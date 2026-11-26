---
declaration: module
origin: cited
lean: GlimmJaffe.FieldMeasure, GlimmJaffe.FieldMeasure.generatingFunctional, GlimmJaffe.FieldMeasure.schwingerFunction, GlimmJaffe.FieldMeasure.schwingerFunction₂, GlimmJaffe.FieldMeasure.smearedTwoPointFunction
statement: formalized
proof: formalized
---

# Glimm–Jaffe Euclidean fields

The module `Physlib.QFT.Euclidean.GlimmJaffe.Basic`, [Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean): 5 declarations, 5 with a docstring.

> Generating functionals and Schwinger functions for a real scalar field.

## i. Overview

> This is the measure-based formulation of a real scalar Euclidean quantum field.
> A field configuration, defined in `FieldConfiguration`, is a tempered distribution `ω`,
> so the basic observable is its evaluation `ω f` on a real Schwartz test function `f`.
> A probability measure on these configurations specifies the field statistics, in a way that
> Schwinger functions are expectations of products of field evaluations, and the
> generating functional is the expectation of `exp(i ⟨ω, f⟩)`. The Glimm–Jaffe axioms
> in the companion file impose analyticity, growth bounds, Euclidean invariance,
> reflection positivity and ergodicity on this measure. This setup supplies the
> Euclidean data for reconstruction.
>
> The parameter `d` counts spatial dimensions. Spacetime is Physlib's
> `TimeAndSpace d = Time × Space d`, with the standard origins used by its real
> vector-space instances. Thus the source's total dimension is `d + 1`.
>
> The Euclidean symmetries, positive-time tests and normalized bumps acting on the
> test functions are in `TimeAndSpace.TestFunctions.Schwartz`.

## ii. Key results

> * `FieldMeasure.generatingFunctional`: the complex characteristic functional.
> * `smearedTwoPointFunction`: the two-point function smeared with an arbitrary normalized bump.

## iv. References

> * Glimm and Jaffe, *Quantum Physics*. [ref: glimm1987quantum]

**`GlimmJaffe.FieldMeasure`**, an abbrev, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean#L64).

> A probability measure on field configurations.
> The Euclidean functional-integral measure `μ`, the rigorous counterpart of `𝒟φ e^{-S}/Z`.

```lean
abbrev FieldMeasure (d : ℕ) : Type
```

## A. Generating functionals

**`GlimmJaffe.FieldMeasure.generatingFunctional`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean#L73).

> The characteristic functional `Z[f] = ∫ exp(i ⟨ω, f⟩) dμ` on complex tests.

```lean
def generatingFunctional (μ : FieldMeasure d)
    (f : 𝓢(TimeAndSpace d, ℂ)) : ℂ
```

## B. Schwinger functions

**`GlimmJaffe.FieldMeasure.schwingerFunction`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean#L80).

> The real `n`-point Schwinger function, the expectation of the product of field evaluations.

```lean
def schwingerFunction (μ : FieldMeasure d) (n : ℕ) (f : Fin n → 𝓢(TimeAndSpace d, ℝ)) : ℝ
```

**`GlimmJaffe.FieldMeasure.schwingerFunction₂`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean#L84).

> The real two-point Schwinger function evaluated on two Schwartz tests.

```lean
def schwingerFunction₂ (μ : FieldMeasure d) (f g : 𝓢(TimeAndSpace d, ℝ)) : ℝ
```

**`GlimmJaffe.FieldMeasure.smearedTwoPointFunction`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean#L90).

> The two-point Schwinger function smeared at `x` and zero with an arbitrary normalized bump.
> This follows `SmearedTwoPointFunction` in `OSforGFF`, with the bump supplied independently
> of the standard sequence used in the OS1 endpoint condition.

```lean
def smearedTwoPointFunction (μ : FieldMeasure d)
    (φ : ContDiffBump (0 : EuclideanSpace ℝ (Fin (d + 1)))) (x : TimeAndSpace d) : ℝ
```

## Depends on

- [Glimm–Jaffe field configurations](glimmjaffe-fieldconfiguration.md)
- [Schwartz test functions on time and space](../../spaceandtime/timeandspace/testfunctions-schwartz.md)

## Sources

- [Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/Basic.lean)
