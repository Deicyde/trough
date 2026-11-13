---
declaration: module
origin: cited
lean: LinearPMap.IsSymmetric.realNumericalRange, LinearPMap.IsSymmetric.realNumericalRange_eq, LinearPMap.IsSymmetric.realNumericalRange_neg, LinearPMap.IsSymmetric.im_eq_zero_of_mem_numericalRange, LinearPMap.IsSymmetric.numericalRange_subset, LinearPMap.IsSymmetric.numericalRange_eq, LinearPMap.IsSymmetric.closure_numericalRange_subset, LinearPMap.IsSymmetric.mem_regularityDomain_of_im_ne_zero
statement: formalized
proof: formalized
---

# Spectral theory for symmetric operators

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.Symmetric`, [Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean): 16 declarations, 13 with a docstring.

## i. Overview

> In this module we develop the spectral theory for symmetric operators.
>
> The numerical range of an operator, `Θ T = {⟪x, T x⟫_ℂ | x ∈ T.domain ∧ ‖x‖ = 1}`, is a subset of ℂ.
> For symmetric operators the numerical range consists only of real numbers and it is meaningful
> to discuss its upper/lower bounds. To facilitate this, we define `LinearPMap.realNumericalRange`
> as the projection of `LinearPMap.numericalRange` onto the real axis. For symmetric operators this
> simply reinterprets the numerical range as a subset of ℝ.

## ii. Key results

> - `realNumericalRange` (`Θᵣₑ`) : The projection of the numerical range onto the real axis.
> - `compl_ofReal_subset_regularityDomain` : The regularity domain of a symmetric operator contains
>     all complex numbers with non-zero imaginary part.
> - `regularityDomain_isConnected_iff` : The regularity domain of a symmetric operator is connected
>     if and only if it contains a real number.
> - `IsSymmetric.isEssentiallySelfAdjoint_of_defectNumber_eq_zero` : The basic criterion for
>     essential self-adjointness: symmetric + densely defined + vanishing defect numbers at `± i`.

## iv. References

> * None.

## A. Numerical range

**`LinearPMap.IsSymmetric.realNumericalRange`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L61).

> The projection of the numerical range onto the real axis.

```lean
def realNumericalRange (T : H →ₗ.[ℂ] H) : Set ℝ
```

**`LinearPMap.IsSymmetric.realNumericalRange_eq`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L66).

```lean
lemma realNumericalRange_eq (T : H →ₗ.[ℂ] H) : Θᵣₑ T = re '' Θ T
```

**`LinearPMap.IsSymmetric.realNumericalRange_neg`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L69).

```lean
lemma realNumericalRange_neg (T : H →ₗ.[ℂ] H) : Θᵣₑ (-T) = -Θᵣₑ T
```

**`LinearPMap.IsSymmetric.im_eq_zero_of_mem_numericalRange`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L77).

> The numerical range of a symmetric operator is contained in the real axis.

```lean
lemma im_eq_zero_of_mem_numericalRange {z : ℂ} (hz : z ∈ Θ T) : z.im = 0
```

**`LinearPMap.IsSymmetric.numericalRange_subset`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L83).

> The numerical range of a symmetric operator is contained in the real axis.

```lean
lemma numericalRange_subset : Θ T ⊆ range ofReal
```

**`LinearPMap.IsSymmetric.numericalRange_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L87).

> The numerical range of a symmetric operator is equal to its projection onto the real axis.

```lean
lemma numericalRange_eq : Θ T = ofReal '' Θᵣₑ T
```

**`LinearPMap.IsSymmetric.closure_numericalRange_subset`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L92).

```lean
lemma closure_numericalRange_subset : _root_.closure (Θ T) ⊆ range ofReal
```

## B. Regularity domain

**`LinearPMap.IsSymmetric.mem_regularityDomain_of_im_ne_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L102).

> The regularity domain of a symmetric operator contains all complex numbers with non-zero
> imaginary part.

```lean
lemma mem_regularityDomain_of_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) : z ∈ T.regularityDomain
```

**`LinearPMap.IsSymmetric.compl_ofReal_subset_regularityDomain`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L110).

> The regularity domain of a symmetric operator contains all complex numbers with non-zero
> imaginary part.

```lean
lemma compl_ofReal_subset_regularityDomain : (range ofReal)ᶜ ⊆ T.regularityDomain
```

**`LinearPMap.IsSymmetric.Iio_subset_regularityDomain`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L114).

> If `m` is a lower bound on the numerical range then the regularity domain contains `(-∞,m)`.

```lean
lemma Iio_subset_regularityDomain {m : ℝ} (h : m ∈ lowerBounds (Θᵣₑ T)) :
    ofReal '' Iio m ⊆ T.regularityDomain
```

**`LinearPMap.IsSymmetric.Ioi_subset_regularityDomain`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L134).

> If `m` is an upper bound on the numerical range then the regularity domain contains `(m,∞)`.

```lean
lemma Ioi_subset_regularityDomain {m : ℝ} (h : m ∈ upperBounds (Θᵣₑ T)) :
    ofReal '' Ioi m ⊆ T.regularityDomain
```

**`LinearPMap.IsSymmetric.regularityDomain_isConnected_iff`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L143).

> The regularity domain of a symmetric operator is connected iff it contains a real number.

```lean
lemma regularityDomain_isConnected_iff :
    IsConnected T.regularityDomain ↔ (ofReal ⁻¹' T.regularityDomain).Nonempty
```

**`LinearPMap.IsSymmetric.regularityDomain_isConnected_of_bddBelow`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L191).

> The regularity domain of a lower semibounded symmetric operator is connected.

```lean
lemma regularityDomain_isConnected_of_bddBelow (h : BddBelow (Θᵣₑ T)) :
    IsConnected T.regularityDomain
```

**`LinearPMap.IsSymmetric.regularityDomain_isConnected_of_bddAbove`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L198).

> The regularity domain of an upper semibounded symmetric operator is connected.

```lean
lemma regularityDomain_isConnected_of_bddAbove (h : BddAbove (Θᵣₑ T)) :
    IsConnected T.regularityDomain
```

## C. Point spectrum

**`LinearPMap.IsSymmetric.pointSpectrum_real`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L209).

> Eigenvalues of a symmetric unbounded operator are real.

```lean
lemma pointSpectrum_real : σᵖ T ⊆ range ofReal
```

## D. Essential self-adjointness

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_of_defectNumber_eq_zero`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L230).

> The basic criterion for essential self-adjointness: a symmetric, densely-defined operator
> whose defect numbers at `I` and `-I` both vanish is essentially self-adjoint.

```lean
lemma isEssentiallySelfAdjoint_of_defectNumber_eq_zero
    (hdense : T.HasDenseDomain) (hpos : T.defectNumber I = 0) (hneg : T.defectNumber (-I) = 0) :
    T.IsEssentiallySelfAdjoint
```

## Depends on

- [Spectral theory for closed operators](basic.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean)
