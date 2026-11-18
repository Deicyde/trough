---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.maxCurrent, CondensedMatter.TightBindingChain.abs_currentEigenvalue_le, CondensedMatter.TightBindingChain.currentBasisVec, CondensedMatter.TightBindingChain.norm_currentBasisVec, CondensedMatter.TightBindingChain.orthonormal_currentBasisVec, CondensedMatter.TightBindingChain.currentBasis, CondensedMatter.TightBindingChain.current_currentBasis, CondensedMatter.TightBindingChain.re_inner_current_eq_sum
statement: formalized
proof: formalized
---

# The speed limit of the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Current.SpeedLimit`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean): 12 declarations, 11 with a docstring.

## i. Overview

> For `t ≠ 0` the current eigenstates `ψ_1, …, ψ_N` carry distinct currents, so, normalized, they
> form an orthonormal basis. Every current `2 a t cos (k π / (N + 1))` is at most
> `maxCurrent = 2 |a t| cos (π / (N + 1))` in absolute value, hence so is the current `⟨J⟩` of
> every state, pure or mixed: no state moves faster. The maximal current state reaches the bound.

## ii. Key results

> - `currentBasis` : the orthonormal basis of normalized current eigenstates.
> - `re_inner_current_eq_sum` : `re ⟨ψ|J|ψ⟩ = ∑ k, λ_k |⟨k|ψ⟩|²` in that basis.
> - `abs_currentEigenvalue_le` : `|2 a t cos (k π / (N + 1))| ≤ maxCurrent` for `1 ≤ k ≤ N`.
> - `expectation_current_maxCurrentState` : `⟨J⟩ = 2 a t cos (π / (N + 1))` in the maximal current
>   state.
> - `abs_expectation_current_le` : `|⟨J⟩| ≤ maxCurrent` in every state.
> - `abs_expectation_current_maxCurrentState` : the maximal current state moves at `maxCurrent`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The largest current

**`CondensedMatter.TightBindingChain.maxCurrent`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L58).

> The largest current `2 |a t| cos (π / (N + 1))` of the open chain.

```lean
noncomputable def maxCurrent : ℝ
```

**`CondensedMatter.TightBindingChain.abs_currentEigenvalue_le`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L61).

> Every current eigenvalue is at most `maxCurrent` in absolute value.

```lean
lemma abs_currentEigenvalue_le {k : ℕ} (hk : 1 ≤ k) (hkN : k ≤ T.N) :
    |T.currentEigenvalue k| ≤ T.maxCurrent
```

## B. The basis of current eigenstates

**`CondensedMatter.TightBindingChain.currentBasisVec`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L90).

> The normalized current eigenstates `ψ_{k+1}`, `k < N`.

```lean
noncomputable def currentBasisVec (k : Fin T.N) : T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.norm_currentBasisVec`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L93).

```lean
lemma norm_currentBasisVec (k : Fin T.N) : ‖T.currentBasisVec k‖ = 1
```

**`CondensedMatter.TightBindingChain.orthonormal_currentBasisVec`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L100).

> The normalized current eigenstates are orthonormal.

```lean
lemma orthonormal_currentBasisVec (ht : T.t ≠ 0) : Orthonormal ℂ T.currentBasisVec
```

**`CondensedMatter.TightBindingChain.currentBasis`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L128).

> The orthonormal basis of normalized current eigenstates.

```lean
noncomputable def currentBasis (ht : T.t ≠ 0) : OrthonormalBasis (Fin T.N) ℂ T.HilbertSpace
```

## C. No state is faster

**`CondensedMatter.TightBindingChain.current_currentBasis`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L140).

> The current on the basis of current eigenstates.

```lean
lemma current_currentBasis (ht : T.t ≠ 0) (k : Fin T.N) :
    T.current (T.currentBasis ht k) =
      (T.currentEigenvalue ((k : ℕ) + 1) : ℂ) • T.currentBasis ht k
```

**`CondensedMatter.TightBindingChain.re_inner_current_eq_sum`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L148).

> The mean current in the basis of current eigenstates:
> `re ⟨ψ|J|ψ⟩ = ∑ k, λ_k |⟨k|ψ⟩|²`.

```lean
lemma re_inner_current_eq_sum (ht : T.t ≠ 0) (ψ : T.HilbertSpace) :
    (⟪ψ, T.current ψ⟫_ℂ).re =
      ∑ k : Fin T.N, T.currentEigenvalue ((k : ℕ) + 1) * ‖⟪T.currentBasis ht k, ψ⟫_ℂ‖ ^ 2
```

**`CondensedMatter.TightBindingChain.abs_re_inner_current_le`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L158).

> In every vector, `|re ⟨ψ|J|ψ⟩| ≤ maxCurrent ‖ψ‖²`.

```lean
lemma abs_re_inner_current_le (ht : T.t ≠ 0) (ψ : T.HilbertSpace) :
    |(⟪ψ, T.current ψ⟫_ℂ).re| ≤ T.maxCurrent * ‖ψ‖ ^ 2
```

**`CondensedMatter.TightBindingChain.abs_expectation_current_le`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L171).

> **Speed limit.** In every state, `|⟨J⟩| ≤ maxCurrent`: no state of the open chain moves
> faster than `2 |a t| cos (π / (N + 1))`.

```lean
lemma abs_expectation_current_le (ht : T.t ≠ 0)
    (ω : 𝓢[ℂ, T.HilbertSpace →L[ℂ] T.HilbertSpace]) :
    |ω⟨T.currentObservable⟩| ≤ T.maxCurrent
```

**`CondensedMatter.TightBindingChain.expectation_current_maxCurrentState`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L200).

> The maximal current state carries the current `⟨J⟩ = 2 a t cos (π / (N + 1))`.

```lean
lemma expectation_current_maxCurrentState :
    T.maxCurrentVectorState⟨T.currentObservable⟩ =
      2 * (T.a * T.t * Real.cos (Real.pi / (T.N + 1)))
```

**`CondensedMatter.TightBindingChain.abs_expectation_current_maxCurrentState`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean#L208).

> The maximal current state moves at the speed limit.

```lean
lemma abs_expectation_current_maxCurrentState :
    |T.maxCurrentVectorState⟨T.currentObservable⟩| = T.maxCurrent
```

## Depends on

- [Mandelstam–Tamm and Cramér–Rao in the open tight binding chain](current-mandelstamtamm.md)
- [The maximal current state of the open tight binding chain](maxcurrentstate-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/SpeedLimit.lean)
