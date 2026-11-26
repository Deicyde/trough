---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.mulOperator_isLowerBound, QuantumMechanics.SpaceDHilbertSpace.mulOperator_spectrum_subset_support_map, QuantumMechanics.SpaceDHilbertSpace.mulOperator_spectrum_eq_support_map, QuantumMechanics.SpaceDHilbertSpace.mulOperator_spectrum_eq_closure_range
statement: formalized
proof: formalized
---

# Spectrum of multiplication operators

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.Multiplication`, [Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean): 4 declarations, 4 with a docstring.

## i. Overview

> In this module we compute the spectrum of the multiplication operators `𝓜 μ f` of
> `Operators/Multiplication.lean`. If `ε ≤ ‖f x‖` for `μ`-a.e. `x`, with `ε > 0`, then `𝓜 μ f` is
> bounded below by `ε`. Applied to `f - z`, this shows that the spectrum of `𝓜 μ f` is contained in
> the essential range of `f`, the support of the pushforward measure `μ.map f`. For a σ-finite
> measure the two sets are equal, and for a continuous `f` and a measure which is positive on
> non-empty open sets they are the closure of the range of `f`.

## ii. Key results

> - `mulOperator_isLowerBound` : If `ε ≤ ‖f x‖` for `μ`-a.e. `x`, with `ε > 0`, then `ε` is a
>     lower bound for `𝓜 μ f`.
> - `mulOperator_spectrum_eq_support_map` : For a σ-finite measure `μ` and a `μ`-a.e. strongly
>     measurable `f`, the spectrum of `𝓜 μ f` is the essential range of `f`, the support of the
>     pushforward measure `μ.map f`.
> - `mulOperator_spectrum_eq_closure_range` : For a σ-finite measure `μ` which is positive on
>     non-empty open sets and a continuous `f`, the spectrum of `𝓜 μ f` is the closure of the
>     range of `f`.

## iv. References

> * None.

## A. Lower bound

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_isLowerBound`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean#L63).

> If `ε ≤ ‖f x‖` for `μ`-a.e. `x`, with `ε > 0`, then `ε` is a lower bound for `𝓜 μ f`, that is
> `ε * ‖ψ‖ ≤ ‖𝓜 μ f ψ‖` for every `ψ` in its domain.

```lean
lemma mulOperator_isLowerBound {μ : Measure (Space d)} {f : Space d → ℂ} {ε : ℝ} (hε : 0 < ε)
    (h : ∀ᵐ x ∂μ, ε ≤ ‖f x‖) : IsLowerBound (𝓜 μ f) 0 ε
```

## B. Spectrum

> For an almost everywhere strongly measurable `f`, the essential range of `f` is the support
> `(μ.map f).support` of the pushforward of `μ` by `f`.

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_spectrum_subset_support_map`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean#L81).

> The spectrum of `𝓜 μ f` is contained in the essential range `(μ.map f).support` of `f`,
> for any measure `μ` and any `μ`-a.e. strongly measurable `f`.

```lean
lemma mulOperator_spectrum_subset_support_map {μ : Measure (Space d)} {f : Space d → ℂ}
    (hf : AEStronglyMeasurable f μ) : σ (𝓜 μ f) ⊆ (μ.map f).support
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_spectrum_eq_support_map`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean#L99).

> For a σ-finite measure `μ` and a `μ`-a.e. strongly measurable `f`, the spectrum of `𝓜 μ f`
> is the essential range of `f`, the support of the pushforward measure `μ.map f`.

```lean
lemma mulOperator_spectrum_eq_support_map {μ : Measure (Space d)} [SigmaFinite μ]
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    σ (𝓜 μ f) = (μ.map f).support
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_spectrum_eq_closure_range`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean#L143).

> For a continuous `f` and a σ-finite measure `μ` which is positive on non-empty open sets,
> the spectrum of `𝓜 μ f` is the closure of the range of `f`.

```lean
lemma mulOperator_spectrum_eq_closure_range (μ : Measure (Space d)) [SigmaFinite μ]
    [μ.IsOpenPosMeasure] {f : Space d → ℂ} (hf : Continuous f) :
    σ (𝓜 μ f) = _root_.closure (Set.range f)
```

## Depends on

- [Multiplication operators on `SpaceDHilbertSpace`](../spaced-multiplication.md)
- [Spectral theory for closed operators](basic.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Multiplication.lean)
