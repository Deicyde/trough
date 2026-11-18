---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.fluctuationAngle, CondensedMatter.TightBindingChain.fluctuationAngle_eq, CondensedMatter.TightBindingChain.fluctuationAngle_eq_zero_iff, CondensedMatter.TightBindingChain.fluctuationAngle_pos, CondensedMatter.TightBindingChain.fluctuationAngle_lt_fluctuationAngle, CondensedMatter.TightBindingChain.fluctuationAngle_lt, CondensedMatter.TightBindingChain.dimQuantum, CondensedMatter.TightBindingChain.dimQuantum_nonneg
statement: formalized
proof: formalized
---

# The fluctuation angle of the maximal current state

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.FluctuationAngle`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean): 13 declarations, 12 with a docstring; 1 private, not shown.

## i. Overview

> In the maximal current state the energy and position fluctuations are uncorrelated, so the
> pairing `ω(δH δX)` reduces to the bracket term `a t cos (π / (N + 1))`. Its modulus over
> `σ_H σ_X` is the cosine of the angle between the two fluctuations: the fluctuation angle, with
> `cos θ = 1 / C`. It vanishes exactly for `N = 2, 3`, opens from four sites on, grows
> strictly with `N` and stays below `arccos (1 / √(π² / 3 - 2))`. The excess `δ = C - 1` is the
> dimensional quantum of the chain, and it fixes the angle.

## ii. Key results

> - `fluctuationAngle` : the angle between the energy and position fluctuations.
> - `fluctuationAngle_eq` : `θ = arccos (1 / C)`.
> - `fluctuationAngle_eq_zero_iff`, `fluctuationAngle_pos` : it vanishes iff `N = 2, 3`, and opens
>   from `N = 4`.
> - `fluctuationAngle_lt_fluctuationAngle`, `fluctuationAngle_lt` : it grows strictly with `N`, below
>   its limit.
> - `dimQuantum` : the dimensional quantum `δ = C - 1`.
> - `fluctuationAngle_eq_dimQuantum` : `θ = arccos (1 / (1 + δ))`.

## iv. References

> * H. P. Robertson, *A general formulation of the uncertainty principle and its classical
>   interpretation*, Phys. Rev. 35 (1930) 667.

## A. The fluctuation angle

**`CondensedMatter.TightBindingChain.fluctuationAngle`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L61).

> The fluctuation angle: the angle between the energy and position fluctuations in the maximal
> current state, `arccos (‖ω(δH δX)‖ / (σ_H σ_X))`.

```lean
noncomputable def fluctuationAngle : ℝ
```

**`CondensedMatter.TightBindingChain.fluctuationAngle_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L69).

> The fluctuation angle: `cos θ = 1 / C`.

```lean
lemma fluctuationAngle_eq (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.fluctuationAngle = Real.arccos (1 / T.uncertaintyRatio)
```

**`CondensedMatter.TightBindingChain.fluctuationAngle_eq_zero_iff`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L81).

> The fluctuation angle vanishes exactly for `N = 2` and `N = 3`.

```lean
lemma fluctuationAngle_eq_zero_iff (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.fluctuationAngle = 0 ↔ T.N = 2 ∨ T.N = 3
```

**`CondensedMatter.TightBindingChain.fluctuationAngle_pos`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L89).

> From four sites on, the fluctuation angle is open.

```lean
lemma fluctuationAngle_pos (ht : T.t ≠ 0) (hN : 4 ≤ T.N) : 0 < T.fluctuationAngle
```

**`CondensedMatter.TightBindingChain.fluctuationAngle_lt_fluctuationAngle`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L99).

> From four sites on, the fluctuation angle grows strictly with the number of sites.

```lean
lemma fluctuationAngle_lt_fluctuationAngle {T T' : TightBindingChain} (ht : T.t ≠ 0)
    (ht' : T'.t ≠ 0) (hN : 4 ≤ T.N) (hNN' : T.N < T'.N) :
    T.fluctuationAngle < T'.fluctuationAngle
```

**`CondensedMatter.TightBindingChain.fluctuationAngle_lt`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L107).

> From four sites on, the fluctuation angle stays below `arccos (1 / √(π² / 3 - 2))`.

```lean
lemma fluctuationAngle_lt (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    T.fluctuationAngle < Real.arccos (1 / √(Real.pi ^ 2 / 3 - 2))
```

## B. The dimensional quantum

**`CondensedMatter.TightBindingChain.dimQuantum`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L120).

> The dimensional quantum of the chain: the excess `C - 1` over saturation.

```lean
noncomputable def dimQuantum : ℝ
```

**`CondensedMatter.TightBindingChain.dimQuantum_nonneg`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L122).

```lean
lemma dimQuantum_nonneg (ht : T.t ≠ 0) (hN : 2 ≤ T.N) : 0 ≤ T.dimQuantum
```

**`CondensedMatter.TightBindingChain.dimQuantum_eq_zero_iff`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L126).

> The dimensional quantum vanishes exactly for `N = 2` and `N = 3`.

```lean
lemma dimQuantum_eq_zero_iff (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.dimQuantum = 0 ↔ T.N = 2 ∨ T.N = 3
```

**`CondensedMatter.TightBindingChain.dimQuantum_pos`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L131).

> From four sites on, the dimensional quantum is positive.

```lean
lemma dimQuantum_pos (ht : T.t ≠ 0) (hN : 4 ≤ T.N) : 0 < T.dimQuantum
```

**`CondensedMatter.TightBindingChain.dimQuantum_lt_dimQuantum`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L135).

> From four sites on, the dimensional quantum grows strictly with the number of sites.

```lean
lemma dimQuantum_lt_dimQuantum {T T' : TightBindingChain} (ht : T.t ≠ 0) (ht' : T'.t ≠ 0)
    (hN : 4 ≤ T.N) (hNN' : T.N < T'.N) : T.dimQuantum < T'.dimQuantum
```

**`CondensedMatter.TightBindingChain.dimQuantum_lt`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L140).

> From four sites on, the dimensional quantum stays below `√(π² / 3 - 2) - 1`.

```lean
lemma dimQuantum_lt (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    T.dimQuantum < √(Real.pi ^ 2 / 3 - 2) - 1
```

**`CondensedMatter.TightBindingChain.fluctuationAngle_eq_dimQuantum`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean#L145).

> The dimensional quantum fixes the fluctuation angle: `θ = arccos (1 / (1 + δ))`.

```lean
lemma fluctuationAngle_eq_dimQuantum (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.fluctuationAngle = Real.arccos (1 / (1 + T.dimQuantum))
```

## Depends on

- [The elemental uncertainty of the open tight binding chain](maxcurrentstate-uncertaintyratio.md)

## Proof depends on

- [`C` grows with the length of the chain](maxcurrentstate-longchainmonotonicity.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/FluctuationAngle.lean)
