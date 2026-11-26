---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.position, CondensedMatter.TightBindingChain.position_apply_localizedState, CondensedMatter.TightBindingChain.position_hermitian, CondensedMatter.TightBindingChain.openHamiltonian, CondensedMatter.TightBindingChain.openHamiltonian_hermitian, CondensedMatter.TightBindingChain.inner_openHamiltonian, CondensedMatter.TightBindingChain.inner_openHamiltonian_eq_adjMatrix, CondensedMatter.TightBindingChain.inner_commutator_position
statement: formalized
proof: formalized
---

# The tight binding chain with open boundary conditions

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Open.Basic`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean): 8 declarations, 8 with a docstring; 1 private, not shown.

> The position operator and the Hamiltonian of the tight binding chain with open boundaries.

## i. Overview

> A finite piece of a 1d solid has two ends: the electron cannot hop from the last site back to
> the first. This is the tight binding chain with open boundary conditions. It also carries a
> position operator, which the periodic chain lacks, since there the site `N` is identified
> with the site `0`.

## ii. Key results

> - `position` : the position operator `X = ∑ n, a n |n⟩⟨n|`.
> - `openHamiltonian` : the Hamiltonian with open boundary conditions.
> - `inner_openHamiltonian` : the open chain only hops between neighbouring sites.
> - `inner_openHamiltonian_eq_adjMatrix` : its matrix elements are `E0` times the identity minus `t`
>   times the adjacency matrix of the path graph.
> - `inner_commutator_position` : `⟨m|(A X - X A)|n⟩ = a (n - m) ⟨m|A|n⟩`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The position operator

**`CondensedMatter.TightBindingChain.position`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L60).

> The position operator `X = ∑ n, a n |n⟩⟨n|`, measuring from the site `0`.

```lean
noncomputable def position : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.position_apply_localizedState`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L64).

> The localized states are the eigenstates of the position operator.

```lean
lemma position_apply_localizedState (n : Fin T.N) :
    T.position |n⟩ = ((T.a * (n : ℕ) : ℝ) : ℂ) • |n⟩ := by
  simp [position, localizedComp_apply_localizedState]
```

**`CondensedMatter.TightBindingChain.position_hermitian`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L69).

> The position operator is hermitian.

```lean
lemma position_hermitian (ψ φ : T.HilbertSpace) :
    ⟪T.position ψ, φ⟫_ℂ = ⟪ψ, T.position φ⟫_ℂ
```

## B. The Hamiltonian with open boundary conditions

**`CondensedMatter.TightBindingChain.openHamiltonian`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L83).

> The Hamiltonian of the tight binding chain with open boundary conditions: the periodic
> `hamiltonian` with one hopping between the end sites `0` and `N - 1` removed. For `N = 2` the
> periodic chain counts the single bond twice, and one copy remains.

```lean
noncomputable def openHamiltonian : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace
```

### B.1. Hermiticity

**`CondensedMatter.TightBindingChain.openHamiltonian_hermitian`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L93).

> The Hamiltonian with open boundary conditions is hermitian.

```lean
lemma openHamiltonian_hermitian (ψ φ : T.HilbertSpace) :
    ⟪T.openHamiltonian ψ, φ⟫_ℂ = ⟪ψ, T.openHamiltonian φ⟫_ℂ
```

### B.2. Matrix elements

**`CondensedMatter.TightBindingChain.inner_openHamiltonian`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L115).

> The open chain hops only between neighbouring sites, with amplitude `-t`.

```lean
lemma inner_openHamiltonian (m n : Fin T.N) :
    ⟪|m⟩, T.openHamiltonian |n⟩⟫_ℂ =
      if m = n then (T.E0 : ℂ)
      else if (m : ℕ) + 1 = n ∨ (n : ℕ) + 1 = m then -(T.t : ℂ) else 0 := by
  simp only [openHamiltonian, LinearMap.add_apply, LinearMap.smul_apply,
    hamiltonian_apply_localizedState, localizedComp_apply_localizedState, inner_add_right,
    inner_sub_right, inner_smul_right, localizedState_orthonormal_eq_ite]
  rw [apply_ite (inner ℂ _), apply_ite (inner ℂ _)]
  simp only [inner_zero_right, localizedState_orthonormal_eq_ite]
  have h (k l : Fin T.N) : k = l - 1 ↔ l = k + 1 := by rw [eq_sub_iff_add_eq, eq_comm]
  have hl (k : Fin T.N) : -1 = k ↔ (k : ℕ) + 1 = T.N := by
    rw [neg_eq_iff_add_eq_zero, add_comm, eq_comm, eq_add_one_iff_val]
    simp
  simp only [h m n, hl n, eq_comm (a := m) (b := -1), hl m, eq_add_one_iff_val m n,
    eq_add_one_iff_val n m]
  simp only [Fin.ext_iff, Fin.val_zero]
  split_ifs <;> first | omega | ring
```

**`CondensedMatter.TightBindingChain.inner_openHamiltonian_eq_adjMatrix`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L135).

> The open chain is the hopping Hamiltonian of the path graph: the matrix element between
> two sites is `E0` times the identity minus `t` times the adjacency matrix of `pathGraph N`.

```lean
lemma inner_openHamiltonian_eq_adjMatrix (m n : Fin T.N) :
    ⟪|m⟩, T.openHamiltonian |n⟩⟫_ℂ =
      (T.E0 : ℂ) * (1 : Matrix (Fin T.N) (Fin T.N) ℂ) m n -
        (T.t : ℂ) * (SimpleGraph.pathGraph T.N).adjMatrix ℂ m n := by
  rw [inner_openHamiltonian]
  by_cases h : m = n
  · subst h
    simp
  · simp [h, Matrix.one_apply_ne h, SimpleGraph.adjMatrix_apply, SimpleGraph.pathGraph_adj]
    split_ifs <;> simp_all
```

## C. Commutators with the position operator

**`CondensedMatter.TightBindingChain.inner_commutator_position`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean#L154).

> Commuting with the position operator weighs each matrix element by the hopping distance:
> `⟨m|(A X - X A)|n⟩ = a (n - m) ⟨m|A|n⟩`.

```lean
lemma inner_commutator_position (A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace) (m n : Fin T.N) :
    ⟪|m⟩, (A ∘ₗ T.position - T.position ∘ₗ A) |n⟩⟫_ℂ =
      ((T.a * ((n : ℕ) - (m : ℕ)) : ℝ) : ℂ) * ⟪|m⟩, A |n⟩⟫_ℂ := by
  rw [LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.comp_apply, inner_sub_right,
    ← position_hermitian, position_apply_localizedState, position_apply_localizedState,
    map_smul, inner_smul_left, inner_smul_right, Complex.conj_ofReal]
  push_cast
  ring
```

## Depends on

- [The tight binding chain](../../../../physlib/condensedmatter/tightbindingchain/basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/Basic.lean)
