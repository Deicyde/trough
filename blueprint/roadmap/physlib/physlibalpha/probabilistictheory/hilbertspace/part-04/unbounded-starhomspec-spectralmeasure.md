---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux, ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux_inner, ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator, ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_inner, ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_apply_eq_zero_of_not_measurableSet, ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_eq_negI_smul, ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_conj_symm, ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_isSelfAdjoint
statement: formalized
proof: formalized
---

# The spectral measure of a representation of continuous functions

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.StarHomSpec.SpectralMeasure`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean): 44 declarations, 24 with a docstring.

> The projection-valued measure of a unital ⋆-homomorphism from the continuous functions on a compact
> Hausdorff space to the bounded operators of a Hilbert space.

## i. Overview

> The sesquilinear form of the indicator of a Borel set `S` is represented by an operator `E(S)`.
> These operators are projections, countably additive in the weak operator topology, and commute with
> every operator commuting with the range of the ⋆-homomorphism. They form the spectral measure of the
> ⋆-homomorphism, whose integral of a continuous function `f` is `Φ f`. This is the construction of
> `UnitaryInfra.SpectralMeasure` with the continuous functional calculus of a normal operator
> replaced by an arbitrary ⋆-homomorphism, so that it applies to commuting families.

## ii. Key results

> - `starHomSpectralOperator` : the operator `E(S)`.
> - `starHomSpectralOperator_isStarProjection` : each `E(S)` is an orthogonal projection.
> - `starHomSpectralMeasure` : the spectral measure of a ⋆-homomorphism.
> - `starHomSpectralMeasure_reconstruction` : integrating a real continuous `f` gives `Φ f`.
> - `starHomSpectralMeasure_commute` : `E` commutes with operators commuting with the range of `Φ`.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L67).

> The Riesz-represented operator at the measurable set `S`.

```lean
noncomputable def starHomSpectralOperatorAux (S : Set (X)) (hS : MeasurableSet S) :
    H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux_inner`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L71).

```lean
lemma starHomSpectralOperatorAux_inner (S : Set (X)) (hS : MeasurableSet S) (x y : H) :
    ⟪y, starHomSpectralOperatorAux Φ S hS x⟫_ℂ =
      polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L82).

> The Riesz-represented operator on every set, `0` off the measurable sets so that this
> directly matches `MeasureTheory.VectorMeasure`'s `not_measurable'` convention.

```lean
noncomputable def starHomSpectralOperator (S : Set (X)) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_inner`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L85).

```lean
lemma starHomSpectralOperator_inner (S : Set (X)) (x y : H) :
    ⟪y, starHomSpectralOperator Φ S x⟫_ℂ = polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_apply_eq_zero_of_not_measurableSet`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L92).

```lean
lemma starHomSpectralOperator_apply_eq_zero_of_not_measurableSet {S : Set (X)}
    (hS : ¬MeasurableSet S) : starHomSpectralOperator Φ S = 0
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_eq_negI_smul`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L100).

> The `Complex.I`-inversion companion of `starHomScalarMeasure_real_I_smul`: rewrites a Riesz
> measure at `v` as the Riesz measure at `(-I) • v`.  This is the algebraic engine behind
> Hermitian symmetry of the polarized measure below.

```lean
lemma starHomScalarMeasure_real_eq_negI_smul (v : H) (S : Set (X)) :
    (starHomScalarMeasure Φ v).real S = (starHomScalarMeasure Φ ((-Complex.I) • v)).real S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_conj_symm`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L111).

> Hermitian symmetry of the polarized measure: `B(y,x,S) = conj (B(x,y,S))`, matching the
> convention that `B` is exactly `⟪y, starHomRealOperator Φ f x⟫` in the limit and inner products
> are conjugate-symmetric.  This is the input `starHomSpectralOperator_isSelfAdjoint` needs.

```lean
lemma polarizedStarHomScalarMeasure_conj_symm (x y : H) (S : Set (X)) :
    polarizedStarHomScalarMeasure Φ y x S =
      starRingEnd ℂ (polarizedStarHomScalarMeasure Φ x y S)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_isSelfAdjoint`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L144).

> `starHomSpectralOperator Φ S` is self-adjoint, for every `S` (measurable or not — the
> non-measurable case is trivial since the operator is `0`).  This follows from
> `polarizedStarHomScalarMeasure_conj_symm` via `LinearMap.IsSymmetric`.

```lean
lemma starHomSpectralOperator_isSelfAdjoint (S : Set (X)) :
    IsSelfAdjoint (starHomSpectralOperator Φ S)
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_univ`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L154).

> The polarized measure of the whole spectrum is `⟪y, x⟫`.

```lean
lemma polarizedStarHomScalarMeasure_univ (x y : H) :
    polarizedStarHomScalarMeasure Φ x y Set.univ = ⟪y, x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_univ_apply`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L168).

```lean
lemma starHomSpectralOperator_univ_apply (x : H) :
    starHomSpectralOperator Φ Set.univ x = x
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_univ`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L175).

```lean
lemma starHomSpectralOperator_univ : starHomSpectralOperator Φ Set.univ = 1
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_inner_self`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L180).

> On the diagonal, `⟪x, E(S) x⟫` is the diagonal measure of `S`.

```lean
lemma starHomSpectralOperator_inner_self {S : Set (X)} (hS : MeasurableSet S) (x : H) :
    ⟪x, starHomSpectralOperator Φ S x⟫_ℂ = ((starHomScalarMeasure Φ x).real S : ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_reApplyInnerSelf`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L205).

> `reApplyInnerSelf` version of `starHomSpectralOperator_inner_self`, in the exact shape
> `ContinuousLinearMap.IsPositive` consumes.

```lean
lemma starHomSpectralOperator_reApplyInnerSelf {S : Set (X)} (hS : MeasurableSet S)
    (x : H) :
    (starHomSpectralOperator Φ S).reApplyInnerSelf x = (starHomScalarMeasure Φ x).real S
```

## A. Order properties of the spectral operators

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_isPositive`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L215).

> `starHomSpectralOperator Φ S` is a positive operator, for measurable `S`.

```lean
lemma starHomSpectralOperator_isPositive {S : Set (X)} (hS : MeasurableSet S) :
    ContinuousLinearMap.IsPositive (starHomSpectralOperator Φ S)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_nonneg`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L222).

```lean
lemma starHomSpectralOperator_nonneg {S : Set (X)} (hS : MeasurableSet S) :
    0 ≤ starHomSpectralOperator Φ S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_mono`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L228).

> `starHomSpectralOperator Φ S` is monotone in `S`, for measurable sets, in the Loewner order on
> `H →L[ℂ] H`.

```lean
lemma starHomSpectralOperator_mono {S T : Set (X)} (hS : MeasurableSet S)
    (hT : MeasurableSet T) (hST : S ⊆ T) :
    starHomSpectralOperator Φ S ≤ starHomSpectralOperator Φ T
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_le_one`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L246).

```lean
lemma starHomSpectralOperator_le_one {S : Set (X)} (hS : MeasurableSet S) :
    starHomSpectralOperator Φ S ≤ 1
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_empty`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L251).

```lean
lemma starHomSpectralOperator_empty : starHomSpectralOperator Φ ∅ = 0
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_add_of_disjoint`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L259).

> Finite additivity of `starHomSpectralOperator` on disjoint measurable sets.

```lean
lemma starHomSpectralOperator_add_of_disjoint {S T : Set (X)} (hS : MeasurableSet S)
    (hT : MeasurableSet T) (hdisj : Disjoint S T) :
    starHomSpectralOperator Φ (S ∪ T) =
      starHomSpectralOperator Φ S + starHomSpectralOperator Φ T
```

## B. Weak countable additivity

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasureFun`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L273).

> The operator at `S`, valued in the weak-operator-topology type.

```lean
noncomputable def starHomSpectralMeasureFun (S : Set (X)) : H →WOT[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasureFun_inner`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L277).

```lean
lemma starHomSpectralMeasureFun_inner (S : Set (X)) (x y : H) :
    ⟪y, starHomSpectralMeasureFun Φ S x⟫_ℂ = polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralVectorMeasure`**, a def, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L283).

> The operators `E(S)`, as a vector measure in the weak operator topology.

```lean
noncomputable def starHomSpectralVectorMeasure :
    VectorMeasure (X) (H →WOT[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralVectorMeasure_apply`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L307).

```lean
lemma starHomSpectralVectorMeasure_apply (S : Set (X)) :
    starHomSpectralVectorMeasure Φ S = starHomSpectralMeasureFun Φ S
```

## C. The spectral operators are projections

> For a compact set `K` and an open `V ⊇ K`, a Urysohn function `f` gives `E(K) ≤ f(U) ≤ E(V)`. With
> the estimate `‖A x‖² ≤ re ⟪x, A x⟫` for `0 ≤ A ≤ 1` and outer regularity this shows `E(K)² = E(K)`.
> Inner regularity extends it to measurable sets, and multiplicativity on intersections follows from
> additivity.

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux_nonneg`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L322).

```lean
lemma starHomSpectralOperatorAux_nonneg {S : Set (X)} (hS : MeasurableSet S) :
    0 ≤ starHomSpectralOperatorAux Φ S hS
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux_le_one`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L326).

```lean
lemma starHomSpectralOperatorAux_le_one {S : Set (X)} (hS : MeasurableSet S) :
    starHomSpectralOperatorAux Φ S hS ≤ 1
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux_mono`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L330).

```lean
lemma starHomSpectralOperatorAux_mono {S T : Set (X)} (hS : MeasurableSet S)
    (hT : MeasurableSet T) (hST : S ⊆ T) :
    starHomSpectralOperatorAux Φ S hS ≤ starHomSpectralOperatorAux Φ T hT
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_reApplyInnerSelf`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L335).

```lean
lemma starHomRealOperator_reApplyInnerSelf
    (f : CompactlySupportedContinuousMap (X) ℝ) (x : H) :
    (starHomRealOperator Φ f).reApplyInnerSelf x =
      ∫ z, f z ∂starHomScalarMeasure Φ x
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_le_cfcRealOperator_of_compact_subset_open`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L342).

```lean
lemma starHomSpectralOperator_le_cfcRealOperator_of_compact_subset_open
    {K V : Set (X)} (hK : IsCompact K) (_hV : IsOpen V) (_hKV : K ⊆ V)
    (f : CompactlySupportedContinuousMap (X) ℝ)
    (hfK : Set.EqOn f 1 K) (_hfV : tsupport f ⊆ V) (hf : ∀ z, f z ∈ Set.Icc 0 1) :
    starHomSpectralOperator Φ K ≤ starHomRealOperator Φ f
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_le_cfcSpectralOperator_of_support_subse`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L357).

```lean
lemma starHomRealOperator_le_cfcSpectralOperator_of_support_subse
    {V : Set (X)} (hV : IsOpen V)
    (f : CompactlySupportedContinuousMap (X) ℝ)
    (hfV : tsupport f ⊆ V) (hf : ∀ z, f z ∈ Set.Icc 0 1) :
    starHomRealOperator Φ f ≤ starHomSpectralOperator Φ V
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_mul_self`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L374).

```lean
lemma starHomRealOperator_mul_self
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    starHomRealOperator Φ (f * f) = starHomRealOperator Φ f * starHomRealOperator Φ f
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_sub_mul_self`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L385).

```lean
lemma starHomRealOperator_sub_mul_self
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    starHomRealOperator Φ (f - f * f) =
      starHomRealOperator Φ f - starHomRealOperator Φ f * starHomRealOperator Φ f
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_isIdempotent_of_isCompact`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L400).

```lean
lemma starHomSpectralOperator_isIdempotent_of_isCompact
    {K : Set (X)} (hK : IsCompact K) :
    IsIdempotentElem (starHomSpectralOperator Φ K)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperatorAux_isIdempotentElem`**, a lemma, [line 634](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L634).

> **`E(S)` is idempotent.** For compact `S` this follows from a Urysohn function between `S` and
> an open neighbourhood, using `0 ≤ A ≤ 1 ⟹ ‖A x‖² ≤ re ⟪x, A x⟫`; inner regularity extends it to
> measurable `S`.

```lean
lemma starHomSpectralOperatorAux_isIdempotentElem (S : Set (X)) (hS : MeasurableSet S) :
    starHomSpectralOperatorAux Φ S hS * starHomSpectralOperatorAux Φ S hS =
      starHomSpectralOperatorAux Φ S hS
```

> The idempotency proof above is the reusable order/regularity construction.  It first proves
> the compact case with an Urysohn cutoff and outer regularity, then approximates an arbitrary
> measurable set from inside by compact sets.  The only analytic estimate is the positive
> contraction inequality `0 ≤ A ≤ 1 ⟹ ‖A x‖² ≤ re ⟪x, A x⟫`; no weak/strong operator topology
> argument or multiplication of operator limits is involved.

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_isIdempotentElem`**, a lemma, [line 759](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L759).

> Idempotency of `starHomSpectralOperator` on every set — `0` (hence trivially idempotent) off the
> measurable sets, and the order/regularity theorem above on measurable sets.

```lean
lemma starHomSpectralOperator_isIdempotentElem (S : Set (X)) :
    IsIdempotentElem (starHomSpectralOperator Φ S)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_isStarProjection`**, a lemma, [line 768](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L768).

> `starHomSpectralOperator Φ S` is a star-projection, for every `S`; both self-adjointness and
> idempotency are proved.

```lean
lemma starHomSpectralOperator_isStarProjection (S : Set (X)) :
    IsStarProjection (starHomSpectralOperator Φ S)
```

## D. The spectral measure

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure`**, a def, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L777).

> **The weak-operator spectral measure of a bounded normal operator.**  Assembled from the
> Riesz-represented, weakly σ-additive family `starHomSpectralOperator` (Steps B–C, fully proved) and
> the star-projection property (Step D), including the order/regularity proof of idempotency.

```lean
noncomputable def starHomSpectralMeasure : QuantumMechanics.WOTSpectralMeasure (X) H
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_apply`**, a lemma, [line 797](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L797).

```lean
lemma starHomSpectralMeasure_apply (S : Set (X)) :
    starHomSpectralMeasure Φ S = starHomSpectralMeasureFun Φ S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_scalarMeasure`**, a lemma, [line 803](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L803).

> The scalar
>   measure attached to `starHomSpectralMeasure` is exactly the polarized Riesz measure it
> was built from.

```lean
lemma starHomSpectralMeasure_scalarMeasure (x y : H) :
    (starHomSpectralMeasure Φ).scalarMeasure x y = polarizedStarHomScalarMeasure Φ x y
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_reconstruction`**, a lemma, [line 812](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L812).

> **The spectral measure reconstructs the functional calculus**: integrating a continuous function
> `f` gives `f(U)`.

```lean
lemma starHomSpectralMeasure_reconstruction
    (f : CompactlySupportedContinuousMap (X) ℝ) (x y : H) :
    (starHomSpectralMeasure Φ).complexWeakIntegral (fun z => (f z : ℂ)) x y =
      ⟪y, starHomRealOperator Φ f x⟫_ℂ
```

## E. Commutation with the commutant

> omit [MeasurableSpace X] in
> An operator commuting with the range of `Φ` commutes with `Φ f` for continuous `f`, and by
> uniqueness in the Riesz–Markov–Kakutani theorem with every spectral projection of `Φ`.

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_commute`**, a lemma, [line 828](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L828).

> An operator commuting with the range of `Φ` commutes with `Φ` at every real test function.

```lean
lemma starHomRealOperator_commute {T : H →L[ℂ] H} (hT : ∀ f : C(X, ℂ), Commute (Φ f) T)
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    Commute (starHomRealOperator Φ f) T
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_eq_of_commute_isometry`**, a lemma, [line 836](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L836).

> If `T` is an isometry (`star T * T = 1`) commuting with `U` and `star U`, the vector-state
> Riesz measure at `T v` agrees with the one at `v`: an isometric intertwiner of `U` leaves the
> diagonal spectral measure unchanged.

```lean
lemma starHomScalarMeasure_eq_of_commute_isometry
    {T : H →L[ℂ] H} (hT : ∀ f : C(X, ℂ), Commute (Φ f) T)
    (hTiso : star T * T = 1) (v : H) :
    starHomScalarMeasure Φ (T v) = starHomScalarMeasure Φ v
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_eq_of_commute_unitary`**, a lemma, [line 863](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L863).

> If `T` is unitary and commutes with `U` and `star U`, the polarized Riesz measure intertwines:
> testing at `(T x, y)` matches testing at `(x, star T y)`.  This is the sesquilinear form of the
> commutation identity,
>   and is exactly what `starHomSpectralOperator_inner` needs to see commutation of
> each spectral projection with `T`.

```lean
lemma polarizedStarHomScalarMeasure_eq_of_commute_unitary
    {T : H →L[ℂ] H} (hT : ∀ f : C(X, ℂ), Commute (Φ f) T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (x y : H) :
    polarizedStarHomScalarMeasure Φ (T x) y =
      polarizedStarHomScalarMeasure Φ x (star T y)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_commute_of_commute_unitary`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L892).

> Every spectral operator `starHomSpectralOperator Φ S` commutes with any unitary intertwiner of
> `U` (i.e. any unitary commuting with both `U` and `star U`).  Holds for *every* `S`, measurable or
> not, since `starHomSpectralOperator_inner` itself needs no measurability hypothesis.

```lean
lemma starHomSpectralOperator_commute_of_commute_unitary
    {T : H →L[ℂ] H} (hT : ∀ f : C(X, ℂ), Commute (Φ f) T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (S : Set (X)) :
    starHomSpectralOperator Φ S * T = T * starHomSpectralOperator Φ S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_commute_of_commute_unitary`**, a lemma, [line 910](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean#L910).

> The weak-operator spectral measure `starHomSpectralMeasure Φ` commutes with any unitary
> intertwiner of `U`, at every set (measurable or not).

```lean
lemma starHomSpectralMeasure_commute_of_commute_unitary
    {T : H →L[ℂ] H} (hT : ∀ f : C(X, ℂ), Commute (Φ f) T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (S : Set (X)) :
    starHomSpectralMeasure Φ S * ContinuousLinearMapWOT.ofCLM T =
      ContinuousLinearMapWOT.ofCLM T * starHomSpectralMeasure Φ S
```

## Depends on

- [The spectral forms of a representation of continuous functions](unbounded-starhomspec-sesquilinearform.md)
- [The vector-measure integral against a scalar matrix coefficient](../part-02/unbounded-weakintegral.md)

## Proof depends on

- [The spectral measure of a bounded normal operator](unbounded-unitaryinfra-spectralmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SpectralMeasure.lean)
