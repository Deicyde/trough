---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.toObservable, CondensedMatter.TightBindingChain.openHamiltonianObservable, CondensedMatter.TightBindingChain.positionObservable, CondensedMatter.TightBindingChain.inner_bracket_openHamiltonian_position, CondensedMatter.TightBindingChain.inner_bracket_openHamiltonian_position_eq, CondensedMatter.TightBindingChain.robertson_schrodinger_openHamiltonian_position
statement: formalized
proof: formalized
---

# Energy–position uncertainty in the open tight binding chain

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Open.Uncertainty`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean): 6 declarations, 6 with a docstring.

> The energy–position uncertainty relation for the tight binding chain with open boundaries.

## i. Overview

> The Hamiltonian and the position operator of the tight binding chain with open boundary
> conditions are observables of the C⋆-algebra of operators on the Hilbert space of the chain.
> The Robertson–Schrödinger relation then bounds their spreads in every state by the expected
> bracket `⁅H, X⁆ = -(i/2) (H X - X H)`, which only sees hopping: its matrix elements are
> `-(i/2) a (n - m) ⟨m|H|n⟩`.

## ii. Key results

> - `toObservable` : a hermitian operator of the chain as an observable.
> - `openHamiltonianObservable`, `positionObservable` : `H` and `X` as observables.
> - `inner_bracket_openHamiltonian_position` : the matrix elements of `⁅H, X⁆`.
> - `inner_bracket_openHamiltonian_position_eq` : `⁅H, X⁆` moves exactly one site `a`.
> - `robertson_schrodinger_openHamiltonian_position` : the energy–position uncertainty relation.

## iv. References

> * None.

## A. The Hamiltonian and position as observables

**`CondensedMatter.TightBindingChain.toObservable`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean#L63).

> A hermitian operator of the chain as an observable.

```lean
noncomputable def toObservable (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) (hA : A.IsSymmetric) :
    Observable (T.HilbertSpace →L[ℂ] T.HilbertSpace)
```

**`CondensedMatter.TightBindingChain.openHamiltonianObservable`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean#L68).

> The Hamiltonian with open boundary conditions as an observable.

```lean
noncomputable abbrev openHamiltonianObservable
```

**`CondensedMatter.TightBindingChain.positionObservable`**, an abbrev, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean#L72).

> The position operator as an observable.

```lean
noncomputable abbrev positionObservable
```

## B. The bracket of the Hamiltonian and position

**`CondensedMatter.TightBindingChain.inner_bracket_openHamiltonian_position`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean#L81).

> The bracket `⁅H, X⁆` only connects sites joined by hopping, weighted by their distance.

```lean
lemma inner_bracket_openHamiltonian_position (m n : Fin T.N) :
    ⟪|m⟩, ((⁅T.openHamiltonianObservable, T.positionObservable⁆ : Observable _) :
      _ →L[ℂ] _) |n⟩⟫_ℂ =
      -(Complex.I / 2) * ((T.a * ((n : ℕ) - (m : ℕ)) : ℝ) : ℂ) *
        ⟪|m⟩, T.openHamiltonian |n⟩⟫_ℂ := by
  rw [selfAdjoint.coe_bracket, smul_apply, inner_smul_right, mul_assoc,
    ← inner_commutator_position]
  rfl
```

**`CondensedMatter.TightBindingChain.inner_bracket_openHamiltonian_position_eq`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean#L92).

> The bracket `⁅H, X⁆` moves the particle exactly one site, a distance `a`, with amplitude
> `± i a t / 2`; every other matrix element vanishes.

```lean
lemma inner_bracket_openHamiltonian_position_eq (m n : Fin T.N) :
    ⟪|m⟩, ((⁅T.openHamiltonianObservable, T.positionObservable⁆ : Observable _) :
      _ →L[ℂ] _) |n⟩⟫_ℂ =
      if (m : ℕ) + 1 = n then Complex.I * (T.a * T.t / 2 : ℝ)
      else if (n : ℕ) + 1 = m then -(Complex.I * (T.a * T.t / 2 : ℝ)) else 0 := by
  rw [inner_bracket_openHamiltonian_position, inner_openHamiltonian]
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

## C. The uncertainty relation

**`CondensedMatter.TightBindingChain.robertson_schrodinger_openHamiltonian_position`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean#L118).

> **Energy–position uncertainty of the open tight binding chain.** In every state `ω`,
> `Cov(H, X)² + ⟨⁅H, X⁆⟩² ≤ Var H · Var X`.

```lean
lemma robertson_schrodinger_openHamiltonian_position
    (ω : 𝓢[ℂ, T.HilbertSpace →L[ℂ] T.HilbertSpace]) :
    covariance ω T.openHamiltonianObservable T.positionObservable ^ 2 +
        ω⟨⁅T.openHamiltonianObservable, T.positionObservable⁆⟩ ^ 2 ≤
      variance ω T.openHamiltonianObservable * variance ω T.positionObservable
```

## Depends on

- [The tight binding chain with open boundary conditions](open-basic.md)
- [The Lie bracket of observables](../../../probabilistictheory/staralgebra/lie.md)
- [Expectation, variance and covariance](../../../probabilistictheory/staralgebra/statistics.md)
- [Operators on the Hilbert space of a finite target system](../../../quantummechanics/hilbertspaces/finitetarget-operators.md)

## Proof depends on

- [Uncertainty relations](../../../probabilistictheory/cstaralgebra/uncertainty.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Uncertainty.lean)
