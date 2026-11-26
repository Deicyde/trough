---
declaration: module
origin: cited
lean: LinearPMap.numericalRange_convex, LinearPMap.resolvent, LinearPMap.IsLowerBound, LinearPMap.isLowerBound_neg, LinearPMap.isLowerBound_of_right_le, LinearPMap.isLowerBound_of_left_le, LinearPMap.isLowerBound_closure, LinearPMap.regularityDomain
statement: formalized
proof: formalized
---

# Spectral theory for closed operators

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.Basic`, [Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean): 70 declarations, 31 with a docstring, 1 listed as significant; 1 private, not shown.

## i. Overview

> In this module we develop the basics for the spectral theory of closed unbounded operators.
> This forms the basis for the spectral theory of self-adjoint unbounded operators,
> which are of central importance in quantum mechanics.
>
> Definitions for subsets of ℂ associated to an operator `T : H →ₗ.[ℂ] H` vary by author.
> Here we adopt those used in
> [Konrad Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space][Schmudgen2012]
> [ref: Schmudgen2012], summarized in the following table:
>
> | Subset of ℂ | abbrev. | `D(T - z)` | `R(T - z)` | `(T - z)⁻¹` |
> | :---------- | :-----: | :--------: | :--------: | :---------: |
> | Regularity domain | | `= ⊥` | | continuous |
> | Resolvent set | `ρ` | `= ⊥` | `= ⊤` | continuous |
> | Point spectrum | `σᵖ` | `≠ ⊥` | | |
> | Residual spectrum | `σʳ` | `= ⊥` | `≠ ⊤` | continuous |
> | Continuous spectrum | `σᶜ` | | not closed | |

## ii. Key results

> Definitions (corresponding to an operator `T : H →ₗ.[ℂ] H`)
> - `LinearPMap.regularityDomain` : The set of regular points. A complex number `z` is a regular
>     point if there exists `c > 0` such that `c * ‖x‖ ≤ ‖T x - z • x‖` for all `x : T.domain`.
> - `LinearPMap.deficiencySubspace` : Given a complex number `z`, the closed submodule which
>     is orthogonal to the range of `T - z • 1`.
> - `LinearPMap.defectNumber` : Given a complex number `z`, the rank of the corresponding
>     deficiency subspace as a (possibly infinite) cardinal.
> - `LinearPMap.numericalRange` (`Θ`) : The set of complex numbers `⟪x, T x⟫_ℂ` as `x` ranges over
>     the unit sphere in `T.domain`.
> - `LinearPMap.resolventSet` (`ρ`) : The set of complex numbers `z` for which `T - z • 1`
>     has a continuous (equivalently, bounded) inverse with domain all of `H`.
> - `LinearPMap.spectrum` (`σ`) : The complement of the resolvent set.
> - `LinearPMap.pointSpectrum` (`σᵖ`) : The set of complex numbers `z` for which `T - z • 1`
>     is not injective, that is, the eigenvalues of `T`.
> - `LinearPMap.residualSpectrum` (`σʳ`) : The set of complex numbers `z` for which `T - z • 1`
>     has a continuous (equivalently, bounded) inverse with domain not all of `H`.
> - `LinearPMap.continuousSpectrum` (`σᶜ`) : The set of complex numbers `z` for which
>     the range of `T - z • 1` is not dense in `H`.
>
> Main results
> - `regularityDomain_isOpen` : The regularity domain is an open subset of `ℂ`.
> - `closure_range_sub_eq_range_closure_sub` : If `z` is a regular point for a closable operator `T`
>     then the closure of `(T - z • 1).range` is `(T.closure - z • 1).range`.
> - `defectNumber_const` : The defect number is constant on each connected component
>     of the regularity domain.
> - `compl_closure_numericalRange_subset_regularityDomain` : The regularity domain contains
>     the exterior of the numerical range.
> - `numericalRange_convex` : The Toeplitz-Hausdorff theorem — the numerical range is a convex set.
> - `resolventSet_isOpen` and `spectrum_isClosed` : The resolvent set is an open subset of ℂ
>     and its complement, the spectrum, is closed.
> - `IsClosed.spectrum_eq` : For a closed operator the spectrum is the union of the point, residual
>     and continuous spectra.

## iv. References

> * Konrad Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space. [ref: Schmudgen2012]

**`LinearPMap.resolvent`**, an abbrev, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L107).

> The resolvent, `(T - z • 1)⁻¹`.

```lean
abbrev resolvent (T : H →ₗ.[ℂ] H) (z : ℂ) : H →ₗ.[ℂ] H
```

## A. Regularity domain

**`LinearPMap.IsLowerBound`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L117).

> `IsLowerBound T z c` is the property that `c * ‖x‖ ≤ ‖T x - z • x‖` for all `x : T.domain`.

```lean
def IsLowerBound (T : H →ₗ.[ℂ] H) (z : ℂ) (c : ℝ) : Prop
```

**`LinearPMap.isLowerBound_neg`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L119).

```lean
lemma isLowerBound_neg {T : H →ₗ.[ℂ] H} {z : ℂ} {c : ℝ} (h : IsLowerBound T z c) :
    IsLowerBound (-T) (-z) c
```

**`LinearPMap.isLowerBound_of_right_le`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L123).

```lean
lemma isLowerBound_of_right_le
    {T : H →ₗ.[ℂ] H} {z : ℂ} {c₁ c₂ : ℝ} (hle : c₁ ≤ c₂) (h : IsLowerBound T z c₂) :
    IsLowerBound T z c₁
```

**`LinearPMap.isLowerBound_of_left_le`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L128).

```lean
lemma isLowerBound_of_left_le
    {T₁ T₂ : H →ₗ.[ℂ] H} (hle : T₁ ≤ T₂) {z : ℂ} {c : ℝ} (h : IsLowerBound T₂ z c) :
    IsLowerBound T₁ z c
```

**`LinearPMap.isLowerBound_closure`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L133).

```lean
lemma isLowerBound_closure
    {T : H →ₗ.[ℂ] H} {z : ℂ} {c : ℝ} (h : IsLowerBound T z c) : IsLowerBound T.closure z c
```

**`LinearPMap.regularityDomain`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L150).

> The regular points for `T`.
>
> `z : ℂ` is a regular point for `T` iff there exists a constant `c > 0` such that
> `c * ‖x‖ ≤ ‖(T - z • 1) x‖` for all `x ∈ T.domain`.

```lean
def regularityDomain (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.regularityDomain_neg`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L153).

```lean
lemma regularityDomain_neg (T : H →ₗ.[ℂ] H) : (-T).regularityDomain = -T.regularityDomain
```

**`LinearPMap.regularityDomain_smul`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L160).

```lean
lemma regularityDomain_smul (T : H →ₗ.[ℂ] H) {w : ℂ} (hw : w ≠ 0) :
    (w • T).regularityDomain = w • T.regularityDomain
```

**`LinearPMap.regularityDomain_antitone`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L180).

> `T ≤ T'` implies `T'.regularityDomain ⊆ T.regularityDomain`.

```lean
lemma regularityDomain_antitone : Antitone (regularityDomain (H := H))
```

**`LinearPMap.mem_regularityDomain_iff`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L185).

> `z` is a regular point for `T` iff `T - z • 1` has
> a continuous (equivalently, bounded) inverse.

```lean
lemma mem_regularityDomain_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ T.regularityDomain ↔ (T - z • 1).toFun.ker = ⊥ ∧ Continuous (𝑅 T z)
```

**`LinearPMap.ball_subset_regularityDomain`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L215).

> The regularity domain of `T` contains open balls with radii controlled by the lower bounds.

```lean
lemma ball_subset_regularityDomain
    {T : H →ₗ.[ℂ] H} {z : ℂ} {c : ℝ} (h : IsLowerBound T z c) : ball z c ⊆ T.regularityDomain
```

**`LinearPMap.regularityDomain_isOpen`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L226).

> The regularity domain is an open set.

```lean
lemma regularityDomain_isOpen (T : H →ₗ.[ℂ] H) : IsOpen T.regularityDomain
```

**`LinearPMap.regularityDomain_closure`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L230).

> `T` and `T.closure` have the same regularity domain.

```lean
lemma regularityDomain_closure (T : H →ₗ.[ℂ] H) :
    T.closure.regularityDomain = T.regularityDomain
```

**`LinearPMap.IsClosable.closure_range_sub_eq_range_closure_sub`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L235).

```lean
lemma IsClosable.closure_range_sub_eq_range_closure_sub [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosable) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    (T - z • 1).toFun.range.closure = (T.closure - z • 1).toFun.range
```

**`LinearPMap.IsClosed.sub_range_isClosed`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L276).

```lean
lemma IsClosed.sub_range_isClosed [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    _root_.IsClosed ((T - z • 1).toFun.range : Set H)
```

**`LinearPMap.IsUnbounded.orthogonal_closure_sub_range`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L282).

> `(T.closure - z • 1).rangeᗮ = (T† - conj z • 1).ker`

```lean
lemma IsUnbounded.orthogonal_closure_sub_range [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsUnbounded) (z : ℂ) :
    (T.closure - z • 1).toFun.rangeᗮ
      = (T† - conj z • 1).toFun.ker.map (T† - conj z • 1).domain.subtype
```

**`LinearPMap.IsUnbounded.orthogonal_adjoint_sub_ker`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L296).

> `(T† - conj z • 1).kerᗮ = (T.closure - z • 1).range`

```lean
lemma IsUnbounded.orthogonal_adjoint_sub_ker [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsUnbounded) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    ((T† - conj z • 1).toFun.ker.map (T† - conj z • 1).domain.subtype)ᗮ
      = (T.closure - z • 1).toFun.range
```

## B. Deficiency subspace & defect number

**`LinearPMap.deficiencySubspace`**, a def, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L313).

> For a partial linear map `T` and any complex number `z`, the closed submodule which
> is orthogonal to the range of `T - z • 1`.
>
> `T.defectNumber z` is defined as the rank of this subspace.

```lean
def deficiencySubspace (T : H →ₗ.[ℂ] H) (z : ℂ) : ClosedSubmodule ℂ H
```

**`LinearPMap.deficiencySubspace_coe`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L317).

```lean
lemma deficiencySubspace_coe (T : H →ₗ.[ℂ] H) (z : ℂ) :
    T.deficiencySubspace z = (T - z • 1).toFun.rangeᗮ
```

**`LinearPMap.defectNumber`**, a def, [line 321](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L321).

> The rank of `T.deficiencySubspace z = (T - z • 1).rangeᗮ`.

```lean
def defectNumber (T : H →ₗ.[ℂ] H) (z : ℂ) : Cardinal
```

**`LinearPMap.defectNumber_eq`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L323).

```lean
lemma defectNumber_eq (T : H →ₗ.[ℂ] H) (z : ℂ) :
    T.defectNumber z = Module.rank ℂ (T.deficiencySubspace z)
```

**`LinearPMap.IsClosed.defectNumber_eq_zero_iff`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L326).

```lean
lemma IsClosed.defectNumber_eq_zero_iff [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    T.defectNumber z = 0 ↔ (T - z • 1).toFun.range = ⊤
```

**`LinearPMap.defectNumber_eq_zero_iff_dense`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L333).

> The defect number of `T` at `z` vanishes if and only if the range of `T - z • 1` is dense.

```lean
lemma defectNumber_eq_zero_iff_dense [CompleteSpace H] {T : H →ₗ.[ℂ] H} {z : ℂ} :
    T.defectNumber z = 0 ↔ Dense ((T - z • 1).toFun.range : Set H)
```

**`LinearPMap.defectNumber_closure`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L340).

> `T` and `T.closure` have the same defect number at points in their regularity domain.

```lean
lemma defectNumber_closure [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} {z : ℂ} (hz : z ∈ T.regularityDomain) :
    T.closure.defectNumber z = T.defectNumber z
```

**`Submodule.inf_ne_bot_of_rank_lt`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L348).

```lean
lemma _root_.Submodule.inf_ne_bot_of_rank_lt
    {E F : Submodule ℂ H} [E.HasOrthogonalProjection] (h_rank : Module.rank ℂ E < Module.rank ℂ F) :
    Eᗮ ⊓ F ≠ ⊥
```

**`LinearPMap.IsClosed.exists_inner_eq_zero_of_defectNumber_lt`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L361).

```lean
lemma IsClosed.exists_inner_eq_zero_of_defectNumber_lt [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosed)
    {z₁ z₂ : ℂ} (hz₁ : z₁ ∈ T.regularityDomain) (h : T.defectNumber z₁ < T.defectNumber z₂) :
    ∃ x : T.domain, x ≠ 0 ∧ ⟪T x - z₁ • x, T x - z₂ • x⟫_ℂ = 0
```

**`LinearPMap.IsClosable.defectNumber_eq_of_mem_ball`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L375).

```lean
lemma IsClosable.defectNumber_eq_of_mem_ball [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosable)
    {z₁ z₂ : ℂ} {c : ℝ} (h : IsLowerBound T z₁ c) (h_ball : z₂ ∈ ball z₁ c) :
    T.defectNumber z₁ = T.defectNumber z₂
```

**`LinearPMap.IsClosable.defectNumber_const`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L403).

> The defect number is constant on each connected component of the regularity domain.

```lean
lemma IsClosable.defectNumber_const [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosable)
    {z₁ z₂ : ℂ} (hz : z₂ ∈ connectedComponentIn T.regularityDomain z₁) :
    T.defectNumber z₁ = T.defectNumber z₂
```

## C. Numerical range

**`LinearPMap.numericalRange`**, a def, [line 467](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L467).

> The set `{⟪x, T x⟫_ℂ | x ∈ T.domain ∧ ‖x‖ = 1} ⊆ ℂ`.

```lean
def numericalRange (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.numericalRange_eq`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L472).

```lean
lemma numericalRange_eq (T : H →ₗ.[ℂ] H) : Θ T = (fun x ↦ ⟪↑x, T x⟫_ℂ) '' {x | ‖x‖ = 1}
```

**`LinearPMap.mem_numericalRange`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L474).

```lean
lemma mem_numericalRange {T : H →ₗ.[ℂ] H} {x : T.domain} (hx : x ≠ 0) :
    (‖x‖ ^ 2)⁻¹ * ⟪↑x, T x⟫_ℂ ∈ Θ T
```

**`LinearPMap.numericalRange_nonempty`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L480).

```lean
lemma numericalRange_nonempty {T : H →ₗ.[ℂ] H} (hT : T.domain ≠ ⊥) : (Θ T).Nonempty
```

**`LinearPMap.numericalRange_neg`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L485).

```lean
lemma numericalRange_neg (T : H →ₗ.[ℂ] H) : Θ (-T) = -Θ T
```

**`LinearPMap.numericalRange_smul`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L490).

```lean
lemma numericalRange_smul (T : H →ₗ.[ℂ] H) (c : ℂ) : Θ (c • T) = c • Θ T
```

**`LinearPMap.numericalRange_sub_const`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L494).

```lean
lemma numericalRange_sub_const (T : H →ₗ.[ℂ] H) (c : ℂ) : Θ (T - c • 1) = Θ T - {c}
```

**`LinearPMap.compl_closure_numericalRange_subset_regularityDomain`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L506).

> The regularity domain contains the exterior of the numerical range.

```lean
lemma compl_closure_numericalRange_subset_regularityDomain (T : H →ₗ.[ℂ] H) :
    (_root_.closure (Θ T))ᶜ ⊆ T.regularityDomain
```

### C.1. The Toeplitz-Hausdorff theorem

**`LinearPMap.numericalRange_convex`**, a theorem, [line 552](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L552). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/scripts/lint/exemptions/Theorems.txt).

> The Toeplitz-Hausdorff theorem.

```lean
theorem numericalRange_convex (T : H →ₗ.[ℂ] H) : Convex ℝ (Θ T)
```

## D. Spectrum of a closed operator

### D.1. Resolvent set

**`LinearPMap.resolventSet`**, a def, [line 638](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L638).

> The resolvent set, `ρ`, of a partial linear map.
>
> A complex number `z` is in `ρ T` iff the linear map `T - z • 1` from `T.domain` to `H`
> is a bijection with continuous (equivalently, bounded) inverse.

```lean
def resolventSet (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.resolventSet_eq`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L644).

```lean
lemma resolventSet_eq (T : H →ₗ.[ℂ] H) :
    ρ T = {z | (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range = ⊤ ∧ Continuous (𝑅 T z)}
```

**`LinearPMap.mem_resolventSet_iff`**, a lemma, [line 648](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L648).

```lean
lemma mem_resolventSet_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ ρ T ↔ (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range = ⊤ ∧ Continuous (𝑅 T z)
```

**`LinearPMap.resolventSet_eq_empty`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L653).

> If an operator is not closed then its resolvent set is empty.

```lean
lemma resolventSet_eq_empty [CompleteSpace H] {T : H →ₗ.[ℂ] H} (h : ¬T.IsClosed) : ρ T = ∅
```

**`LinearPMap.resolventSet_subset_regularityDomain`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L663).

```lean
lemma resolventSet_subset_regularityDomain (T : H →ₗ.[ℂ] H) : ρ T ⊆ T.regularityDomain
```

**`LinearPMap.IsClosed.resolventSet_eq`**, a lemma, [line 668](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L668).

> For a closed operator the continuity of the resolvent is redundant
> in the definition of the resolvent set.

```lean
lemma IsClosed.resolventSet_eq [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) :
    ρ T = {z : ℂ | (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range = ⊤}
```

**`LinearPMap.IsClosed.resolventSet_eq'`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L680).

> For a closed operator the resolvent set consists of those regular points for which
> the defect number is zero.

```lean
lemma IsClosed.resolventSet_eq' [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) :
    ρ T = T.regularityDomain ∩ T.defectNumber ⁻¹' {0}
```

**`LinearPMap.resolventSet_isOpen`**, a lemma, [line 690](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L690).

> The resolvent set is an open subset of ℂ.

```lean
lemma resolventSet_isOpen [CompleteSpace H] (T : H →ₗ.[ℂ] H) : IsOpen (ρ T)
```

### D.2. Spectrum

**`LinearPMap.spectrum`**, a def, [line 711](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L711).

> The spectrum, `σ`, of a partial linear map.
>
> `σ T` is the complement of `ρ T`. A complex number `z` is in `σ T` iff the linear map `T - z • 1`
> from `T.domain` to `H` fails to be bijective or `(T - z • 1)⁻¹` is not continuous
> (equivalently, is not bounded).

```lean
def spectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.spectrum_eq`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L716).

```lean
lemma spectrum_eq (T : H →ₗ.[ℂ] H) : σ T = (ρ T)ᶜ
```

**`LinearPMap.mem_spectrum_iff`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L718).

```lean
lemma mem_spectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ σ T ↔ (T - z • 1).toFun.ker ≠ ⊥ ∨ (T - z • 1).toFun.range ≠ ⊤ ∨ ¬Continuous (𝑅 T z)
```

**`LinearPMap.spectrum_eq_univ`**, a lemma, [line 723](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L723).

> If an operator is not closed then its spectrum is all of ℂ.

```lean
lemma spectrum_eq_univ [CompleteSpace H] {T : H →ₗ.[ℂ] H} (h : ¬T.IsClosed) : σ T = univ
```

**`LinearPMap.spectrum_isClosed`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L727).

> The spectrum is a closed subset of ℂ.

```lean
lemma spectrum_isClosed [CompleteSpace H] (T : H →ₗ.[ℂ] H) : _root_.IsClosed (σ T)
```

#### D.2.1. Point spectrum

**`LinearPMap.pointSpectrum`**, a def, [line 737](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L737).

> The point spectrum, `σᵖ`, of a partial linear map.
>
> A complex number `z` is in `σᵖ T` iff `T - z • 1` is not injective.

```lean
def pointSpectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.pointSpectrum_eq`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L742).

```lean
lemma pointSpectrum_eq (T : H →ₗ.[ℂ] H) : σᵖ T = {z | (T - z • 1).toFun.ker ≠ ⊥}
```

**`LinearPMap.mem_pointSpectrum_iff`**, a lemma, [line 744](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L744).

```lean
lemma mem_pointSpectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} : z ∈ σᵖ T ↔ (T - z • 1).toFun.ker ≠ ⊥
```

**`LinearPMap.IsEigenvector.mem_pointSpectrum`**, a lemma, [line 749](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L749).

> If `x` is an eigenvector of `T` with eigenvalue `c`, then `c` lies in the point spectrum
> of `T`.

```lean
lemma IsEigenvector.mem_pointSpectrum {T : H →ₗ.[ℂ] H} {x : T.domain} {c : ℂ}
    (hx : T.IsEigenvector x c) : c ∈ σᵖ T
```

**`LinearPMap.mem_range_sub_of_apply_eq`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L756).

> If `T x = c • x` and `c ≠ z`, then `x` lies in the range of `T - z • 1`.

```lean
lemma mem_range_sub_of_apply_eq {T : H →ₗ.[ℂ] H} {x : T.domain} {c z : ℂ}
    (hx : T x = c • (x : H)) (hcz : c ≠ z) : (x : H) ∈ (T - z • 1).toFun.range
```

**`LinearPMap.pointSpectrum_subset_spectrum`**, a lemma, [line 763](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L763).

```lean
lemma pointSpectrum_subset_spectrum (T : H →ₗ.[ℂ] H) : σᵖ T ⊆ σ T
```

#### D.2.2. Residual spectrum

**`LinearPMap.residualSpectrum`**, a def, [line 774](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L774).

> The residual spectrum, `σʳ`, of a partial linear map.
>
> A complex number `z` is in `σʳ T` iff `T - z • 1` is injective but not surjective
> and `(T - z • 1)⁻¹` is continuous (equivalently, bounded).

```lean
def residualSpectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.residualSpectrum_eq`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L780).

```lean
lemma residualSpectrum_eq (T : H →ₗ.[ℂ] H) :
    σʳ T = {z | (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range ≠ ⊤ ∧ Continuous (𝑅 T z)}
```

**`LinearPMap.mem_residualSpectrum_iff`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L784).

```lean
lemma mem_residualSpectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ σʳ T ↔ (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range ≠ ⊤ ∧ Continuous (𝑅 T z)
```

**`LinearPMap.residualSpectrum_subset_spectrum`**, a lemma, [line 788](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L788).

```lean
lemma residualSpectrum_subset_spectrum (T : H →ₗ.[ℂ] H) : σʳ T ⊆ σ T
```

**`LinearPMap.residualSpectrum_subset_regularityDomain`**, a lemma, [line 791](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L791).

```lean
lemma residualSpectrum_subset_regularityDomain (T : H →ₗ.[ℂ] H) : σʳ T ⊆ T.regularityDomain
```

#### D.2.3. Continuous spectrum

**`LinearPMap.continuousSpectrum`**, a def, [line 801](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L801).

> The continuous spectrum, `σᶜ`, of a partial linear map.
>
> A complex number `z` is in `σᶜ T` iff the range of `T - z • 1` is not closed.

```lean
def continuousSpectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.continuousSpectrum_eq`**, a lemma, [line 807](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L807).

```lean
lemma continuousSpectrum_eq (T : H →ₗ.[ℂ] H) :
    σᶜ T = {z | ¬_root_.IsClosed ((T - z • 1).toFun.range : Set H)}
```

**`LinearPMap.mem_continuousSpectrum_iff`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L810).

```lean
lemma mem_continuousSpectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ σᶜ T ↔ ¬_root_.IsClosed ((T - z • 1).toFun.range : Set H)
```

**`LinearPMap.continuousSpectrum_subset_spectrum`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L813).

```lean
lemma continuousSpectrum_subset_spectrum (T : H →ₗ.[ℂ] H) : σᶜ T ⊆ σ T
```

### D.3. Spectrum decomposition

**`LinearPMap.IsClosed.spectrum_eq`**, a lemma, [line 820](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L820).

```lean
lemma IsClosed.spectrum_eq [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) :
    σ T = σᵖ T ∪ σʳ T ∪ σᶜ T
```

**`LinearPMap.pointSpectrum_inter_residualSpectrum`**, a lemma, [line 838](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L838).

```lean
lemma pointSpectrum_inter_residualSpectrum (T : H →ₗ.[ℂ] H) : σᵖ T ∩ σʳ T = ∅
```

## E. Resolvent identities

**`LinearPMap.resolvent_sub`**, a lemma, [line 845](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L845).

```lean
lemma resolvent_sub
    {T₁ T₂ : H →ₗ.[ℂ] H} (hT : T₂.domain ≤ T₁.domain) {z : ℂ} (hz₁ : z ∈ ρ T₁) (hz₂ : z ∈ ρ T₂) :
    𝑅 T₁ z - 𝑅 T₂ z = 𝑅 T₁ z * (T₂ - T₁) * 𝑅 T₂ z
```

**`LinearPMap.resolvent_sub'`**, a lemma, [line 876](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L876).

```lean
lemma resolvent_sub' {T : H →ₗ.[ℂ] H} (z₁ z₂ : ℂ) (hz₁ : z₁ ∈ ρ T) (hz₂ : z₂ ∈ ρ T) :
    𝑅 T z₁ - 𝑅 T z₂ = (z₁ - z₂) • (𝑅 T z₁ * 𝑅 T z₂)
```

## Depends on

- [Unbounded operators (Basic)](../basic.md)
- [Eigenvectors of partial linear maps](../stateobservables-iseigenvector.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean)
