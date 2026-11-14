---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.uncertaintyRatioSqForm, CondensedMatter.TightBindingChain.tendsto_uncertaintyRatioSqForm, CondensedMatter.TightBindingChain.uncertaintyRatio_sq_eq_uncertaintyRatioSqForm, CondensedMatter.TightBindingChain.tendsto_uncertaintyRatio, CondensedMatter.TightBindingChain.one_lt_sqrt_pi_sq_div_three_sub_two
statement: formalized
proof: formalized
---

# The long chain limit of `C`

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.LongChainLimit`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean): 5 declarations, 5 with a docstring.

## i. Overview

> In the maximal current state, `C` depends only on the number of sites `N`. As the chain
> grows, `θ = π / (N + 1) → 0`, `(N + 1) sin θ → π` and `cos θ → 1`, so the closed form of
> `C²` tends to `2 (π² / 6 - 1) = π² / 3 - 2`. Every long enough chain has
> `C` close to `C_∞ = √(π² / 3 - 2) ≈ 1.1357`, which is strictly larger than one: the
> uncertainty relation stays strict in the long chain limit.

## ii. Key results

> - `uncertaintyRatioSqForm` : the closed form of `C²` as a function of `n = N + 1`.
> - `uncertaintyRatio_sq_eq_uncertaintyRatioSqForm` : `C² = uncertaintyRatioSqForm (N + 1)` for
>   `N ≥ 2`.
> - `tendsto_uncertaintyRatioSqForm` : `uncertaintyRatioSqForm n → π² / 3 - 2` as `n → ∞`.
> - `tendsto_uncertaintyRatio` : `C → √(π² / 3 - 2)` along any family of chains with `N → ∞`.
> - `one_lt_sqrt_pi_sq_div_three_sub_two` : `1 < √(π² / 3 - 2)`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The limit of the closed form

**`CondensedMatter.TightBindingChain.uncertaintyRatioSqForm`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean#L55).

> The closed form of `C²` as a function of `n = N + 1`, written with `sinc`.

```lean
noncomputable def uncertaintyRatioSqForm (n : ℝ) : ℝ
```

**`CondensedMatter.TightBindingChain.tendsto_uncertaintyRatioSqForm`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean#L60).

> The closed form tends to `π² / 3 - 2` as `n → ∞`.

```lean
lemma tendsto_uncertaintyRatioSqForm :
    Tendsto uncertaintyRatioSqForm atTop (𝓝 (Real.pi ^ 2 / 3 - 2))
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_sq_eq_uncertaintyRatioSqForm`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean#L79).

> For `N ≥ 2`, `C²` is the closed form at `n = N + 1`.

```lean
lemma uncertaintyRatio_sq_eq_uncertaintyRatioSqForm (T : TightBindingChain) (ht : T.t ≠ 0)
    (hN : 2 ≤ T.N) :
    T.uncertaintyRatio ^ 2 = uncertaintyRatioSqForm (T.N + 1)
```

## B. The limit of `C`

**`CondensedMatter.TightBindingChain.tendsto_uncertaintyRatio`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean#L96).

> **The long chain limit.** Along any family of chains whose number of sites tends to infinity,
> the constant `C` of the maximal current state tends to `√(π² / 3 - 2)`.

```lean
lemma tendsto_uncertaintyRatio {ι : Type*} {l : Filter ι} (T : ι → TightBindingChain)
    (ht : ∀ i, (T i).t ≠ 0) (hN : Tendsto (fun i => (T i).N) l atTop) :
    Tendsto (fun i => (T i).uncertaintyRatio) l (𝓝 √(Real.pi ^ 2 / 3 - 2))
```

**`CondensedMatter.TightBindingChain.one_lt_sqrt_pi_sq_div_three_sub_two`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean#L108).

> The limit `√(π² / 3 - 2)` is strictly larger than one, since `π > 3`.

```lean
lemma one_lt_sqrt_pi_sq_div_three_sub_two : 1 < √(Real.pi ^ 2 / 3 - 2)
```

## Depends on

- [The elemental uncertainty of the open tight binding chain](maxcurrentstate-uncertaintyratio.md)

## Proof depends on

- [The variances of the maximal current state](maxcurrentstate-variances.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/LongChainLimit.lean)
