---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.timeReversal, CondensedMatter.TightBindingChain.timeReversal_val, CondensedMatter.TightBindingChain.timeReversal_sub, CondensedMatter.TightBindingChain.timeReversal_smul, CondensedMatter.TightBindingChain.timeReversal_real_smul, CondensedMatter.TightBindingChain.inner_timeReversal, CondensedMatter.TightBindingChain.norm_timeReversal, CondensedMatter.TightBindingChain.apply_timeReversal
statement: formalized
proof: formalized
---

# Time reversal in the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Current.TimeReversal`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean): 11 declarations, 3 with a docstring.

## i. Overview

> Time reversal `Θ` conjugates the amplitudes of a state in the site basis. It is antiunitary. The
> Hamiltonian and the position operator have real matrix elements, so they commute with `Θ`, while
> the current `J = i (H X - X H)` changes sign.

## ii. Key results

> - `timeReversal` : complex conjugation of amplitudes.
> - `inner_timeReversal`, `norm_timeReversal` : `Θ` is antiunitary.
> - `apply_timeReversal` : an operator with real matrix elements commutes with `Θ`.
> - `openHamiltonian_timeReversal`, `position_timeReversal` : `H` and `X` commute with `Θ`.
> - `current_timeReversal` : `Θ` reverses the current.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Time reversal

**`CondensedMatter.TightBindingChain.timeReversal`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L51).

> Time reversal: complex conjugation of the amplitudes.

```lean
noncomputable def timeReversal (ψ : T.HilbertSpace) : T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.timeReversal_val`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L54).

```lean
lemma timeReversal_val (ψ : T.HilbertSpace) (n : Fin T.N) :
    (T.timeReversal ψ).val n = (starRingEnd ℂ) (ψ.val n)
```

**`CondensedMatter.TightBindingChain.timeReversal_sub`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L57).

```lean
lemma timeReversal_sub (ψ φ : T.HilbertSpace) :
    T.timeReversal (ψ - φ) = T.timeReversal ψ - T.timeReversal φ
```

**`CondensedMatter.TightBindingChain.timeReversal_smul`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L62).

```lean
lemma timeReversal_smul (c : ℂ) (ψ : T.HilbertSpace) :
    T.timeReversal (c • ψ) = (starRingEnd ℂ) c • T.timeReversal ψ
```

**`CondensedMatter.TightBindingChain.timeReversal_real_smul`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L67).

```lean
lemma timeReversal_real_smul (r : ℝ) (ψ : T.HilbertSpace) :
    T.timeReversal (r • ψ) = r • T.timeReversal ψ
```

**`CondensedMatter.TightBindingChain.inner_timeReversal`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L71).

```lean
lemma inner_timeReversal (ψ φ : T.HilbertSpace) :
    ⟪T.timeReversal ψ, T.timeReversal φ⟫_ℂ = (starRingEnd ℂ) ⟪ψ, φ⟫_ℂ
```

**`CondensedMatter.TightBindingChain.norm_timeReversal`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L76).

```lean
lemma norm_timeReversal (ψ : T.HilbertSpace) : ‖T.timeReversal ψ‖ = ‖ψ‖
```

**`CondensedMatter.TightBindingChain.apply_timeReversal`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L81).

> An operator with real matrix elements commutes with time reversal.

```lean
lemma apply_timeReversal {A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace}
    (hA : ∀ n m, (starRingEnd ℂ) ⟪|n⟩, A |m⟩⟫_ℂ = ⟪|n⟩, A |m⟩⟫_ℂ) (ψ : T.HilbertSpace) :
    A (T.timeReversal ψ) = T.timeReversal (A ψ) := by
  ext n
  rw [val_apply, timeReversal_val, val_apply, map_sum]
  exact Finset.sum_congr rfl fun m _ => by
    rw [map_mul, timeReversal_val, val_apply_basisFun]
    exact congrArg (· * _) (hA n m).symm
```

**`CondensedMatter.TightBindingChain.openHamiltonian_timeReversal`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L90).

```lean
lemma openHamiltonian_timeReversal (ψ : T.HilbertSpace) :
    T.openHamiltonian (T.timeReversal ψ) = T.timeReversal (T.openHamiltonian ψ)
```

**`CondensedMatter.TightBindingChain.position_timeReversal`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L94).

```lean
lemma position_timeReversal (ψ : T.HilbertSpace) :
    T.position (T.timeReversal ψ) = T.timeReversal (T.position ψ)
```

**`CondensedMatter.TightBindingChain.current_timeReversal`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean#L101).

> Time reversal reverses the current.

```lean
lemma current_timeReversal (ψ : T.HilbertSpace) :
    T.current (T.timeReversal ψ) = -T.timeReversal (T.current ψ)
```

## Depends on

- [The current operator of the open tight binding chain](current-basic.md)

## Proof depends on

- [Operators on one coordinate of a product of finite targets](../../../quantummechanics/hilbertspaces/finitetarget-product.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/TimeReversal.lean)
