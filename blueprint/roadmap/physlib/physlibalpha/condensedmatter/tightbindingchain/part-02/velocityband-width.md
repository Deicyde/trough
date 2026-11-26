---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.meanOf_timeReversal, CondensedMatter.TightBindingChain.meanOf_current_timeReversal, CondensedMatter.TightBindingChain.flucOf_timeReversal, CondensedMatter.TightBindingChain.defectOf_timeReversal, CondensedMatter.TightBindingChain.defectOf_smul, CondensedMatter.TightBindingChain.timeReversal_currentEigenstate_one, CondensedMatter.TightBindingChain.currentBasis_zero, CondensedMatter.TightBindingChain.currentBasis_last
statement: formalized
proof: formalized
---

# The velocity band is open from four sites on

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.VelocityBand.Width`, [PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean): 12 declarations, 8 with a docstring; 2 private, not shown.

## i. Overview

> Time reversal `Θ` (`Current/TimeReversal`) commutes with `H` and `X` and reverses the current `J`,
> so it keeps the uncertainty defect, as does a global phase. A unit vector moving at the
> speed limit is, up to a phase, an extreme current eigenstate, the maximal current state or its
> time reverse, so it has the defect of the maximal current state. From four sites on this defect
> is positive, and since the threshold is attained it lies strictly below the speed limit: the
> velocity band is not empty.

## ii. Key results

> - `defectOf_timeReversal`, `meanOf_current_timeReversal` : `Θ` keeps the defect and reverses
>   the current.
> - `defectOf_eq_of_meanOf_current_eq` : at the speed limit, the defect of the maximal current state.
> - `threshold_lt_maxCurrent`, `maxCurrent_mem_velocityBand` : for `N ≥ 4` the band is not empty.
> - `three_div_two_mul_abs_le_threshold` : for `N = 4` the threshold is at least `3/2 |a t|`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Time reversal and the uncertainty defect

**`CondensedMatter.TightBindingChain.meanOf_timeReversal`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L57).

```lean
lemma meanOf_timeReversal {A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace}
    (hA : ∀ ψ, A (T.timeReversal ψ) = T.timeReversal (A ψ)) (ψ : T.HilbertSpace) :
    T.meanOf A (T.timeReversal ψ) = T.meanOf A ψ
```

**`CondensedMatter.TightBindingChain.meanOf_current_timeReversal`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L62).

```lean
lemma meanOf_current_timeReversal (ψ : T.HilbertSpace) :
    T.meanOf T.current (T.timeReversal ψ) = -T.meanOf T.current ψ
```

**`CondensedMatter.TightBindingChain.flucOf_timeReversal`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L67).

```lean
lemma flucOf_timeReversal {A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace}
    (hA : ∀ ψ, A (T.timeReversal ψ) = T.timeReversal (A ψ)) (ψ : T.HilbertSpace) :
    T.flucOf A (T.timeReversal ψ) = T.timeReversal (T.flucOf A ψ)
```

**`CondensedMatter.TightBindingChain.defectOf_timeReversal`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L73).

> Time reversal keeps the uncertainty defect.

```lean
lemma defectOf_timeReversal (ψ : T.HilbertSpace) :
    T.defectOf (T.timeReversal ψ) = T.defectOf ψ
```

**`CondensedMatter.TightBindingChain.defectOf_smul`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L80).

> A global phase keeps the uncertainty defect.

```lean
lemma defectOf_smul {c : ℂ} (hc : ‖c‖ = 1) (ψ : T.HilbertSpace) :
    T.defectOf (c • ψ) = T.defectOf ψ
```

## B. The speed limit is reached only by extreme eigenstates

**`CondensedMatter.TightBindingChain.timeReversal_currentEigenstate_one`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L99).

> The time reverse of the longest standing wave is the shortest one.

```lean
lemma timeReversal_currentEigenstate_one :
    T.timeReversal (T.currentEigenstate 1) = T.currentEigenstate T.N
```

**`CondensedMatter.TightBindingChain.currentBasis_zero`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L113).

> The maximal current state and its time reverse are the extreme current eigenstates.

```lean
lemma currentBasis_zero (ht : T.t ≠ 0) :
    T.currentBasis ht ⟨0, Nat.pos_of_neZero _⟩ = T.maxCurrentState
```

**`CondensedMatter.TightBindingChain.currentBasis_last`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L117).

```lean
lemma currentBasis_last (ht : T.t ≠ 0) :
    T.currentBasis ht ⟨T.N - 1, Nat.sub_lt (Nat.pos_of_neZero _) one_pos⟩ =
      T.timeReversal T.maxCurrentState
```

**`CondensedMatter.TightBindingChain.defectOf_eq_of_meanOf_current_eq`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L125).

> A unit vector moving at the speed limit has the defect of the maximal current state.

```lean
lemma defectOf_eq_of_meanOf_current_eq (ht : T.t ≠ 0) {ψ : T.HilbertSpace} (hψ : ‖ψ‖ = 1)
    (hv : T.meanOf T.current ψ = T.maxCurrent) :
    T.defectOf ψ = T.defectOf T.maxCurrentState
```

## C. The band is not empty

**`CondensedMatter.TightBindingChain.threshold_lt_maxCurrent`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L189).

> From four sites on, the threshold lies strictly below the speed limit.

```lean
lemma threshold_lt_maxCurrent (ht : T.t ≠ 0) (hN : 4 ≤ T.N) : T.threshold < T.maxCurrent
```

**`CondensedMatter.TightBindingChain.maxCurrent_mem_velocityBand`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L205).

> From four sites on, the velocity band is not empty: it contains the speed limit.

```lean
lemma maxCurrent_mem_velocityBand (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    T.maxCurrent ∈ T.velocityBand
```

## D. A vector of minimum uncertainty on four sites

**`CondensedMatter.TightBindingChain.three_div_two_mul_abs_le_threshold`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L232).

> On four sites the threshold is at least `3/2 |a t|`: the unit vector
> `√2/8 (2i, -(3 + i√3), √3 - 3i, 2)` has zero defect and current `3 a t / 2`.

```lean
lemma three_div_two_mul_abs_le_threshold (hN : T.N = 4) :
    3 / 2 * |T.a * T.t| ≤ T.threshold
```

## Depends on

- [Time reversal in the open tight binding chain](../part-01/current-timereversal.md)
- [The velocity band of forced uncertainty](velocityband-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean)
