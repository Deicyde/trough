---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.meanOf, CondensedMatter.TightBindingChain.flucOf, CondensedMatter.TightBindingChain.defectOf, CondensedMatter.TightBindingChain.continuous_meanOf, CondensedMatter.TightBindingChain.continuous_defectOf, CondensedMatter.TightBindingChain.defectOf_nonneg, CondensedMatter.TightBindingChain.expectation_ofVec, CondensedMatter.TightBindingChain.centeredGramDefect_ofVec_eq
statement: formalized
proof: formalized
---

# The velocity band of forced uncertainty

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.VelocityBand.Basic`, [PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean): 18 declarations, 12 with a docstring.

## i. Overview

> A unit vector has minimum uncertainty when the energy–position uncertainty relation is an
> equality, that is when the centered Gram defect of `H` and `X` vanishes. These vectors form a
> compact set, so among them some moves fastest: the threshold `v*` is attained. Every vector
> moving faster, with `v* < |⟨J⟩| ≤ maxCurrent`, carries a positive defect. This is the velocity
> band `(v*, maxCurrent]`. For `N = 2, 3` the maximal current state has minimum uncertainty,
> so the band is empty.

## ii. Key results

> - `defectOf` : the centered Gram defect of `H` and `X` in a vector.
> - `minUncertainty` : the unit vectors of minimum uncertainty, a compact set.
> - `threshold` : the largest speed `|⟨J⟩|` of a vector of minimum uncertainty, attained by
>   `exists_threshold`.
> - `velocityBand` : the band `(threshold, maxCurrent]`.
> - `defectOf_pos_of_mem_velocityBand` : in the band, the defect is forced.
> - `velocityBand_eq_empty` : for `N = 2, 3` the band is empty.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Uncertainty in a vector

**`CondensedMatter.TightBindingChain.meanOf`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L60).

> The mean `re ⟨ψ|A|ψ⟩` of an operator in a vector.

```lean
noncomputable def meanOf (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) (ψ : T.HilbertSpace) : ℝ
```

**`CondensedMatter.TightBindingChain.flucOf`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L64).

> The fluctuation `A ψ - ⟨A⟩ ψ` of an operator in a vector.

```lean
noncomputable def flucOf (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) (ψ : T.HilbertSpace) :
    T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.defectOf`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L69).

> The centered Gram defect `‖u‖² ‖w‖² - |⟪u, w⟫|²` of `H` and `X` in a vector.

```lean
noncomputable def defectOf (ψ : T.HilbertSpace) : ℝ
```

**`CondensedMatter.TightBindingChain.continuous_meanOf`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L73).

```lean
lemma continuous_meanOf (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) : Continuous (T.meanOf A)
```

**`CondensedMatter.TightBindingChain.continuous_defectOf`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L76).

```lean
lemma continuous_defectOf : Continuous T.defectOf
```

**`CondensedMatter.TightBindingChain.defectOf_nonneg`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L82).

```lean
lemma defectOf_nonneg (ψ : T.HilbertSpace) : 0 ≤ T.defectOf ψ
```

**`CondensedMatter.TightBindingChain.expectation_ofVec`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L87).

> In a unit vector, the mean is the expectation of the vector state.

```lean
lemma expectation_ofVec {ψ : T.HilbertSpace} (h : ‖ψ‖ = 1)
    (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) (hA : A.IsSymmetric) :
    (ofVec h)⟨T.toObservable A hA⟩ = T.meanOf A ψ
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_ofVec_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L94).

> In a unit vector, `defectOf` is the centered Gram defect of the vector state.

```lean
lemma centeredGramDefect_ofVec_eq {ψ : T.HilbertSpace} (h : ‖ψ‖ = 1) :
    centeredGramDefect (ofVec h) T.openHamiltonianObservable T.positionObservable =
      T.defectOf ψ
```

## B. The threshold

**`CondensedMatter.TightBindingChain.minUncertainty`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L110).

> The unit vectors of minimum uncertainty.

```lean
noncomputable def minUncertainty : Set T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.isCompact_minUncertainty`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L112).

```lean
lemma isCompact_minUncertainty : IsCompact T.minUncertainty
```

**`CondensedMatter.TightBindingChain.localizedState_mem_minUncertainty`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L117).

> A localized electron has minimum uncertainty: its position is sharp.

```lean
lemma localizedState_mem_minUncertainty (n : Fin T.N) : (|n⟩ : T.HilbertSpace) ∈
    T.minUncertainty := by
  have hX : T.flucOf T.position |n⟩ = 0 := by
    rw [flucOf, meanOf, position_apply_localizedState, inner_smul_right,
      T.localizedState_orthonormal_eq_ite, ite_eq_left rfl, mul_one, Complex.ofReal_re,
      ← Complex.coe_smul, sub_self]
  refine ⟨by simp [(localizedState (T := T)).orthonormal.1 n], ?_⟩
  simp [defectOf, hX]
```

**`CondensedMatter.TightBindingChain.threshold`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L127).

> The largest speed `|⟨J⟩|` of a vector of minimum uncertainty.

```lean
noncomputable def threshold : ℝ
```

**`CondensedMatter.TightBindingChain.exists_threshold`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L130).

> The threshold is attained by a vector of minimum uncertainty.

```lean
lemma exists_threshold :
    ∃ ψ ∈ T.minUncertainty, |T.meanOf T.current ψ| = T.threshold
```

**`CondensedMatter.TightBindingChain.le_threshold`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L135).

```lean
lemma le_threshold {ψ : T.HilbertSpace} (hψ : ψ ∈ T.minUncertainty) :
    |T.meanOf T.current ψ| ≤ T.threshold
```

**`CondensedMatter.TightBindingChain.threshold_le_maxCurrent`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L140).

```lean
lemma threshold_le_maxCurrent (ht : T.t ≠ 0) : T.threshold ≤ T.maxCurrent
```

## C. The band

**`CondensedMatter.TightBindingChain.velocityBand`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L153).

> The velocity band `(threshold, maxCurrent]` of forced uncertainty.

```lean
noncomputable def velocityBand : Set ℝ
```

**`CondensedMatter.TightBindingChain.defectOf_pos_of_mem_velocityBand`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L156).

> In the velocity band, the uncertainty defect is forced.

```lean
lemma defectOf_pos_of_mem_velocityBand {ψ : T.HilbertSpace} (hψ : ‖ψ‖ = 1)
    (hv : |T.meanOf T.current ψ| ∈ T.velocityBand) : 0 < T.defectOf ψ
```

**`CondensedMatter.TightBindingChain.velocityBand_eq_empty`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean#L162).

> For `N = 2, 3` the maximal current state has minimum uncertainty: the band is empty.

```lean
lemma velocityBand_eq_empty (ht : T.t ≠ 0) (hN : T.N = 2 ∨ T.N = 3) :
    T.velocityBand = ∅
```

## Depends on

- [The speed limit of the open tight binding chain](../part-01/current-speedlimit.md)
- [Uncertainty relations](../../../probabilistictheory/cstaralgebra/uncertainty.md)

## Proof depends on

- [Saturation of the uncertainty relation in the maximal current state](../part-01/maxcurrentstate-saturation.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Basic.lean)
