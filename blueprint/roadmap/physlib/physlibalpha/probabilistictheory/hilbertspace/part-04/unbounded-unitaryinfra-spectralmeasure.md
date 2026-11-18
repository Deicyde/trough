---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux, ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux_inner, ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator, ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_inner, ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_apply_eq_zero_of_not_measurableSet, ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_eq_negI_smul, ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_conj_symm, ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_isSelfAdjoint
statement: formalized
proof: formalized
---

# The spectral measure of a bounded normal operator

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.UnitaryInfra.SpectralMeasure`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean): 48 declarations, 26 with a docstring.

> The projection-valued spectral measure `E` of a bounded normal operator `U`, built from its CFC.

## i. Overview

> The sesquilinear form of the indicator of a Borel set `S` is represented by an operator `E(S)`.
> These operators are projections, countably additive in the weak operator topology, and commute with
> every operator commuting with `U` and `U⋆`. They form the spectral measure of `U`, whose integral of
> the identity is `U`.

## ii. Key results

> - `cfcSpectralOperator` : the operator `E(S)`.
> - `cfcSpectralOperator_isSelfAdjoint` : each `E(S)` is self-adjoint.
> - `cfcSpectralOperator_isStarProjection` : each `E(S)` is an orthogonal projection.
> - `cfcSpectralVectorMeasure` : `E` as a vector measure in the weak operator topology.
> - `cfcSpectralMeasure` : the spectral measure of a bounded normal operator.
> - `cfcSpectralMeasure_reconstruction` : integrating a real continuous `f` against `E` gives `f(U)`.
> - `cfcSpectralMeasure_commute_of_commute_unitary` : `E` commutes with unitaries commuting with
>   `U` and `U⋆`.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L66).

> The Riesz-represented operator at the measurable set `S`.

```lean
noncomputable def cfcSpectralOperatorAux (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) :
    H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux_inner`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L70).

```lean
lemma cfcSpectralOperatorAux_inner (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) (x y : H) :
    ⟪y, cfcSpectralOperatorAux U hU S hS x⟫_ℂ =
      polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L81).

> The Riesz-represented operator on every set, `0` off the measurable sets so that this
> directly matches `MeasureTheory.VectorMeasure`'s `not_measurable'` convention.

```lean
noncomputable def cfcSpectralOperator (S : Set (spectrum ℂ U)) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_inner`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L84).

```lean
lemma cfcSpectralOperator_inner (S : Set (spectrum ℂ U)) (x y : H) :
    ⟪y, cfcSpectralOperator U hU S x⟫_ℂ = polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_apply_eq_zero_of_not_measurableSet`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L91).

```lean
lemma cfcSpectralOperator_apply_eq_zero_of_not_measurableSet {S : Set (spectrum ℂ U)}
    (hS : ¬MeasurableSet S) : cfcSpectralOperator U hU S = 0
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_eq_negI_smul`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L99).

> The `Complex.I`-inversion companion of `cfcScalarMeasure_real_I_smul`: rewrites a Riesz
> measure at `v` as the Riesz measure at `(-I) • v`.  This is the algebraic engine behind
> Hermitian symmetry of the polarized measure below.

```lean
lemma cfcScalarMeasure_real_eq_negI_smul (v : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU v).real S = (cfcScalarMeasure U hU ((-Complex.I) • v)).real S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_conj_symm`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L110).

> Hermitian symmetry of the polarized measure: `B(y,x,S) = conj (B(x,y,S))`, matching the
> convention that `B` is exactly `⟪y, cfcRealOperator U hU f x⟫` in the limit and inner products
> are conjugate-symmetric.  This is the input `cfcSpectralOperator_isSelfAdjoint` needs.

```lean
lemma polarizedCfcScalarMeasure_conj_symm (x y : H) (S : Set (spectrum ℂ U)) :
    polarizedCfcScalarMeasure (hU := hU) U y x S =
      starRingEnd ℂ (polarizedCfcScalarMeasure (hU := hU) U x y S)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_isSelfAdjoint`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L143).

> `cfcSpectralOperator U hU S` is self-adjoint, for every `S` (measurable or not — the
> non-measurable case is trivial since the operator is `0`).  This follows from
> `polarizedCfcScalarMeasure_conj_symm` via `LinearMap.IsSymmetric`.

```lean
lemma cfcSpectralOperator_isSelfAdjoint (S : Set (spectrum ℂ U)) :
    IsSelfAdjoint (cfcSpectralOperator U hU S)
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_univ`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L152).

> The polarized measure of the whole spectrum is `⟪y, x⟫`.

```lean
lemma polarizedCfcScalarMeasure_univ (x y : H) :
    polarizedCfcScalarMeasure (hU := hU) U x y Set.univ = ⟪y, x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_univ_apply`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L166).

```lean
lemma cfcSpectralOperator_univ_apply (x : H) :
    cfcSpectralOperator U hU Set.univ x = x
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_univ`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L173).

```lean
lemma cfcSpectralOperator_univ : cfcSpectralOperator U hU Set.univ = 1
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_inner_self`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L178).

> On the diagonal, `⟪x, E(S) x⟫` is the diagonal measure of `S`.

```lean
lemma cfcSpectralOperator_inner_self {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) (x : H) :
    ⟪x, cfcSpectralOperator U hU S x⟫_ℂ = ((cfcScalarMeasure U hU x).real S : ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_reApplyInnerSelf`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L202).

> `reApplyInnerSelf` version of `cfcSpectralOperator_inner_self`, in the exact shape
> `ContinuousLinearMap.IsPositive` consumes.

```lean
lemma cfcSpectralOperator_reApplyInnerSelf {S : Set (spectrum ℂ U)} (hS : MeasurableSet S)
    (x : H) :
    (cfcSpectralOperator U hU S).reApplyInnerSelf x = (cfcScalarMeasure U hU x).real S
```

## A. Order properties of the spectral operators

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_isPositive`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L212).

> `cfcSpectralOperator U hU S` is a positive operator, for measurable `S`.

```lean
lemma cfcSpectralOperator_isPositive {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) :
    ContinuousLinearMap.IsPositive (cfcSpectralOperator U hU S)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_nonneg`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L219).

```lean
lemma cfcSpectralOperator_nonneg {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) :
    0 ≤ cfcSpectralOperator U hU S
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_mono`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L225).

> `cfcSpectralOperator U hU S` is monotone in `S`, for measurable sets, in the Loewner order on
> `H →L[ℂ] H`.

```lean
lemma cfcSpectralOperator_mono {S T : Set (spectrum ℂ U)} (hS : MeasurableSet S)
    (hT : MeasurableSet T) (hST : S ⊆ T) :
    cfcSpectralOperator U hU S ≤ cfcSpectralOperator U hU T
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_le_one`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L243).

```lean
lemma cfcSpectralOperator_le_one {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) :
    cfcSpectralOperator U hU S ≤ 1
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_empty`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L248).

```lean
lemma cfcSpectralOperator_empty : cfcSpectralOperator U hU ∅ = 0
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_add_of_disjoint`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L256).

> Finite additivity of `cfcSpectralOperator` on disjoint measurable sets.

```lean
lemma cfcSpectralOperator_add_of_disjoint {S T : Set (spectrum ℂ U)} (hS : MeasurableSet S)
    (hT : MeasurableSet T) (hdisj : Disjoint S T) :
    cfcSpectralOperator U hU (S ∪ T) = cfcSpectralOperator U hU S + cfcSpectralOperator U hU T
```

## B. Weak countable additivity

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasureFun`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L269).

> The operator at `S`, valued in the weak-operator-topology type.

```lean
noncomputable def cfcSpectralMeasureFun (S : Set (spectrum ℂ U)) : H →WOT[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasureFun_inner`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L273).

```lean
lemma cfcSpectralMeasureFun_inner (S : Set (spectrum ℂ U)) (x y : H) :
    ⟪y, cfcSpectralMeasureFun U hU S x⟫_ℂ = polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralVectorMeasure`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L279).

> The operators `E(S)`, as a vector measure in the weak operator topology.

```lean
noncomputable def cfcSpectralVectorMeasure :
    VectorMeasure (spectrum ℂ U) (H →WOT[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralVectorMeasure_apply`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L303).

```lean
lemma cfcSpectralVectorMeasure_apply (S : Set (spectrum ℂ U)) :
    cfcSpectralVectorMeasure U hU S = cfcSpectralMeasureFun U hU S
```

## C. The spectral operators are projections

> For a compact set `K` and an open `V ⊇ K`, a Urysohn function `f` gives `E(K) ≤ f(U) ≤ E(V)`. With
> the estimate `‖A x‖² ≤ re ⟪x, A x⟫` for `0 ≤ A ≤ 1` and outer regularity this shows `E(K)² = E(K)`.
> Inner regularity extends it to measurable sets, and multiplicativity on intersections follows from
> additivity.

**`ProbabilisticTheory.QuantumMechanics.measureReal_compact_le_integral_of_eqOn_one`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L322).

> A compactly supported continuous function that is `1` on a compact set `K` has integral at least
> the measure of `K`.

```lean
lemma measureReal_compact_le_integral_of_eqOn_one
    (μ : Measure X) [IsFiniteMeasure μ] {K : Set X} (hK : IsCompact K)
    (f : CompactlySupportedContinuousMap X ℝ) (hfK : Set.EqOn f 1 K)
    (hf0 : ∀ x, 0 ≤ f x) :
    μ.real K ≤ ∫ x, f x ∂μ
```

**`ProbabilisticTheory.QuantumMechanics.integral_le_measureReal_of_support_subset`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L341).

> A `[0, 1]`-valued compactly supported continuous function supported in an open set `V` has
> integral at most the measure of `V`.

```lean
lemma integral_le_measureReal_of_support_subset
    (μ : Measure X) [IsFiniteMeasure μ] {V : Set X} (hV : IsOpen V)
    (f : CompactlySupportedContinuousMap X ℝ) (hfV : tsupport f ⊆ V)
    (hf : ∀ x, f x ∈ Set.Icc 0 1) :
    (∫ x, f x ∂μ) ≤ μ.real V
```

**`ProbabilisticTheory.QuantumMechanics.integral_le_measureReal_of_le_indicator`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L358).

```lean
lemma integral_le_measureReal_of_le_indicator
    (μ : Measure X) [IsFiniteMeasure μ] {D : Set X} (hD : MeasurableSet D)
    (f : CompactlySupportedContinuousMap X ℝ) (_hf : ∀ x, 0 ≤ f x)
    (hfd : ∀ x, f x ≤ D.indicator 1 x) :
    (∫ x, f x ∂μ) ≤ μ.real D
```

**`ProbabilisticTheory.QuantumMechanics.measureReal_lt_of_measure_lt_of_pos`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L375).

```lean
lemma measureReal_lt_of_measure_lt_of_pos
    (μ : Measure X) [IsFiniteMeasure μ] {S : Set X} {ε : ℝ} (hε : 0 < ε)
    (hμε : μ S < ENNReal.ofReal ε) : μ.real S < ε
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux_nonneg`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L382).

```lean
lemma cfcSpectralOperatorAux_nonneg {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) :
    0 ≤ cfcSpectralOperatorAux U hU S hS
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux_le_one`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L386).

```lean
lemma cfcSpectralOperatorAux_le_one {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) :
    cfcSpectralOperatorAux U hU S hS ≤ 1
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux_mono`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L390).

```lean
lemma cfcSpectralOperatorAux_mono {S T : Set (spectrum ℂ U)} (hS : MeasurableSet S)
    (hT : MeasurableSet T) (hST : S ⊆ T) :
    cfcSpectralOperatorAux U hU S hS ≤ cfcSpectralOperatorAux U hU T hT
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator_reApplyInnerSelf`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L395).

```lean
lemma cfcRealOperator_reApplyInnerSelf
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (x : H) :
    (cfcRealOperator U hU f).reApplyInnerSelf x =
      ∫ z, f z ∂cfcScalarMeasure U hU x
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_le_cfcRealOperator_of_compact_subset_open`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L402).

```lean
lemma cfcSpectralOperator_le_cfcRealOperator_of_compact_subset_open
    {K V : Set (spectrum ℂ U)} (hK : IsCompact K) (_hV : IsOpen V) (_hKV : K ⊆ V)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ)
    (hfK : Set.EqOn f 1 K) (_hfV : tsupport f ⊆ V) (hf : ∀ z, f z ∈ Set.Icc 0 1) :
    cfcSpectralOperator U hU K ≤ cfcRealOperator U hU f
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator_le_cfcSpectralOperator_of_support_subset`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L417).

```lean
lemma cfcRealOperator_le_cfcSpectralOperator_of_support_subset
    {V : Set (spectrum ℂ U)} (hV : IsOpen V)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ)
    (hfV : tsupport f ⊆ V) (hf : ∀ z, f z ∈ Set.Icc 0 1) :
    cfcRealOperator U hU f ≤ cfcSpectralOperator U hU V
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator_mul_self`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L433).

```lean
lemma cfcRealOperator_mul_self
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    cfcRealOperator U hU (f * f) = cfcRealOperator U hU f * cfcRealOperator U hU f
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator_sub_mul_self`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L443).

```lean
lemma cfcRealOperator_sub_mul_self
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    cfcRealOperator U hU (f - f * f) =
      cfcRealOperator U hU f - cfcRealOperator U hU f * cfcRealOperator U hU f
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_isIdempotent_of_isCompact`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L458).

```lean
lemma cfcSpectralOperator_isIdempotent_of_isCompact
    {K : Set (spectrum ℂ U)} (hK : IsCompact K) :
    IsIdempotentElem (cfcSpectralOperator U hU K)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperatorAux_isIdempotentElem`**, a lemma, [line 692](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L692).

> **`E(S)` is idempotent.** For compact `S` this follows from a Urysohn function between `S` and
> an open neighbourhood, using `0 ≤ A ≤ 1 ⟹ ‖A x‖² ≤ re ⟪x, A x⟫`; inner regularity extends it to
> measurable `S`.

```lean
lemma cfcSpectralOperatorAux_isIdempotentElem (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) :
    cfcSpectralOperatorAux U hU S hS * cfcSpectralOperatorAux U hU S hS =
      cfcSpectralOperatorAux U hU S hS
```

> The idempotency proof above is the reusable order/regularity construction.  It first proves
> the compact case with an Urysohn cutoff and outer regularity, then approximates an arbitrary
> measurable set from inside by compact sets.  The only analytic estimate is the positive
> contraction inequality `0 ≤ A ≤ 1 ⟹ ‖A x‖² ≤ re ⟪x, A x⟫`; no weak/strong operator topology
> argument or multiplication of operator limits is involved.

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_isIdempotentElem`**, a lemma, [line 817](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L817).

> Idempotency of `cfcSpectralOperator` on every set — `0` (hence trivially idempotent) off the
> measurable sets, and the order/regularity theorem above on measurable sets.

```lean
lemma cfcSpectralOperator_isIdempotentElem (S : Set (spectrum ℂ U)) :
    IsIdempotentElem (cfcSpectralOperator U hU S)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_isStarProjection`**, a lemma, [line 826](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L826).

> `cfcSpectralOperator U hU S` is a star-projection, for every `S`; both self-adjointness and
> idempotency are proved.

```lean
lemma cfcSpectralOperator_isStarProjection (S : Set (spectrum ℂ U)) :
    IsStarProjection (cfcSpectralOperator U hU S)
```

## D. The spectral measure

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure`**, a def, [line 835](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L835).

> **The weak-operator spectral measure of a bounded normal operator.**  Assembled from the
> Riesz-represented, weakly σ-additive family `cfcSpectralOperator` (Steps B–C, fully proved) and
> the star-projection property (Step D), including the order/regularity proof of idempotency.

```lean
noncomputable def cfcSpectralMeasure : QuantumMechanics.WOTSpectralMeasure (spectrum ℂ U) H
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure_apply`**, a lemma, [line 855](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L855).

```lean
lemma cfcSpectralMeasure_apply (S : Set (spectrum ℂ U)) :
    cfcSpectralMeasure U hU S = cfcSpectralMeasureFun U hU S
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure_scalarMeasure`**, a lemma, [line 860](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L860).

> The scalar measure attached to `cfcSpectralMeasure` is exactly the polarized Riesz measure it
> was built from.

```lean
lemma cfcSpectralMeasure_scalarMeasure (x y : H) :
    (cfcSpectralMeasure U hU).scalarMeasure x y = polarizedCfcScalarMeasure (hU := hU) U x y
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure_reconstruction`**, a lemma, [line 869](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L869).

> **The spectral measure reconstructs the functional calculus**: integrating a continuous function
> `f` gives `f(U)`.

```lean
lemma cfcSpectralMeasure_reconstruction
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (x y : H) :
    (cfcSpectralMeasure U hU).complexWeakIntegral (fun z => (f z : ℂ)) x y =
      ⟪y, cfcRealOperator U hU f x⟫_ℂ
```

## E. Commutation with the commutant

> An operator commuting with `U` and `U⋆` commutes with `f(U)` for continuous `f`, and by uniqueness
> in the Riesz–Markov–Kakutani theorem with every spectral projection of `U`.

**`ProbabilisticTheory.QuantumMechanics.commute_cfcRealOperator`**, a lemma, [line 884](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L884).

> An operator commuting with `U` and `star U` commutes with the continuous functional calculus
> of `U` at every real test function.

```lean
lemma commute_cfcRealOperator {T : H →L[ℂ] H} (hTU : Commute U T) (hTU' : Commute (star U) T)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    Commute (cfcRealOperator U hU f) T
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_eq_of_commute_isometry`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L892).

> If `T` is an isometry (`star T * T = 1`) commuting with `U` and `star U`, the vector-state
> Riesz measure at `T v` agrees with the one at `v`: an isometric intertwiner of `U` leaves the
> diagonal spectral measure unchanged.

```lean
lemma cfcScalarMeasure_eq_of_commute_isometry
    {T : H →L[ℂ] H} (hTU : Commute U T) (hTU' : Commute (star U) T)
    (hTiso : star T * T = 1) (v : H) :
    cfcScalarMeasure U hU (T v) = cfcScalarMeasure U hU v
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_eq_of_commute_unitary`**, a lemma, [line 918](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L918).

> If `T` is unitary and commutes with `U` and `star U`, the polarized Riesz measure intertwines:
> testing at `(T x, y)` matches testing at `(x, star T y)`.  This is the sesquilinear form of the
> commutation identity, and is exactly what `cfcSpectralOperator_inner` needs to see commutation of
> each spectral projection with `T`.

```lean
lemma polarizedCfcScalarMeasure_eq_of_commute_unitary
    {T : H →L[ℂ] H} (hTU : Commute U T) (hTU' : Commute (star U) T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (x y : H) :
    polarizedCfcScalarMeasure (hU := hU) U (T x) y =
      polarizedCfcScalarMeasure (hU := hU) U x (star T y)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralOperator_commute_of_commute_unitary`**, a lemma, [line 947](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L947).

> Every spectral operator `cfcSpectralOperator U hU S` commutes with any unitary intertwiner of
> `U` (i.e. any unitary commuting with both `U` and `star U`).  Holds for *every* `S`, measurable or
> not, since `cfcSpectralOperator_inner` itself needs no measurability hypothesis.

```lean
lemma cfcSpectralOperator_commute_of_commute_unitary
    {T : H →L[ℂ] H} (hTU : Commute U T) (hTU' : Commute (star U) T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (S : Set (spectrum ℂ U)) :
    cfcSpectralOperator U hU S * T = T * cfcSpectralOperator U hU S
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure_commute_of_commute_unitary`**, a lemma, [line 965](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean#L965).

> The weak-operator spectral measure `cfcSpectralMeasure U hU` commutes with any unitary
> intertwiner of `U`, at every set (measurable or not).

```lean
lemma cfcSpectralMeasure_commute_of_commute_unitary
    {T : H →L[ℂ] H} (hTU : Commute U T) (hTU' : Commute (star U) T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (S : Set (spectrum ℂ U)) :
    cfcSpectralMeasure U hU S * ContinuousLinearMapWOT.ofCLM T =
      ContinuousLinearMapWOT.ofCLM T * cfcSpectralMeasure U hU S
```

## Depends on

- [The spectral forms of a bounded normal operator](unbounded-unitaryinfra-sesquilinearform.md)
- [The vector-measure integral against a scalar matrix coefficient](../part-02/unbounded-weakintegral.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SpectralMeasure.lean)
