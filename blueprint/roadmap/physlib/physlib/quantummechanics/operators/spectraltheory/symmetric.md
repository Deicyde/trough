---
declaration: module
origin: cited
lean: LinearPMap.IsSymmetric.realNumericalRange, LinearPMap.IsSymmetric.realNumericalRange_eq, LinearPMap.IsSymmetric.realNumericalRange_neg, LinearPMap.IsSymmetric.im_eq_zero_of_mem_numericalRange, LinearPMap.IsSymmetric.numericalRange_subset, LinearPMap.IsSymmetric.numericalRange_eq, LinearPMap.IsSymmetric.closure_numericalRange_subset, LinearPMap.IsSymmetric.mem_regularityDomain_of_im_ne_zero
statement: formalized
proof: formalized
---

# Spectral theory for symmetric operators

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.Symmetric`, [Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean): 18 declarations, 15 with a docstring.

## i. Overview

> In this module we develop the spectral theory for symmetric operators.
>
> The numerical range of an operator, `Θ T = {⟪x, T x⟫_ℂ | x ∈ T.domain ∧ ‖x‖ = 1}`, is a subset of ℂ.
> For symmetric operators the numerical range consists only of real numbers and it is meaningful
> to discuss its upper/lower bounds. To facilitate this, we define `LinearPMap.realNumericalRange`
> as the projection of `LinearPMap.numericalRange` onto the real axis. For symmetric operators this
> simply reinterprets the numerical range as a subset of ℝ.
>
> A self-adjoint operator generates a one-parameter group of unitary operators (Stone's theorem).
> Operators of quantum mechanics are often first defined on a convenient dense domain, where they
> are only symmetric, and one then asks whether they are essentially self-adjoint, that is, whether
> their closure is self-adjoint. A sufficient criterion is that the eigenvectors of the operator
> lying in its domain span a dense subspace. For example, the eigenfunctions of the Hamiltonian of
> the quantum harmonic oscillator span a dense subspace of `L²(ℝ)` (proved in Physlib assuming
> Plancherel's theorem), so this Hamiltonian, defined on their span, is essentially self-adjoint.

## ii. Key results

> - `realNumericalRange` (`Θᵣₑ`) : The projection of the numerical range onto the real axis.
> - `compl_ofReal_subset_regularityDomain` : The regularity domain of a symmetric operator contains
>     all complex numbers with non-zero imaginary part.
> - `regularityDomain_isConnected_iff` : The regularity domain of a symmetric operator is connected
>     if and only if it contains a real number.
> - `IsSymmetric.isEssentiallySelfAdjoint_of_defectNumber_eq_zero` : The basic criterion for
>     essential self-adjointness: symmetric + densely defined + vanishing defect numbers at `± i`.
> - `IsSymmetric.isEssentiallySelfAdjoint_of_dense_span_eigenvectors` : A symmetric operator whose
>     eigenvectors span a dense subspace is essentially self-adjoint.

## iv. References

> * None.

## A. Numerical range

**`LinearPMap.IsSymmetric.realNumericalRange`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L73).

> The projection of the numerical range onto the real axis.

```lean
def realNumericalRange (T : H →ₗ.[ℂ] H) : Set ℝ
```

**`LinearPMap.IsSymmetric.realNumericalRange_eq`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L78).

```lean
lemma realNumericalRange_eq (T : H →ₗ.[ℂ] H) : Θᵣₑ T = re '' Θ T
```

**`LinearPMap.IsSymmetric.realNumericalRange_neg`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L81).

```lean
lemma realNumericalRange_neg (T : H →ₗ.[ℂ] H) : Θᵣₑ (-T) = -Θᵣₑ T
```

**`LinearPMap.IsSymmetric.im_eq_zero_of_mem_numericalRange`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L89).

> The numerical range of a symmetric operator is contained in the real axis.

```lean
lemma im_eq_zero_of_mem_numericalRange {z : ℂ} (hz : z ∈ Θ T) : z.im = 0
```

**`LinearPMap.IsSymmetric.numericalRange_subset`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L95).

> The numerical range of a symmetric operator is contained in the real axis.

```lean
lemma numericalRange_subset : Θ T ⊆ range ofReal
```

**`LinearPMap.IsSymmetric.numericalRange_eq`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L99).

> The numerical range of a symmetric operator is equal to its projection onto the real axis.

```lean
lemma numericalRange_eq : Θ T = ofReal '' Θᵣₑ T
```

**`LinearPMap.IsSymmetric.closure_numericalRange_subset`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L104).

```lean
lemma closure_numericalRange_subset : _root_.closure (Θ T) ⊆ range ofReal
```

## B. Regularity domain

**`LinearPMap.IsSymmetric.mem_regularityDomain_of_im_ne_zero`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L114).

> The regularity domain of a symmetric operator contains all complex numbers with non-zero
> imaginary part.

```lean
lemma mem_regularityDomain_of_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) : z ∈ T.regularityDomain
```

**`LinearPMap.IsSymmetric.compl_ofReal_subset_regularityDomain`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L122).

> The regularity domain of a symmetric operator contains all complex numbers with non-zero
> imaginary part.

```lean
lemma compl_ofReal_subset_regularityDomain : (range ofReal)ᶜ ⊆ T.regularityDomain
```

**`LinearPMap.IsSymmetric.Iio_subset_regularityDomain`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L126).

> If `m` is a lower bound on the numerical range then the regularity domain contains `(-∞,m)`.

```lean
lemma Iio_subset_regularityDomain {m : ℝ} (h : m ∈ lowerBounds (Θᵣₑ T)) :
    ofReal '' Iio m ⊆ T.regularityDomain
```

**`LinearPMap.IsSymmetric.Ioi_subset_regularityDomain`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L146).

> If `m` is an upper bound on the numerical range then the regularity domain contains `(m,∞)`.

```lean
lemma Ioi_subset_regularityDomain {m : ℝ} (h : m ∈ upperBounds (Θᵣₑ T)) :
    ofReal '' Ioi m ⊆ T.regularityDomain
```

**`LinearPMap.IsSymmetric.regularityDomain_isConnected_iff`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L155).

> The regularity domain of a symmetric operator is connected iff it contains a real number.

```lean
lemma regularityDomain_isConnected_iff :
    IsConnected T.regularityDomain ↔ (ofReal ⁻¹' T.regularityDomain).Nonempty
```

**`LinearPMap.IsSymmetric.regularityDomain_isConnected_of_bddBelow`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L203).

> The regularity domain of a lower semibounded symmetric operator is connected.

```lean
lemma regularityDomain_isConnected_of_bddBelow (h : BddBelow (Θᵣₑ T)) :
    IsConnected T.regularityDomain
```

**`LinearPMap.IsSymmetric.regularityDomain_isConnected_of_bddAbove`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L210).

> The regularity domain of an upper semibounded symmetric operator is connected.

```lean
lemma regularityDomain_isConnected_of_bddAbove (h : BddAbove (Θᵣₑ T)) :
    IsConnected T.regularityDomain
```

## C. Point spectrum

**`LinearPMap.IsSymmetric.pointSpectrum_real`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L221).

> Eigenvalues of a symmetric unbounded operator are real.

```lean
lemma pointSpectrum_real : σᵖ T ⊆ range ofReal
```

**`LinearPMap.IsSymmetric.mem_range_sub_of_apply_eq_of_im_ne_zero`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L236).

> If `T` is symmetric and `T x = c • x`, then `x` lies in the range of `T - z • 1` for every `z`
> with non-zero imaginary part.

```lean
lemma mem_range_sub_of_apply_eq_of_im_ne_zero {x : T.domain} {c z : ℂ}
    (hx : T x = c • (x : H)) (hz : z.im ≠ 0) : (x : H) ∈ (T - z • 1).toFun.range
```

## D. Essential self-adjointness

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_of_defectNumber_eq_zero`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L252).

> The basic criterion for essential self-adjointness: a symmetric, densely-defined operator
> whose defect numbers at `I` and `-I` both vanish is essentially self-adjoint.

```lean
lemma isEssentiallySelfAdjoint_of_defectNumber_eq_zero
    (hdense : T.HasDenseDomain) (hpos : T.defectNumber I = 0) (hneg : T.defectNumber (-I) = 0) :
    T.IsEssentiallySelfAdjoint
```

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_of_dense_span_eigenvectors`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean#L273).

> A symmetric operator `T` is essentially self-adjoint if a family of vectors `v j` of its
> domain, with `T (v j) = c j • v j`, spans a dense subspace. The `v j` need not be orthonormal,
> and some of them may be zero.

```lean
lemma isEssentiallySelfAdjoint_of_dense_span_eigenvectors {ι : Type*} (v : ι → T.domain)
    {c : ι → ℂ} (hv : ∀ j, T (v j) = c j • (v j : H))
    (hspan : Dense (Submodule.span ℂ (Set.range fun j ↦ (v j : H)) : Set H)) :
    T.IsEssentiallySelfAdjoint
```

## Depends on

- [Essentially self-adjoint operators](../essentiallyselfadjoint.md)
- [Spectral theory for closed operators](basic.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Symmetric.lean)
