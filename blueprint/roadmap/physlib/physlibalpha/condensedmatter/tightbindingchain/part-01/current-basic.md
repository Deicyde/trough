---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.current, CondensedMatter.TightBindingChain.current_hermitian, CondensedMatter.TightBindingChain.inner_current, CondensedMatter.TightBindingChain.inner_current_eq, CondensedMatter.TightBindingChain.inner_current_self_of_eigen, CondensedMatter.TightBindingChain.inner_current_localizedState, CondensedMatter.TightBindingChain.hopping, CondensedMatter.TightBindingChain.inner_hopping
statement: formalized
proof: formalized
---

# The current operator of the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Current.Basic`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean): 18 declarations, 18 with a docstring; 4 private, not shown.

> The current operator `J = i (H X - X H)` of the open tight binding chain and its matrix elements.

## i. Overview

> By the Heisenberg equation the velocity of the electron is `dX/dt = i [H, X]` (with `ħ = 1`).
> On the open tight binding chain this current operator `J = i (H X - X H)` only moves the
> electron to a neighbouring site, with amplitude `∓ i a t`. Stationary states and localized
> states carry no current.
>
> The current only sees the hopping part `K = H - E₀` of the Hamiltonian, its kinetic energy. With
> position it closes on `K`: `J X - X J = i a² K`. With the Hamiltonian it gives the rate of change
> of the current, and `H J - J H` is diagonal and vanishes inside the chain: the current changes only
> at the two ends, `-2 i a t²` on the first site and `2 i a t²` on the last. Finally `K` and `J` share
> no eigenvector: `K ψ = μ ψ` is a recurrence fixed by `ψ` on the first site, and `J ψ = 0` forces
> `X ψ` to solve the same recurrence and vanish there.

## ii. Key results

> - `current` : the current operator `J = i (H X - X H)`.
> - `inner_current_eq` : `J` moves the electron exactly one site, with amplitude `∓ i a t`.
> - `inner_current_self_of_eigen` : stationary states carry no current.
> - `inner_current_localizedState` : localized states carry no current.
> - `hopping` : the hopping part `K = H - E₀` of the Hamiltonian.
> - `current_comp_position_sub` : `J X - X J = i a² K`.
> - `inner_openHamiltonian_comp_current_sub` : `H J - J H` lives on the two ends of the chain.
> - `eq_zero_of_hopping_eq_smul` : a solution of `K ψ = μ ψ` vanishing on the first site vanishes.
> - `eq_zero_of_hopping_eq_smul_of_current_eq_zero` : `K` and `J` share no eigenvector.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The current operator

**`CondensedMatter.TightBindingChain.current`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L69).

> The current operator `J = i (H X - X H)` of the open chain, the velocity `dX/dt`.

```lean
noncomputable def current : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.current_hermitian`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L73).

> The current operator is hermitian.

```lean
lemma current_hermitian (ψ φ : T.HilbertSpace) :
    ⟪T.current ψ, φ⟫_ℂ = ⟪ψ, T.current φ⟫_ℂ
```

## B. Matrix elements

**`CondensedMatter.TightBindingChain.inner_current`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L87).

> The matrix elements of `J` are those of `H`, weighted by `i` times the hopping distance.

```lean
lemma inner_current (m n : Fin T.N) :
    ⟪|m⟩, T.current |n⟩⟫_ℂ =
      Complex.I * ((T.a * ((n : ℕ) - (m : ℕ)) : ℝ) : ℂ) * ⟪|m⟩, T.openHamiltonian |n⟩⟫_ℂ := by
  rw [current, LinearMap.smul_apply, inner_smul_right, inner_commutator_position, mul_assoc]
```

**`CondensedMatter.TightBindingChain.inner_current_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L94).

> The current moves the electron exactly one site, a distance `a`, with amplitude `∓ i a t`;
> every other matrix element vanishes.

```lean
lemma inner_current_eq (m n : Fin T.N) :
    ⟪|m⟩, T.current |n⟩⟫_ℂ =
      if (m : ℕ) + 1 = n then -(Complex.I * (T.a * T.t : ℝ))
      else if (n : ℕ) + 1 = m then Complex.I * (T.a * T.t : ℝ) else 0 := by
  rw [inner_current, inner_openHamiltonian]
  by_cases hA : (m : ℕ) + 1 = n
  · have hn : ((n : ℕ) : ℂ) = (m : ℕ) + 1 := by exact_mod_cast hA.symm
    simp only [hA, Fin.ext_iff, true_or, ite_true, show (m : ℕ) ≠ n by omega, ite_false]
    push_cast [hn]
    ring
  by_cases hB : (n : ℕ) + 1 = m
  · have hm : ((m : ℕ) : ℂ) = (n : ℕ) + 1 := by exact_mod_cast hB.symm
    simp only [hA, hB, Fin.ext_iff, or_true, ite_true, show (m : ℕ) ≠ n by omega, ite_false]
    push_cast [hm]
    ring
  split_ifs with h <;> simp_all
```

## C. States without current

**`CondensedMatter.TightBindingChain.inner_current_self_of_eigen`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L118).

> Stationary states carry no current: `⟨ψ|J|ψ⟩ = 0` whenever `H ψ = E ψ`.

```lean
lemma inner_current_self_of_eigen {ψ : T.HilbertSpace} {E : ℝ}
    (h : T.openHamiltonian ψ = (E : ℂ) • ψ) : ⟪ψ, T.current ψ⟫_ℂ = 0
```

**`CondensedMatter.TightBindingChain.inner_current_localizedState`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L125).

> A localized electron carries no current: `⟨n|J|n⟩ = 0`.

```lean
lemma inner_current_localizedState (n : Fin T.N) : ⟪|n⟩, T.current |n⟩⟫_ℂ = 0 := by
  rw [inner_current, sub_self, mul_zero, Complex.ofReal_zero, mul_zero, zero_mul]
```

## D. The hopping part of the Hamiltonian

**`CondensedMatter.TightBindingChain.hopping`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L135).

> The hopping part `K = H - E₀` of the open Hamiltonian: its kinetic energy.

```lean
noncomputable def hopping : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.inner_hopping`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L139).

> `K` hops between neighbouring sites only, with amplitude `-t`, and has no diagonal.

```lean
lemma inner_hopping (m n : Fin T.N) :
    ⟪|m⟩, T.hopping |n⟩⟫_ℂ = if (m : ℕ) + 1 = n ∨ (n : ℕ) + 1 = m then -(T.t : ℂ) else 0 := by
  rw [hopping, LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.id_apply, inner_sub_right,
    inner_smul_right, inner_openHamiltonian, localizedState_orthonormal_eq_ite]
  by_cases h : m = n
  · subst h
    simp
  · simp [h]
```

**`CondensedMatter.TightBindingChain.inner_apply_eq_sum`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L149).

> An operator in components: `⟨m|A ψ⟩ = ∑ n, ⟨m|A|n⟩ ⟨n|ψ⟩`.

```lean
lemma inner_apply_eq_sum (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) (m : Fin T.N)
    (ψ : T.HilbertSpace) : ⟪|m⟩, A ψ⟫_ℂ = ∑ n, ⟪|m⟩, A |n⟩⟫_ℂ * ⟪|n⟩, ψ⟫_ℂ := by
  conv_lhs => rw [← T.localizedState.sum_repr' ψ]
  simp only [map_sum, map_smul, inner_sum, inner_smul_right, mul_comm]
```

**`CondensedMatter.TightBindingChain.ext_localizedState`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L155).

> Two vectors with the same components on every site are equal.

```lean
lemma ext_localizedState {ψ φ : T.HilbertSpace} (h : ∀ m, ⟪|m⟩, ψ⟫_ℂ = ⟪|m⟩, φ⟫_ℂ) : ψ = φ := by
  rw [← T.localizedState.sum_repr' ψ, ← T.localizedState.sum_repr' φ]
  simp only [h]
```

**`CondensedMatter.TightBindingChain.current_eq_hopping`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L160).

> The current only sees the hopping: `J = i (K X - X K)`.

```lean
lemma current_eq_hopping :
    T.current = Complex.I • (T.hopping ∘ₗ T.position - T.position ∘ₗ T.hopping)
```

**`CondensedMatter.TightBindingChain.inner_current_hopping`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L168).

> The matrix elements of `J` are those of `K`, weighted by `i` times the hopping distance.

```lean
lemma inner_current_hopping (m n : Fin T.N) :
    ⟪|m⟩, T.current |n⟩⟫_ℂ =
      Complex.I * ((T.a * ((n : ℕ) - (m : ℕ)) : ℝ) : ℂ) * ⟪|m⟩, T.hopping |n⟩⟫_ℂ := by
  rw [current_eq_hopping, LinearMap.smul_apply, inner_smul_right, inner_commutator_position,
    mul_assoc]
```

## E. Commutators of the current

**`CondensedMatter.TightBindingChain.current_comp_position_sub`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L181).

> **Position and current close on the kinetic energy.** `J X - X J = i a² K`.

```lean
lemma current_comp_position_sub :
    T.current ∘ₗ T.position - T.position ∘ₗ T.current =
      (Complex.I * (T.a : ℂ) ^ 2) • T.hopping
```

**`CondensedMatter.TightBindingChain.inner_hopping_comp_current_sub`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L198).

> On the hopping, `⟨m|(K J - J K)|n⟩ = i a ∑ k, ⟨m|K|k⟩ ⟨k|K|n⟩ (n + m - 2 k)`.

```lean
lemma inner_hopping_comp_current_sub (m n : Fin T.N) :
    ⟪|m⟩, (T.hopping ∘ₗ T.current - T.current ∘ₗ T.hopping) |n⟩⟫_ℂ =
      ∑ k, Complex.I * T.a * ⟪|m⟩, T.hopping |k⟩⟫_ℂ * ⟪|k⟩, T.hopping |n⟩⟫_ℂ *
        (((n : ℕ) + (m : ℕ) - 2 * (k : ℕ) : ℝ) : ℂ) := by
  rw [LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.comp_apply, inner_sub_right,
    T.inner_apply_eq_sum _ m, T.inner_apply_eq_sum T.current m, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [inner_current_hopping, inner_current_hopping]
  push_cast
  ring
```

**`CondensedMatter.TightBindingChain.openHamiltonian_comp_current_sub`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L267).

> The current commutes with `H` as with its hopping part: `H J - J H = K J - J K`.

```lean
lemma openHamiltonian_comp_current_sub :
    T.openHamiltonian ∘ₗ T.current - T.current ∘ₗ T.openHamiltonian =
      T.hopping ∘ₗ T.current - T.current ∘ₗ T.hopping
```

**`CondensedMatter.TightBindingChain.inner_openHamiltonian_comp_current_sub`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L276).

> **The current changes only at the two ends of the chain.** `H J - J H` is diagonal, with
> entry `-2 i a t²` on the first site, `2 i a t²` on the last, and `0` inside the chain.

```lean
lemma inner_openHamiltonian_comp_current_sub (m n : Fin T.N) :
    ⟪|m⟩, (T.openHamiltonian ∘ₗ T.current - T.current ∘ₗ T.openHamiltonian) |n⟩⟫_ℂ =
      if m = n then 2 * Complex.I * T.a * T.t ^ 2 *
        ((if 1 ≤ (m : ℕ) then 1 else 0) - (if (m : ℕ) + 1 < T.N then 1 else 0)) else 0 := by
  rw [openHamiltonian_comp_current_sub, inner_hopping_comp_current_sub]
  by_cases h : m = n
  · subst h
    rw [ite_eq_left rfl]
    simp only [hopping_term_self, ← Finset.mul_sum, Finset.sum_sub_distrib, sum_ite_succ_eq,
      sum_ite_eq_succ]
  · rw [ite_eq_right h]
    exact Finset.sum_eq_zero fun k _ => T.hopping_term_ne h k
```

## F. The hopping and the current share no eigenvector

**`CondensedMatter.TightBindingChain.eq_zero_of_hopping_eq_smul`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L297).

> **The recurrence of the hopping.** A solution of `K ψ = μ ψ` vanishing on the first site
> vanishes: the row `n` fixes `ψ (n + 1)` from `ψ n` and `ψ (n - 1)`.

```lean
lemma eq_zero_of_hopping_eq_smul (ht : T.t ≠ 0) (hN : 0 < T.N) {μ : ℂ} {ψ : T.HilbertSpace}
    (h : T.hopping ψ = μ • ψ) (h0 : ⟪|(⟨0, hN⟩ : Fin T.N)⟩, ψ⟫_ℂ = 0) : ψ = 0 := by
  have htc : -(T.t : ℂ) ≠ 0 := neg_ne_zero.mpr (Complex.ofReal_ne_zero.mpr ht)
  have key : ∀ j (hj : j < T.N), ⟪|(⟨j, hj⟩ : Fin T.N)⟩, ψ⟫_ℂ = 0 := by
    intro j
    induction j using Nat.strong_induction_on with
```

**`CondensedMatter.TightBindingChain.eq_zero_of_hopping_eq_smul_of_current_eq_zero`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean#L327).

> **The hopping and the current share no eigenvector.** For `t ≠ 0` and `N ≥ 2`, `K ψ = μ ψ`
> and `J ψ = 0` force `ψ = 0`: `X ψ` solves the same recurrence and vanishes on the first site, so
> `ψ` lives on the first site, from which `K` moves it.

```lean
lemma eq_zero_of_hopping_eq_smul_of_current_eq_zero (ht : T.t ≠ 0) (hN : 2 ≤ T.N) {μ : ℂ}
    {ψ : T.HilbertSpace} (hK : T.hopping ψ = μ • ψ) (hJ : T.current ψ = 0) : ψ = 0
```

## Depends on

- [The tight binding chain with open boundary conditions](open-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Current/Basic.lean)
