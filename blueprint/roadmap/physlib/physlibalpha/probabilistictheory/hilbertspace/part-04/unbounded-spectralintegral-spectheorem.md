---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_boundedIntegral_eq_withDensity, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expIntegral_mem_spectralSquareMomentDomain, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedMultiplier_mem_spectralSquareMomentDomain, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedMultiplier_mem_spectralSquareMomentDomain_of_bound, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_apply_boundedMultiplier, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_apply_boundedMultiplier_of_bound, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.plusResolventMultiplier, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.minusResolventMultiplier
statement: formalized
proof: formalized
---

# The integral of the identity is self-adjoint

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.SpectralIntegral.SpecTheorem`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean): 46 declarations, 9 with a docstring.

> The integral of the identity against a spectral measure on `ℝ` is self-adjoint.

## i. Overview

> The integral of the identity against a spectral measure on `ℝ` has resolvents at `± i` given by the
> bounded integrals of `1 / (λ ∓ i)`. So it is self-adjoint. An operator resolved by a spectral
> measure equals this integral, which identifies its domain with the vectors of finite second moment.

## ii. Key results

> - `resolventMultiplier` : the bounded function `λ ↦ (λ - z)⁻¹` for non-real `z`.
> - `maximalSpectralIntegral_resolvent_range` : the shifts by non-real `z` of the maximal integral
>   are onto.
> - `maximalSpectralIntegral_isSelfAdjoint` : the integral of the identity is self-adjoint.
> - `measurableSpectralIntegral_isSelfAdjoint` : so is the integral of any measurable real function.
> - `maximalSpectralIntegral_eq_of_isSelfAdjoint_of_isWeakSpectralResolution` : a self-adjoint
>   operator resolved by a spectral measure equals the integral of the identity.
> - `domainAwareSelfAdjointSpectralTheorem_of_isWeakSpectralResolution` : a spectral measure resolving
>   a self-adjoint operator resolves it together with its domain.

## iv. References

> * None.

## A. Weighted diagonal measures

> Applying a bounded spectral multiplier changes the vector spectral measure by the squared
> multiplier.  This is the measure-level statement that turns bounded resolvents into vectors in the
> maximal square-moment domain.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_boundedIntegral_eq_withDensity`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L70).

```lean
lemma diagonalMeasure_boundedIntegral_eq_withDensity
    {α : Type*} [MeasurableSpace α] [Nonempty α]
    (μS : WOTSpectralMeasure α H) {g : α → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C) (x : H) :
    μS.diagonalMeasure (boundedIntegral μS g hg hgb x) =
      Measure.withDensity (μS.diagonalMeasure x)
        (fun a => ENNReal.ofReal (‖g a‖ ^ 2))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.expIntegral_mem_spectralSquareMomentDomain`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L110).

```lean
lemma expIntegral_mem_spectralSquareMomentDomain
    (μS : WOTSpectralMeasure ℝ H) (t : ℝ) (x : H)
    (hx : x ∈ spectralSquareMomentDomain μS) :
    expIntegral μS t x ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedMultiplier_mem_spectralSquareMomentDomain`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L129).

```lean
lemma boundedMultiplier_mem_spectralSquareMomentDomain
    {α : Type*} [MeasurableSpace α] [Nonempty α]
    (μS : WOTSpectralMeasure ℝ H) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C)
    (hcoord : ∀ a : ℝ, ‖(a : ℂ) * g a‖ ≤ 1) (x : H) :
    boundedIntegral μS g hg hgb x ∈ spectralSquareMomentDomain μS
```

> The unit bound used by the first resolvent construction is convenient, but it is not
> mathematically essential.  Keeping the finite-bound version separate makes the later general
> resolvent API usable at arbitrary non-real parameters without weakening any of the existing
> callers.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedMultiplier_mem_spectralSquareMomentDomain_of_bound`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L161).

```lean
lemma boundedMultiplier_mem_spectralSquareMomentDomain_of_bound
    {α : Type*} [MeasurableSpace α] [Nonempty α]
    (μS : WOTSpectralMeasure ℝ H) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C)
    (hcoord : ∃ C : ℝ, 0 ≤ C ∧ ∀ a : ℝ, ‖(a : ℂ) * g a‖ ≤ C) (x : H) :
    boundedIntegral μS g hg hgb x ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_apply_boundedMultiplier`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L189).

```lean
lemma maximalSpectralIntegral_apply_boundedMultiplier
    (μS : WOTSpectralMeasure ℝ H) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C)
    (hcoord : ∀ a : ℝ, ‖(a : ℂ) * g a‖ ≤ 1)
    (hcoord_meas : Measurable (fun a : ℝ => (a : ℂ) * g a))
    (x : H) :
    (maximalSpectralIntegral μS)
        ⟨boundedIntegral μS g hg hgb x,
          boundedMultiplier_mem_spectralSquareMomentDomain (α := ℝ) μS hg hgb hcoord x⟩ =
      boundedIntegral μS (fun a : ℝ => (a : ℂ) * g a) hcoord_meas
        ⟨1, hcoord⟩ x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_apply_boundedMultiplier_of_bound`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L254).

```lean
lemma maximalSpectralIntegral_apply_boundedMultiplier_of_bound
    (μS : WOTSpectralMeasure ℝ H) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C)
    (hcoord : ∃ C : ℝ, 0 ≤ C ∧ ∀ a : ℝ, ‖(a : ℂ) * g a‖ ≤ C)
    (hcoord_meas : Measurable (fun a : ℝ => (a : ℂ) * g a))
    (x : H) :
    (maximalSpectralIntegral μS)
        ⟨boundedIntegral μS g hg hgb x,
          boundedMultiplier_mem_spectralSquareMomentDomain_of_bound
            (α := ℝ) μS hg hgb hcoord x⟩ =
      boundedIntegral μS (fun a : ℝ => (a : ℂ) * g a) hcoord_meas
        (by
          rcases hcoord with ⟨C, _hC0, hC⟩
          exact ⟨C, hC⟩) x
```

## B. The two Cayley resolvents

> These are the bounded multipliers which realize the inverse of the shifts by `± i`.  Their
> construction is independent of any pre-existing self-adjoint operator; it is purely the real PVM
> calculus applied to the scalar functions `(r ± i)⁻¹`.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.plusResolventMultiplier`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L333).

> The scalar multiplier `r ↦ (r + i)⁻¹`.

```lean
def plusResolventMultiplier (r : ℝ) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.minusResolventMultiplier`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L336).

> The scalar multiplier `r ↦ (r - i)⁻¹`.

```lean
def minusResolventMultiplier (r : ℝ) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier`**, a def, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L339).

> The scalar resolvent multiplier at an arbitrary non-real parameter.

```lean
def resolventMultiplier (z : ℂ) (r : ℝ) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier_measurable`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L341).

```lean
lemma resolventMultiplier_measurable (z : ℂ) :
    Measurable (resolventMultiplier z)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier_denom_ne_zero`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L346).

```lean
lemma resolventMultiplier_denom_ne_zero {z : ℂ} (hz : z.im ≠ 0) (r : ℝ) :
    (r : ℂ) - z ≠ 0
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier_bounded`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L352).

```lean
lemma resolventMultiplier_bounded {z : ℂ} (hz : z.im ≠ 0) :
    ∃ C : ℝ, ∀ r, ‖resolventMultiplier z r‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier_coordinate_bounded`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L366).

```lean
lemma resolventMultiplier_coordinate_bounded {z : ℂ} (hz : z.im ≠ 0) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ r : ℝ,
      ‖(r : ℂ) * resolventMultiplier z r‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier_coordinate_measurable`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L397).

```lean
lemma resolventMultiplier_coordinate_measurable (z : ℂ) :
    Measurable (fun r : ℝ => (r : ℂ) * resolventMultiplier z r)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.resolventMultiplier_identity`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L402).

```lean
lemma resolventMultiplier_identity {z : ℂ} (hz : z.im ≠ 0) (r : ℝ) :
    (r : ℂ) * resolventMultiplier z r - z * resolventMultiplier z r = 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.plusResolventMultiplier_measurable`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L409).

```lean
lemma plusResolventMultiplier_measurable :
    Measurable plusResolventMultiplier
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.minusResolventMultiplier_measurable`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L414).

```lean
lemma minusResolventMultiplier_measurable :
    Measurable minusResolventMultiplier
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.plusResolventMultiplier_bounded`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L419).

```lean
lemma plusResolventMultiplier_bounded :
    ∃ C : ℝ, ∀ r, ‖plusResolventMultiplier r‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.minusResolventMultiplier_bounded`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L432).

```lean
lemma minusResolventMultiplier_bounded :
    ∃ C : ℝ, ∀ r, ‖minusResolventMultiplier r‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.plusResolventMultiplier_coordinate_bounded`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L445).

```lean
lemma plusResolventMultiplier_coordinate_bounded :
    ∀ r : ℝ, ‖(r : ℂ) * plusResolventMultiplier r‖ ≤ 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.minusResolventMultiplier_coordinate_bounded`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L459).

```lean
lemma minusResolventMultiplier_coordinate_bounded :
    ∀ r : ℝ, ‖(r : ℂ) * minusResolventMultiplier r‖ ≤ 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.plusResolventMultiplier_coordinate_measurable`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L473).

```lean
lemma plusResolventMultiplier_coordinate_measurable :
    Measurable (fun r : ℝ => (r : ℂ) * plusResolventMultiplier r)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.minusResolventMultiplier_coordinate_measurable`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L478).

```lean
lemma minusResolventMultiplier_coordinate_measurable :
    Measurable (fun r : ℝ => (r : ℂ) * minusResolventMultiplier r)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_shift_range_of_multiplier`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L483).

```lean
lemma maximalSpectralIntegral_shift_range_of_multiplier
    (μS : WOTSpectralMeasure ℝ H) (c : ℂ) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C)
    (hcoord : ∀ a : ℝ, ‖(a : ℂ) * g a‖ ≤ 1)
    (hcoord_meas : Measurable (fun a : ℝ => (a : ℂ) * g a))
    (hidentity : ∀ a : ℝ, (a : ℂ) * g a + c * g a = 1) :
    (maximalSpectralIntegral μS + c • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_shift_range_of_multiplier_of_bound`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L539).

```lean
lemma maximalSpectralIntegral_shift_range_of_multiplier_of_bound
    (μS : WOTSpectralMeasure ℝ H) (c : ℂ) {g : ℝ → ℂ} (hg : Measurable g)
    (hgb : ∃ C : ℝ, ∀ a, ‖g a‖ ≤ C)
    (hcoord : ∃ C : ℝ, 0 ≤ C ∧ ∀ a : ℝ, ‖(a : ℂ) * g a‖ ≤ C)
    (hcoord_meas : Measurable (fun a : ℝ => (a : ℂ) * g a))
    (hidentity : ∀ a : ℝ, (a : ℂ) * g a + c * g a = 1) :
    (maximalSpectralIntegral μS + c • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_resolvent_range`**, a lemma, [line 601](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L601).

> Every non-real shift of the canonical spectral integral is onto.  This is the concrete range
> form of the resolvent theorem, proved directly from the bounded scalar multiplier
> `r ↦ (r - z)⁻¹`.

```lean
lemma maximalSpectralIntegral_resolvent_range {z : ℂ} (hz : z.im ≠ 0) :
    (maximalSpectralIntegral μS - z • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_resolvent_inverse_apply`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L623).

> The value of the inverse of a general non-real shift is the corresponding bounded spectral
> multiplier.  This is the operator-level resolvent formula, including its domain proof.

```lean
lemma maximalSpectralIntegral_resolvent_inverse_apply {z : ℂ} (hz : z.im ≠ 0) (x : H) :
    (maximalSpectralIntegral μS - z • (1 : H →ₗ.[ℂ] H)).inverse
        ⟨x, by
          rw [LinearPMap.inverse_domain, maximalSpectralIntegral_resolvent_range hz]
          exact Submodule.mem_top⟩ =
      boundedIntegral μS (resolventMultiplier z) (resolventMultiplier_measurable z)
        (resolventMultiplier_bounded hz) x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_plus_resolvent_range`**, a lemma, [line 728](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L728).

```lean
lemma maximalSpectralIntegral_plus_resolvent_range :
    (maximalSpectralIntegral μS + Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_minus_resolvent_range`**, a lemma, [line 748](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L748).

```lean
lemma maximalSpectralIntegral_minus_resolvent_range :
    (maximalSpectralIntegral μS - Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤
```

## C. Resolvent values of the maximal realization

> The range statements above show that the two shifted maximal realizations are onto.  The
> following sharpen them to an actual value formula for their partial inverses.  This is the
> operator-level form of the bounded Borel identities
>
> `(λ + i)⁻¹ (λ + i) = 1` and `(λ - i)⁻¹ (λ - i) = 1`.
>
> These lemmas are intentionally stated for `LinearPMap.inverse`: they do not introduce a second
> unbounded-operator hierarchy, and they are exactly what the Cayley adapter needs when converting
> between a self-adjoint operator and its bounded unitary transform.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_plus_resolvent_inverse_apply`**, a lemma, [line 790](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L790).

```lean
lemma maximalSpectralIntegral_plus_resolvent_inverse_apply (x : H) :
    (maximalSpectralIntegral μS + Complex.I • (1 : H →ₗ.[ℂ] H)).inverse
        ⟨x, by
          rw [LinearPMap.inverse_domain, maximalSpectralIntegral_plus_resolvent_range]
          exact Submodule.mem_top⟩ =
      boundedIntegral μS plusResolventMultiplier plusResolventMultiplier_measurable
        plusResolventMultiplier_bounded x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_minus_resolvent_inverse_apply`**, a lemma, [line 900](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L900).

```lean
lemma maximalSpectralIntegral_minus_resolvent_inverse_apply (x : H) :
    (maximalSpectralIntegral μS - Complex.I • (1 : H →ₗ.[ℂ] H)).inverse
        ⟨x, by
          rw [LinearPMap.inverse_domain, maximalSpectralIntegral_minus_resolvent_range]
          exact Submodule.mem_top⟩ =
      boundedIntegral μS minusResolventMultiplier minusResolventMultiplier_measurable
        minusResolventMultiplier_bounded x
```

## D. The canonical self-adjoint realization

> The preceding two range lemmas are the concrete Cayley-resolvent calculation.  They are worth
> keeping separate from the abstract range criterion: this theorem is the point at which a real PVM
> itself produces a self-adjoint (closed) unbounded operator, with no prior operator or domain datum.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isSelfAdjoint`**, a lemma, [line 1011](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1011).

```lean
lemma maximalSpectralIntegral_isSelfAdjoint (μS : WOTSpectralMeasure ℝ H) :
    IsSelfAdjoint (maximalSpectralIntegral μS)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_sub_smul_surjective`**, a lemma, [line 1020](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1020).

> The canonical maximal realization has a surjective shifted operator at every non-real
> spectral parameter.  The preceding explicit `± Complex.I` calculations establish
> self-adjointness; this general form then follows from the self-adjoint resolvent theorem.

```lean
lemma maximalSpectralIntegral_sub_smul_surjective
    (μS : WOTSpectralMeasure ℝ H) {z : ℂ} (hz : z.im ≠ 0) :
    Function.Surjective
      (maximalSpectralIntegral μS - z • (1 : H →ₗ.[ℂ] H)).toFun
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_mem_resolventSet`**, a lemma, [line 1031](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1031).

> Every non-real point belongs to the resolvent set of the canonical maximal spectral
> integral.  This is the public `resolventSet` form of the preceding range theorem and the
> self-adjoint resolvent criterion; downstream users can therefore use the ordinary resolvent API
> without unpacking the Cayley shifts or the spectral multiplier construction.

```lean
lemma maximalSpectralIntegral_mem_resolventSet
    (μS : WOTSpectralMeasure ℝ H) {z : ℂ} (hz : z.im ≠ 0) :
    z ∈ LinearPMap.resolventSet (maximalSpectralIntegral μS)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_resolvent_apply`**, a lemma, [line 1040](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1040).

> Resolvent notation for the canonical spectral integral is exactly the bounded spectral
> multiplier `λ ↦ (λ - z)⁻¹`.  The subtype in the left-hand side is the canonical full-domain
> element supplied by the resolvent theorem.

```lean
lemma maximalSpectralIntegral_resolvent_apply {z : ℂ} (hz : z.im ≠ 0) (x : H) :
    LinearPMap.resolvent (maximalSpectralIntegral μS) z
        ⟨x, by
          rw [LinearPMap.inverse_domain, maximalSpectralIntegral_resolvent_range hz]
          exact Submodule.mem_top⟩ =
      boundedIntegral μS (resolventMultiplier z) (resolventMultiplier_measurable z)
        (resolventMultiplier_bounded hz) x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_closure_eq_self_adjoint`**, a lemma, [line 1049](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1049).

```lean
lemma maximalSpectralIntegral_closure_eq_self_adjoint (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).closure = maximalSpectralIntegral μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isEssentiallySelfAdjoint`**, a lemma, [line 1053](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1053).

```lean
lemma maximalSpectralIntegral_isEssentiallySelfAdjoint (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).IsEssentiallySelfAdjoint
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_isSelfAdjoint`**, a lemma, [line 1059](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1059).

```lean
lemma measurableSpectralIntegral_isSelfAdjoint
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f) :
    _root_.IsSelfAdjoint (measurableSpectralIntegral μS f hf)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_closure_eq_self`**, a lemma, [line 1064](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1064).

```lean
lemma measurableSpectralIntegral_closure_eq_self
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f) :
    (measurableSpectralIntegral μS f hf).closure =
      measurableSpectralIntegral μS f hf
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_isEssentiallySelfAdjoint`**, a lemma, [line 1070](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1070).

```lean
lemma measurableSpectralIntegral_isEssentiallySelfAdjoint
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f) :
    (measurableSpectralIntegral μS f hf).IsEssentiallySelfAdjoint
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_norm_sq`**, a lemma, [line 1075](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1075).

```lean
lemma measurableSpectralIntegral_norm_sq
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f)
    (x : H) (hx : x ∈ (measurableSpectralIntegral μS f hf).domain) :
    ENNReal.ofReal
        (‖(measurableSpectralIntegral μS f hf) ⟨x, hx⟩‖ ^ 2) =
      ∫⁻ r, ENNReal.ofReal ((f r) ^ 2) ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_norm_sq_eq_integral`**, a lemma, [line 1092](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1092).

```lean
lemma measurableSpectralIntegral_norm_sq_eq_integral
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f)
    (x : H) (hx : x ∈ (measurableSpectralIntegral μS f hf).domain) :
    ‖(measurableSpectralIntegral μS f hf) ⟨x, hx⟩‖ ^ 2 =
      ∫ r, f r ^ 2 ∂μS.diagonalMeasure x
```

## E. Uniqueness of the domain-aware realization

> A self-adjoint operator resolved by a spectral measure is the integral of the identity on its
> maximal domain.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_eq_of_isSelfAdjoint_of_isWeakSpectralResolution`**, a lemma, [line 1115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1115).

```lean
lemma maximalSpectralIntegral_eq_of_isSelfAdjoint_of_isWeakSpectralResolution
    (T : H →ₗ.[ℂ] H) (hT : _root_.IsSelfAdjoint T)
    (hres : IsWeakSpectralResolution T μS)
    (hdom : ∀ x : T.domain,
      (x : H) ∈ spectralSquareMomentDomain μS) :
    maximalSpectralIntegral μS = T
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.domainAwareSelfAdjointSpectralTheorem_of_isWeakSpectralResolution`**, a lemma, [line 1183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1183).

> **A spectral resolution determines the domain.** If `μ` resolves the self-adjoint operator `T`
> and the domain of `T` has finite second moments, then the domain of `T` is exactly the set of
> vectors of finite second moment.

```lean
lemma domainAwareSelfAdjointSpectralTheorem_of_isWeakSpectralResolution
    (T : H →ₗ.[ℂ] H) (hT : _root_.IsSelfAdjoint T)
    (hres : IsWeakSpectralResolution T μS)
    (hdom : ∀ x : T.domain,
      (x : H) ∈ spectralSquareMomentDomain μS) :
    DomainAwareSelfAdjointSpectralTheorem T μS
```

## F. The canonical operator equality

> The domain-aware certificate contains exactly the extra hypothesis needed by the uniqueness
> theorem: its operator domain is the square-moment domain of its PVM.  Exposing this equality as a
> method keeps later Cayley and representation proofs from reconstructing the same argument.

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.maximal_eq`**, a lemma, [line 1222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1222).

```lean
lemma maximal_eq (D : DomainAwareSelfAdjointSpectralTheorem T μS) :
    maximalSpectralIntegral μS = T
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointSpectralTheorem.maximal_eq_of_domain_inclusion`**, a lemma, [line 1239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean#L1239).

```lean
lemma maximal_eq_of_domain_inclusion
    (D : SelfAdjointSpectralTheorem T μS)
    (hdom : ∀ x : T.domain,
      (x : H) ∈ spectralSquareMomentDomain μS) :
    maximalSpectralIntegral μS = T
```

## Depends on

- [Integrating unbounded functions against a spectral measure](../part-03/unbounded-spectralintegral-construction.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/SpecTheorem.lean)
