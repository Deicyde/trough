---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.uncertaintyRatioSqForm_strictMonoOn, CondensedMatter.TightBindingChain.uncertaintyRatio_lt_uncertaintyRatio, CondensedMatter.TightBindingChain.uncertaintyRatio_lt_sqrt_pi_sq_div_three_sub_two
statement: formalized
proof: formalized
---

# `C` grows with the length of the chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.LongChainMonotonicity`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean): 3 declarations, 3 with a docstring; 11 private, not shown.

## i. Overview

> From four sites on, `C` of the maximal current state is strictly increasing in the number
> of sites `N`, and so it stays strictly below its long chain limit `√(π² / 3 - 2)`. With
> `x = π / (N + 1)`, the closed form of `C²` is
> `((π² / x² - 2π / x - 4 + 8x / π) / 3) tan² x - 2 + 4x / π`, whose derivative is negative on
> `0 < x ≤ π / 5`. The sign follows from Taylor bounds for `sin` and `cos`, the bounds
> `3.141592 < π < 3.141593`, and a Bernstein certificate for one polynomial of degree twelve.

## ii. Key results

> - `uncertaintyRatioSqForm_strictMonoOn` : the closed form of `C²` is strictly increasing on `n ≥ 5`.
> - `uncertaintyRatio_lt_uncertaintyRatio` : `C` strictly increases with `N` from four sites on.
> - `uncertaintyRatio_lt_sqrt_pi_sq_div_three_sub_two` : `C < √(π² / 3 - 2)` from four sites on.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Taylor bounds

## B. A polynomial certificate

## C. The closed form in the angle

## D. Monotonicity

**`CondensedMatter.TightBindingChain.uncertaintyRatioSqForm_strictMonoOn`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean#L259).

> The closed form of `C²` is strictly increasing on `n ≥ 5`, that is, from four sites on.

```lean
lemma uncertaintyRatioSqForm_strictMonoOn : StrictMonoOn uncertaintyRatioSqForm (Ici 5)
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_lt_uncertaintyRatio`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean#L272).

> **Monotonicity.** From four sites on, `C` strictly increases with the number of sites.

```lean
lemma uncertaintyRatio_lt_uncertaintyRatio {T T' : TightBindingChain} (ht : T.t ≠ 0)
    (ht' : T'.t ≠ 0) (hN : 4 ≤ T.N) (hNN' : T.N < T'.N) :
    T.uncertaintyRatio < T'.uncertaintyRatio
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_lt_sqrt_pi_sq_div_three_sub_two`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean#L285).

> From four sites on, `C` stays strictly below its long chain limit `√(π² / 3 - 2)`.

```lean
lemma uncertaintyRatio_lt_sqrt_pi_sq_div_three_sub_two (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    T.uncertaintyRatio < √(Real.pi ^ 2 / 3 - 2)
```

## Depends on

- [The long chain limit of `C`](maxcurrentstate-longchainlimit.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainMonotonicity.lean)
