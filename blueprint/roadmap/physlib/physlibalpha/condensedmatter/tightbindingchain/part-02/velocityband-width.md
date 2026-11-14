---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.meanOf_timeReversal, CondensedMatter.TightBindingChain.meanOf_current_timeReversal, CondensedMatter.TightBindingChain.flucOf_timeReversal, CondensedMatter.TightBindingChain.defectOf_timeReversal, CondensedMatter.TightBindingChain.defectOf_smul, CondensedMatter.TightBindingChain.timeReversal_currentEigenstate_one, CondensedMatter.TightBindingChain.currentBasis_zero, CondensedMatter.TightBindingChain.currentBasis_last
statement: formalized
proof: formalized
---

# The velocity band is open from four sites on

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.VelocityBand.Width`, [PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean): 11 declarations, 7 with a docstring.

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

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Time reversal and the uncertainty defect

**`CondensedMatter.TightBindingChain.meanOf_timeReversal`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L55).

```lean
lemma meanOf_timeReversal {A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace}
    (hA : ∀ ψ, A (T.timeReversal ψ) = T.timeReversal (A ψ)) (ψ : T.HilbertSpace) :
    T.meanOf A (T.timeReversal ψ) = T.meanOf A ψ
```

**`CondensedMatter.TightBindingChain.meanOf_current_timeReversal`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L60).

```lean
lemma meanOf_current_timeReversal (ψ : T.HilbertSpace) :
    T.meanOf T.current (T.timeReversal ψ) = -T.meanOf T.current ψ
```

**`CondensedMatter.TightBindingChain.flucOf_timeReversal`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L65).

```lean
lemma flucOf_timeReversal {A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace}
    (hA : ∀ ψ, A (T.timeReversal ψ) = T.timeReversal (A ψ)) (ψ : T.HilbertSpace) :
    T.flucOf A (T.timeReversal ψ) = T.timeReversal (T.flucOf A ψ)
```

**`CondensedMatter.TightBindingChain.defectOf_timeReversal`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L71).

> Time reversal keeps the uncertainty defect.

```lean
lemma defectOf_timeReversal (ψ : T.HilbertSpace) :
    T.defectOf (T.timeReversal ψ) = T.defectOf ψ
```

**`CondensedMatter.TightBindingChain.defectOf_smul`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L78).

> A global phase keeps the uncertainty defect.

```lean
lemma defectOf_smul {c : ℂ} (hc : ‖c‖ = 1) (ψ : T.HilbertSpace) :
    T.defectOf (c • ψ) = T.defectOf ψ
```

## B. The speed limit is reached only by extreme eigenstates

**`CondensedMatter.TightBindingChain.timeReversal_currentEigenstate_one`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L97).

> The time reverse of the longest standing wave is the shortest one.

```lean
lemma timeReversal_currentEigenstate_one :
    T.timeReversal (T.currentEigenstate 1) = T.currentEigenstate T.N
```

**`CondensedMatter.TightBindingChain.currentBasis_zero`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L111).

> The maximal current state and its time reverse are the extreme current eigenstates.

```lean
lemma currentBasis_zero (ht : T.t ≠ 0) :
    T.currentBasis ht ⟨0, Nat.pos_of_neZero _⟩ = T.maxCurrentState
```

**`CondensedMatter.TightBindingChain.currentBasis_last`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L115).

```lean
lemma currentBasis_last (ht : T.t ≠ 0) :
    T.currentBasis ht ⟨T.N - 1, Nat.sub_lt (Nat.pos_of_neZero _) one_pos⟩ =
      T.timeReversal T.maxCurrentState
```

**`CondensedMatter.TightBindingChain.defectOf_eq_of_meanOf_current_eq`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L123).

> A unit vector moving at the speed limit has the defect of the maximal current state.

```lean
lemma defectOf_eq_of_meanOf_current_eq (ht : T.t ≠ 0) {ψ : T.HilbertSpace} (hψ : ‖ψ‖ = 1)
    (hv : T.meanOf T.current ψ = T.maxCurrent) :
    T.defectOf ψ = T.defectOf T.maxCurrentState
```

## C. The band is not empty

**`CondensedMatter.TightBindingChain.threshold_lt_maxCurrent`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L187).

> From four sites on, the threshold lies strictly below the speed limit.

```lean
lemma threshold_lt_maxCurrent (ht : T.t ≠ 0) (hN : 4 ≤ T.N) : T.threshold < T.maxCurrent
```

**`CondensedMatter.TightBindingChain.maxCurrent_mem_velocityBand`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean#L203).

> From four sites on, the velocity band is not empty: it contains the speed limit.

```lean
lemma maxCurrent_mem_velocityBand (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    T.maxCurrent ∈ T.velocityBand
```

## Depends on

- [Time reversal in the open tight binding chain](../part-01/current-timereversal.md)
- [The velocity band of forced uncertainty](velocityband-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/VelocityBand/Width.lean)
