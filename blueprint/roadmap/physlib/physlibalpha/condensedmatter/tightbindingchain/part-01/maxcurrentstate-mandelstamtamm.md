---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.mandelstamTammRatio_maxCurrentState, CondensedMatter.TightBindingChain.mandelstamTammRatio_maxCurrentState_eq_one_iff, CondensedMatter.TightBindingChain.mandelstamTammRatio_maxCurrentState_lt_one
statement: formalized
proof: formalized
---

# Mandelstam–Tamm and Cramér–Rao in the maximal current state

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.MandelstamTamm`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean): 3 declarations, 3 with a docstring.

## i. Overview

> In the maximal current state the current is `⟨J⟩ = 2 a t cos (π / (N + 1))`
> (`expectation_current_maxCurrentState`), and the Mandelstam–Tamm ratio
> `⟨J⟩² / (4 Var H · Var X)` is exactly `1 / C²`. Mandelstam–Tamm and Cramér–Rao are therefore
> attained together, exactly for `N = 2` and `N = 3`, and both are missed from four sites on.

## ii. Key results

> - `mandelstamTammRatio_maxCurrentState` : the ratio is `1 / C²`.
> - `mandelstamTammRatio_maxCurrentState_eq_one_iff` : both bounds are attained iff `N = 2, 3`.
> - `mandelstamTammRatio_maxCurrentState_lt_one` : both are missed for `N ≥ 4`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The Mandelstam–Tamm ratio of the maximal current state

**`CondensedMatter.TightBindingChain.mandelstamTammRatio_maxCurrentState`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean#L52).

> In the maximal current state the Mandelstam–Tamm ratio is `1 / C²`.

```lean
lemma mandelstamTammRatio_maxCurrentState :
    T.mandelstamTammRatio T.maxCurrentVectorState = 1 / T.uncertaintyRatio ^ 2
```

**`CondensedMatter.TightBindingChain.mandelstamTammRatio_maxCurrentState_eq_one_iff`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean#L59).

> Mandelstam–Tamm and Cramér–Rao are attained in the maximal current state iff `N = 2, 3`.

```lean
lemma mandelstamTammRatio_maxCurrentState_eq_one_iff (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    T.mandelstamTammRatio T.maxCurrentVectorState = 1 ↔ T.N = 2 ∨ T.N = 3
```

**`CondensedMatter.TightBindingChain.mandelstamTammRatio_maxCurrentState_lt_one`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean#L66).

> From four sites on, the maximal current state misses Mandelstam–Tamm and Cramér–Rao.

```lean
lemma mandelstamTammRatio_maxCurrentState_lt_one (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    T.mandelstamTammRatio T.maxCurrentVectorState < 1
```

## Depends on

- [Mandelstam–Tamm and Cramér–Rao in the open tight binding chain](current-mandelstamtamm.md)
- [The elemental uncertainty of the open tight binding chain](maxcurrentstate-uncertaintyratio.md)

## Proof depends on

- [The speed limit of the open tight binding chain](current-speedlimit.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/MandelstamTamm.lean)
