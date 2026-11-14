---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.currentEigenvalue_le_one, CondensedMatter.TightBindingChain.inner_openHamiltonian_currentEigenstate, CondensedMatter.TightBindingChain.maxCurrentState, CondensedMatter.TightBindingChain.norm_maxCurrentState, CondensedMatter.TightBindingChain.inner_maxCurrentState, CondensedMatter.TightBindingChain.inner_openHamiltonian_maxCurrentState, CondensedMatter.TightBindingChain.current_maxCurrentState, CondensedMatter.TightBindingChain.maxCurrentVectorState
statement: formalized
proof: formalized
---

# The maximal current state of the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.Basic`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean): 13 declarations, 13 with a docstring; 2 private, not shown.

## i. Overview

> The longest standing wave, the current eigenstate with `k = 1`, carries the largest current
> `2 a t cos (π / (N + 1))` among the current eigenstates when `t ≥ 0`. Normalized, it is the
> maximal current state. It sits at
> the centre of the chain, `⟨X⟩ = a (N - 1) / 2`, at the centre of the band, `⟨H⟩ = E0`, and
> `⟨⁅H, X⁆⟩ = -a t cos (π / (N + 1))` is the bound of its energy–position uncertainty relation.

## ii. Key results

> - `currentEigenvalue_le_one` : for `t ≥ 0`, `k = 1` carries the largest current.
> - `inner_openHamiltonian_currentEigenstate` : the Hamiltonian on the current eigenstates.
> - `maxCurrentState` : the maximal current state, of norm one by `norm_maxCurrentState`.
> - `expectation_openHamiltonian_maxCurrentState` : `⟨H⟩ = E0`.
> - `expectation_position_maxCurrentState` : `⟨X⟩ = a (N - 1) / 2`.
> - `expectation_bracket_maxCurrentState` : `⟨⁅H, X⁆⟩ = -a t cos (π / (N + 1))`.
> - `robertson_schrodinger_maxCurrentState` : the energy–position uncertainty relation of the maximal
>   current state.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The largest current

**`CondensedMatter.TightBindingChain.currentEigenvalue_le_one`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L61).

> For `t ≥ 0`, the current eigenstate with `k = 1` carries the largest current.

```lean
lemma currentEigenvalue_le_one (ht : 0 ≤ T.t) {k : ℕ} (hk : 1 ≤ k) (hkN : k ≤ T.N) :
    T.currentEigenvalue k ≤ T.currentEigenvalue 1
```

## B. The Hamiltonian on the current eigenstates

**`CondensedMatter.TightBindingChain.inner_openHamiltonian_currentEigenstate`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L81).

> The Hamiltonian on the current eigenstates:
> `⟨m|H ψ_k⟩ = E0 ⟨m|ψ_k⟩ - 2 t sin θ iᵐ⁺¹ cos ((m + 1) θ)` with `θ = k π / (N + 1)`.

```lean
lemma inner_openHamiltonian_currentEigenstate (k : ℕ) (m : Fin T.N) :
    ⟪|m⟩, T.openHamiltonian (T.currentEigenstate k)⟫_ℂ =
      T.E0 * ⟪|m⟩, T.currentEigenstate k⟫_ℂ - 2 * T.t * Real.sin (k * Real.pi / (T.N + 1)) *
        Complex.I ^ ((m : ℕ) + 1) * Real.cos (((m : ℕ) + 1) * (k * Real.pi / (T.N + 1))) := by
  have hN : Real.sin (((T.N : ℝ) + 1) * (k * Real.pi / (T.N + 1))) = 0 := by
    rw [mul_div_cancel₀ _ (by positivity)]
    exact Real.sin_nat_mul_pi k
  rw [inner_currentEigenstate]
  simp only [currentEigenstate, map_sum, map_smul, inner_sum, inner_smul_right,
    inner_openHamiltonian]
  generalize (k : ℝ) * Real.pi / (T.N + 1) = θ at hN ⊢
  have key (n : Fin T.N) : Complex.I ^ (n : ℕ) * Real.sin (((n : ℕ) + 1) * θ) *
      (if m = n then (T.E0 : ℂ)
        else if (m : ℕ) + 1 = n ∨ (n : ℕ) + 1 = m then -(T.t : ℂ) else 0) =
      (if m = n then T.E0 * (Complex.I ^ (m : ℕ) * Real.sin (((m : ℕ) + 1) * θ)) else 0) +
      ((if (m : ℕ) + 1 = n then -(T.t * Complex.I ^ ((m : ℕ) + 1) *
        Real.sin (((m : ℕ) + 2) * θ)) else 0) +
      if (n : ℕ) + 1 = m then T.t * Complex.I ^ ((m : ℕ) + 1) *
        Real.sin ((m : ℕ) * θ) else 0) := by
    by_cases hmn : m = n
    · subst hmn
      rw [ite_eq_left rfl, ite_eq_left rfl, ite_eq_right (by omega), ite_eq_right (by omega)]
      ring
    by_cases hA : (m : ℕ) + 1 = n
    · have hn : (n : ℕ) = m + 1 := hA.symm
      simp only [hmn, hn, true_or, show ¬ ((m : ℕ) + 1 + 1 = m) by omega, ite_true,
        ite_false, zero_add, add_zero]
      rw [show (((m + 1 : ℕ) : ℝ) + 1) = (m : ℕ) + 2 by push_cast; ring]
      ring
    by_cases hB : (n : ℕ) + 1 = m
    · simp only [hmn, hA, hB, or_true, ite_true, ite_false, zero_add]
      rw [← hB, Nat.cast_add_one, pow_succ, pow_succ]
      linear_combination (-(T.t : ℂ) * Complex.I ^ (n : ℕ) *
        Real.sin (((n : ℕ) + 1) * θ)) * Complex.I_sq
    · simp [hmn, hA, hB]
  have hv1 (h : ∀ n : Fin T.N, ¬ ((m : ℕ) + 1 = n)) : Real.sin (((m : ℕ) + 2) * θ) = 0 := by
    have hm : (m : ℕ) + 1 = T.N := by
      by_contra hne
      exact h ⟨(m : ℕ) + 1, by omega⟩ rfl
    have hm' : ((m : ℕ) : ℝ) + 1 = T.N := by exact_mod_cast hm
    rw [show ((m : ℕ) + 2 : ℝ) = T.N + 1 by linarith, hN]
  have hv2 (h : ∀ n : Fin T.N, ¬ ((n : ℕ) + 1 = m)) : Real.sin ((m : ℕ) * θ) = 0 := by
    have hm : (m : ℕ) = 0 := by
      by_contra hne
      exact h ⟨(m : ℕ) - 1, by omega⟩ (Nat.sub_add_cancel (by omega))
    simp [hm]
  have hr : Real.sin (((m : ℕ) + 2) * θ) - Real.sin ((m : ℕ) * θ) =
      2 * Real.sin θ * Real.cos (((m : ℕ) + 1) * θ) := by
    rw [show ((m : ℕ) + 2) * θ = ((m : ℕ) + 1) * θ + θ by ring,
      show ((m : ℕ) : ℝ) * θ = ((m : ℕ) + 1) * θ - θ by ring, Real.sin_add, Real.sin_sub]
    ring
  rw [Finset.sum_congr rfl fun n _ => key n, Finset.sum_add_distrib, Finset.sum_add_distrib,
    Finset.sum_ite_eq, ite_eq_left (Finset.mem_univ _),
    sum_ite_eq_of_unique _ _ (fun n n' h h' => Fin.ext (by omega)) fun h => by simp [hv1 h],
    sum_ite_eq_of_unique _ _ (fun n n' h h' => Fin.ext (by omega)) fun h => by simp [hv2 h]]
  have hc := congrArg (fun x : ℝ => (x : ℂ)) hr
  push_cast at hc ⊢
  linear_combination (-(T.t : ℂ) * Complex.I ^ ((m : ℕ) + 1)) * hc
```

## C. The maximal current state

**`CondensedMatter.TightBindingChain.maxCurrentState`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L147).

> The maximal current state: the current eigenstate with `k = 1`, times `√(2 / (N + 1))`.

```lean
noncomputable def maxCurrentState : T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.norm_maxCurrentState`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L151).

> The maximal current state has norm one.

```lean
lemma norm_maxCurrentState : ‖T.maxCurrentState‖ = 1
```

**`CondensedMatter.TightBindingChain.inner_maxCurrentState`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L158).

> The amplitude of the maximal current state on the site `m`.

```lean
lemma inner_maxCurrentState (m : Fin T.N) :
    ⟪|m⟩, T.maxCurrentState⟫_ℂ = (√(2 / (T.N + 1)) : ℝ) *
      (Complex.I ^ (m : ℕ) * Real.sin (((m : ℕ) + 1) * (Real.pi / (T.N + 1)))) := by
  rw [maxCurrentState, inner_smul_right, inner_currentEigenstate, Nat.cast_one, one_mul]
```

**`CondensedMatter.TightBindingChain.inner_openHamiltonian_maxCurrentState`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L164).

> The Hamiltonian on the maximal current state, site by site.

```lean
lemma inner_openHamiltonian_maxCurrentState (m : Fin T.N) :
    ⟪|m⟩, T.openHamiltonian T.maxCurrentState⟫_ℂ = T.E0 * ⟪|m⟩, T.maxCurrentState⟫_ℂ -
      (√(2 / (T.N + 1)) : ℝ) * (2 * T.t * Real.sin (Real.pi / (T.N + 1)) *
        Complex.I ^ ((m : ℕ) + 1) * Real.cos (((m : ℕ) + 1) * (Real.pi / (T.N + 1)))) := by
  rw [maxCurrentState, map_smul, inner_smul_right, inner_openHamiltonian_currentEigenstate,
    inner_smul_right, Nat.cast_one, one_mul]
  ring
```

**`CondensedMatter.TightBindingChain.current_maxCurrentState`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L173).

> The maximal current state carries the current `2 a t cos (π / (N + 1))`.

```lean
lemma current_maxCurrentState :
    T.current T.maxCurrentState = (T.currentEigenvalue 1 : ℂ) • T.maxCurrentState
```

**`CondensedMatter.TightBindingChain.maxCurrentVectorState`**, an abbrev, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L178).

> The maximal current state as a state on the operators of the chain.

```lean
noncomputable abbrev maxCurrentVectorState :
    𝓢[ℂ, T.HilbertSpace →L[ℂ] T.HilbertSpace]
```

## D. Expectations

**`CondensedMatter.TightBindingChain.expectation_maxCurrentState`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L189).

> Expectations in the maximal current state are real parts of its diagonal matrix elements.

```lean
lemma expectation_maxCurrentState (A : Observable (T.HilbertSpace →L[ℂ] T.HilbertSpace)) :
    T.maxCurrentVectorState⟨A⟩ =
      (⟪T.maxCurrentState, (A : T.HilbertSpace →L[ℂ] T.HilbertSpace) T.maxCurrentState⟫_ℂ).re
```

**`CondensedMatter.TightBindingChain.expectation_openHamiltonian_maxCurrentState`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L206).

> The maximal current state sits at the centre of the band, `⟨H⟩ = E0`.

```lean
lemma expectation_openHamiltonian_maxCurrentState :
    T.maxCurrentVectorState⟨T.openHamiltonianObservable⟩ = T.E0
```

**`CondensedMatter.TightBindingChain.expectation_position_maxCurrentState`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L231).

> The maximal current state sits at the centre of the chain, `⟨X⟩ = a (N - 1) / 2`.

```lean
lemma expectation_position_maxCurrentState :
    T.maxCurrentVectorState⟨T.positionObservable⟩ = T.a * (T.N - 1) / 2
```

**`CondensedMatter.TightBindingChain.expectation_bracket_maxCurrentState`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L269).

> The bracket of the maximal current state: `⟨⁅H, X⁆⟩ = -a t cos (π / (N + 1))`.

```lean
lemma expectation_bracket_maxCurrentState :
    T.maxCurrentVectorState⟨⁅T.openHamiltonianObservable, T.positionObservable⁆⟩ =
      -(T.a * T.t * Real.cos (Real.pi / (T.N + 1)))
```

**`CondensedMatter.TightBindingChain.robertson_schrodinger_maxCurrentState`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean#L291).

> **Energy–position uncertainty of the maximal current state.**
> `Cov(H, X)² + (a t cos (π / (N + 1)))² ≤ Var H · Var X` in the maximal current state.

```lean
lemma robertson_schrodinger_maxCurrentState :
    covariance T.maxCurrentVectorState T.openHamiltonianObservable T.positionObservable ^ 2 +
        (T.a * T.t * Real.cos (Real.pi / (T.N + 1))) ^ 2 ≤
      variance T.maxCurrentVectorState T.openHamiltonianObservable *
        variance T.maxCurrentVectorState T.positionObservable
```

## Depends on

- [The current eigenstates of the open tight binding chain](current-eigenstates.md)
- [Energy–position uncertainty in the open tight binding chain](open-uncertainty.md)
- [Vector states](../../../probabilistictheory/hilbertspace/part-01/state-vector.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Basic.lean)
