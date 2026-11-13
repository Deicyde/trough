---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain, CondensedMatter.TightBindingChain.HilbertSpace, CondensedMatter.TightBindingChain.finrank_hilbertSpace, CondensedMatter.TightBindingChain.localizedState, CondensedMatter.TightBindingChain.localizedState_orthonormal, CondensedMatter.TightBindingChain.localizedState_orthonormal_eq_ite, CondensedMatter.TightBindingChain.localizedComp, CondensedMatter.TightBindingChain.localizedComp_apply_localizedState
statement: formalized
proof: formalized
---

# The tight binding chain

The module `Physlib.CondensedMatter.TightBindingChain.Basic`, [Physlib/CondensedMatter/TightBindingChain/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean): 34 declarations (1 instance with no name), 28 with a docstring.

## i. Overview

> The tight binding chain corresponds to an electron in motion
> in a 1d solid with the assumption the electron can sit only on the atoms of the solid.
>
> The solid is assumed to consist of `N` sites with a separation of `a` between them
>
> Mathematically, the tight binding chain corresponds to a
> QM problem located on a lattice with only self and nearest neighbour interactions,
> with periodic boundary conditions.

## ii. Key results

> - `TightBindingChain` : The physical parameters making up the tight binding chain.
> - `localizedState` : The orthonormal basis of localized states.
> - `hamiltonian` : The Hamiltonian of the tight binding chain.
> - `BrillouinZone` : The Brillouin zone of the tight binding chain.
> - `QuantaWaveNumber` : The quantized wavenumbers of the energy eigenstates.
> - `energyEigenstate` : The energy eigenstates of the tight binding chain.
> - `energyEigenbasis` : The orthonormal basis of normalized energy eigenstates.
> - `energyEigenvalue` : The energy eigenvalues of the tight binding chain.
> - `hamiltonian_energyEigenstate` : The Hamiltonian acting on an energy eigenstate
>   gives the corresponding energy eigenvalue times the energy eigenstate.
> - `hasEigenvalue_hamiltonian_iff` : The eigenvalues of the Hamiltonian are exactly the
>   energy eigenvalues.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The setup

### A.1. The input data for the tight binding chain

**`CondensedMatter.TightBindingChain`**, a structure, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L92).

> The physical parameters making up the tight binding chain.

```lean
structure TightBindingChain where
  /-- The number of sites, or atoms, in the chain -/
  N : Nat
  [N_ne_zero : NeZero N]
  /-- The distance between the sites -/
  a : ℝ
  a_pos : 0 < a
  /-- The energy associate with a particle sitting at a fixed site. -/
  E0 : ℝ
  /-- The hopping parameter. -/
  t : ℝ
```

**An instance with no name**, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L108).

```lean
instance : NeZero T.N
```

### A.2. The Hilbert space

**`CondensedMatter.TightBindingChain.HilbertSpace`**, an abbrev, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L118).

> The Hilbert space of a `TightBindingchain` is the `N`-dimensional finite dimensional
> Hilbert space.

```lean
abbrev HilbertSpace
```

**`CondensedMatter.TightBindingChain.finrank_hilbertSpace`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L121).

> The Hilbert space of the chain has dimension `N`.

```lean
lemma finrank_hilbertSpace : Module.finrank ℂ T.HilbertSpace = T.N
```

## B. The localized states

> Localized states correspond to the electron being located on a specific site in the chain.

### B.1. The orthonormal basis of localized states

**`CondensedMatter.TightBindingChain.localizedState`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L140).

> The eigenstate corresponding to the particle been located on the `n`th site.

```lean
noncomputable def localizedState {T : TightBindingChain} :
    OrthonormalBasis (Fin T.N) ℂ (HilbertSpace T)
```

### B.2. Notation for localized states

### B.3. Orthonormality of the localized states

**`CondensedMatter.TightBindingChain.localizedState_orthonormal`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L163).

> The localized states are normalized.

```lean
lemma localizedState_orthonormal : Orthonormal ℂ (localizedState (T := T))
```

**`CondensedMatter.TightBindingChain.localizedState_orthonormal_eq_ite`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L166).

```lean
lemma localizedState_orthonormal_eq_ite (m n : Fin T.N) :
    ⟨m|n⟩ = if m = n then 1 else 0
```

## C. The operator `|m⟩⟨n|`

### C.1. Definition of the operator `|m⟩⟨n|`

**`CondensedMatter.TightBindingChain.localizedComp`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L182).

> The linear map `|m⟩⟨n|` for `⟨n|` localized states.

```lean
noncomputable def localizedComp {T : TightBindingChain} (m n : Fin T.N) :
    T.HilbertSpace →ₗ[ℂ] T.HilbertSpace
```

### C.2. Notation for the operator `|m⟩⟨n|`

### C.3. The operator `|m⟩⟨n|` applied to a localized state

**`CondensedMatter.TightBindingChain.localizedComp_apply_localizedState`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L202).

```lean
lemma localizedComp_apply_localizedState (m n p : Fin T.N) :
```

**`CondensedMatter.TightBindingChain.localizedComp_adjoint`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L208).

> The adjoint of localizedComp |m⟩⟨n| is |n⟩⟨m|.

```lean
lemma localizedComp_adjoint (m n : Fin T.N) (ψ φ : T.HilbertSpace) :
    ⟪|m⟩⟨n| ψ, φ⟫_ℂ = ⟪ψ, |n⟩⟨m| φ⟫_ℂ := by
  simp only [localizedComp, LinearMap.coe_mk, AddHom.coe_mk, inner_smul_left, inner_smul_right,
    inner_conj_symm]
  ring
```

## D. The Hamiltonian of the tight binding chain

**`CondensedMatter.TightBindingChain.hamiltonian`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L224).

> The Hamiltonian of the tight binding chain with periodic
> boundary conditions is given by `E₀ ∑ n, |n⟩⟨n| - t ∑ n, (|n⟩⟨n + 1| + |n + 1⟩⟨n|)`.
> The periodic boundary conditions is manifested by the `+` in `n + 1` being
> within `Fin T.N` (that is modulo `T.N`).

```lean
noncomputable def hamiltonian : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace
```

### D.1. Hermiticity of the Hamiltonian

**`CondensedMatter.TightBindingChain.hamiltonian_hermitian`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L234).

> The hamiltonian of the tight binding chain is hermitian.

```lean
lemma hamiltonian_hermitian (ψ φ : T.HilbertSpace) :
    ⟪T.hamiltonian ψ, φ⟫_ℂ = ⟪ψ, T.hamiltonian φ⟫_ℂ
```

### D.2. Hamiltonian applied to a localized state

**`CondensedMatter.TightBindingChain.hamiltonian_apply_localizedState`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L255).

> The Hamiltonian applied to the localized state `|n⟩` gives
> `T.E0 • |n⟩ - T.t • (|n + 1⟩ + |n - 1⟩)`.

```lean
lemma hamiltonian_apply_localizedState (n : Fin T.N) :
    T.hamiltonian |n⟩ = (T.E0 : ℂ) • |n⟩ - (T.t : ℂ) • (|n + 1⟩ + |n - 1⟩) := by
  simp only [hamiltonian, LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.coe_sum,
    Finset.sum_apply, LinearMap.add_apply, smul_add, Finset.sum_add_distrib,
    localizedComp_apply_localizedState, ← eq_sub_iff_add_eq, Finset.sum_ite_eq', Finset.mem_univ,
    ite_true]
  module
```

### D.3. Mean energy of a localized state

**`CondensedMatter.TightBindingChain.energy_localizedState`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L272).

> The energy of a localized state in the tight binding chain is `E0`.
> This lemma assumes that there is more then one site in the chain otherwise the
> result is not true.

```lean
lemma energy_localizedState (n : Fin T.N) (htn : 1 < T.N) : ⟪|n⟩, T.hamiltonian |n⟩⟫_ℂ = T.E0 := by
  rw [hamiltonian_apply_localizedState]
  simp only [smul_add, inner_sub_right, inner_add_right, inner_smul_right,
    localizedState_orthonormal_eq_ite, ↓reduceIte, mul_one, left_eq_add, eq_sub_iff_add_eq,
    add_eq_left, Fin.one_eq_zero_iff, mul_ite, mul_zero, sub_eq_self]
  simp [show T.N ≠ 1 from by omega]
```

## E. The Brillouin zone and quantized wavenumbers

### E.1. The Brillouin zone

**`CondensedMatter.TightBindingChain.BrillouinZone`**, a def, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L293).

> The Brillouin zone of the tight binding model is `[-π/a, π/a)`.
> This is the set in which wave functions are uniquely defined.

```lean
noncomputable def BrillouinZone : Set ℝ
```

### E.2. The quantized wavenumbers of the energy eigenstates

**`CondensedMatter.TightBindingChain.QuantaWaveNumber`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L304).

> The wavenumbers associated with the energy eigenstates.
> This corresponds to the set `2 π / (a N) * (n - ⌊N/2⌋)` for `n : Fin T.N`.
> It is defined as such so it sits in the Brillouin zone.

```lean
def QuantaWaveNumber : Set ℝ
```

**`CondensedMatter.TightBindingChain.quantaWaveNumber`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L308).

> The quantized wavenumber `2 π / (a N) * (n - ⌊N/2⌋)` of the index `n`.

```lean
noncomputable def quantaWaveNumber (n : Fin T.N) : T.QuantaWaveNumber
```

**`CondensedMatter.TightBindingChain.quantaWaveNumber_injective`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L311).

> Distinct indices give distinct quantized wavenumbers.

```lean
lemma quantaWaveNumber_injective : Function.Injective T.quantaWaveNumber
```

### E.3. Wavenumbers lie in the Brillouin zone

**`CondensedMatter.TightBindingChain.quantaWaveNumber_subset_brillouinZone`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L325).

> The quantized wavenumbers form a subset of the `BrillouinZone`.

```lean
lemma quantaWaveNumber_subset_brillouinZone : T.QuantaWaveNumber ⊆ T.BrillouinZone
```

### E.4. Expotentials related to the quantized wavenumbers

**`CondensedMatter.TightBindingChain.quantaWaveNumber_exp_N`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L350).

```lean
lemma quantaWaveNumber_exp_N (n : ℕ) (k : T.QuantaWaveNumber) :
    Complex.exp (Complex.I * k * n * T.N * T.a) = 1
```

**`CondensedMatter.TightBindingChain.quantaWaveNumber_exp_sub_one`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L361).

```lean
lemma quantaWaveNumber_exp_sub_one (n : Fin T.N) (k : T.QuantaWaveNumber) :
    Complex.exp (Complex.I * k * (n - 1).val * T.a) =
    Complex.exp (Complex.I * k * n * T.a) * Complex.exp (- Complex.I * k * T.a)
```

**`CondensedMatter.TightBindingChain.quantaWaveNumber_exp_add_one`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L400).

```lean
lemma quantaWaveNumber_exp_add_one (n : Fin T.N) (k : T.QuantaWaveNumber) :
    Complex.exp (Complex.I * k * (n + 1).val * T.a) =
    Complex.exp (Complex.I * k * n * T.a) * Complex.exp (Complex.I * k * T.a)
```

## F. The energy eigenstates and eigenvalues

### F.1. The energy eigenstates

**`CondensedMatter.TightBindingChain.energyEigenstate`**, a def, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L422).

> The energy eigenstates of the tight binding chain They are given by
> `∑ n, exp (I * k * n * T.a) • |n⟩`.

```lean
noncomputable def energyEigenstate (k : T.QuantaWaveNumber) : T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.energyEigenstate_ne_zero`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L426).

> An energy eigenstate is not zero.

```lean
lemma energyEigenstate_ne_zero (k : T.QuantaWaveNumber) : T.energyEigenstate k ≠ 0
```

**`CondensedMatter.TightBindingChain.energyEigenstate_inner_self`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L433).

> The inner product of an energy eigenstate with itself is `N`.

```lean
lemma energyEigenstate_inner_self (k : T.QuantaWaveNumber) :
    ⟪T.energyEigenstate k, T.energyEigenstate k⟫_ℂ = T.N
```

### F.2. Orthonormality of the energy eigenstates

**`CondensedMatter.TightBindingChain.energyEigenstate_orthogonal`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L460).

> The energy eigenstates of the tight binding chain are orthogonal.
>
> This is a fundamental quantum mechanical result: eigenstates of a Hermitian operator
> (the Hamiltonian) with distinct eigenvalues are orthogonal. Here we prove it directly
> using the periodic boundary conditions which quantize the wavenumbers.
>
> The key physical insight is that different wavenumbers k₁ ≠ k₂ give rise to different
> N-th roots of unity exp(i(k₂-k₁)a), and the sum of all N-th roots of unity equals zero.

```lean
lemma energyEigenstate_orthogonal :
    Pairwise fun k1 k2 => ⟪T.energyEigenstate k1, T.energyEigenstate k2⟫_ℂ = 0
```

**`CondensedMatter.TightBindingChain.energyEigenstate_linearIndependent`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L497).

> The energy eigenstates are linearly independent.

```lean
lemma energyEigenstate_linearIndependent :
    LinearIndependent ℂ (fun n : Fin T.N => T.energyEigenstate (T.quantaWaveNumber n))
```

**`CondensedMatter.TightBindingChain.energyEigenstate_span`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L504).

> The energy eigenstates span the Hilbert space.

```lean
lemma energyEigenstate_span :
    ⊤ ≤ Submodule.span ℂ (Set.range fun n : Fin T.N =>
      T.energyEigenstate (T.quantaWaveNumber n))
```

**`CondensedMatter.TightBindingChain.energyEigenstate_orthonormal`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L511).

> The normalized energy eigenstates `N ^ (-1/2) • energyEigenstate k` are orthonormal.

```lean
lemma energyEigenstate_orthonormal :
    Orthonormal ℂ (fun n : Fin T.N =>
      (((Real.sqrt T.N)⁻¹ : ℝ) : ℂ) • T.energyEigenstate (T.quantaWaveNumber n))
```

**`CondensedMatter.TightBindingChain.energyEigenbasis`**, a def, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L533).

> The normalized energy eigenstates form an orthonormal basis of the Hilbert space.

```lean
noncomputable def energyEigenbasis : OrthonormalBasis (Fin T.N) ℂ T.HilbertSpace
```

**`CondensedMatter.TightBindingChain.energyEigenbasis_apply`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L542).

> The `n`-th vector of the basis is the normalized energy eigenstate of the `n`-th
> wavenumber.

```lean
lemma energyEigenbasis_apply (n : Fin T.N) :
    T.energyEigenbasis n =
      (((Real.sqrt T.N)⁻¹ : ℝ) : ℂ) • T.energyEigenstate (T.quantaWaveNumber n)
```

### F.3. The energy eigenvalues

**`CondensedMatter.TightBindingChain.energyEigenvalue`**, a def, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L555).

> The energy eigenvalue of the tight binding chain for a `k` in `QuantaWaveNumber` is
> `E0 - 2 * t * Real.cos (k * T.a)`.

```lean
noncomputable def energyEigenvalue (k : T.QuantaWaveNumber) : ℝ
```

### F.4. The time-independent Schrodinger equation

**`CondensedMatter.TightBindingChain.hamiltonian_energyEigenstate`**, a lemma, [line 565](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L565).

> The energy eigenstates satisfy the time-independent Schrodinger equation.

```lean
lemma hamiltonian_energyEigenstate (k : T.QuantaWaveNumber) :
    T.hamiltonian (T.energyEigenstate k) = T.energyEigenvalue k• T.energyEigenstate k
```

### F.5. The spectrum of the Hamiltonian

**`CondensedMatter.TightBindingChain.hasEigenvalue_hamiltonian_iff`**, a lemma, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean#L615).

> The eigenvalues of the Hamiltonian are exactly the energies `E0 - 2 t cos (k a)` of the
> quantized wavenumbers.

```lean
lemma hasEigenvalue_hamiltonian_iff (E : ℂ) :
    Module.End.HasEigenvalue T.hamiltonian E ↔
      ∃ k : T.QuantaWaveNumber, E = T.energyEigenvalue k
```

## Depends on

- [The Hilbert space of a finite target quantum mechanical system](../../quantummechanics/hilbertspaces/finitetarget-basic.md)

## Sources

- [Physlib/CondensedMatter/TightBindingChain/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/TightBindingChain/Basic.lean)
