---
declaration: module
origin: cited
lean: LinearPMap.numericalRange_convex, LinearPMap.resolvent, LinearPMap.IsLowerBound, LinearPMap.isLowerBound_neg, LinearPMap.isLowerBound_of_right_le, LinearPMap.isLowerBound_of_left_le, LinearPMap.isLowerBound_closure, LinearPMap.regularityDomain
statement: formalized
proof: formalized
---

# Spectral theory for closed operators

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.Basic`, [Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean): 67 declarations, 28 with a docstring, 1 listed as significant; 1 private, not shown.

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
>     fails to be invertible.
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

**`LinearPMap.resolvent`**, an abbrev, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L106).

> The resolvent, `(T - z • 1)⁻¹`.

```lean
abbrev resolvent (T : H →ₗ.[ℂ] H) (z : ℂ) : H →ₗ.[ℂ] H
```

## A. Regularity domain

**`LinearPMap.IsLowerBound`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L116).

> `IsLowerBound T z c` is the property that `c * ‖x‖ ≤ ‖T x - z • x‖` for all `x : T.domain`.

```lean
def IsLowerBound (T : H →ₗ.[ℂ] H) (z : ℂ) (c : ℝ) : Prop
```

**`LinearPMap.isLowerBound_neg`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L118).

```lean
lemma isLowerBound_neg {T : H →ₗ.[ℂ] H} {z : ℂ} {c : ℝ} (h : IsLowerBound T z c) :
    IsLowerBound (-T) (-z) c
```

**`LinearPMap.isLowerBound_of_right_le`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L122).

```lean
lemma isLowerBound_of_right_le
    {T : H →ₗ.[ℂ] H} {z : ℂ} {c₁ c₂ : ℝ} (hle : c₁ ≤ c₂) (h : IsLowerBound T z c₂) :
    IsLowerBound T z c₁
```

**`LinearPMap.isLowerBound_of_left_le`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L127).

```lean
lemma isLowerBound_of_left_le
    {T₁ T₂ : H →ₗ.[ℂ] H} (hle : T₁ ≤ T₂) {z : ℂ} {c : ℝ} (h : IsLowerBound T₂ z c) :
    IsLowerBound T₁ z c
```

**`LinearPMap.isLowerBound_closure`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L132).

```lean
lemma isLowerBound_closure
    {T : H →ₗ.[ℂ] H} {z : ℂ} {c : ℝ} (h : IsLowerBound T z c) : IsLowerBound T.closure z c
```

**`LinearPMap.regularityDomain`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L149).

> The regular points for `T`.
>
> `z : ℂ` is a regular point for `T` iff there exists a constant `c > 0` such that
> `c * ‖x‖ ≤ ‖(T - z • 1) x‖` for all `x ∈ T.domain`.

```lean
def regularityDomain (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.regularityDomain_neg`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L152).

```lean
lemma regularityDomain_neg (T : H →ₗ.[ℂ] H) : (-T).regularityDomain = -T.regularityDomain
```

**`LinearPMap.regularityDomain_smul`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L159).

```lean
lemma regularityDomain_smul (T : H →ₗ.[ℂ] H) {w : ℂ} (hw : w ≠ 0) :
    (w • T).regularityDomain = w • T.regularityDomain
```

**`LinearPMap.regularityDomain_antitone`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L179).

> `T ≤ T'` implies `T'.regularityDomain ⊆ T.regularityDomain`.

```lean
lemma regularityDomain_antitone : Antitone (regularityDomain (H := H))
```

**`LinearPMap.mem_regularityDomain_iff`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L184).

> `z` is a regular point for `T` iff `T - z • 1` has
> a continuous (equivalently, bounded) inverse.

```lean
lemma mem_regularityDomain_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ T.regularityDomain ↔ (T - z • 1).toFun.ker = ⊥ ∧ Continuous (𝑅 T z)
```

**`LinearPMap.ball_subset_regularityDomain`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L214).

> The regularity domain of `T` contains open balls with radii controlled by the lower bounds.

```lean
lemma ball_subset_regularityDomain
    {T : H →ₗ.[ℂ] H} {z : ℂ} {c : ℝ} (h : IsLowerBound T z c) : ball z c ⊆ T.regularityDomain
```

**`LinearPMap.regularityDomain_isOpen`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L225).

> The regularity domain is an open set.

```lean
lemma regularityDomain_isOpen (T : H →ₗ.[ℂ] H) : IsOpen T.regularityDomain
```

**`LinearPMap.regularityDomain_closure`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L229).

> `T` and `T.closure` have the same regularity domain.

```lean
lemma regularityDomain_closure (T : H →ₗ.[ℂ] H) :
    T.closure.regularityDomain = T.regularityDomain
```

**`LinearPMap.IsClosable.closure_range_sub_eq_range_closure_sub`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L234).

```lean
lemma IsClosable.closure_range_sub_eq_range_closure_sub [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosable) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    (T - z • 1).toFun.range.closure = (T.closure - z • 1).toFun.range
```

**`LinearPMap.IsClosed.sub_range_isClosed`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L275).

```lean
lemma IsClosed.sub_range_isClosed [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    _root_.IsClosed ((T - z • 1).toFun.range : Set H)
```

**`LinearPMap.IsUnbounded.orthogonal_closure_sub_range`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L281).

> `(T.closure - z • 1).rangeᗮ = (T† - conj z • 1).ker`

```lean
lemma IsUnbounded.orthogonal_closure_sub_range [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsUnbounded) (z : ℂ) :
    (T.closure - z • 1).toFun.rangeᗮ
      = (T† - conj z • 1).toFun.ker.map (T† - conj z • 1).domain.subtype
```

**`LinearPMap.IsUnbounded.orthogonal_adjoint_sub_ker`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L295).

> `(T† - conj z • 1).kerᗮ = (T.closure - z • 1).range`

```lean
lemma IsUnbounded.orthogonal_adjoint_sub_ker [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsUnbounded) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    ((T† - conj z • 1).toFun.ker.map (T† - conj z • 1).domain.subtype)ᗮ
      = (T.closure - z • 1).toFun.range
```

## B. Deficiency subspace & defect number

**`LinearPMap.deficiencySubspace`**, a def, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L312).

> For a partial linear map `T` and any complex number `z`, the closed submodule which
> is orthogonal to the range of `T - z • 1`.
>
> `T.defectNumber z` is defined as the rank of this subspace.

```lean
def deficiencySubspace (T : H →ₗ.[ℂ] H) (z : ℂ) : ClosedSubmodule ℂ H
```

**`LinearPMap.deficiencySubspace_coe`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L316).

```lean
lemma deficiencySubspace_coe (T : H →ₗ.[ℂ] H) (z : ℂ) :
    T.deficiencySubspace z = (T - z • 1).toFun.rangeᗮ
```

**`LinearPMap.defectNumber`**, a def, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L320).

> The rank of `T.deficiencySubspace z = (T - z • 1).rangeᗮ`.

```lean
def defectNumber (T : H →ₗ.[ℂ] H) (z : ℂ) : Cardinal
```

**`LinearPMap.defectNumber_eq`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L322).

```lean
lemma defectNumber_eq (T : H →ₗ.[ℂ] H) (z : ℂ) :
    T.defectNumber z = Module.rank ℂ (T.deficiencySubspace z)
```

**`LinearPMap.IsClosed.defectNumber_eq_zero_iff`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L325).

```lean
lemma IsClosed.defectNumber_eq_zero_iff [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) {z : ℂ} (hz : z ∈ T.regularityDomain) :
    T.defectNumber z = 0 ↔ (T - z • 1).toFun.range = ⊤
```

**`LinearPMap.defectNumber_closure`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L332).

> `T` and `T.closure` have the same defect number at points in their regularity domain.

```lean
lemma defectNumber_closure [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} {z : ℂ} (hz : z ∈ T.regularityDomain) :
    T.closure.defectNumber z = T.defectNumber z
```

**`Submodule.inf_ne_bot_of_rank_lt`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L340).

```lean
lemma _root_.Submodule.inf_ne_bot_of_rank_lt
    {E F : Submodule ℂ H} [E.HasOrthogonalProjection] (h_rank : Module.rank ℂ E < Module.rank ℂ F) :
    Eᗮ ⊓ F ≠ ⊥
```

**`LinearPMap.IsClosed.exists_inner_eq_zero_of_defectNumber_lt`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L353).

```lean
lemma IsClosed.exists_inner_eq_zero_of_defectNumber_lt [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosed)
    {z₁ z₂ : ℂ} (hz₁ : z₁ ∈ T.regularityDomain) (h : T.defectNumber z₁ < T.defectNumber z₂) :
    ∃ x : T.domain, x ≠ 0 ∧ ⟪T x - z₁ • x, T x - z₂ • x⟫_ℂ = 0
```

**`LinearPMap.IsClosable.defectNumber_eq_of_mem_ball`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L367).

```lean
lemma IsClosable.defectNumber_eq_of_mem_ball [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosable)
    {z₁ z₂ : ℂ} {c : ℝ} (h : IsLowerBound T z₁ c) (h_ball : z₂ ∈ ball z₁ c) :
    T.defectNumber z₁ = T.defectNumber z₂
```

**`LinearPMap.IsClosable.defectNumber_const`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L395).

> The defect number is constant on each connected component of the regularity domain.

```lean
lemma IsClosable.defectNumber_const [CompleteSpace H]
    {T : H →ₗ.[ℂ] H} (hT : T.IsClosable)
    {z₁ z₂ : ℂ} (hz : z₂ ∈ connectedComponentIn T.regularityDomain z₁) :
    T.defectNumber z₁ = T.defectNumber z₂
```

## C. Numerical range

**`LinearPMap.numericalRange`**, a def, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L459).

> The set `{⟪x, T x⟫_ℂ | x ∈ T.domain ∧ ‖x‖ = 1} ⊆ ℂ`.

```lean
def numericalRange (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.numericalRange_eq`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L464).

```lean
lemma numericalRange_eq (T : H →ₗ.[ℂ] H) : Θ T = (fun x ↦ ⟪↑x, T x⟫_ℂ) '' {x | ‖x‖ = 1}
```

**`LinearPMap.mem_numericalRange`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L466).

```lean
lemma mem_numericalRange {T : H →ₗ.[ℂ] H} {x : T.domain} (hx : x ≠ 0) :
    (‖x‖ ^ 2)⁻¹ * ⟪↑x, T x⟫_ℂ ∈ Θ T
```

**`LinearPMap.numericalRange_nonempty`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L472).

```lean
lemma numericalRange_nonempty {T : H →ₗ.[ℂ] H} (hT : T.domain ≠ ⊥) : (Θ T).Nonempty
```

**`LinearPMap.numericalRange_neg`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L477).

```lean
lemma numericalRange_neg (T : H →ₗ.[ℂ] H) : Θ (-T) = -Θ T
```

**`LinearPMap.numericalRange_smul`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L482).

```lean
lemma numericalRange_smul (T : H →ₗ.[ℂ] H) (c : ℂ) : Θ (c • T) = c • Θ T
```

**`LinearPMap.numericalRange_sub_const`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L486).

```lean
lemma numericalRange_sub_const (T : H →ₗ.[ℂ] H) (c : ℂ) : Θ (T - c • 1) = Θ T - {c}
```

**`LinearPMap.compl_closure_numericalRange_subset_regularityDomain`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L498).

> The regularity domain contains the exterior of the numerical range.

```lean
lemma compl_closure_numericalRange_subset_regularityDomain (T : H →ₗ.[ℂ] H) :
    (_root_.closure (Θ T))ᶜ ⊆ T.regularityDomain
```

### C.1. The Toeplitz-Hausdorff theorem

**`LinearPMap.numericalRange_convex`**, a theorem, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L544). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Toeplitz-Hausdorff theorem.

```lean
theorem numericalRange_convex (T : H →ₗ.[ℂ] H) : Convex ℝ (Θ T)
```

## D. Spectrum of a closed operator

### D.1. Resolvent set

**`LinearPMap.resolventSet`**, a def, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L630).

> The resolvent set, `ρ`, of a partial linear map.
>
> A complex number `z` is in `ρ T` iff the linear map `T - z • 1` from `T.domain` to `H`
> is a bijection with continuous (equivalently, bounded) inverse.

```lean
def resolventSet (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.resolventSet_eq`**, a lemma, [line 636](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L636).

```lean
lemma resolventSet_eq (T : H →ₗ.[ℂ] H) :
    ρ T = {z | (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range = ⊤ ∧ Continuous (𝑅 T z)}
```

**`LinearPMap.mem_resolventSet_iff`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L640).

```lean
lemma mem_resolventSet_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ ρ T ↔ (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range = ⊤ ∧ Continuous (𝑅 T z)
```

**`LinearPMap.resolventSet_eq_empty`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L645).

> If an operator is not closed then its resolvent set is empty.

```lean
lemma resolventSet_eq_empty [CompleteSpace H] {T : H →ₗ.[ℂ] H} (h : ¬T.IsClosed) : ρ T = ∅
```

**`LinearPMap.resolventSet_subset_regularityDomain`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L655).

```lean
lemma resolventSet_subset_regularityDomain (T : H →ₗ.[ℂ] H) : ρ T ⊆ T.regularityDomain
```

**`LinearPMap.IsClosed.resolventSet_eq`**, a lemma, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L660).

> For a closed operator the continuity of the resolvent is redundant
> in the definition of the resolvent set.

```lean
lemma IsClosed.resolventSet_eq [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) :
    ρ T = {z : ℂ | (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range = ⊤}
```

**`LinearPMap.IsClosed.resolventSet_eq'`**, a lemma, [line 672](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L672).

> For a closed operator the resolvent set consists of those regular points for which
> the defect number is zero.

```lean
lemma IsClosed.resolventSet_eq' [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) :
    ρ T = T.regularityDomain ∩ T.defectNumber ⁻¹' {0}
```

**`LinearPMap.resolventSet_isOpen`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L682).

> The resolvent set is an open subset of ℂ.

```lean
lemma resolventSet_isOpen [CompleteSpace H] (T : H →ₗ.[ℂ] H) : IsOpen (ρ T)
```

### D.2. Spectrum

**`LinearPMap.spectrum`**, a def, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L703).

> The spectrum, `σ`, of a partial linear map.
>
> `σ T` is the complement of `ρ T`. A complex number `z` is in `σ T` iff the linear map `T - z • 1`
> from `T.domain` to `H` fails to be bijective or `(T - z • 1)⁻¹` is not continuous
> (equivalently, is not bounded).

```lean
def spectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.spectrum_eq`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L708).

```lean
lemma spectrum_eq (T : H →ₗ.[ℂ] H) : σ T = (ρ T)ᶜ
```

**`LinearPMap.mem_spectrum_iff`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L710).

```lean
lemma mem_spectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ σ T ↔ (T - z • 1).toFun.ker ≠ ⊥ ∨ (T - z • 1).toFun.range ≠ ⊤ ∨ ¬Continuous (𝑅 T z)
```

**`LinearPMap.spectrum_eq_univ`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L715).

> If an operator is not closed then its spectrum is all of ℂ.

```lean
lemma spectrum_eq_univ [CompleteSpace H] {T : H →ₗ.[ℂ] H} (h : ¬T.IsClosed) : σ T = univ
```

**`LinearPMap.spectrum_isClosed`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L719).

> The spectrum is a closed subset of ℂ.

```lean
lemma spectrum_isClosed [CompleteSpace H] (T : H →ₗ.[ℂ] H) : _root_.IsClosed (σ T)
```

#### D.2.1. Point spectrum

**`LinearPMap.pointSpectrum`**, a def, [line 729](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L729).

> The point spectrum, `σᵖ`, of a partial linear map.
>
> A complex number `z` is in `σᵖ T` iff `T - z • 1` is not injective.

```lean
def pointSpectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.pointSpectrum_eq`**, a lemma, [line 734](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L734).

```lean
lemma pointSpectrum_eq (T : H →ₗ.[ℂ] H) : σᵖ T = {z | (T - z • 1).toFun.ker ≠ ⊥}
```

**`LinearPMap.mem_pointSpectrum_iff`**, a lemma, [line 736](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L736).

```lean
lemma mem_pointSpectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} : z ∈ σᵖ T ↔ (T - z • 1).toFun.ker ≠ ⊥
```

**`LinearPMap.pointSpectrum_subset_spectrum`**, a lemma, [line 739](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L739).

```lean
lemma pointSpectrum_subset_spectrum (T : H →ₗ.[ℂ] H) : σᵖ T ⊆ σ T
```

#### D.2.2. Residual spectrum

**`LinearPMap.residualSpectrum`**, a def, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L750).

> The residual spectrum, `σʳ`, of a partial linear map.
>
> A complex number `z` is in `σʳ T` iff `T - z • 1` is injective but not surjective
> and `(T - z • 1)⁻¹` is continuous (equivalently, bounded).

```lean
def residualSpectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.residualSpectrum_eq`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L756).

```lean
lemma residualSpectrum_eq (T : H →ₗ.[ℂ] H) :
    σʳ T = {z | (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range ≠ ⊤ ∧ Continuous (𝑅 T z)}
```

**`LinearPMap.mem_residualSpectrum_iff`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L760).

```lean
lemma mem_residualSpectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ σʳ T ↔ (T - z • 1).toFun.ker = ⊥ ∧ (T - z • 1).toFun.range ≠ ⊤ ∧ Continuous (𝑅 T z)
```

**`LinearPMap.residualSpectrum_subset_spectrum`**, a lemma, [line 764](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L764).

```lean
lemma residualSpectrum_subset_spectrum (T : H →ₗ.[ℂ] H) : σʳ T ⊆ σ T
```

**`LinearPMap.residualSpectrum_subset_regularityDomain`**, a lemma, [line 767](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L767).

```lean
lemma residualSpectrum_subset_regularityDomain (T : H →ₗ.[ℂ] H) : σʳ T ⊆ T.regularityDomain
```

#### D.2.3. Continuous spectrum

**`LinearPMap.continuousSpectrum`**, a def, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L777).

> The continuous spectrum, `σᶜ`, of a partial linear map.
>
> A complex number `z` is in `σᶜ T` iff the range of `T - z • 1` is not closed.

```lean
def continuousSpectrum (T : H →ₗ.[ℂ] H) : Set ℂ
```

**`LinearPMap.continuousSpectrum_eq`**, a lemma, [line 783](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L783).

```lean
lemma continuousSpectrum_eq (T : H →ₗ.[ℂ] H) :
    σᶜ T = {z | ¬_root_.IsClosed ((T - z • 1).toFun.range : Set H)}
```

**`LinearPMap.mem_continuousSpectrum_iff`**, a lemma, [line 786](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L786).

```lean
lemma mem_continuousSpectrum_iff {T : H →ₗ.[ℂ] H} {z : ℂ} :
    z ∈ σᶜ T ↔ ¬_root_.IsClosed ((T - z • 1).toFun.range : Set H)
```

**`LinearPMap.continuousSpectrum_subset_spectrum`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L789).

```lean
lemma continuousSpectrum_subset_spectrum (T : H →ₗ.[ℂ] H) : σᶜ T ⊆ σ T
```

### D.3. Spectrum decomposition

**`LinearPMap.IsClosed.spectrum_eq`**, a lemma, [line 796](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L796).

```lean
lemma IsClosed.spectrum_eq [CompleteSpace H] {T : H →ₗ.[ℂ] H} (hT : T.IsClosed) :
    σ T = σᵖ T ∪ σʳ T ∪ σᶜ T
```

**`LinearPMap.pointSpectrum_inter_residualSpectrum`**, a lemma, [line 814](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L814).

```lean
lemma pointSpectrum_inter_residualSpectrum (T : H →ₗ.[ℂ] H) : σᵖ T ∩ σʳ T = ∅
```

## E. Resolvent identities

**`LinearPMap.resolvent_sub`**, a lemma, [line 821](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L821).

```lean
lemma resolvent_sub
    {T₁ T₂ : H →ₗ.[ℂ] H} (hT : T₂.domain ≤ T₁.domain) {z : ℂ} (hz₁ : z ∈ ρ T₁) (hz₂ : z ∈ ρ T₂) :
    𝑅 T₁ z - 𝑅 T₂ z = 𝑅 T₁ z * (T₂ - T₁) * 𝑅 T₂ z
```

**`LinearPMap.resolvent_sub'`**, a lemma, [line 852](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean#L852).

```lean
lemma resolvent_sub' {T : H →ₗ.[ℂ] H} (z₁ z₂ : ℂ) (hz₁ : z₁ ∈ ρ T) (hz₂ : z₂ ∈ ρ T) :
    𝑅 T z₁ - 𝑅 T z₂ = (z₁ - z₂) • (𝑅 T z₁ * 𝑅 T z₂)
```

## Depends on

- [Unbounded operators (Operators/Unbounded)](../unbounded.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/Basic.lean)
