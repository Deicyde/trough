---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.currentEigenstate, CondensedMatter.TightBindingChain.currentEigenvalue, CondensedMatter.TightBindingChain.inner_currentEigenstate, CondensedMatter.TightBindingChain.sum_ite_eq_of_unique, CondensedMatter.TightBindingChain.current_currentEigenstate, CondensedMatter.TightBindingChain.norm_sq_currentEigenstate
statement: formalized
proof: formalized
---

# The current eigenstates of the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Current.Eigenstates`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean): 6 declarations, 6 with a docstring; 2 private, not shown.

## i. Overview

> The standing waves `sin ((n + 1) k π / (N + 1))` of the open chain vanish just outside both
> ends. Dressed with the phase `iⁿ`, they diagonalize the current operator `J`: the state
> `∑ n, iⁿ sin ((n + 1) k π / (N + 1)) |n⟩` moves with current `2 a t cos (k π / (N + 1))`.

## ii. Key results

> - `currentEigenstate` : the current eigenstate with quantum number `k`.
> - `current_currentEigenstate` : `J ψ_k = 2 a t cos (k π / (N + 1)) ψ_k`.
> - `norm_sq_currentEigenstate` : `‖ψ_k‖² = (N + 1) / 2` for `1 ≤ k ≤ N`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The current eigenstates

**`CondensedMatter.TightBindingChain.currentEigenstate`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean#L51).

> The current eigenstate `∑ n, iⁿ sin ((n + 1) k π / (N + 1)) |n⟩`.

```lean
noncomputable def currentEigenstate (k : ℕ) : T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.currentEigenvalue`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean#L56).

> The current `2 a t cos (k π / (N + 1))` of the eigenstate with quantum number `k`.

```lean
noncomputable def currentEigenvalue (k : ℕ) : ℝ
```

**`CondensedMatter.TightBindingChain.inner_currentEigenstate`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean#L60).

> The amplitude of the current eigenstate on the site `m`.

```lean
lemma inner_currentEigenstate (k : ℕ) (m : Fin T.N) :
    ⟪|m⟩, T.currentEigenstate k⟫_ℂ =
      Complex.I ^ (m : ℕ) * Real.sin (((m : ℕ) + 1) * (k * Real.pi / (T.N + 1))) := by
  rw [currentEigenstate, T.localizedState_orthonormal.inner_right_fintype]
```

## B. The eigenvalue equation

**`CondensedMatter.TightBindingChain.sum_ite_eq_of_unique`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean#L72).

> A sum over the sites picking at most one site.

```lean
lemma sum_ite_eq_of_unique {N : ℕ} (P : Fin N → Prop) [DecidablePred P] (v : ℂ)
    (h : ∀ n n', P n → P n' → n = n') (hv : (∀ n, ¬ P n) → v = 0) :
    ∑ n, (if P n then v else 0) = v
```

**`CondensedMatter.TightBindingChain.current_currentEigenstate`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean#L83).

> The current eigenstates satisfy `J ψ_k = 2 a t cos (k π / (N + 1)) ψ_k`.

```lean
lemma current_currentEigenstate (k : ℕ) :
    T.current (T.currentEigenstate k) =
      (T.currentEigenvalue k : ℂ) • T.currentEigenstate k
```

## C. The norm

**`CondensedMatter.TightBindingChain.norm_sq_currentEigenstate`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean#L169).

> The current eigenstates have squared norm `(N + 1) / 2` for `1 ≤ k ≤ N`.

```lean
lemma norm_sq_currentEigenstate {k : ℕ} (hk : 1 ≤ k) (hkN : k ≤ T.N) :
    ‖T.currentEigenstate k‖ ^ 2 = (T.N + 1) / 2
```

## Depends on

- [The current operator of the open tight binding chain](current-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Eigenstates.lean)
